---
tags: [bd2, p2, recuperacao]
---
# 03 · Recuperação de Falhas

[[Banco de dados 2|↑ Índice]] · anterior: [[02 - Outros Métodos de Concorrência e Níveis de Isolamento]] · próximo: [[04 - BDD - Conceitos, Fragmentação e Replicação]]
Livro: Elmasri & Navathe 7ª ed., **cap. 22** "Database Recovery Techniques", pp. 813–833 (6ª ed. PT: **cap. 23**, pp. 543–558)
Exercícios: **L2** (todas as questões em [[Banco de Questões P2#L2 - recuperação de falhas]])

> [!note] Os slides do professor **não têm** a seção de técnicas de recuperação; ela aparece no índice, mas o PDF termina antes. O conteúdo cobrado vem do **livro** e da lista **L2**. Esta nota foi montada a partir dos dois.

## Tipos de falha
1. **De transação**: erro lógico, violação de restrição, aborto pelo controle de concorrência (deadlock), cancelamento pelo usuário.
2. **De sistema**: queda de energia, crash do SO/SGBD. Perde a **memória** (cache/buffer), não o disco.
3. **De mídia (disco)**: perde dados do disco. Resolve com **backup + log** (lento) ou com um **espelho sempre atualizado** (rápido).

> L2 Q9: "Para lidar com falhas de **disco rapidamente**, é necessário e suficiente": **manter uma cópia redundante (espelho) sempre atualizada de todo o BD.** Backup + log recupera, mas **demora** (L2 Q7: refazer pelo log desde o último backup "pode ser demorado").

## Buffer/cache e políticas
- O SGBD mantém páginas do BD em **cache**. A questão é **quando** elas vão para o disco.
- **Steal / No-steal**: pode (ou não) gravar no disco uma página alterada por T **antes do commit** de T. Steal ⇒ vai precisar de **UNDO**.
- **Force / No-force**: no commit, força (ou não) a gravação de todas as páginas de T. No-force ⇒ vai precisar de **REDO**.
- SGBDs reais usam **steal + no-force**, o que exige **UNDO/REDO**.
- **In-place** (grava no mesmo lugar, e precisa de log) × **sombreamento / shadowing** (grava a nova versão em **outro lugar** do disco).

## Write-Ahead Logging (WAL)
- O **registro de log** de uma operação é gravado no disco **antes** do dado alterado (o *before image* precisa estar no log antes de sobrescrever o disco).
- E, antes de confirmar, todos os registros de log de T (inclusive o `commit`) precisam estar no disco.
- L2 Q2: WAL = "o registro de log de cada operação deve ser gravado **antes dos dados em cache**".
- **Desempenho mantendo a recuperabilidade** (L2 Q1): agrupar a gravação dos logs de **múltiplas transações confirmadas** em **batch** (*group commit*).

## Técnicas
| Técnica | Quando o dado vai para o disco | Log de escrita guarda | Na recuperação |
|---|---|---|---|
| **Atualização adiada** (*deferred*) | só **depois do commit** | **só o valor novo** (AFIM) | **NO-UNDO / REDO**: só **REDO** das confirmadas |
| **Atualização imediata** (*immediate*) | pode ir **antes** do commit | **valor antigo e novo** (BFIM e AFIM) | **UNDO/REDO**: desfaz as não confirmadas, refaz as confirmadas |
| Imediata + force no commit | antes/no commit | valor antigo | **UNDO / NO-REDO** |
| **Shadow paging** | nova versão em **outro lugar**; troca o diretório no commit | (log mínimo) | **NO-UNDO / NO-REDO**: descarta o diretório novo |

Respostas da L2:
- **Adiada** precisa necessariamente guardar o **valor novo** (Q4). Se uma transação **falha** com atualização adiada, o que se faz é **REDO** (Q6, gabarito).
- **Imediata**: cada registro de escrita tem **id da transação, id do item, valor antigo e valor novo** (Q5).
- **Sombreamento**: o item é gravado num **local diferente** do disco (Q8).
- **UNDO e REDO devem ser idempotentes** (Q10): aplicar 1 vez ou N vezes dá o mesmo resultado, porque a recuperação pode falhar no meio e recomeçar.

## Checkpoint
- `[checkpoint]` no log: suspende as transações, **força** as páginas sujas da cache para o disco e grava a marca (no checkpoint *fuzzy*, sem parar tudo).
- Transações que **confirmaram antes** do checkpoint **não precisam de REDO**. A recuperação só olha o log a partir do último checkpoint.

## Recuperação com UNDO/REDO (receita)
1. Lê o log de trás para frente até o último checkpoint e monta as listas: **confirmadas** (têm `commit`) e **ativas** (sem `commit`).
2. **UNDO** das ativas: percorre o log **de trás para frente**, restaurando o valor **antigo**.
3. **REDO** das confirmadas desde o checkpoint: percorre **de frente para trás**, aplicando o valor **novo**.

(O **ARIES**, usado em SGBDs reais, faz análise → REDO "repetindo a história" → UNDO, e usa LSN nas páginas.)

## Falha catastrófica e rollback em cascata
- Disco perdido: restaura o **backup** e faz REDO pelo log arquivado (demorado). Por isso o espelho é a opção rápida.
- **Rollback em cascata** acontece quando uma T **lê item escrito por T' não confirmada** (L2 Q3, ver nota em [[Banco de Questões P2#L2 - recuperação de falhas]]). Por isso SGBDs preferem escalonamentos **estritos** (2PL estrito).
