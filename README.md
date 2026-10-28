# After Effects 25.6 — Complete Windows Learning Manual

An offline, **Linux- and Windows-readable**, step-by-step Windows After Effects **25.6** learning environment modeled on the organization and navigation of the supplied Factorio offline reference project. This is original instructional material, not an Adobe publication or a redistribution of copyrighted Adobe documentation.

## Begin here

1. **On Linux (recommended for reading):** extract the ZIP with your file manager or `unzip after_effects_25_6_windows_offline_manual.zip -d ae_manual`. Open `ae_manual/index.html` with a modern Firefox- or Chromium-based browser. No installation, server, JavaScript package, or internet is required for normal reading.
2. **On Windows:** extract the same ZIP in File Explorer and open `index.html` in a current browser. All After Effects menu, setup, and keyboard instructions in the manual refer only to Windows.
3. **Across Linux and a Windows VM:** browser progress is not synchronized between host and guest. Use **Progress & settings → Export progress (.json)** and **Import progress (.json)** to move it. Some Linux/Windows browser profiles may block or isolate local storage for `file://` pages; export regularly. If local storage is blocked, the manual remains readable and exports of progress still work.
4. **Fallback:** open `ALL_CONTENT.md` in a Markdown viewer for read-only, no-JavaScript access on either operating system.
5. Choose **Step-by-step walkthrough** and begin at Lesson 01. The six stages progress from START → FOUNDATIONS → INTERMEDIATE → ADVANCED → DELIVERY → CAPSTONE, with explicit end-of-stage readiness challenges. Complete each action in a real AE 25.6 project and check the step off in the guide.
6. Use **Deep topic library** when you need the reasoning behind an action, **Practical recipes** for complete production tasks, or **Effects / Shortcuts / Troubleshooting** as a desk reference.
7. When available, your progress is saved locally by the browser. Use **Progress & settings → Export progress** to back up your progress as JSON, and **Import progress** to restore it. This is not synced across browsers or PCs.

For a simple read-only guide, open **`ALL_CONTENT.md`** in any Markdown reader. The two CSV files provide searchable, sortable shortcut and effect directories. `manual_data.json` has the same content in structured form.

## What's included

- 35 ordered lessons in six monotonic difficulty stages, with explicit action sequences, experiments, self-checks, stage gates, and common errors.
- 78 technical deep-dives with multiple sections and practical experiments.
- 27 complete production recipes ordered by their suggested prerequisite lesson, 35 quiz questions, conceptual diagrams and a frame-count/export lab.
- Reference catalogs for native/bundled effects (285 entries), Windows key bindings and mouse gestures (373 entries), troubleshooting (67 entries), and a technical glossary (145 terms).
- Search, browse-by-category, reading preferences, optional one-step-at-a-time mode, lesson completion tracking and progress backup/restore.
- Original editable sources plus a reproducible, standard-library-only Python build and validation scripts.

Counts are reported from `manual_data.json`; they can change when the sources are revised and rebuilt.

## Version and platform rules

- The **application lessons** target **Adobe After Effects 25.6**, released November 2025, **on Windows**, with the default English shortcut layout. The **offline reader** is platform-neutral HTML and Markdown, designed for Linux and Windows.
- Use a security-patched 25.6.x build where available; Adobe security bulletin APSB26-78 (14 July 2026) identifies 25.6.6, after updates 25.6.4 and 25.6.5. Applying security patches does not mean using 26.x features.
- The supplied starter AE note documents **26.5**. It was used only as a coverage/terminology seed. Items introduced after 25.6 are intentionally removed from instructions and isolated in the version-audit notes.
- Adobe's online documentation evolves with later versions. The 25.6 release history and version-specific system requirements are used for feature gating; current Adobe articles are references, not proof that every described UI control existed in 25.6.
- Some less-common shortcuts are panel-specific, may be remapped, or are ambiguous across Adobe's references. **Edit → Keyboard Shortcuts** in the installed 25.6 program is the final check.
- The effects list is a *broad orientation directory*, not a promise that all effect variants or legacy plug-ins are installed, nor a per-parameter catalog for third-party products. Check **Effects & Presets** in your own build.
- Media, fonts, plugins, codecs, GPU hardware, source footage, and project settings affect actual outputs. Test important techniques in the version you have installed and inspect final renders.

Not part of 25.6: features originating in the 26.x series such as Quick Apply, Object Matte, native SVG-to-shape import, native parametric meshes, Unmult, Curl Noise, advanced 3D in-engine depth of field, variable-font-axis animation, revised 26.5 guides, or the 26.5 bundled ACES 2.0 configurations.

## Folder guide

| File | Purpose |
|---|---|
| `index.html` | Single-file offline browser manual, recommended first entry point |
| `ALL_CONTENT.md` | Whole written guide for Markdown readers and print workflows |
| `manual_data.json` | Machine-readable content and provenance |
| `MANIFEST.sha256` | SHA-256 checksums of all ZIP payload files (except the manifest itself); on Linux run `sha256sum -c MANIFEST.sha256` in the extracted folder |
| `shortcuts.csv`, `effects.csv` | Standalone reference indexes |
| `content.py` | Authoring source for curriculum, topics, recipes, extra glossary/troubleshooting, quiz and sources |
| `data/*_seed.json` | Curated reference collections from the provided AE note, expanded for the 25.6 manual |
| `web/template.html`, `web/styles.css`, `web/app.js` | Single-file app source |
| `build.py`, `validate.py`, `tests/test_manual.py`, `tests/browser_logic.cjs` | Generation, verification and structural tests |
| `AUDIT.md` | Version boundary, sourcing decisions, coverage and limitations |
| `AGENT_HANDOFF.md` | Notes for future guide editors |
| `tools/curate_starter.py` | Optional one-time inventory extraction from a user-supplied AE note; not needed to rebuild |

## Rebuild and verify

On Linux or Windows with Python 3.10+ (authoring/rebuilding only; NOT needed to read):

```text
cd /path/to/ae_manual  # Linux; or cd to the extracted folder on Windows
python build.py
python validate.py
python -m unittest discover -s tests -v
```

Optional on any operating system with Node.js installed (not required for reading): `node --check web/app.js` and `node tests/browser_logic.cjs` run JavaScript syntax and simulated route/state tests. They do not replace a real-browser test.

The builder requires no third-party Python packages or web access and recreates the `index.html`, reference exports and ZIP. Do not edit these generated files directly; make lasting content edits in `content.py`, `data/*.json`, or `web/*` and rebuild.

## Source and safety policy

Links inside the offline manual lead to public Adobe documentation if you click them; the manual itself makes **no network requests**. There are no external fonts, JavaScript libraries, telemetry, embedded third-party files, or proprietary teaching videos. Your lesson checks and quiz answers stay in browser storage unless you explicitly export the progress JSON.

This manual is a substantial learning foundation, but it has **not** been run against every menu, installed plug-in, media format, renderer or possible Windows hardware combination in a live AE 25.6 installation. For a discrepancy, prefer your installed application, then Adobe's historically relevant documentation and release history.

## Second-pass audit notes

The revised edition corrects an opacity-keyframe teaching sequence, fills gaps in the effects reference (including expression controls, 3D Camera Tracker, Echo, CC Rainfall and CC Snowfall), improves navigation in the Markdown manual, clarifies cross-platform reading, protects malformed URL fragments, and uses exact non-integer broadcast frame rates in the calculator. Runtime browser automation was restricted in the auditing environment; HTML/JS and data checks are supplied, but live browser/device testing and every AE 25.6 UI action remain unverified. See `AUDIT.md`.

## Final pass changes (28 October 2026)

- Reordered the old scripting lesson ahead of rendering and delivery, preserving internal lesson IDs and exported progress keys while renumbering displayed lesson headings.
- Added a six-stage learning roadmap, practical readiness challenge for each stage, and suggested prerequisites for recipes; these are advisory, not artificial access locks.
- Fixed an ineffective timeline trim exercise and clarified the single-layer-only “Leave all attributes” precomposition option.
- Corrected the 25.6.x security-patch reference to Adobe’s July 2026 25.6.6 bulletin.
- Split combined effect categories into clearer filters.
- Revalidated all built files and the ZIP. Browser runtime smoke testing was attempted but blocked by the execution environment for both local file and local HTTP origins, so actual Linux/Windows browser behavior and live AE execution are not certified.
