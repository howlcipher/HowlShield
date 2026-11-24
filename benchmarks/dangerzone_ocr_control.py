"""Measure text recovery from the two benign Dangerzone pixel streams."""

import argparse
import json
import os
import subprocess
from hashlib import sha256
from pathlib import Path
from struct import unpack
from tempfile import TemporaryDirectory

import pymupdf

MAX_DIMENSION = 3000
HEADER_BYTES = 6
MAX_STREAM_BYTES = HEADER_BYTES + MAX_DIMENSION**2 * 3
EXPECTED_TEXT = "Quarterly review"
DPI = 150


def read_pixmap(stream: Path) -> pymupdf.Pixmap:
    with stream.open("rb") as source:
        data = source.read(MAX_STREAM_BYTES + 1)
    if len(data) < HEADER_BYTES:
        raise ValueError(f"Missing pixel header in {stream.name}")
    pages, width, height = unpack(">HHH", data[:HEADER_BYTES])
    if not (
        pages == 1
        and 0 < width <= MAX_DIMENSION
        and 0 < height <= MAX_DIMENSION
        and len(data) == HEADER_BYTES + width * height * 3
    ):
        raise ValueError(f"Invalid single-page pixel stream in {stream.name}")
    pixmap = pymupdf.Pixmap(pymupdf.csRGB, width, height, data[HEADER_BYTES:], False)
    pixmap.set_dpi(DPI, DPI)
    return pixmap


def extract(page_bytes: bytes, directory: Path) -> dict[str, str | int]:
    with pymupdf.open("pdf", page_bytes) as page, pymupdf.open() as output:
        output.insert_pdf(page)
        pdf_bytes = output.tobytes()
    pdf_path = directory / "output.pdf"
    pdf_path.write_bytes(pdf_bytes)
    result = subprocess.run(
        ["pdftotext", pdf_path, "-"],
        capture_output=True,
        check=True,
        text=True,
        encoding="utf-8",
        timeout=10,
    )
    return {
        "bytes": len(pdf_bytes),
        "sha256": sha256(pdf_bytes).hexdigest(),
        "text": result.stdout.strip(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_rgb", type=Path)
    parser.add_argument("docx_rgb", type=Path)
    parser.add_argument("tessdata", type=Path)
    args = parser.parse_args()
    os.environ["OMP_THREAD_LIMIT"] = "1"
    os.environ["OMP_NUM_THREADS"] = "1"
    results = {}
    with TemporaryDirectory() as directory:
        for kind, stream in (("pdf", args.pdf_rgb), ("docx", args.docx_rgb)):
            pixmap = read_pixmap(stream)
            with pymupdf.open() as image_pdf:
                image_pdf.insert_file(pixmap)
                raster = image_pdf.tobytes(deflate_images=True)
            searchable = pixmap.pdfocr_tobytes(
                compress=True, language="eng", tessdata=str(args.tessdata)
            )
            results[kind] = {
                "without_ocr": extract(raster, Path(directory)),
                "with_ocr": extract(searchable, Path(directory)),
            }
    print(json.dumps(results, indent=2))
    return int(
        any(
            row["without_ocr"]["text"] != "" or row["with_ocr"]["text"] != EXPECTED_TEXT
            for row in results.values()
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
