# Source files (not patient-facing)

Build sources for SDG pages and PDFs. Nothing here contains patient information.

- `plan-builder/` builds `/plan/index.html` (the Plan Builder).
  - Edit `template.html`, then run `python3 build.py` to inline fonts and the logo into `sdg-plan-builder.html`, and copy that to `/plan/index.html`.
  - Packet content (pages, community items, closing line) lives in the `CONTENT` object near the top of the script in `template.html`. Modules: cover, plan, details, obstacles, community.
  - The builder reads only the text after "PATIENT-FACING DRAFT" in a pasted Heidi note.
- `workbook/` builds My 2027 Vision and My 2027 Planning Pages (printable via `render.js`, fillable via `fill.js`).
- `rd-checklist/` builds the one-page RD in-session checklist.
- `rd-training-pdf/` builds the branded PDF of the RD Session Guide from a markdown export.

Fonts are the @fontsource packages (Cormorant Garamond, Josefin Sans, Mulish); update the font paths in each build script to wherever they are installed.
