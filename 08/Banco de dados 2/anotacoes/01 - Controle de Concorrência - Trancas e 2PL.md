---
tags: [bd2, p2, concorrencia]
---
# 01 · Controle de Concorrência: Trancas e 2PL

[[Banco de dados 2|↑ Índice]] · anterior: [[00 - Base - Caracterização de Escalonamentos]] · próximo: [[02 - Outros Métodos de Concorrência e Níveis de Isolamento]]
Slides: [[03 - Transações, concorrência e recuperação.pdf]] (parte depois da P1) · Livro: Elmasri & Navathe 7ª ed., **cap. 21** (6ª ed. PT: cap. 22)
Exercícios: Exercício 3.3 (2PL) no Moodle, ainda **não feito** · **E3** (questões 15 a 18 em [[Banco de Questões P2]])

## Tranca (lock)
Mecanismo que indica o estado de um item (campo, registro, tabela, BD, bloco de dados ou de índice) quanto ao acesso concorrente. Usado com **protocolos** para garantir escalonamentos **seriáveis** e ao menos **recuperáveis**.
- **Granularidade**: campo < registro < tabela < BD. Fina = mais concorrência e mais overhead.

### Binária
- Estados: 0 livre, 1 trancado.
- `L(X)`: espera enquanto `X.locked = 1`, depois seta 1.
- `UL(X)`: zera e acorda quem espera.
- Os dois precisam ser **região crítica** (atômicos). Senão, duas transações podem ver `locked = 0` e ambas pegar a tranca.

### Compartilhada (a mais usada)
- Estados: 0 livre · 1 **leitura** (compartilhada, várias T podem ler) · 2 **escrita** (exclusiva).
- `RL(X)`: suspende se X está trancado para **escrita**.
- `WL(X)`: suspende se X está trancado para escrita **ou** para leitura por **outra** T.
- `UL(X)`: libera; se havia vários leitores, só decrementa o contador.

**Compatibilidade**
| | RL | WL |
|---|---|---|
| **RL** | ✅ | ❌ |
| **WL** | ❌ | ❌ |

**Diretrizes**
1. `WL(X)` antes de `W(X)`.
2. `RL(X)` ou `WL(X)` antes de `R(X)`.
3. Liberar toda tranca antes de terminar (commit ou abort).
4. Só fazer `UL(X)` se tiver a tranca.
5. **Upgrade** `RL(X) → WL(X)` é permitido, mas pode suspender T se outra T estiver lendo X.

> [!warning] Trancas sozinhas **não** garantem serialidade
> Liberar cedo ("pega, usa, solta") mantém o escalonamento não seriável:
> `RL1(X) R1(X) UL1(X) RL2(X) R2(X) UL2(X) WL1(X) W1(X) ...`

## Two-Phase Locking (2PL)
> **Nenhuma transação libera tranca alguma antes de ter alocado todas as trancas de que precisa.**

- **Fase de expansão** (só aloca) → **lock point** → **fase de contração** (só libera).
- Garante **seriabilidade** (a ordem dos lock points é uma ordem serial equivalente).
- **Não** evita **deadlock** (exceto o conservativo) e, sozinho, **não** garante recuperabilidade.

### Variantes
| Variante | Regra | Efeito |
|---|---|---|
| **Simples / básico** | só a regra das 2 fases | pode ter deadlock e rollback em cascata |
| **Conservativo** (estático) | aloca **todas** as trancas, no estado mais forte necessário, **antes da 1ª leitura/escrita**; se não conseguir alguma, libera as que pegou e tenta depois | **livre de deadlock**, mas pode ter **starvation**; precisa saber de antemão o que vai acessar |
| **Estrito** | retém as trancas de **escrita** até o **COMMIT/ABORT** | escalonamentos **estritos**, simplifica a recuperação |
| **Rigoroso** | retém **todas** as trancas (leitura e escrita) até o **COMMIT** | ainda mais simples; a ordem de commit é a ordem serial |

"Conservativo" fala de **quando aloca** (início). "Estrito/rigoroso" fala de **quando libera** (fim). Dá para combinar: *conservativo e estrito*, *conservativo e rigoroso*.

### Como identificar a variante numa sequência (receita para a prova)
Para **cada transação**:
1. **É 2PL?** Existe algum `UL` **antes** de algum `RL/WL` da **mesma** transação? Se sim, **não é 2PL**.
2. **Conservativo?** Todos os `RL/WL` dela aparecem **antes** do primeiro `R/W` dela?
3. **Estrito?** Todo `UL` de item com **WL** aparece **depois** do `C` dela?
4. **Rigoroso?** **Todo** `UL` (inclusive dos RL) aparece **depois** do `C`?
5. Se só uma das transações quebra a regra, a sequência **não** segue aquela variante.

### Exemplo do slide: `R1(X) R2(Y) W1(X) C1 W2(Y) C2`
- **Simples**: `RL1(X) R1(X) RL2(Y) R2(Y) WL1(X) W1(X) UL1(X) C1 WL2(Y) W2(Y) UL2(Y) C2`
- **Conservativo** (não estrito): `WL1(X) R1(X) WL2(Y) R2(Y) W1(X) UL1(X) C1 W2(Y) UL2(Y) C2`
- **Estrito/rigoroso** (não conservativo): `RL1(X) R1(X) RL2(Y) R2(Y) WL1(X) W1(X) C1 UL1(X) WL2(Y) W2(Y) C2 UL2(Y)`
- **Conservativo e estrito/rigoroso**: `WL1(X) R1(X) WL2(Y) R2(Y) W1(X) C1 UL1(X) W2(Y) C2 UL2(Y)`

Repare: no conservativo, quem vai ler **e** escrever X já pede `WL(X)` no início ("no estado mais forte").

## Deadlock e starvation
- **Deadlock**: ciclo no **grafo de espera** (*wait-for graph*): Ti → Tj se Ti espera tranca que Tj tem.
  Ex.: `RL1(X) R1(X) RL2(X) R2(X) WL1(X) WL2(X)`: T1 espera T2 e T2 espera T1.
- **Prevenção**:
  - **2PL conservativo**;
  - ordenar os itens e sempre trancar nessa ordem;
  - por timestamp (TS menor = mais velha):
    - **wait-die**: se a mais velha pede, **espera**; se a mais nova pede, **morre** (aborta e reinicia com o mesmo TS);
    - **wound-wait**: se a mais velha pede, **fere** (aborta) a mais nova; se a mais nova pede, **espera**;
  - **no-waiting** (aborta na hora) e **cautious waiting** (só espera se quem tem a tranca não estiver esperando ninguém).
- **Detecção**: o sistema mantém o grafo de espera e, achando ciclo, aborta uma **vítima** (a que fez menos trabalho, por exemplo).
- **Timeout**: espera demais ⇒ aborta (simples, pode abortar sem haver deadlock).
- **Starvation**: uma T nunca consegue executar (sempre é a vítima, ou sempre perde a tranca). Resolve com prioridade crescente, FIFO, ou o reinício com o mesmo TS em wait-die/wound-wait.
