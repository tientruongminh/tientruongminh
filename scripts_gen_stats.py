import json, subprocess, html, datetime
from collections import Counter
from pathlib import Path

def gh_json(args, input_text=None):
    out = subprocess.check_output(['gh'] + args, input=input_text, text=True)
    return json.loads(out)

user = gh_json(['api', 'users/tientruongminh'])
repos = gh_json(['repo', 'list', 'tientruongminh', '--limit', '100', '--json', 'name,isPrivate,stargazerCount,forkCount,primaryLanguage,pushedAt'])
public = [r for r in repos if not r.get('isPrivate')]
langs = Counter((r.get('primaryLanguage') or {}).get('name') or 'Other' for r in public)
stars = sum(r.get('stargazerCount') or 0 for r in public)
forks = sum(r.get('forkCount') or 0 for r in public)
updated = sorted(public, key=lambda r: r.get('pushedAt') or '', reverse=True)[:4]
top_langs = langs.most_common(6)

# real contribution data from GitHub GraphQL
query = '''query($login:String!){ user(login:$login){ contributionsCollection{ contributionCalendar{ totalContributions weeks{ contributionDays{ contributionCount date } } } } } }'''
try:
    contrib = gh_json(['api','graphql','-f','login=tientruongminh','-f',f'query={query}'])
    calendar = contrib['data']['user']['contributionsCollection']['contributionCalendar']
    total_contrib = calendar['totalContributions']
    days = [d for w in calendar['weeks'] for d in w['contributionDays']]
except Exception:
    total_contrib = 0
    days = []

def esc(x): return html.escape(str(x), quote=True)

def write(path, svg): Path(path).write_text(svg)

common = '''<defs><linearGradient id="bg" x1="0" y1="0" x2="100%" y2="100%"><stop stop-color="#020617"/><stop offset="1" stop-color="#0f172a"/></linearGradient><style>.title{font:800 22px ui-sans-serif,system-ui;fill:#34d399}.label{font:600 14px ui-sans-serif,system-ui;fill:#cbd5e1}.value{font:800 28px ui-sans-serif,system-ui;fill:#f8fafc}.mono{font:600 12px ui-monospace,monospace;fill:#99f6e4}.muted{fill:#64748b}.bar{animation:grow 2s ease-out infinite alternate;transform-origin:left}.pulse{animation:pulse 1.8s ease-in-out infinite}@keyframes grow{from{transform:scaleX(.25);opacity:.55}to{transform:scaleX(1);opacity:1}}@keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}</style></defs>'''

overview = f'''<svg width="495" height="220" viewBox="0 0 495 220" fill="none" xmlns="http://www.w3.org/2000/svg">{common}<rect width="495" height="220" rx="16" fill="url(#bg)" stroke="#164e63"/><text class="title" x="24" y="38">Tien's GitHub Stats</text><text class="label" x="28" y="78">Public repositories</text><text class="value" x="230" y="80">{user.get('public_repos', len(public))}</text><text class="label" x="28" y="112">Followers</text><text class="value" x="230" y="114">{user.get('followers',0)}</text><text class="label" x="28" y="146">Total stars</text><text class="value" x="230" y="148">{stars}</text><text class="label" x="28" y="180">Total forks</text><text class="value" x="230" y="182">{forks}</text><circle class="pulse" cx="430" cy="52" r="20" fill="#34d399" opacity=".35"/><circle class="pulse" cx="430" cy="52" r="7" fill="#34d399"/></svg>'''
write('assets/github-overview-card.svg', overview)

maxc=max([c for _,c in top_langs] or [1])
colors=['#34d399','#38bdf8','#a78bfa','#f59e0b','#fb7185','#22c55e']
rows=[]
for i,(name,count) in enumerate(top_langs):
    y=66+i*24; w=int(260*count/maxc)
    rows.append(f'<text class="label" x="24" y="{y}">{esc(name)}</text><rect x="150" y="{y-13}" width="{w}" height="10" rx="5" fill="{colors[i%len(colors)]}" class="bar"/><text class="mono" x="425" y="{y}">{count}</text>')
langsvg=f'''<svg width="495" height="220" viewBox="0 0 495 220" fill="none" xmlns="http://www.w3.org/2000/svg">{common}<rect width="495" height="220" rx="16" fill="url(#bg)" stroke="#164e63"/><text class="title" x="24" y="38">Most Used Languages</text>{''.join(rows)}<text class="mono" x="24" y="202">by repository primary language, from GitHub API</text></svg>'''
write('assets/github-languages-card.svg', langsvg)

# contribution graph last ~98 days for compact card
last_days=days[-98:] if days else []
mx=max([d['contributionCount'] for d in last_days] or [1])
cells=[]
for idx,d in enumerate(last_days):
    col=idx//7; row=idx%7; x=24+col*17; y=70+row*15; c=d['contributionCount']
    if c==0: color='#0f172a'
    elif c < mx*.25: color='#064e3b'
    elif c < mx*.55: color='#059669'
    elif c < mx*.85: color='#34d399'
    else: color='#a7f3d0'
    cells.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="3" fill="{color}"/>')
contribsvg=f'''<svg width="1000" height="230" viewBox="0 0 1000 230" fill="none" xmlns="http://www.w3.org/2000/svg">{common}<rect width="1000" height="230" rx="18" fill="url(#bg)" stroke="#164e63"/><text class="title" x="28" y="42">Contribution Activity</text><text class="value" x="760" y="44">{total_contrib}</text><text class="label" x="830" y="42">contributions this year</text>{''.join(cells)}<text class="mono" x="28" y="202">real contribution calendar from GitHub GraphQL</text><text class="mono" x="700" y="202">recent: {esc(' · '.join(r['name'] for r in updated)[:45])}</text></svg>'''
write('assets/github-contribution-card.svg', contribsvg)

print(json.dumps({'public_repos':user.get('public_repos'), 'followers':user.get('followers'), 'stars':stars, 'forks':forks, 'total_contributions':total_contrib, 'top_langs':top_langs}, indent=2))
