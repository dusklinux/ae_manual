# Scope, coverage, evidence and verification audit

**Application:** Adobe After Effects **25.6**, Windows only, default English keyboard.  
**Version introduced:** November 11, 2025.  
**Research cutoff:** October 28, 2026.  
**Nature:** Independently authored learning manual, adapted from the supplied offline Factorio package's *design principles* and the supplied AE note's *topic coverage*. This is not Adobe-certified training.

## What was inspected

- The supplied Factorio offline package: single-HTML offline app, structured datasets, guided lessons, quick lookup, agent notes, deterministic build/validation design.
- The supplied AE Notes markdown: source mental models, shortcut families, effects inventory, 3D and compositing workflows, expressions, troubleshooting and practice. That document targets **AE 26.5** and therefore contains post-25.6 functionality.
- Adobe 25.6 release announcement, Adobe-maintained feature history and 25.x Windows technical requirements.
- Official Adobe manuals for keyboard shortcuts, expressions, effects, color/OCIO, Motion Graphics templates, memory, multiframe rendering and troubleshooting. These are continuously updated, so they must be checked against the version history before describing a 25.6 UI capability.

## Version boundary decisions

| Version | Relevant additions | Treatment in this manual |
|---|---|---|
| 25.2 | Improved preview system, FBX support and 3D/color workflow changes | Included where useful; verify exact renderer limits |
| 25.3 | Improved composition zoom behavior | Included in general viewing guidance |
| 25.4 | Quick Offset; copying/pasting text formatting | Covered as 25.6-available |
| **25.6** | Multiple 3D-layer gizmo behavior, default camera settings, tips and timeline close commands | Target edition |
| 26.0 | Native parametric meshes, Substance materials, Unmult, new audio effects, variable-font axis animation, native SVG-to-shape import | Excluded |
| 26.2 | Object Matte, Quick Apply, Proportional Scrubbing | Excluded |
| 26.3 | Curl Noise, new Mask Tracker behavior, in-engine Advanced 3D depth of field, clipboard frame capture | Excluded |
| 26.5 | Revised guides, effect color labels, bundled OCIO 2.5.1/ACES 2.0 | Excluded |

The document is not silently updated to 26.5 even where the source notes cover it in detail. Abbreviations and older features are kept only where compatible with 25.6.

## Detailed learning coverage

- **Orientation:** install, panels, compositions, source media, pixel channels, file organization.
- **Animation:** keyframes, space/time interpolation, graphs, paths, easing, motion blur, speed curves, layer timing, time remapping.
- **Drawing and text:** masks, shape operators, path edits, text animators, typography, design systems.
- **Compositing:** alpha, mattes, blending, keying, masks, roto, color, premultiplication, integration/grain.
- **Motion and 3D:** track/planar track, camera track, stabilization, parenting, expressions, 3D cameras, lights, renderer distinctions, 3D assets.
- **Technical:** effects chains, expressions, data, motion-graphics templates, JavaScript/ExtendScript concepts, previews, caches, multi-frame rendering, audio, color-management decisions, video masters/alpha, portability.
- **Reference:** extensive keyboard catalog, effect explanations, glossary, repeated troubleshooting patterns, practical projects and review quizzes.

## Checks by this package

`validate.py`, `tests/test_manual.py` and `tests/browser_logic.cjs` establish that every lesson is actionable, link targets are valid, no known post-25.6 effect labels slip into the effects directory, no macOS shortcuts appear, both JSON and embedded HTML match, ZIP content is complete and exports are structurally parseable. Optional browser smoke tests are described by the developer notes and may be performed when a browser automation runner is available.

## Limits / nonclaims

- **Not live-product certified:** no licensed AE 25.6 application was available to execute all steps against every Windows variant, user preset or installed plug-in.
- **Not mathematically exhaustive:** no finite static guide can reproduce every property of every plug-in, every scripting API and all external formats. The effects directory is a learning-oriented lookup.
- **Compatibility:** shortcut bindings depend on panel focus, input language, custom presets and keyboard hardware. Punctuation keys in particular should be checked in the application.
- **Third-party dependencies:** Mocha AE, Cinema 4D integration and external encoders or file types may vary by AE license, plug-in bundles, installation and workflow.
- **Network:** offline app doesn't load external resources; clicking source links is intentional internet browsing.
- **Copyright:** source material was used as research/context. No Adobe proprietary documentation pages, images, license assets or plug-in binaries are bundled.

## Primary sources

- [Adobe 25.6 announcement](https://community.adobe.com/announcements-527/after-effects-25-6-is-now-available-to-download-60888)
- [Adobe-maintained AE feature history](https://github.com/AdobeDocs/after-effects-feature-history)
- [Adobe AE 25.x Windows requirements](https://helpx.adobe.com/after-effects/desktop/get-started/technical-requirements/2025.html)
- [Adobe AE keyboard shortcuts](https://helpx.adobe.com/after-effects/desktop/get-started/keyboard-shortcuts/keyboard-shortcuts-reference.html)
- [Adobe AE effects reference](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html)
- [Adobe AE help index](https://helpx.adobe.com/after-effects/desktop.html)

The UI's **Version / sources / audit** tab includes the complete topic-associated source list.

## Second pass — 28 October 2026

### Confirmed and repaired

- **Linux/Windows reader** explicitly supported; the actual AE curriculum remains Windows-only. Offline `index.html` uses relative/inline resources only and does not depend on operating-system font paths, Windows APIs, or an HTTP server. Browser storage may be restricted with `file://`, and progress must be exported/imported when moving between Linux and a Windows virtual machine. The Markdown edition is a fallback.
- **Lesson 06** now creates an initial Opacity keyframe at time zero before changing the second value; the previous sequence risked teaching a constant change rather than a fade.
- **Effects directory** expanded with missing official families: expression controllers, camera tracking, rain/snow, VR, legacy compatibility, time, text, transition and utility effects. Entries remain concise descriptions, not per-parameter claims. Adobe's effect list is rolling, so entries not certified in an installed 25.6 are explicitly labeled for local verification.
- **Navigation/precision**: Markdown topic cross-links, safe treatment of malformed URL fragments, standard browser scroll behavior, exact 24000/1001 and 30000/1001 calculator rates; dropped fractional-frame rows from the quick timing table.
- **Version security**: Adobe bulletin APSB26-15 documents updates affecting 25.6 and earlier builds, including 25.6.4; security patches within 25.6.x do not authorize 26.x-only features.

### What validation cannot prove

Byte-level ZIP integrity, SHA-256 manifest checks, rebuild reproducibility, structured links, JavaScript syntax, CSS and HTML embedding, JSON/CSV parity and the reading platform's lack of external assets can be validated automatically. These checks cannot establish that every shortcut works with a particular Windows keyboard preset, every effects panel is present in a particular AE build, or a 3D render succeeds with virtualized GPU drivers. Live Chromium navigation was blocked by the available execution environment during the second pass. No claim of actual Linux browser E2E or licensed After Effects run is made.

## Final macro + micro audit — 28 October 2026

**Curriculum:** reorganized into strictly ascending START (5 lessons), FOUNDATIONS (8), INTERMEDIATE (11), ADVANCED (6), DELIVERY (4) and CAPSTONE (1). The former lesson 34 (scripts) now appears as lesson 30, before rendering and delivery. Stable IDs and step indices preserve existing exported progress. Each stage has a self-directed challenge, and recipes are now sorted by suggested prerequisite lesson. The levels are guidance rather than restrictions.

**Instruction-level corrections:** fixed the timing lesson's unproductive same-playhead move/trim comparison; improved a source-instancing lab to use assets actually created in the prior steps; and fixed the precompose lesson's misleading multi-layer choice. Adobe documents that *Leave all attributes* is unavailable for multiple selections or shape/text layers. See source key `precompose`.

**Patch accuracy:** Adobe's July 14, 2026 bulletin APSB26-78 gives version **25.6.6** as the 25.6-series update, superseding the previously highlighted 25.6.4 security guidance. The 25.6 lesson feature boundary remains November 2025.

**Catalog organization:** split a mixed Stylize/Time/Transition effects category into actual technique families, retaining IDs so references remain stable. Counts are not proof of exhaustive installed-effect coverage; many entries are compatibility-only or require local verification in a licensed AE 25.6 installation.

**Testing scope:** tests of source schemas, references, version prohibitions, link routes, all-generated export consistency, ZIP manifest and JavaScript syntax are executable locally. A real Chromium browser smoke test was attempted on `file://` and `http://127.0.0.1` but navigation was blocked by administrative execution policy, not an observed app crash. Live AE 25.6 Windows VM instructions and different Linux browser/storage configurations remain unverified. Do not describe this package as fully certified in either environment.
