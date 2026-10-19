# Portfolio image provenance

Selected and inspected on **2026-10-19**. Images are real application captures or existing public interface examples. No generated replacement interfaces or stock images were added. All served assets live in `assets/`; WebP derivatives use quality 86 and widths up to 640, 1280, or 1920 pixels without upscaling. Linked larger views keep small interface text available on phones.

| Asset stem | Source and capture date | Context and treatment |
| --- | --- | --- |
| `aics-3d` | Public AICS 3D Ryan scenario at `https://aics-sim.com/3d/?persona=ryan&activity=scenario&scenario=airline_unruly_passenger_deescalation`, fresh capture 2026-10-19 at 1440 × 1100 | User-authorized synthetic demonstration: two typed participant turns and actual returned Ryan replies. Character and conversation are captured together. Crop `(130,75,1310,1034)` yields 1180 × 959; variants 640 × 520 and 1180 × 959. The four visible dialogue turns are also copied faithfully into accessible HTML. No private transcripts, generated replacement dialogue, or UI reconstruction. |
| `aics-feedback` | `C:/dev/aics/site/beta/ryan-animation-preview/review/current-audit/cooperative-analysis.png`, existing capture 2026-09-27 (file timestamp), inspected 2026-10-19 | Synthetic development exercise with the Ryan persona. Crop to the results panel excludes the review header and blue inspection outline. Caption explicitly identifies a development test. No learner identity or private conversation. |
| `teachlive` | `C:/dev/TeachLivE-Builds/ABA-Absence-Fix-20260905-231931/Evidence/highschool-runtime.png`, existing runtime evidence 2026-09-05 | Full clean classroom frame, five virtual students; no real students or debug overlay. Existing local runtime evidence reused under the user's request to feature the work. TeachLivE attribution stays with the collaborative UCF platform. |
| `martin-aba` | `C:/dev/TeachLivE-Builds/ABA-Prop-Startup-Fix-20260905-223253/Evidence/runtime-high-five.png`, existing runtime capture 2026-09-05; selected 2026-10-19 | Martin raising a hand in the ABA furnished-room scene. Source project identified by adjacent `console-reentry.txt`: `C:/dev/TeachLivE-Unity-eric/Assets/Scenes/ABA TRAINING/ABA_Training.unity`; adjacent `runtime-MP_KMartin_*` captures corroborate actor identity. Crop `(140,130,1060,820)` makes Martin clearer while retaining his environment; WebP variants 640 × 480 and 920 × 690. Hero only; classroom capture remains in the TeachLivE section. No Unity instance launched, source edited, or running work interrupted. |
| `flite` | `https://flitestemcoaching.org/`, captured 2026-10-19 at 1440 × 1000 | Public resource suggestions for the ordinary keyword `feedback`. No search or contact form submitted. Crop retains navigation, search, and resource suggestions. The thumbnail inside the original website is part of that product capture; it is not presented as Hughes Virtual product evidence on its own. |
| `debriefscape` | Actual local DebriefScape build at `http://localhost:8767/CREST/DSCAPE/beta/`, captured 2026-10-19 at 1920 × 1200 with a full-page output of 1920 × 1474 | Loaded video paused at 18.77 seconds, decoded and ready (readyState 4), with two synthetic annotation tracks and the actual tag legend. Crop `(0, 69, 1920, 1390)` removes the standalone-mode banner and bottom unrelated control; no interface reconstruction. WebP variants: 640 × 440, 1280 × 881, 1920 × 1321. No participant data, loading state, research records or private conversations. |
| `pantheon` | `C:/dev/Pantheon/artifacts/beauty-lab/final/after-vista-day.png`, existing in-engine capture 2026-10-15 | Representative island, cottages, villagers, Moss and water. Top 150 pixels cropped to remove HUD. Beauty Lab report documents protected artifact review slots and preserved owner saves. No new game launched and no save touched during this refresh. |
| `pantheon-village` | `C:/dev/Pantheon/artifacts/beauty-lab/final/after-cottage-day.png`, existing in-engine capture 2026-10-15 | Complementary village detail; same provenance and top-HUD crop. No gameplay or art reconstructed. |

`assets/social-preview.jpg` is a 1200 × 630 composition made from the above TeachLivE and Pantheon images with a plain Hughes Virtual title. The existing `assets/hv-logo.svg`, favicon, and touch icon were preserved.

## Content evidence and boundaries

- **AICS:** current public persona/setup/3D pages and `C:/dev/aics/README.md`; current source and review captures show scenario practice, voice/text controls, animated characters, and after-action review. Open conversation is unscored and has no scenario AAR. Old company planning notes are historical and were not used as current product status. The website calls AICS a public prototype and describes collaborative development, not sole ownership or training certification.
- **TeachLivE:** local Unity README documents Unity 6, Netcode, interactor and VR systems; existing runtime evidence and Darin's repository contributions support the engineering role. Institutional attribution: [UCF TeachLivE overview](https://www.ucf.edu/research/research-project/teachlive/). This refresh does not claim the platform, institutional history, or all its development belong to Hughes Virtual.
- **FLITE STEM Coaching:** current public website establishes the resource/coaching experience. Company operational notes (`HughesVirtual/docs/meetings/notes/2026-08-14/executive-planning.md`, `HughesVirtual/projects/README.md`) record site support. `flightstemcoaching-infrastructure/README.md` and company infrastructure inventory establish the hosting/support scope. That infrastructure repository uses inconsistent historical domain spellings; the portfolio uses the verified user-specified public `.org` destination. No original design, resource authorship, or exclusive ownership is claimed. This is distinct from FLITE/ICA.
- **DebriefScape:** README, DEVELOPMENT.md, current local backend file IO, and company project profile support annotation, local folder access, and collaborative development/support. `https://debriefscape.org/` redirects to `https://sreal.ucf.edu/CREST/DSCAPE/`, verified in browser on 2026-10-19. Public access currently begins with a name/email/role screen; no login submitted. Local-first describes the local workflow, not a claim that every hosted integration is offline or never communicates.
- **Pantheon:** README, `docs/PANTHEON_STATUS.md` and `docs/BEAUTY_LAB_REPORT.md` support the implemented village, family/history, voyage and presentation features. Clearly in development; no release, public repository, open-source license, or mod-support promise. Longer-term direction is stated as ambition.
- **Founder:** experience and professional scope retained from the prior publishing site.

## Remaining limits

No new independent rights grant was inferred from repository presence; the user authorized featuring these projects and approved existing visuals. Institutional ownership is credited. Any desired contractual credit wording can be adjusted before publication.

## DebriefScape replacement capture and sample credit

The user requested a loaded-video replacement and approved publication after verification on 2026-10-19. The former empty-player promotional example was replaced.

- Capture used the **unchanged existing local `DebriefScape/dist` bundle** in a fresh headless Playwright Chrome profile. All browser requests were restricted to `http://localhost:8767`; the stopped native Chrome session was not controlled. No browser safety setting was disabled.
- The isolated test fixture supplied actual native browser-private filesystem (OPFS) files to the app's folder-selection entry point. The app's own config/video/CSV parsers, video player, timeline, and legend rendered the result. No DOM/CSS interface elements were inserted or altered. No source-project files, owner sessions, or existing browser storage were edited.
- Session title: **Synthetic demo - Big Buck Bunny**. Two CSV tracks contain invented scene/action/reflection markers and review prompts. These demonstrate annotation controls, not observations about learners. No facial analysis or recording was run.
- Sample video: [Big Buck Bunny](https://peach.blender.org/about/), © 2008 Blender Foundation / [www.bigbuckbunny.org](https://www.bigbuckbunny.org/), [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Sample downloaded from [chintan9/Big-Buck-Bunny](https://github.com/chintan9/Big-Buck-Bunny/blob/915c4b2aba75614b20dec3852375b394bb305f10/BigBuckBunny1080p30s.mp4); the repository includes the film's attribution/license statement. A still frame from the 30.036-second sample appears inside the application screenshot. The film is sample content, not Hughes Virtual work. Attribution and license are also visible in the portfolio caption.
- Video SHA-256: `d365adcb5bc0981acbae633fd7b25b7fd3118cd7389712b86b7bbb484b9d6bcc`.
- Full selected 1920-wide capture SHA-256: `ee663a7326636a52f05993ae987589d2bb13b823b0925148d07fa887722d7264`. The optimized public image is a crop and compression of the final actual capture.

## Martin hero and AICS conversation update — 2026-10-19

The user approved these two focused changes and publication. Existing screenshots were investigated first. Martin's clean runtime capture was sufficient. Saved Ryan tests did not contain the requested acknowledgment-and-question interaction, so a fresh synthetic exchange was recorded through the supported in-app browser on the real public AICS page. No microphone or private participant account was used. The actual 3D interface was captured after replies arrived, not during a loading state. The existing feedback image is retained and captioned as a **separate development test**.

Exact dialogue copied into the HTML excerpt (speaker labels clarified as Participant/Ryan):

- **Participant:** I hear that you feel singled out. I can't serve more alcohol, but I can offer water. What's bothering you most right now?
- **Ryan:** I'm listening. Don't talk down to me.
- **Participant:** I want to speak with you respectfully. Would you prefer some water or juice while we sort this out?
- **Ryan:** Juice, I guess. But I still don't see why you can't make one exception.

Source integrity:

- Martin original PNG SHA-256: `580c89b607b1aba3d8ba3845e28f9b3b073c197ec15c24e2cf9f89b7c7243215`.
- AICS original full screenshot SHA-256: `9c2f1ca286a921f62004bc3da2a5dcb0113c9618802fe708c10f24015a7a590f`.
- The social preview remains the reviewed classroom/Pantheon composition; its existing image and matching alt text were preserved. Other project images and sections are unchanged.
