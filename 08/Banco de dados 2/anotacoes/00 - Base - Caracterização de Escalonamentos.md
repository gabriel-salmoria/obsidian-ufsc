---
tags: [bd2, p1, base]
---
# 00 · Base (matéria da P1): caracterização de escalonamentos

[[Banco de dados 2|↑ Índice]] · próximo: [[01 - Controle de Concorrência - Trancas e 2PL]]
Slides: [[03 - Transações, concorrência e recuperação.pdf]] (até "FINAL DA MATÉRIA PARA 1ª PROVA")

> [!info] Por que está aqui
> É matéria da P1, mas a lista **E3** (da época da P2) ainda cobra isso, e 2PL, recuperação e 2PC dependem desses conceitos. Revise rápido.

## Transação
- "Execução de um trecho de programa que acessa e/ou modifica o BD." Pode ser vista como uma **sequência de leituras e escritas**. Precisa executar **completamente** para ser confirmada; depois de confirmada **não** pode ser desfeita.
- **ACID**:
  - **Atomicidade**: tudo ou nada (aborto desfaz as escritas);
  - **Consistência**: leva o BD de estado consistente para estado consistente;
  - **Isolamento (Independência)**: comporta-se como se estivesse sozinha;
  - **Durabilidade**: o que foi confirmado não se perde.
  
  (Distratores do quiz: "flexibilidade", "versatilidade", "sigilo", "execução em série".)
- Marcas do **log**: `[start_transaction,T]`, `[write_item,T,X,old,new]`, `[read_item,T,X]`, `[commit,T]`, `[abort,T]`, `[checkpoint]`.

## Notação
`R1(X)` leitura de X por T1 · `W1(X)` escrita · `C1` commit · `A1` abort · `RL/WL/UL` read-lock / write-lock / unlock (ver [[01 - Controle de Concorrência - Trancas e 2PL]]).

## Recuperabilidade (do mais fraco ao mais forte)
| Propriedade | Restrição | Violação típica |
|---|---|---|
| **Recuperável** | nenhuma T que **leu** item escrito por T' confirma **antes** de T' | `R1(X)W1(X)R2(X)W2(X)C2` (T2 leu de T1 e confirmou primeiro) |
| **Livre de rollback em cascata (ACA)** | nenhuma T **lê** item escrito por T' não confirmada (**sem leitura suja**) | `R1(X)W1(X)R2(X)W2(X)` |
| **Estrito** | nenhuma T **lê nem escreve** item escrito por T' não confirmada | `R2(X)R1(X)W1(X)W2(X)` |

Estrito ⊂ ACA ⊂ Recuperável. Se a escrita "suja" veio de uma T' que **abortou**, a leitora tem que abortar também: é o **rollback em cascata**.

## Serialidade
- **Serial**: as transações executam **uma inteira depois da outra**.
- **Seriável** (serial-equivalente): resultado igual ao de **algum** escalonamento serial (por conflito).
- **Conflito**: duas operações de transações **diferentes**, no **mesmo item**, com **pelo menos uma escrita** (R-W, W-R, W-W).
- **Grafo de precedência**: aresta Ti → Tj se uma operação de Ti conflita com uma operação **posterior** de Tj.
  - **Sem ciclo** ⇒ seriável. Os escalonamentos seriais equivalentes são as **ordenações topológicas** (pode haver mais de uma).
  - **Com ciclo** ⇒ não seriável (0 seriais equivalentes).

### Exemplo resolvido (Ex. 3.2, questão 1)
`r1(X) r2(Z) r3(X) r1(Z) r2(Y) r3(Y) w1(X) c1 w2(Z) w3(Y) w2(Y) c3 c2`
- Conflitos: X: r3 → w1 ⇒ **T3→T1** · Z: r1 → w2 ⇒ **T1→T2** · Y: r2 → w3 ⇒ **T2→T3**; r3/w3 → w2 ⇒ **T3→T2** ⇒ **ciclo** T2↔T3
- Serial **não** · seriável **não** · **0** seriais equivalentes
- Nenhuma leitura suja (todas as leituras vêm antes de qualquer escrita) ⇒ **recuperável sim**, **ACA sim**
- `w2(Y)` escreve Y escrito por T3 **antes** de `c3` ⇒ **estrito não**

Outros dois do mesmo exercício estão em [[Banco de Questões P2#Escalonamentos (revisão P1, cobrados na E3)]].
