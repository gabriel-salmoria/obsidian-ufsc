---
tags: [bd2, p2, concorrencia]
---
# 02 · Outros Métodos de Concorrência e Níveis de Isolamento

[[Banco de dados 2|↑ Índice]] · anterior: [[01 - Controle de Concorrência - Trancas e 2PL]] · próximo: [[03 - Recuperação de Falhas]]
Slides: [[03 - Transações, concorrência e recuperação.pdf]] (fim) · Livro: Elmasri & Navathe 7ª ed., cap. 21 · Moodle: [Níveis de isolamento ANSI e SGBDs](https://presencial.moodle.ufsc.br/mod/page/view.php?id=1625463) ([paper do O'Neil, "A Critique of ANSI SQL Isolation Levels"](http://www.cs.umb.edu/~poneil/iso.pdf), [PostgreSQL](https://www.postgresql.org/docs/current/transaction-iso.html))

## Ordenação por timestamp (TO)
- **Não usa trancas ⇒ não tem deadlock.**
- Cada T recebe um **timestamp** (ordem de início). O escalonamento equivalente é o serial na **ordem dos timestamps**.
- Para cada item X o sistema guarda **Read_TS(X)** e **Write_TS(X)**, os maiores TS que leram e que escreveram X.
- T é **abortada** (e reinicia com TS novo) se tentar:
  - `R(X)` com **TS(T) < Write_TS(X)**: uma T mais nova já escreveu X;
  - `W(X)` com **TS(T) < Write_TS(X)** ou **TS(T) < Read_TS(X)**: uma T mais nova já leu ou escreveu X.
- Sujeito a **rollbacks (inclusive em cascata)** e **starvation**.
- **TO estrito**: atrasa R/W em X até a T que escreveu X confirmar (dá escalonamentos estritos).
- **Regra de escrita de Thomas**: se `TS(T) < Write_TS(X)` numa escrita, **ignora** a escrita obsoleta em vez de abortar.

## Multiversão
- Guarda **versões antigas** dos itens quando são escritos. Uma leitura pega a **versão apropriada** para manter a serialidade, então leituras quase nunca são rejeitadas.
- Rollback = descartar as versões novas escritas pela T abortada.
- Custa **mais memória**. Caso extremo: **BD temporal** (guarda versões para sempre).
- Variantes com timestamps (MVTO) ou com 2PL (trancas de **certificação**).
- **Snapshot isolation** (PostgreSQL, Oracle): cada T lê um snapshot do início dela.

## Otimista (validação / certificação)
- Executa **sem verificar nada** durante a execução, escrevendo em cópias locais.
- Três fases: **leitura** → **validação** (checa conflito com transações concorrentes já validadas) → **escrita** (aplica no BD).
- Em caso de conflito, a transação (normalmente a mais nova) é desfeita e **reexecutada**.
- Bom quando **há pouca interferência** entre transações.

## Granularidade múltipla
- Trancas **intencionais** (IS, IX, SIX) nos nós ancestrais (BD → tabela → página → registro) para poder trancar em níveis diferentes sem checar todos os descendentes.

## Níveis de isolamento SQL-92
Fenômenos:
- **Dirty read**: lê um valor escrito por T não confirmada.
- **Nonrepeatable read**: relê a mesma linha e o valor mudou (outra T confirmou um UPDATE).
- **Phantom**: refaz a mesma consulta e aparecem ou somem **linhas** (INSERT/DELETE de outra T).

| Nível | Dirty read | Nonrepeatable read | Phantom |
|---|---|---|---|
| **READ UNCOMMITTED** | permitido | permitido | permitido |
| **READ COMMITTED** | — | permitido | permitido |
| **REPEATABLE READ** | — | — | permitido |
| **SERIALIZABLE** | — | — | — |

- Default do **PostgreSQL** e do **Oracle**: READ COMMITTED. MySQL/InnoDB: REPEATABLE READ.
- No PostgreSQL, READ UNCOMMITTED se comporta como READ COMMITTED, e o REPEATABLE READ dele (snapshot) também não deixa fantasmas.

## Comandos SQL de transação
- **`SET TRANSACTION`** define propriedades (ex.: `ISOLATION LEVEL SERIALIZABLE`, `READ ONLY`).
- **`BEGIN`** marca o início. **`SAVEPOINT nome`** marca um ponto até onde se pode desfazer. **`ROLLBACK [TO nome]`** desfaz. **`COMMIT`** confirma.
- Comandos sem `BEGIN/COMMIT` são tratados como **transações por default** (autocommit).

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE idDep = '1234';
SAVEPOINT meu_savepoint;
UPDATE accounts SET balance = balance + 100 WHERE idDep = '4321';
ROLLBACK TO meu_savepoint;   -- oops, conta errada
UPDATE accounts SET balance = balance + 100 WHERE idDep = '5432';
COMMIT;
```
