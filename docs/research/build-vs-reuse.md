# Build versus reuse

| Option | Advantages | Costs and gaps to measure |
| --- | --- | --- |
| Adopt an existing scanner | Fast baseline, tested structural rules, existing reports | Verify per-format coverage, report stability, licensing, and whether the evidence identifies omitted content |
| Compose established parsers and an optional renderer | Independent views, familiar packaging and minimized parsing code | Parser disagreement, version drift, native runtime constraints, worker isolation |
| Adopt pixel reconstruction as an external baseline | Mature isolation approach, visible layout retained where rendering succeeds | Accessibility and logical reading order, OCR errors, installation footprint, policy trace granularity |
| Implement format parsing from scratch | Control over the exact parser contract | Large specification surface, long validation cycle, added parser security exposure |

Python favors parser availability and concise evidence tooling. Go favors
distribution and subprocess supervision, with a different parser ecosystem.
A browser-first TypeScript implementation offers local UX and worker
isolation, with browser library and resource constraints. Select after a
bounded baseline and license review.

## Local ecosystem inspection

| Project and inspected revision | Candidate role |
| --- | --- |
| HowlDream `9724147` | Budgeted exploration with separately labeled mock and live modes. Local Ollama endpoint was unavailable at discovery. |
| HowlProof `dbbdb60` | Trusted local artifact checks and explicit evidence verdicts. Keep evaluation of project artifacts separate from parser isolation. |
| HowlFrame `9c739c9d` | Evaluate capability contracts as an optional implementation of the action authorization boundary. |
| HowlWriter `8607c6a` | Optional locally validated research writing workflow. |
| HowlPlane `0386887` | Optional orchestration of engineering and evidence runs. |
| Password Arena `029dae7` | Reference for transparent benchmark presentation and fixture-led demonstrations. |
| william_elias `e652435` | Reference for the eventual independent project case study. |

No runtime integration is selected. Validate ecosystem candidates with
measurable cost and evidence benefits.

## Paired architecture study

| Candidate | Main benefit | Failure mode to measure |
| --- | --- | --- |
| Structural selection with visual corroboration | Retains exact characters and can represent accessibility units explicitly | Alignment between structure and visual evidence can fail or produce ambiguous matches |
| Raster-first reconstruction with independent OCR and parallel structural inventory | Limits the reconstruction input to page pixels while retaining a separate omission inventory | OCR and rendering can lose reading order, links, accessibility and text fidelity |

Use paired, manually labeled PDF and DOCX controls covering scanned pages,
accessibility descriptions, ligatures, columns, tables, footnotes, comments
and metadata. Predeclare the policy and acceptable task answers. Compare
allowed-unit recall, excluded-unit leakage, reading-order edit distance,
task accuracy, unresolved-unit fraction, replay stability, peak memory and
elapsed time. Pin renderer, fonts and OCR. Keep failed parses in the coverage
denominator. Prefer the option with stronger legitimate content preservation
at the same predeclared leakage threshold if its evidence also passes
independent verification.

The initial [raster proxy](../evidence/m0.md#raster-reconstruction-proxy)
establishes a simple difference between the visible and extractable views.
It neither tests OCR nor selects the architecture.
