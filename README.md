# Hughes Virtual portfolio

Lightweight, buildless HTML/CSS website for `https://darinehughes.github.io/`; `https://hughesvr.com` redirects there. No package install, framework, client JavaScript, analytics, or external font request is needed.

## Preview and check

```powershell
Set-Location C:\dev\darinehughes.github.io
python tools/check_site.py
python -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Stop the server with Ctrl+C. Opening `index.html` directly also works.

Edit `index.html` and `assets/site.css`. Project images and responsive variants are in `assets/projects/`. Full-size image links help preserve interface legibility at mobile sizes. Image and factual sources are recorded in [ASSET-PROVENANCE.md](ASSET-PROVENANCE.md).

## Publication

The user approved publication of the reviewed refresh after replacing the DebriefScape image on 2026-10-19. GitHub Pages API configuration was confirmed: `build_type: legacy`, source branch `main`, path `/`, HTTPS enforced, CNAME `null`. `https://hughesvr.com` is an existing redirect to the canonical publishing URL; preserve that domain configuration.

The repository has no tracked custom deployment workflow or framework build. Publish through normal Git: fetch, verify/reconcile current `main`, merge the reviewed refresh, and push `main`. Then check the Pages build status and the served HTML and image at both public URLs. Do not force-push, alter DNS, or add a CNAME for the redirect domain.
