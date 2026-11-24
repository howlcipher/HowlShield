# HowlShield

HowlShield investigates whether controlled document representations can reduce
indirect prompt injection risk while preserving legitimate information and task
accuracy. Prompt Arena is the planned educational and benchmarking interface.

The project is in M0 research. See the [roadmap](ROADMAP.md) and the
[competitive assessment](docs/research/competitive-analysis.md).

The initial target is local PDF and DOCX inspection with explicit coverage,
source locations, deterministic content selection, and independently checkable
reconstruction evidence. Document content remains untrusted throughout.

A [PDF extractor smoke check](docs/evidence/m0.md) records the first benign control.

The research branch also records [scanner and raster controls](docs/evidence/m0.md).

The [browser control](docs/evidence/m0.md#whatsinmypdf-browser-control) checks the local file-selection flow.

[Contributing](CONTRIBUTING.md) describes owner approval for agent-authored pull requests.

The [DOCX differential control](docs/evidence/m0.md#docx-structure-versus-renderer-export) compares structural extraction with renderer export.

The [Dangerzone control](docs/evidence/m0.md#dangerzone-document-to-pixels-baseline) exercises its signed conversion image on PDF and DOCX.

The [OCR control](docs/evidence/m0.md#dangerzone-pixel-to-pdf-and-ocr-control) measures searchable text after raster reconstruction.

The [upstream replay](docs/evidence/m0.md#pinned-upstream-dangerzone-replay) cross-checks the local OCR control.
