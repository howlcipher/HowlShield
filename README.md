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
