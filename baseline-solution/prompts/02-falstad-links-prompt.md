# Prompt: Analyse Schematics and Generate Falstad Links

## Context

Read the following for background before starting:
- `work-diary.md` — project history and decisions
- `baseline-solution/prompts/01-schematic-images-prompt.md` — how the schematic images were collected and named
- `baseline-solution/data/schematics/README.md` — summary table of downloaded images (filename, source, licence, component count)

## Task

For each schematic image in `baseline-solution/data/schematics/`, analyse the circuit and produce a working Falstad circuit simulator link that recreates it. Collect everything into a single Markdown page at `baseline-solution.md` in the repository root.

## Steps

### 1. Analyse each schematic image

For each image file (sorted by filename, i.e. by increasing component count):

- Identify every component in the schematic: type, value, and how it is connected.
- Build a complete netlist description of the circuit (nodes, component types, pin connections).

### 2. Generate a Falstad link

Falstad circuits are encoded as a compressed, URL-safe string in the fragment of `https://www.falstad.com/circuit/circuitjs.html#`. The encoding format is:

1. Write the circuit as a Falstad plain-text circuit file. Each line is one element, for example:
   ```
   $ 1 0.000005 10.20027730826997 50 5 43 5e-11
   r 160 128 160 240 0 1000
   c 160 240 160 352 0 1e-5 0
   g 160 352 160 400 0 0
   v 160 128 160 400 0 0 40 5 0 0 0.5
   o 1 64 0 4099 5 0.025 0 2 1 3
   ```
2. Compress the text with `zlib` (deflate, level 9).
3. Base64-encode the compressed bytes using the URL-safe alphabet (`-` and `_` instead of `+` and `/`), no padding.
4. Append as the URL fragment: `https://www.falstad.com/circuit/circuitjs.html#<encoded>`

Write a small script (Python or Node.js) to perform steps 2–4 given the plain-text circuit. Run it for each circuit and verify the resulting URL is well-formed.

If you cannot faithfully reconstruct a circuit from the image, produce the closest reasonable approximation and note the discrepancy.

### 3. Write `baseline-solution.md`

Create `/home/daniel/git/electroai-hackathon/baseline-solution.md` with the following structure:

```markdown
# Baseline Solution — Electronic Schematic Analysis

## Overview

<Brief paragraph describing the dataset: 10 schematics, complexity range 5–25 components,
source information, and the goal of the Falstad reconstructions.>

## Schematics

For each circuit, one section in order of increasing complexity:

---

### <component_count> — <Circuit Name>

**File:** `baseline-solution/data/schematics/<filename>`  
**Components:** <actual count>  
**Licence:** <licence from README>  
**Source:** <source URL from README>

<img src="baseline-solution/data/schematics/<filename>" alt="<Circuit Name>" width="600">

**Circuit description:** <2–4 sentence description of what the circuit does.>

**Falstad simulation:** [Open in Falstad](<falstad URL>)

---
```

Repeat the section block for all 10 images.

### 4. Validate

- Open (or `curl`) each generated Falstad URL and confirm it returns HTTP 200 and loads the circuit page.
- Check that every image renders at a sensible width (scale down with `width="600"` if needed; use a smaller value if the image is naturally narrow).

## Done

When `baseline-solution.md` is written and all links are validated, add an entry to `work-diary.md` describing the analysis, the reconstruction approach, and any circuits that required approximation. Sign the entry.
