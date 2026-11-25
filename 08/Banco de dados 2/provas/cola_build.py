import re, sys
t = open('cola_src.tex').read()
KW = 'SELECT DISTINCT FROM WHERE GROUP BY HAVING ORDER ASC DESC CREATE VIEW AS INNER NATURAL LEFT RIGHT JOIN ON AND OR NOT IN IS NULL UNION ALL INTERSECT EXCEPT EXISTS BETWEEN LIKE INSERT INTO VALUES UPDATE SET DELETE DROP BEGIN COMMIT SAVEPOINT ROLLBACK TO TRANSACTION ISOLATION LEVEL ANY'.split()
FN = 'COUNT SUM AVG MIN MAX'.split()
kw_re = re.compile(r'(?<![A-Za-z0-9_\\])(' + '|'.join(KW) + r')(?![A-Za-z0-9_])')
fn_re = re.compile(r'(?<![A-Za-z0-9_\\])(' + '|'.join(FN) + r')(?![A-Za-z0-9_])')
def sql_color(s):
    s = kw_re.sub(r'\\K{\1}', s)
    s = fn_re.sub(r'\\F{\1}', s)
    return s
op_re = re.compile(r'(?<![A-Za-z0-9_\\])((?:RL|WL|UL)\d(?:\([A-Z]\))?|[RWrw]\d(?:\([A-Z]\))?|[CAca]\d|<(?:START|READY|PREPARE) T\d>)(?![A-Za-z0-9_])')
def op_color(m):
    s = m.group(1)
    if s.startswith('<'): return r'\oLog{' + s + '}'
    if s.startswith('RL'): return r'\oRL{' + s + '}'
    if s.startswith('WL'): return r'\oWL{' + s + '}'
    if s.startswith('UL'): return r'\oUL{' + s + '}'
    if s[0] in 'Ww': return r'\oW{' + s + '}'
    if s[0] in 'Rr': return s
    if s[0] in 'Cc': return r'\oC{' + s + '}'
    if s[0] in 'Aa': return r'\oA{' + s + '}'
    return s
def q_repl(m):
    s = m.group(1)
    s = op_re.sub(op_color, s)
    s = sql_color(s)
    return r'\q{' + s + '}'
# \q{...} sem chaves aninhadas
t = re.sub(r'\\q\{([^{}]*)\}', q_repl, t)
# blocos Verbatim: colore SQL, exceto linhas de rótulo \N{
out, inv = [], False
for line in t.split('\n'):
    if line.startswith(r'\begin{Verbatim}'): inv = True; out.append(line); continue
    if line.startswith(r'\end{Verbatim}'): inv = False; out.append(line); continue
    if inv and not line.lstrip().startswith(r'\N{'):
        # nao mexe dentro de \Tr{...}
        parts = re.split(r'(\\Tr\{[^{}]*\})', line)
        line = ''.join(p if p.startswith(r'\Tr{') else sql_color(p) for p in parts)
    out.append(line)
open('cola.tex', 'w').write('\n'.join(out))
