"""Dependency-free checks for this buildless portfolio. Run from any directory."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


page = Page()
page.feed((ROOT / 'index.html').read_text(encoding='utf-8-sig'))
ids = [a['id'] for _, a in page.elements if 'id' in a]
assert len(ids) == len(set(ids)), 'Duplicate HTML id'
assert sum(t == 'h1' for t, _ in page.elements) == 1
assert all(x in ids for x in ['aics', 'teachlive', 'flite', 'debriefscape', 'workshop'])
references = set()
for tag, attrs in page.elements:
    if tag == 'img':
        assert 'alt' in attrs, f'Missing alt: {attrs}'
        assert int(attrs['width']) > 0 and int(attrs['height']) > 0
        if attrs.get('fetchpriority') != 'high' and attrs.get('alt'):
            assert attrs.get('loading') == 'lazy', f'Unnecessary eager image: {attrs}'
    for key in ['href', 'src']:
        value = attrs.get(key, '')
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or not value:
            continue
        if parsed.path:
            path = ROOT / unquote(parsed.path)
            assert path.is_file(), f'Missing file: {value}'
            references.add(path)
        if parsed.fragment and not parsed.path:
            assert parsed.fragment in ids, f'Broken anchor: {value}'
    for candidate in attrs.get('srcset', '').split(','):
        if candidate.strip():
            path = ROOT / candidate.strip().split()[0]
            assert path.is_file(), f'Missing responsive image: {path}'
            references.add(path)
assert (ROOT / 'assets/social-preview.jpg').is_file()
assert not any(t in ['script', 'form'] for t, _ in page.elements)
assert any(t == 'a' and a.get('href') == 'mailto:darinehughes@gmail.com' for t, a in page.elements)
print(f'PASS: 5 project anchors; unique ids; image alt/dimensions/loading; '
      f'{len(references)} local references; responsive sources; contact; social image.')
print(f'Asset total: {sum(p.stat().st_size for p in (ROOT / "assets").rglob("*") if p.is_file()):,} bytes')
