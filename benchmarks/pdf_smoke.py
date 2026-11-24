"""Compare two PDF extractors on one locally generated benign document."""

import json
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

import pypdf

EXPECTED_BODY = "Quarterly review"
EXPECTED_TITLE = "Routine archive title"
POSTSCRIPT = b"""%!PS-Adobe-3.0
[ /Title (Routine archive title) /DOCINFO pdfmark
/Helvetica findfont 18 scalefont setfont
72 720 moveto (Quarterly review) show
showpage
"""


def main() -> None:
    with TemporaryDirectory() as directory:
        source = Path(directory) / "control.ps"
        document = Path(directory) / "control.pdf"
        source.write_bytes(POSTSCRIPT)
        subprocess.run(["ps2pdf", "-dSAFER", source, document], check=True, timeout=10)
        reader = pypdf.PdfReader(document, strict=True)
        pypdf_body = reader.pages[0].extract_text().strip()
        poppler_body = subprocess.run(
            ["pdftotext", document, "-"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
        ).stdout.strip()
        result = {
            "cases": 1,
            "pypdf_version": pypdf.__version__,
            "pypdf_body_matches": pypdf_body == EXPECTED_BODY,
            "poppler_body_matches": poppler_body == EXPECTED_BODY,
            "pypdf_title_matches": (
                reader.metadata is not None and reader.metadata.title == EXPECTED_TITLE
            ),
        }
        print(json.dumps(result, sort_keys=True))
        if not all(
            result[check]
            for check in (
                "pypdf_body_matches",
                "poppler_body_matches",
                "pypdf_title_matches",
            )
        ):
            raise SystemExit(1)


if __name__ == "__main__":
    main()
