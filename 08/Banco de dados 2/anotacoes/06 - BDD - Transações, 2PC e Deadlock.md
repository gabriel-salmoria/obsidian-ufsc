---
tags: [bd2, p2, bdd]
---
# 06 · BDs Distribuídos: Transações, 2PC, Concorrência e Deadlock

[[Banco de dados 2|↑ Índice]] · anterior: [[05 - BDD - Processamento de Consultas]]
Slides: [[04b - Bancos de dados distribuídos.pdf]] (seção 5) · Exercícios: Exercício 4.4 (2PC) no Moodle, ainda **não feito** · **E4** em [[Banco de Questões P2#E4 - BDD, 2PC e fragmentação]]

## Atomicidade: Two-Phase Commit (2PC)
Um participante é o **coordenador**.

**Fase 1, preparação (votação):**
1. O coordenador grava `<PREPARE T>` no log e pede a cada nó envolvido que se **prepare para o commit**.
2. Cada participante, se conseguir, grava os registros de log (e os dados necessários) em disco, grava **`<READY T>`** no seu log e responde **pronto**. **Depois do READY, não pode mais abortar por conta própria.**
3. Se não conseguir, responde **não** (ou não responde: **timeout**).

**Fase 2, decisão:**
- **Todos** responderam READY ⇒ o coordenador grava `<COMMIT T>` e manda **commit** para todos.
- **Algum** respondeu não **ou estourou o timeout da fase 1** ⇒ `<ABORT T>` e manda **rollback** para todos.

### Como resolver as questões de log (E4 e Exercício 4.4)
Para a transação T e um nó que falhou por **mais que o timeout da 1ª fase**:
1. O coordenador já tem `<PREPARE T>`? Se não tem, T nem entrou no 2PC.
2. **O nó que falhou já tinha gravado `<READY T>` antes de cair?**
   - **Sim** ⇒ o voto dele chegou ⇒ se todos os outros também deram READY, a decisão é **COMMIT**. Quando o nó volta, ele vê READY sem decisão no log e **pergunta ao coordenador** (fica bloqueado até saber).
   - **Não** (o log dele termina antes do READY) ⇒ não votou ⇒ timeout ⇒ **ABORT**.
3. Algum outro participante sem READY também leva a **ABORT**.

**E4**: o nó BR já tinha `<READY T2>` quando caiu ⇒ **T2 COMMIT**. O nó UK caiu sem `<READY T1>` (log termina em `RL1(E)`) ⇒ **T1 ABORT**.

- **Bloqueio**: se o **coordenador** cair depois de os participantes darem READY, eles ficam **bloqueados** (não podem decidir sozinhos). O **3PC** (three-phase commit) reduz isso.
- A recuperação local em cada nó usa o log normalmente ([[03 - Recuperação de Falhas]]), mais as marcas READY/COMMIT do 2PC.

### Identificar a variante de 2PL nos logs (E4 Q3)
Mesma receita de [[01 - Controle de Concorrência - Trancas e 2PL#Como identificar a variante numa sequência (receita para a prova)]], aplicada **em cada nó**. No E4: todas as trancas de T2 vêm antes das operações (**conservativo**), e as de escrita não são liberadas antes do fim, mas `UL2(B)` (leitura) é liberado antes do READY/commit ⇒ **conservativo e estrito** (não rigoroso).

## Consistência: serialização distribuída
- **Otimistas**: execução livre, monitoramento de conflitos (grafos ou **relógios lógicos**). Em conflito, a transação **mais nova** é desfeita e refeita depois.
- **Exclusão mútua por bloqueio (locks)**: **troca de mensagens** para pedir bloqueios locais. **Deadlock é mais difícil de detectar.**

### Locks com dados replicados
- **Cópia primária**: a cópia que **coordena os locks** daquele item. A **cópia secundária** é atualizada de forma **síncrona** com a primária e assume em caso de falha.
- **Site primário / coordenador único**: todas as cópias primárias no **mesmo site**. Simples, mas é **ponto único de falha e gargalo**.
- **Cópia primária / coordenadores múltiplos**: cópias primárias em sites diferentes.
- **Eleição** de um novo coordenador quando o atual falha.
- **Protocolo desviado** (*read-one, write-all*): bloqueio **compartilhado** (leitura) **só local**; bloqueio **exclusivo** (escrita) em **todas as réplicas**.
- **Votação**: lock concedido pela maioria das réplicas.
- **Marcador de tempo**: **centralizado** (relógio ou contador local) ou **distribuído** (**relógios lógicos**, Lamport).

## Deadlock distribuído
- Cada site tem um **grafo de espera local**. Um ciclo pode aparecer só no **grafo global** (ex.: T1→T2 no site A e T2→T1 no site B).
- **Detecção centralizada**: os grafos locais vão para um **nó central**, que concatena e procura ciclos.
- **Detecção hierárquica**: nós organizados em hierarquia; cada um manda o grafo para o **pai**.
- **Timeout**: aborta a transação que espera demais e a recomeça logo depois.
