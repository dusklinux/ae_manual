# Guide maintenance handoff

## Purpose

Continue an offline-first Windows-only learning application for **After Effects 25.6**. Do **not** gradually add current/latest-version features. The user explicitly asked for the 25.6 edition, despite supplying a 26.5 personal note as a starting point.

## Authoring hierarchy

1. `content.py`: `SOURCES`, ordered `CHAPTERS` built with `lesson()`, `TOPICS` with `topic()`, `RECIPES` with `recipe()`, and extra glossary/troubleshooting/quiz data.
2. `data/*.json`: curated reference catalogs, with durable IDs.
3. `web/template.html`, `web/styles.css`, `web/app.js`: browser UI; must work from `file://` and make no network requests.
4. `build.py`: builds all deliverables and ZIP. `validate.py` plus unittest verify outputs.
5. `index.html`, `ALL_CONTENT.md`, `manual_data.json`, CSVs and ZIP: **generated; don't hand-edit**.

## Invariants

- Platform Windows only. Shortcuts are Windows defaults or explicitly contextual gestures; label a newly assigned shortcut as custom.
- Curriculum must remain beginner → intermediate → advanced. A lesson includes >=5 actionable steps, a self-check, an independent experiment, common errors, deep-topic references and source keys.
- Topic has multiple explanatory sections, an experiment and pitfalls. Recipe has an explicit verification and a recovery instruction.
- Preserve stable ID strings; they key learners' locally saved progress. If IDs change, provide a migration (edition field) and document it.
- Every externally sourced version fact must distinguish the original release from later revisions to Adobe's rolling Help pages.
- The reference catalogs are substantial but should not make false statements about unverified third-party plug-in availability.
- Full HTML bundle must work offline: no CDN, external JS/CSS, auto-fetch requests, tracking, fonts, iframes or images.
- Avoid promoting post-25.6 features. Key future-feature exclusions: Quick Apply, Object Matte, Curl Noise, native parametric meshes, SVG native import, Unmult, new 26.0 audio effects, 26.2 Proportional Scrubbing, 26.3 advanced 3D depth of field, 26.5 ACES 2.0 configurations and 26.5 guide changes.

## Build and audit

```powershell
python build.py
python validate.py
python -m unittest discover -s tests -v
```

To validate interactive behavior: open the `file:///.../index.html` path in Windows Chromium/Edge, navigate Overview → first Lesson, check a step, reload, confirm progress persists; search for `graph editor`; browse effects filter, test quiz choice, test numeric frame lab and export/import progress. Verify all features without internet.

## Good next improvements

- Capture version-specific screenshots from an appropriately licensed AE 25.6 Windows installation (do not bundle third-party images without rights).
- Trial the complete 35-lesson curriculum on actual 25.6 and mark UI exactness for each lesson.
- Add per-effect parameter references only after verifying the native/bundled installed effect menus in 25.6.
- Add packaged **original** sample footage/shapes/design templates if the owner requests them and licensing is confirmed.
- Add accessible diagrams/keyboard alternates, while maintaining the single-file and offline constraints.

## Source responsibility

Treat user-supplied Factorio project as a format/workflow reference, never copy its unrelated game-specific content. Treat the AE 26.5 note as an annotated coverage seed, not a 25.6 feature-availability authority. Additional version evidence is in `AUDIT.md` and `content.py → SOURCES`.
