import json, subprocess, html
from collections import Counter
from pathlib import Path

def gh_json(args):
    out = subprocess.check_output(['gh'] + args, text=True)
    return json.loads(out)

user = gh_json(['api', 'users/tientruongminh'])
repos = gh_json(['repo', 'list', 'tientruongminh', '--limit', '100', '--json', 'name,description,isPrivate,stargazerCount,forkCount,primaryLanguage,pushedAt'])
public = [r for r in repos if not r.get('isPrivate')]
langs = Counter((r.get('primaryLanguage') or {}).get('name') or 'Other' for r in public)
stars = sum(r.get('stargazerCount') or 0 for r in public)
forks = sum(r.get('forkCount') or 0 for r in public)
updated = sorted(public, key=lambda r: r.get('pushedAt') or '', reverse=True)[:4]
top_langs = langs.most_common(5)
lang_text = ' · '.join(f'{k} {v}' for k, v in top_langs) or 'No language data'
updated_text = ' · '.join(r['name'] for r in updated)

def esc(x):
    return html.escape(str(x), quote=True)

maxc = max([c for _, c in top_langs] or [1])
colors = ['#34d399', '#38bdf8', '#a78bfa', '#f59e0b', '#fb7185']
bars = []
for i, (name, count) in enumerate(top_langs):
    h = 35 + int(105 * count / maxc)
    x = 70 + i * 52
    bars.append(f'<rect class="bar" x="{x}" y="{290-h}" width="28" height="{h}" rx="9" fill="{colors[i % len(colors)]}" style="animation-delay:{i*.18}s"/><text class="k" x="{x-8}" y="318">{esc(name[:6])}</text>')

svg = f'''<svg width="1200" height="360" viewBox="0 0 1200 360" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="g" x1="0" y1="0" x2="1200" y2="360"><stop stop-color="#020617"/><stop offset=".55" stop-color="#052e2b"/><stop offset="1" stop-color="#0f172a"/></linearGradient><style>.card{{fill:#07111f;stroke:#164e63}}.h{{font:800 24px ui-sans-serif,system-ui;fill:#f8fafc}}.k{{font:600 12px ui-monospace,monospace;fill:#99f6e4}}.v{{font:800 42px ui-sans-serif,system-ui;fill:#34d399}}.s{{font:600 14px ui-sans-serif,system-ui;fill:#cbd5e1}}.bar{{animation:grow 2.4s ease-out infinite alternate;transform-origin:bottom}}.line{{stroke:#34d399;stroke-width:3;fill:none;stroke-dasharray:700;stroke-dashoffset:700;animation:draw 4s ease-in-out infinite alternate}}.dot{{fill:#38bdf8;animation:pulse 1.8s ease-in-out infinite}}@keyframes grow{{from{{transform:scaleY(.25);opacity:.55}}to{{transform:scaleY(1);opacity:1}}}}@keyframes draw{{to{{stroke-dashoffset:0}}}}@keyframes pulse{{0%,100%{{opacity:.35;r:4}}50%{{opacity:1;r:8}}}}</style></defs>
<rect width="1200" height="360" rx="30" fill="url(#g)"/>
<text class="h" x="42" y="52">GitHub signal</text><text class="k" x="42" y="78">real data from GitHub API · generated into local SVG</text>
<g transform="translate(42 106)"><rect class="card" width="250" height="132" rx="24"/><text class="k" x="24" y="36">PUBLIC REPOS</text><text class="v" x="24" y="92">{user.get('public_repos', len(public))}</text></g>
<g transform="translate(322 106)"><rect class="card" width="250" height="132" rx="24"/><text class="k" x="24" y="36">FOLLOWERS</text><text class="v" x="24" y="92">{user.get('followers', 0)}</text></g>
<g transform="translate(602 106)"><rect class="card" width="250" height="132" rx="24"/><text class="k" x="24" y="36">TOTAL STARS</text><text class="v" x="24" y="92">{stars}</text></g>
<g transform="translate(882 106)"><rect class="card" width="250" height="132" rx="24"/><text class="k" x="24" y="36">TOTAL FORKS</text><text class="v" x="24" y="92">{forks}</text></g>
<text class="k" x="42" y="268">TOP LANGUAGES BY REPOSITORY COUNT</text>
{''.join(bars)}
<path class="line" d="M610 305C680 240 745 270 810 218S925 248 990 190S1080 205 1140 150"/><circle class="dot" cx="610" cy="305" r="5"/><circle class="dot" cx="810" cy="218" r="5" style="animation-delay:.4s"/><circle class="dot" cx="990" cy="190" r="5" style="animation-delay:.8s"/><circle class="dot" cx="1140" cy="150" r="5" style="animation-delay:1.2s"/>
<text class="s" x="602" y="268">Recent pushes: {esc(updated_text[:70])}</text>
<text class="k" x="602" y="330">Languages: {esc(lang_text[:88])}</text>
</svg>'''
Path('assets/stats.svg').write_text(svg)
print(json.dumps({'public_repos': user.get('public_repos'), 'followers': user.get('followers'), 'stars': stars, 'forks': forks, 'top_langs': top_langs, 'recent': [r['name'] for r in updated]}, indent=2))
