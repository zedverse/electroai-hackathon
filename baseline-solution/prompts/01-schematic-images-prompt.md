# Prompt: Collect Electronic Schematic Images of Increasing Complexity

## Task

Find and download 10 images of electronic schematics that span a complexity range from approximately 5 components to approximately 25 components, in roughly equal steps.

## Steps

1. **Create the output directory** `baseline-solution/data/schematics/` (create parent directories as needed).

2. **Find the images.** Search the web for freely usable electronic schematic images (prefer Creative Commons, public domain, or open-hardware sources). Target the following approximate component counts, one image per count:

   | # | Approx. components |
   |---|--------------------|
   | 1 | 5                  |
   | 2 | 7                  |
   | 3 | 9                  |
   | 4 | 11                 |
   | 5 | 13                 |
   | 6 | 15                 |
   | 7 | 17                 |
   | 8 | 19                 |
   | 9 | 22                 |
   |10 | 25                 |

3. **Download each image** and save it to the output directory using this naming convention:

   ```
   <component_count>-<brief-description>.<ext>
   ```

   Examples:
   - `05-rc-low-pass-filter.png`
   - `13-555-timer-astable.png`
   - `25-audio-amplifier.png`

   Zero-pad the component count to two digits so files sort correctly.

4. **Verify** each downloaded file is a valid image (non-zero size, readable). If a download fails or the image is not clearly a schematic, find a replacement before moving on.

5. **Produce a summary table** listing each file, its source URL, the licence, and the actual component count you estimated from the image. Save this as `baseline-solution/data/schematics/README.md`.

## Constraints

- Use only images that are freely usable (Creative Commons, public domain, open-hardware, or explicitly licence-free). Record the licence for each image in the README.
- Images must be actual circuit schematics (symbol-and-wire diagrams), not photographs of physical PCBs or breadboards.
- Prefer PNG or SVG; accept JPG if no better format is available.
- Do not include duplicate circuits or trivial variations of the same design.

## Done

When all 10 images are downloaded and the README is written, add an entry to `work-diary.md` describing what was collected and sign it.
