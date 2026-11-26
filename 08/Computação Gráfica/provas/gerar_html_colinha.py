"""Colinha.md / Mapa do que cai.md -> standalone HTML (offline, Ctrl+F friendly, sidebar with sections)."""
import os, re, html, unicodedata
from markdown_it import MarkdownIt

P = os.path.expanduser('~/Documents/university/obsidian-ufsc/08/Computação Gráfica/provas/')
FILES = {'Colinha v1': 'Colinha v1.html', 'Colinha': 'Colinha.html', 'Mapa do que cai': 'Mapa do que cai.html'}
md = MarkdownIt('commonmark', {'html': False, 'linkify': False, 'typographer': False}).enable('table')

def slug(t):
    m = re.match(r'\[?(S\d\d)\]?', t.strip('` '))
    if m:
        return m.group(1).lower()
    t = ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')

def wikilinks(s):
    def rep(m):
        target, label = m.group(1), m.group(2) or m.group(1)
        base = target.split('#')[0]
        if base in FILES:
            return f'[{label}](<{FILES[base]}>)'
        return label
    return re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', rep, s)

def convert(name, title, subtitle):
    src = open(P + name + '.md', encoding='utf-8').read()
    src = re.sub(r'^---\n.*?\n---\n', '', src, flags=re.S)
    src = wikilinks(src)
    # "busca:" lines get their own style
    src = re.sub(r'^busca: (.*)$', lambda m: '<<BUSCA>>' + m.group(1), src, flags=re.M)
    body = md.render(src)
    body = re.sub(r'<p>&lt;&lt;BUSCA&gt;&gt;(.*?)</p>', r'<p class="busca"><span>busca:</span> \1</p>', body, flags=re.S)
    toc = []
    def head(m):
        lvl, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', html.unescape(inner))
        sid = slug(text)
        if lvl in ('2', '3'):
            toc.append((lvl, sid, text))
        return f'<h{lvl} id="{sid}">{inner}</h{lvl}>'
    body = re.sub(r'<h([1-3])>(.*?)</h\1>', head, body)
    # make section codes like [S05] / `[S05]` clickable (not inside headings)
    target = '' if name.startswith('Colinha') else 'Colinha v1.html'
    def codes(m):
        return f'<a class="sec" href="{target}#{m.group(1).lower()}">[{m.group(1)}]</a>'
    parts = re.split(r'(<h[1-3][^>]*>.*?</h[1-3]>)', body, flags=re.S)
    for i, p in enumerate(parts):
        if not p.startswith('<h'):
            p = re.sub(r'<code>\[(S\d\d)\]</code>', codes, p)
            p = re.sub(r'(?<![\w"])\[(S\d\d)\]', codes, p)
            parts[i] = p
    body = ''.join(parts)
    nav = ''.join(f'<a class="l{l}" href="#{i}">{html.escape(t)}</a>' for l, i, t in toc)
    other = [f'<a href="{FILES[k]}">{k}</a>' for k in FILES if k != name and k != 'Colinha']
    page = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root{{--bg:#fbfaf7;--fg:#1c1c1e;--muted:#6b6b70;--line:#e2dfd8;--code:#f2efe8;--acc:#2f5fb3;--side:#f3f1ec;--mark:#fff1a8}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151517;--fg:#e9e9ec;--muted:#9a9aa2;--line:#34343a;--code:#222226;--acc:#8fb2ff;--side:#1c1c1f;--mark:#5a4b00}}}}
:root[data-theme="dark"]{{--bg:#151517;--fg:#e9e9ec;--muted:#9a9aa2;--line:#34343a;--code:#222226;--acc:#8fb2ff;--side:#1c1c1f;--mark:#5a4b00}}
*{{box-sizing:border-box}}
html{{scroll-padding-top:12px}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
nav{{position:fixed;top:0;left:0;bottom:0;width:270px;overflow-y:auto;background:var(--side);border-right:1px solid var(--line);padding:14px 10px;font-size:13px}}
nav .top{{font-weight:700;font-size:14px;margin:0 0 4px 6px}}
nav .sub{{color:var(--muted);margin:0 0 10px 6px;font-size:12px}}
nav .other{{margin:0 0 10px 6px}}
nav a{{display:block;color:var(--fg);text-decoration:none;padding:3px 6px;border-radius:5px}}
nav a:hover{{background:var(--line)}}
nav a.l3{{padding-left:18px;color:var(--muted)}}
main{{margin-left:270px;padding:20px 28px 80px;max-width:1080px}}
h1{{font-size:24px;margin:4px 0 10px}}
h2{{font-size:19px;margin:34px 0 8px;padding-bottom:4px;border-bottom:2px solid var(--fg)}}
h3{{font-size:16px;margin:22px 0 6px}}
p{{margin:6px 0}}
ul,ol{{margin:6px 0;padding-left:22px}}
li{{margin:2px 0}}
code{{background:var(--code);padding:1px 4px;border-radius:4px;font:13px ui-monospace,Menlo,Consolas,monospace}}
pre{{background:var(--code);padding:10px 12px;border-radius:8px;overflow-x:auto}}
pre code{{padding:0;background:none;font-size:13px;line-height:1.35}}
table{{border-collapse:collapse;margin:8px 0;width:100%;font-size:14px}}
th,td{{border:1px solid var(--line);padding:4px 8px;vertical-align:top;text-align:left}}
th{{background:var(--code)}}
.busca{{font-size:12px;color:var(--muted);background:var(--code);border-radius:6px;padding:4px 8px}}
.busca span{{font-weight:700}}
a{{color:var(--acc)}} a.sec{{text-decoration:none;font-weight:600}}
hr{{border:0;border-top:1px solid var(--line);margin:24px 0}}
.hint{{font-size:12px;color:var(--muted);margin:0 0 12px}}
@media (max-width:860px){{nav{{position:static;width:auto;border-right:0;border-bottom:1px solid var(--line);max-height:40vh}}main{{margin-left:0;padding:16px}}}}
@media print{{nav{{display:none}}main{{margin:0;max-width:none;padding:0}}body{{font-size:11px;background:#fff;color:#000}}h2{{break-after:avoid}}pre,table{{break-inside:avoid}}}}
</style></head><body>
<nav><div class="top">{html.escape(title)}</div><div class="sub">{html.escape(subtitle)}</div><div class="other">{" · ".join(other)}</div>{nav}</nav>
<main><p class="hint">Ctrl+F busca na página inteira. Dica: busque a raiz da palavra (ex.: "proje", "ilumina") ou o código da seção (ex.: "[S12]").</p>
{body}</main></body></html>'''
    out = P + FILES[name]
    open(out, 'w', encoding='utf-8').write(page)
    return out, len(toc)

print(convert('Colinha v1', 'Colinha CG v1', 'INE5420 · prova 26/11 · com glossário [S22]'))
print(convert('Mapa do que cai', 'Mapa do que cai', 'assunto → seção da Colinha → questões'))
