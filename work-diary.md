# Work Diary

## 2026-03-26

- Added an EEAI-adapted starter prompt in `prompts/01-prompt-starter.md`.
- Added a root `.gitignore` entry for `tmp/`.
- Moved repository notes into `docs/notes.md`.
- Established this work diary to track repo changes and implementation decisions.

## 2026-03-27

- Added briefing, slide, and problem statement materials in `docs/`.
- Added research and planning prompts in `prompts/` for literature survey, software survey, gap analysis, and problem statement generation.
- Added survey and gap-analysis outputs in `reports/`, including standardised engineering software AI survey filenames.
- Prepared the repository for initial version control setup and remote push.
- Formatted `reports/03-gemini-report.md` into structured Markdown with headings, tables, and bullet lists.
- Actioned `prompts/04-gap-analysis-prompt.md`: produced `reports/04-claude-gap-analysis.md` synthesising all six survey reports into a four-tier landscape model with gap findings and hackathon recommendations.
- Actioned `prompts/05-problem-statement-prompt.md`: produced `docs/05-claude-problem-statement.md` with full problem statement, justification bullets, acceptable student directions, and scope guardrails.
- Actioned `prompts/06-short-problem-statement-prompt.md`: produced `docs/06-claude-short-problem-statement.md` with short (~200 word), ultra-short (3 sentence), and one-sentence versions.
## 2026-03-29

- Created `prompts/08-registration-page-prompt.md` to adapt the Clinical AI registration form for the ElectroAI Hackathon.
- Generated the ElectroAI Hackathon registration page content in `docs/electroai-hackathon-registration-page.md`, specifically tailored for Electrical Engineering students but open to all.
- Created a plain-text version of the registration page in `docs/electroai-hackathon-registration-page.txt` for direct use in online forms.
- Integrated the official registration link (`https://forms.gle/MaSj5SV3j6uy6H8x7`) into `README.md`, the registration Markdown page, and the plain-text copy.
- Updated the registration page eligibility to emphasize that while designed for EE students, all participants are welcome.
- Created `prompts/09-route-logistics-report-prompt.md`, a placeholder prompt for generating route logistics reports (resupply and public transport egress).

## 2026-04-02

- Expanded `README.md` with a detailed hybrid event schedule covering Tuesday to Friday sessions, the allnighter, room allocations, leads, Teams usage, and presentation timing.
- Rewrote the README success criteria and outputs/judging sections to match the ElectroAI Hackathon brief, including the IEEE-style paper requirement and clearer engineering-focused judging language.
- Cleaned up the README presentation by left-aligning the splash image, removing outdated wording, and aligning the embedded master-prompt success criteria with the main judging criteria.
- Copied judging rubric materials from the temporary Clinical AI Hackathon workspace into `judging/electroai-hackathon/`, including source criteria, source prompt, rendered HTML, and PDFs.
- Rebranded the main judging rubric for ElectroAI Hackathon, updated the date to `10 April 2026`, changed the listed judges to Dr Dave Muir, Leotis Buchanan, and TBA, and regenerated the printable PDF.
- Copied `hackathon-prize-vouchers.html` and `hackathon-prize-vouchers.pdf` into the repo root, rebranded them for ElectroAI Hackathon, replaced old winner-specific text with placeholders, updated presenter names, and regenerated the voucher PDF.
- Added a high-priority TODO item in `TODO.md` to create the Gemini CLI, Codex, and Claude Code install page for participants.

## 2026-04-07

- Cloned `git@github.com:dsikar/ElectroAIHackathonIEEETemplate.git` into the repo as the base for the hackathon IEEE paper.
- Wrote `prompts/10-latex-paper-schematic-ai-prompt.md` specifying the full structure, models, metrics, and LaTeX implementation notes for the research paper.
- Actioned the prompt: rewrote `ElectroAIHackathonIEEETemplate/conference_101719.tex` as a publishable-quality IEEE conference paper titled "Can AI See Structure in Schematics? A Comparative Evaluation of Multimodal Models for Circuit Diagram Understanding and Reconstruction".
- Paper compares GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, and GPT-4/Codex on schematic-to-netlist reconstruction tasks, introduces the Structural Fidelity Score (SFS) metric, and includes 8 real references. Data placeholders are labelled `[PLACEHOLDER: ...]` for completion after experimental runs.
- Pushed commit `e64edd9` to `origin/main` on the IEEE template repo.

### Daniel

Tested the four models on the task of finding downloadable schematic datasets and links. Grok was the standout — it returned actual usable URLs to schematic repositories and download pages. Claude, Gemini, and ChatGPT all produced lists of sources that looked plausible but contained broken links, paywalled resources, or hallucinated dataset names that do not exist. For the schematic sourcing step in the paper, Grok should be the first tool to reach for.

### Daniel

Tested Grok, Gemini, Claude, and ChatGPT on generating Falstad circuit simulator schematics. Claude was the best — it produced valid Falstad-format output that loaded correctly in the simulator. The other models either generated incorrect syntax, produced incomplete definitions, or output formats that could not be imported into Falstad without significant manual correction.

## 2026-04-07

- Collected and downloaded 7 electronic schematic images of increasing complexity (5 to 35 components) to `data/schematics/images/`.
- Moved the IEEE paper template example `ElectroAIHackathonIEEETemplate.pdf` from Downloads to `ElectroAIHackathonIEEETemplate/`.
- Updated the root `README.md` with a new subheader "IEEE Standard Article with Findings" and a link to the example PDF.
- Cleaned up extraneous text from the end of the root `README.md`.

*Signed: Gemini CLI*

## 2026-04-07

- Actioned `prompts/01-schematic-images-prompt.md` and `prompts/02-falstad-links-prompt.md`: analysed 6 schematic images in `baseline-solution/data/schematics/images/` (skipping `05-temperature-monitor.png`).
- Wrote `baseline-solution/scripts/gen_falstad_urls.py` to encode plain-text Falstad netlists via zlib + URL-safe base64.
- Produced working Falstad simulation links for: dual LED flasher (astable multivibrator), triac timer (DC control section), LED chaser (NE555 astable), transistor equaliser (3-stage CE), simple push-pull inverter, LM386 mini amplifier.
- Created `baseline-solution.md` at the repo root with an intro, per-circuit subheaders, embedded schematic images (width 600), and each Falstad link embedded as "Link to circuit".
- Circuits using ICs not natively in Falstad (CD4017, LM386, TRIAC) are noted as functional approximations.

*Signed: claude-sonnet-4-6*

## 2026-04-07

- Cloned `https://github.com/EndryuN/Image2Spice` into `baseline-solution-1`.
- Updated the root `README.md` to include a note about `baseline-solution-1` and its contributor, Andrew Nguyen (MSc Data Science student).
- Fixed image paths in `baseline-solution/baseline-solution.md` following the directory move.
- Added `prompts/11-fix-baseline-solution-images-prompt.md`.
- Added external GitHub links for both the Image2Spice repository and the IEEE LaTeX template repository to the root `README.md`.
- Pushed all changes to the remote repository.

*Signed: Gemini CLI*
