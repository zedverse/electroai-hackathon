# Prompt: Rewrite IEEE LaTeX Template as Research Paper on AI Schematic Understanding

## Goal

Rewrite `ElectroAIHackathonIEEETemplate/conference_101719.tex` as a complete, publishable-quality IEEE conference paper. The paper investigates whether large language models (LLMs) and multimodal AI systems can perceive structural information in electrical schematics and reconstruct them — either as code (e.g., SPICE netlists, KiCad, TikZ/CircuiTikZ) or as human-readable descriptions.

## Paper Identity

**Title:** Can AI See Structure in Schematics? A Comparative Evaluation of Multimodal Models for Circuit Diagram Understanding and Reconstruction

**Venue:** EEAI Hackathon — IEEE-format paper submission

**Authors:** Use placeholder author blocks for up to 3 authors (e.g., "A. Author", "B. Author", "C. Author") with affiliation "[Author affiliation]" and email "[email]". Do not invent real names or institutions.

## Core Hypothesis

Multimodal AI models can identify structural elements (components, nodes, connections) in electrical schematic images and reconstruct them with varying degrees of fidelity. Fidelity differs across models and prompting strategies.

## Models to Evaluate (use these exactly)

- **OpenAI GPT-4o** (vision-capable)
- **Anthropic Claude 3.5 Sonnet / Claude 3 Opus** (vision-capable)
- **Google Gemini 1.5 Pro** (vision-capable)
- **OpenAI Codex / GPT-4 with code generation** (for code output tasks)

Use "[PLACEHOLDER: actual model versions used]" where specific version strings are needed.

## Paper Structure

### Abstract
- State the research question: can AI perceive and reconstruct schematic structure?
- State the method: image-based prompting of multimodal LLMs, evaluation against ground truth
- State the finding: models vary in fidelity; structural complexity is the key variable
- No symbols or math in abstract (IEEE rule)

### 1. Introduction
- Electrical schematics encode rich structured information: topology, component identity, node connectivity
- Manual interpretation is expert-intensive; automation has applications in EDA, documentation, education, reverse engineering
- Recent multimodal LLMs claim image understanding — but schematics are domain-specific visual languages
- Research question: do these models "see" schematic structure, and to what degree can they reconstruct it?
- Contributions: benchmark methodology, comparative results across models, qualitative error taxonomy

### 2. Related Work
- Schematic recognition: classical CV approaches (symbol detection, graph extraction)
- LLM code generation for hardware description languages (SPICE, HDL)
- Multimodal LLM image understanding benchmarks (not schematic-specific)
- Gap: no systematic comparison of LLMs on schematic reconstruction tasks
- Use placeholder citations: `\cite{b1}` through `\cite{b8}` for 8 realistic but placeholder references

### 3. Methodology

#### 3.1 Task Definition
- **Input**: image of an electrical schematic (PNG/JPG)
- **Output**: one of three formats — (a) natural language description, (b) SPICE netlist, (c) CircuiTikZ/TikZ LaTeX code
- **Evaluation**: structural accuracy score (component count match, connection accuracy, node labelling)

#### 3.2 Schematic Dataset
- Describe a small benchmark set: [PLACEHOLDER: N schematics], ranging from simple (RC filter, voltage divider) to complex (op-amp circuits, H-bridge motor driver)
- Schematics sourced from [PLACEHOLDER: source, e.g., textbook figures, KiCad examples]
- Ground truth: manually verified netlists and component lists

#### 3.3 Prompting Strategy
- Zero-shot prompt: "Describe the circuit in this schematic image. List all components, their values, and how they are connected."
- Code-generation prompt: "Reconstruct this schematic as a SPICE netlist."
- Chain-of-thought prompt: "First identify all components, then trace the connections, then output a netlist."
- Temperature set to 0 for reproducibility

#### 3.4 Evaluation Metrics
- **Component Recall**: fraction of ground-truth components correctly identified
- **Connection Accuracy**: fraction of correct node-to-node connections in reconstructed netlist
- **Structural Fidelity Score (SFS)**: harmonic mean of component recall and connection accuracy
- Include formula as a LaTeX equation

### 4. Results

#### 4.1 Quantitative Comparison
- Include a results table: rows = models, columns = metric (Component Recall, Connection Accuracy, SFS), values = [PLACEHOLDER: X.XX]
- Table caption: "Model performance on schematic reconstruction benchmark (N=[PLACEHOLDER] schematics)"

#### 4.2 Qualitative Observations
- GPT-4o: [PLACEHOLDER: describe strengths/weaknesses]
- Claude: [PLACEHOLDER: describe strengths/weaknesses]
- Gemini: [PLACEHOLDER: describe strengths/weaknesses]
- Common failure modes: hallucinated components, incorrect node merging, inability to parse overlapping wires

#### 4.3 Effect of Schematic Complexity
- Simple circuits (≤5 components): high fidelity across models
- Complex circuits (>10 components): significant degradation
- Chain-of-thought prompting improves connection accuracy by [PLACEHOLDER: X%]

### 5. Discussion
- Models treat schematics as natural images, not symbolic graphs — this is the key limitation
- Component symbol recognition is reasonable; topological reconstruction is harder
- Code output (SPICE) reveals reasoning errors not visible in natural language descriptions
- Implications for EDA tooling and AI-assisted circuit documentation

### 6. Conclusion
- Confirmed hypothesis: AI can see schematic structure to varying degrees
- Best-performing model: [PLACEHOLDER]
- Key bottleneck: wire topology, not component recognition
- Future work: fine-tuned models on schematic datasets, hybrid CV+LLM pipelines

### Acknowledgment
- "This work was conducted as part of the Electrical Engineering and AI Hackathon (EEAI Hackathon)."

### References
- Provide 8 realistic placeholder references in IEEE format covering:
  1. A schematic recognition/OCR paper
  2. A multimodal LLM benchmark paper
  3. A SPICE simulation reference
  4. An LLM code generation paper
  5. A circuit understanding/EDA AI paper
  6. A KiCad or open-source EDA reference
  7. A vision-language model paper (e.g., GPT-4V, Gemini)
  8. A prompt engineering / chain-of-thought paper

## LaTeX Implementation Notes

- Keep all existing `\usepackage` declarations
- Replace the figure (`fig1.png`) reference with a placeholder figure showing a sample schematic — caption: "Example input schematic used in evaluation. [PLACEHOLDER: replace with actual figure.]"
- The results table should use the existing table environment, adapted to show model comparison data
- Include one equation for the Structural Fidelity Score (SFS)
- Remove all IEEE template guidance text (the red warning text at the end)
- Keep `\IEEEoverridecommandlockouts` as required by the class

## Output

Produce the complete replacement `conference_101719.tex` file. Every section must contain real prose, not placeholder instructions. Placeholders for data (numbers, names, versions) should be labeled `[PLACEHOLDER: description]` inline.
