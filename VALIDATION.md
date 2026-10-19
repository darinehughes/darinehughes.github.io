# Portfolio verification — 2026-10-19

## Reviewed refresh

The initial five-project refresh was reviewed on desktop and mobile, including image loading, keyboard skip/focus, native anchors, contact URLs and social metadata. Widths 320, 390, 768 and 1440 had no horizontal overflow. The computed text contrast audit had no failures (minimum 5.06:1). Existing icons, identity, domain settings and the unlinked legacy HTML were preserved. There is no framework build or existing test suite; the site is buildless HTML/CSS.

## Loaded-video DebriefScape replacement

- Actual unchanged local DebriefScape distribution rendered through an isolated Playwright Chrome profile with requests restricted to localhost. Native OPFS fixture files were passed to the app's existing folder loader; its actual player, CSV parsers, timeline and legend rendered the result. Existing browser profiles, sessions and source-project files were not changed.
- Video: 1920 × 1080, duration 30.036 seconds, paused at approximately 18.77 seconds, `readyState: 4`. A decoded bird-on-branch frame is visible, with no loading spinner or toast. Two synthetic annotation tracks are shown. No participant, interview or research footage was used; no recording or facial analysis was run.
- Source capture: 1920 × 1474; public crop: 1920 × 1321. WebP variants at 640, 1280 and 1920 pixels regenerated, quality 86. Intrinsic HTML dimensions updated to 1280 × 881. Descriptive alt text and visible sample-film attribution/license added.
- Desktop 1440 × 1000, phone 390 × 844, and narrow 320 × 844: image decoded, synthetic-demo caption and CC BY 3.0 credit present, no horizontal overflow. Desktop and phone section screenshots inspected. Browser page-error log empty. These are browser viewport checks, not physical-device or screen-reader certification.
- `python tools/check_site.py`: pass (five project anchors, unique ids, local references, responsive sources, image alt/dimensions/loading, email and social image).
- `git diff --check`: pass.
- All assets including every responsive variant, logo and social preview total 1,116,293 bytes. Visitors request selected variants, not every variant.
- The DebriefScape replacement preserved the approved CSS, other project views, and the rest of the reviewed page design. Its scope was the DebriefScape media/caption/dimensions/alt and supporting documentation; subsequent focused changes are recorded below.

## Publishing configuration

The user explicitly approved publication after replacement and verification. Authenticated GitHub Pages API read confirmed `build_type: legacy`, source branch `main`, path `/`, public site, HTTPS enforced, and CNAME `null`. The existing `hughesvr.com` redirect points to `darinehughes.github.io`; no domain/DNS change is needed.

Publish by fetching/reconciling `main`, merging the reviewed branch through normal Git, and pushing `main`. Confirm the Pages build's commit and success status, then compare served HTML and the replacement asset at both requested public URLs. Publication evidence is recorded in the task's output handoff after deployment.

## Martin hero and sample AICS conversation — 2026-10-19

- Martin is shown in a cropped existing clean ABA runtime capture (source 1200 × 900, hero 920 × 690). Hero source, alt and caption updated; 640/920-pixel WebP variants generated without upscaling. Desktop and mobile keep the reviewed 4:3 framing.
- A fresh synthetic AICS scenario demonstration was conducted through the real public Ryan 3D interface, using two typed turns. The returned replies are real responses from that session. Screenshot source 1440 × 1100, crop 1180 × 959; 640/1180-pixel WebP variants regenerated. No private transcripts or fictional replacement dialogue.
- The image is labeled **Sample training conversation**. Four dialogue turns are copied into a semantic HTML description list below the image for legibility at smaller widths. Automated comparison to the captured transcript passed, normalizing only HTML formatting whitespace.
- Rendered reviews at 1440 × 1000 and 390 × 844 inspected: Martin's face/raised hand/environment are visible; Ryan and the conversation appear together; the HTML excerpt remains readable. Additional 320 and 768 width checks passed. Images decoded at each width; no horizontal overflow or browser page errors. Existing larger-image links and navigation retained.
- Byte-for-byte section comparisons confirm TeachLivE, FLITE, DebriefScape, Pantheon, About and Contact HTML unchanged. Existing CSS rules unchanged; new rules apply only to the transcript excerpt. Classroom and feedback asset bytes are unchanged. The feedback caption explicitly identifies a separate development test.
- Static checker and `git diff --check` pass. The complete asset set across all responsive variants totals 1,116,293 bytes; visitors load selected variants. Provenance, source hashes and the exact demonstration exchange are recorded in `ASSET-PROVENANCE.md`.
- Pages source reconfirmed as `main` / repository root, legacy build, HTTPS enforced, no CNAME. The user approved both focused updates for publication.
