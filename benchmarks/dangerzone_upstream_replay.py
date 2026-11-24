"""Exercise pinned upstream Dangerzone assembly with captured pixel streams."""

import argparse
import io
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from dangerzone.document import Document
from dangerzone.isolation_provider.dummy import Dummy


class ReplayProvider(Dummy):
    """Supply a captured stream at the upstream converter I/O boundary."""

    @contextmanager
    def doc_to_pixels_proc(self, document):
        del document
        with self.pixel_path.open("rb") as pixels:
            yield SimpleNamespace(stdin=io.BytesIO(), stdout=pixels)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("controls", type=Path)
    parser.add_argument("streams", type=Path)
    args = parser.parse_args()
    sys.dangerzone_dev = True
    provider = ReplayProvider()

    with TemporaryDirectory() as directory:
        for kind in ("pdf", "docx"):
            provider.pixel_path = args.streams / f"{kind}.rgb"
            for language in (None, "eng"):
                output = Path(directory) / f"{kind}-{language or 'raster'}.pdf"
                document = Document(str(args.controls / f"control.{kind}"), str(output))
                provider.convert(document, language)
                if not document.is_safe():
                    raise RuntimeError(
                        f"Upstream conversion failed for {kind}/{language}"
                    )
                text = subprocess.check_output(
                    ["pdftotext", output, "-"], text=True, timeout=8
                ).strip()
                expected = "Quarterly review" if language else ""
                if text != expected:
                    raise ValueError(f"{kind}/{language}: unexpected text {text!r}")
                print(kind, language, output.stat().st_size, repr(text))


if __name__ == "__main__":
    main()
