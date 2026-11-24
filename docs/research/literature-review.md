# Literature and standards

## Security guidance

OWASP LLM01 describes indirect injection through third-party inputs. NIST
categorizes the threat in its adversarial ML taxonomy. MITRE ATLAS assigns the
indirect variant AML.T0051.001. These sources motivate explicit trust boundaries
between application authority, document data and authorization.
[OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
[NIST AI 100-2e2025](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf)
[MITRE ATLAS](https://atlas.mitre.org/techniques/AML.T0051.001)

## Peer-reviewed work

Greshake et al. studied indirect injection in LLM-integrated applications at
AISec 2023. The document experiment should isolate ingestion fidelity from
downstream model behavior. [ACM proceedings](https://doi.org/10.1145/3605764.3623985)

AgentDojo evaluates both task utility and behavior under adversarial inputs.
For HowlShield, pair each document transformation with a legitimate task and
score authorization independently from model outputs.
[NeurIPS 2024](https://papers.nips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)

## Format specifications

PDF structure, paint operations, extraction order and logical structure can
differ. WordprocessingML and Open Packaging Conventions define document parts
and relationships that may fall outside the body. Preserve these distinctions
in inspection and ground coverage in explicitly supported features.
[PDF ISO 32000-2](https://pdfa.org/sponsored-standards/)
[ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/)

## Preprint reviewed

Beurer-Kellner et al. describe authority and data-flow patterns for agents.
This assessment uses the arXiv version. It motivates testing authorization
separately from extraction and output accuracy.
[Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837)
