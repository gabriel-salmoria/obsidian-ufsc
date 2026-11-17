---
tags: [bd2, p2, questoes]
---
# Banco de Questões: P2 de BD2

[[Banco de dados 2|↑ Índice]]

Fontes: as **minhas tentativas** das listas E3, L2 e E4 no Moodle (todas com nota cheia, exceto L2 Q3) e o Ex. 3.2.
O Moodle do professor **não mostra o gabarito**, só se a opção marcada estava certa. Onde a nota foi parcial, deixei a análise.
Faltam: **Exercício 3.3** (2PL) e **Exercício 4.4** (2PC), que ainda não fiz no Moodle. Fazer antes da prova.

---

## E3 - escalonamentos e 2PL
Nota: [[00 - Base - Caracterização de Escalonamentos]] · [[01 - Controle de Concorrência - Trancas e 2PL]]

### Recuperabilidade (V/F)
| # | Escalonamento | Pergunta | Resp. | Por quê |
|---|---|---|---|---|
| 1 | `R2(Y) R1(Y) R1(X) W1(X) C1 R2(X) W2(Y) C2` | recuperável? | **V** | T2 lê X **depois** de C1 |
| 2 | `R1(Y) R1(X) W1(Y) R2(X) W2(Y) C1 C2` | estrito? | **F** | W2(Y) escreve Y sujo de T1 |
| 3 | `R2(Y) R1(Y) R1(X) W1(X) R2(X) W2(Y) A1 A2` | recuperável? | **V** | leitura suja, mas ninguém confirma antes (os dois abortam) |
| 4 | `... R2(X) W2(Y) C1 A2` | recuperável? | **V** | T1 (de quem T2 leu) confirma primeiro |
| 5 | `... R2(X) W2(Y) A1 C2` | recuperável? | **F** | T2 confirma tendo lido de T1, que abortou |
| 6 | `... R2(X) W2(Y) C2 C1` | recuperável? | **F** | T2 confirma **antes** de T1 |
| 7 | `R2(Y) R1(Y) R1(X) W1(X) C1 R2(X) W2(Y) C2` | estrito? | **V** | nada lido nem escrito sujo |
| 8 | `... R2(X) W2(Y) C2 A1` | recuperável? | **F** | T2 confirma antes de T1 (que ainda aborta) |
| 9 | `... R2(X) W2(Y) C2 C1` | ACA? | **F** | leitura suja R2(X) |
| 10 | `R2(Y) R1(Y) R1(X) W1(X) C1 R2(X) W2(Y) C2` | ACA? | **V** | R2(X) depois de C1 |

### Seriabilidade
- **Q11** `R2(Y) R1(Y) R1(X) R2(X) W2(Y) C2 W1(X) C1`: seriável? **F**. Y: R1 → W2 dá T1→T2; X: R2 → W1 dá T2→T1. **Ciclo.** (Q14: equivale a **nenhum** escalonamento serial.)
- **Q12** `R2(Y) R1(Y) R1(X) W1(X) C1 R2(X) W2(Y) C2`: seriável? **V**. Só arestas T1→T2. (Q13: equivale a **T1 → T2**.)

### Variantes de 2PL (Q15 a Q18)
Escalonamento base: `R2(Z) R1(Z) R1(Y) W1(Y) C1 R2(Y) W2(Z) C2`
| Variante pedida | Resposta |
|---|---|
| **2PL simples** (não estrito, não conservativo) | `RL2(Z) R2(Z) RL1(Z) R1(Z) RL1(Y) R1(Y) WL1(Y) UL1(Z) W1(Y) UL1(Y) C1 RL2(Y) R2(Y) WL2(Z) UL2(Y) W2(Z) UL2(Z) C2` |
| **conservativo** (não estrito) | `WL2(Z) RL2(Y) R2(Z) RL1(Z) R2(Y) UL2(Y) W2(Z) UL2(Z) C2 RL1(Z) WL1(Y) R1(Z) UL1(Z) R1(Y) W1(Y) UL1(Y) C1` |
| **conservativo e rigoroso** | `WL2(Z) RL2(Y) R2(Z) RL1(Z) R2(Y) W2(Z) C2 UL2(Y) UL2(Z) RL1(Z) WL1(Y) R1(Z) R1(Y) W1(Y) C1 UL1(Z) UL1(Y)` |
| **estrito** (não conservativo) | `RL2(Z) R2(Z) RL1(Z) R1(Z) RL1(Y) R1(Y) WL1(Y) UL1(Z) W1(Y) C1 UL1(Y) RL2(Y) R2(Y) WL2(Z) UL2(Y) W2(Z) C2 UL2(Z)` |

Como conferir:
- **Conservativo**: todos os RL/WL de T antes do 1º R/W de T. Note o `RL1(Z)` "tentado" cedo e suspenso porque T2 tem `WL2(Z)`.
- **Estrito**: UL de item com **WL** só depois do C.
- **Rigoroso**: **todo** UL depois do C.
- **Simples**: só a regra das 2 fases (nenhum lock depois de um unlock).

---

## L2 - recuperação de falhas
Nota: [[03 - Recuperação de Falhas]]

1. Melhorar o desempenho mantendo a recuperabilidade → **esperar várias transações confirmarem e gravar os logs em batch** (group commit).
2. **WAL** → **o registro de log de cada operação é gravado antes dos dados em cache**.
3. Há possibilidade de rollback em cascata quando… (**múltipla escolha; tirei 0,5 marcando só a d**)
   - ✅ **d. uma transação lê item previamente escrito por transação não confirmada.**
   - Falta **uma** outra alternativa correta. Pela nota (0,5), são duas corretas com peso igual. A candidata mais provável é **c. "uma transação escreve item previamente escrito por transação não confirmada"**: se T' abortar, restaurar o *before image* de T' apaga a escrita de T, então T também precisa ser desfeita. As outras (ler item escrito por **confirmada**, ler/escrever item só **lido** por não confirmada) não causam cascata. *Não confirmado pelo Moodle.*
4. Logging incremental com **atualizações adiadas** precisa guardar → **o valor novo** do item.
5. Logging incremental com **atualizações imediatas**: cada registro de escrita contém → **id da transação, id do item, valor antigo e valor novo**.
6. Falha de transação com **atualização adiada** → **REDO** (gabarito).
7. Desfazer as não confirmadas e refazer as confirmadas **desde o último backup** é problemático porque → **pode ser demorado**.
8. **Sombreamento** (shadowing) ao fazer flush → **o item é gravado em local diferente do disco**.
9. Lidar **rapidamente** com falha de disco: necessário e suficiente → **cópia redundante (espelho) sempre atualizada** de todo o BD.
10. UNDO e REDO devem ser → **idempotentes**.

---

## E4 - BDD, 2PC e fragmentação
Nota: [[06 - BDD - Transações, 2PC e Deadlock]] · [[05 - BDD - Processamento de Consultas]]

Logs (coordenador = nó IT):
| Nodo BR | Nodo UK | Nodo IT (coord.) |
|---|---|---|
| `<START T2>` | `<START T2>` | `<START T1>` |
| `RL2(B)` | `WL2(A)` | `<START T2>` |
| `R2(B)` | `R2(A)` | `RL2(B)` |
| `WL2(C)` | `RL2(E)` | `R2(B)` |
| `UL2(B)` | `R2(E)` | `UL2(B)` |
| `R2(C)` | `UL2(E)` | `<PREPARE T2>` |
| `W2(C)` | `W2(A)` | `WL1(D)` |
| **`<READY T2>`** | **`<READY T2>`** | `R1(D)` |
| `<START T1>` | `<START T1>` | `W1(D)` |
| `RL1(B)` | `RL1(E)` | `<PREPARE T1>` |

- **Q1**: só **BR** falha por mais que o timeout da 1ª fase. O que acontece com **T2**? → **COMMIT**. BR já tinha gravado `<READY T2>` (o voto chegou), UK também, e o coordenador decide commit.
- **Q2**: só **UK** falha. O que acontece com **T1**? → **ABORT**. UK nunca gravou `<READY T1>` (o log termina em `RL1(E)`), então dá timeout na votação.
- **Q3** (logs com `RL2(B) WL2(C) R2(B)...` em BR, ou seja, trancas antes das operações): variante do 2PL → **conservativo e estrito**. As trancas vêm antes de qualquer R/W; as de leitura são soltas antes do fim e as de escrita não, logo **estrito, não rigoroso**.
- **Q4**: rede social, `Pessoa` fragmentada por `uf`, `Segue` com fragmentação **derivada** (`SegueComSeguidor ∪ SegueComSeguido`). Consulta em **MG**: seguidos de MG com mais de 1 milhão de seguidores de **fora** de MG.
  → **Só executa subconsulta no nodo MG e não gera tráfego em rede.** `MG.Segue` contém **todo** par cujo seguido é de MG. "Seguidor de fora" = `idSeguidor NOT IN (SELECT idP FROM MG.Pessoa)`.

---

## Escalonamentos (revisão P1, cobrados na E3)
Do Ex. 3.2 (eu errei partes das questões 1 e 3; abaixo, as respostas certas):

| Escalonamento | Serial | Seriável | Nº seriais equiv. | Recuperável | ACA | Estrito |
|---|---|---|---|---|---|---|
| `r1(X) r2(Z) r3(X) r1(Z) r2(Y) r3(Y) w1(X) c1 w2(Z) w3(Y) w2(Y) c3 c2` | N | **N** (ciclo T2↔T3) | **0** | S | S | **N** (w2(Y) antes de c3) |
| `r1(X) r2(Z) r1(Z) r3(X) r3(Y) w1(X) c1 w3(Y) c3 r2(Y) w2(Z) w2(Y) c2` | N | S | **1** (T3→T1→T2) | S | S | S |
| `r1(X) r2(Z) r1(Z) r3(X) r3(Y) w1(X) w3(Y) r2(Y) w2(Z) w2(Y) c1 c2 c3` | N | S | **1** (T3→T1→T2) | **N** (T2 leu de T3 e confirmou antes) | N | N |
