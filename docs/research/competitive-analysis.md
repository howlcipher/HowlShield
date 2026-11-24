# Competitive analysis

Repository metadata was queried from GitHub on 2026-11-21. Dates are last push
dates, which can include activity unrelated to releases. Capabilities below are
based on upstream documentation. Runtime comparisons remain pending.

| Project | License and activity | Coverage and execution |
| --- | --- | --- |
| [Shield Scanner](https://github.com/nisake/shield-scanner-mono) | MIT, archived, 2026-06-28 | Local browser, shared core and MCP. PDF, Office, text, web, mail, notebooks and archives. Hidden and obscured content rules. |
| [Prompt Injection Screen](https://github.com/martinmajsawicki/prompt-injection-screen) | Unlicense, 2026-06-18 | Local deterministic PDF, DOCX, HTML and text observations with optional classifier layers. CLI and Claude hooks. |
| [Hidden Content Detector](https://github.com/Davin-Willis/hidden-content-detector) | GitHub SPDX field empty, 2026-08-16 | Unicode, PDF extraction and render-state observations, and DOCX run inspection. Redistribution review pending. |
| [Hidden Text Detector](https://github.com/wppoland/hidden-text-detector) | MIT, 2026-07-28 | PDF and DOCX hidden text observations, including geometry, font size, render mode and Unicode. |
| [ContextGate](https://github.com/kanekoyuichi/contextgate) | MIT, 2026-05-07 | Local text and document rules with Python scanning API. Record released capabilities separately from roadmap. |
| [WhatsInMyPDF](https://github.com/whatsinmypdf/whatsinmypdf) | AGPL-3.0, 2026-11-03 | Browser-local PDF detection and fixture-backed UI. Documents extraction blind spots caused by page clipping. |
| [Microsoft Prompt Shields](https://learn.microsoft.com/azure/foundry/openai/concepts/content-filter-prompt-shields) | Hosted Azure service | User and document text classification through Foundry. |
| [Meta Prompt Guard](https://github.com/meta-llama/PurpleLlama/blob/main/Prompt-Guard/MODEL_CARD.md) | Model-specific terms | Local text classification is possible with weights and inference runtime. Record exact checkpoint and license before comparison. |
| [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Apache-2.0 per license file, 2026-11-19 | Configurable input, retrieval and output rails with pluggable providers. |
| [LLM Guard](https://github.com/protectai/llm-guard) | MIT, archived, 2026-07-08 | Local text scanners with optional inference dependencies, including a prompt injection scanner. |
| [garak](https://github.com/NVIDIA/garak) | Apache-2.0, 2026-11-18 | Model evaluation framework. Relevant to evaluation methodology. |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | MIT core, 2026-11-21 | Configurable evaluation and reporting with provider-dependent execution. |
| [Lakera Guard](https://docs.lakera.ai/) | Hosted service | Text classification API. Service evaluation requires terms and cost review. |
| [Dangerzone](https://github.com/freedomofpress/dangerzone) | AGPL-3.0, 2026-11-18 | Sandboxed PDF and Office pixel reconstruction with optional OCR. Strong baseline for reconstruction. |
| [mat2](https://github.com/jvoisin/mat2) | LGPL-3.0, 2026-11-15 | Metadata inspection and removal across multiple formats. Cleaning options have fidelity tradeoffs. |
| [pypdf](https://github.com/py-pdf/pypdf) | BSD 3-clause terms per license file, 2026-11-21 | PDF objects, text, metadata and attachments. Python library with extraction blind spots. |
| [pdfminer.six](https://github.com/pdfminer/pdfminer.six) | MIT, 2026-03-13 | Independent Python PDF extraction and layout analysis. |

For each tested version, capture installation footprint, formats, report schema,
extensibility, integration boundary, independent representations, reconstruction,
and preservation evidence. Use the same benign controls and score structural
observations separately from semantic interpretation. False positive and
negative rates, latency, memory and coverage require measured results. A missing
feature in these summaries means its status is unverified.

## Baseline evidence

The initial PDF extractor smoke run is recorded in
[M0 evidence](../evidence/m0.md). These snapshots pin the three most relevant
external candidates for source and runtime comparison.

| Candidate | Revision | Evidence level |
| --- | --- | --- |
| Hidden Text Detector | `ce9e505dc1c128701e921e8d7e1a133c7ff28db8` | README, dependency manifest and two benign runtime controls. PyMuPDF and python-docx required. pikepdf and NumPy optional with coverage or performance tradeoffs. |
| WhatsInMyPDF | `3bdd2e746f4b9fa617ea87bf702b8c7fe95d97f8` | Upstream documentation. Core runtime control recorded. Benign browser flow reproduced with request instrumentation. |
| Dangerzone | `f97310cad237d2f96a58df3ab004c241628a39dd` | Upstream documentation and release notes. Signed image and first-stage PDF and DOCX runtime controls recorded. Local single-page PDF and OCR assembly control recorded; packaged CLI pending. |
