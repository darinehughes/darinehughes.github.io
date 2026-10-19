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

## Publication boundary

The refresh is prepared on `refresh/visual-portfolio`, based on `origin/main` at `8f2f93a`. No push or production deployment is authorized by the refresh request.

The repository has no tracked build/deployment workflow, CNAME, or framework configuration. Existing icons, identity assets, the unlinked legacy HTML file, and domain configuration are preserved. The local GitHub CLI has no authenticated session, so the GitHub Pages source setting could not be independently read; verify **Settings → Pages → Build and deployment** before publishing.

After explicit publication approval: fetch the latest remote, recheck the diff, confirm Pages uses `main` / root (or follow the configured publishing branch), merge the reviewed refresh into that branch, and push. A push to the configured source can publish immediately. Do not change DNS or create a CNAME for the redirect domain. Confirm the Pages deployment succeeds and inspect `https://darinehughes.github.io/` and the `https://hughesvr.com` redirect afterward.
