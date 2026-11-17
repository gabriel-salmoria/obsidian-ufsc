---
tags: [bd2, p2, bdd]
---
# 04 · BDs Distribuídos: Conceitos, Fragmentação e Replicação

[[Banco de dados 2|↑ Índice]] · anterior: [[03 - Recuperação de Falhas]] · próximo: [[05 - BDD - Processamento de Consultas]]
Slides: [[04a - Sistemas de BDs descentralizados.pdf]] · [[04b - Bancos de dados distribuídos.pdf]] · Livro: Elmasri & Navathe 7ª ed., **cap. 23**, pp. 841–882 (6ª ed. PT: **cap. 25**, pp. 589–615) · Özsu & Valduriez (no Moodle)
Exercícios: [[Exercícios 4.1 a 4.5 - BDD]]

## Arquiteturas (slides "descentralizados")
- Sistemas em geral: **cliente-servidor** × **peer-to-peer**.
- Sistemas de BD: **centralizado**, **distribuído**, **federações / multidatabases** (BDs autônomos integrados), **BDs na Web** (browser → servidor web → middleware → SGBD), **data warehouse / data lake**.

## Definições
- **BDD**: dados com propriedades análogas às de um BD centralizado (acesso sistemático via SQL, compartilhado, **integrado num esquema único**), mas **armazenados e gerenciados em vários locais**.
- **SBDD**: coleção de **nós**, cada um com um BD local, que juntos funcionam como **um único BD lógico**. Os nós executam consultas locais e consultas que acessam dados de outros nós.
- **Homogêneo**: todos os nós com o mesmo SGBD. **Heterogêneo**: SGBDs diferentes (até não relacionais), integrados via **gateways**.
- Arquiteturas físicas (Elmasri): verdadeiramente distribuída (WAN), centralizada com acesso via rede, BD paralelo *shared-nothing*.

## Características desejáveis (Date & Codd, 1987)
1. **Autonomia local**: cada nó é independente (segurança, bloqueio, integridade, recuperação próprios).
2. **Não dependência de nó central**: evita ponto único de falha e gargalo.
3. **Operação contínua**: nunca desligar; backup e recuperação online e incrementais.
4. **Transparência / independência de localização**: o usuário não sabe onde estão os dados (sinônimos, dicionário de dados), e aplicações podem migrar de nó.
5. **Independência de fragmentação**: tabelas fragmentadas de forma transparente.
6. **Independência de replicação**: réplicas sincronizadas automaticamente, de forma transparente.
7. **Processamento de consultas distribuído**: desempenho independente de onde a consulta é submetida; o otimizador considera localização, CPU, I/O e **rede**.
8. **Gerenciamento de transações distribuídas**: ACID e serialização também para transações distribuídas.
9. Independência de **hardware**, 10. de **SO**, 11. de **rede**, 12. de **SGBD**.

Na prática, a maioria dos SGBDDs **não** dá independência total de distribuição (às vezes nem é desejável, pelo overhead), e ACID costuma violar parcialmente a "não dependência de nó central" (há um coordenador).

### Teorema CAP
Um sistema distribuído **não suporta simultaneamente mais de 2 de 3**:
- **C**onsistência: toda leitura recebe o valor mais recente ou um erro;
- **A**vailability (disponibilidade): toda requisição recebe resposta sem erro;
- **P**artition tolerance (tolerância a partição): continua operando com falha de comunicação entre nós.

### Vantagens × desvantagens (em relação ao centralizado)
- ✅ Flexibilidade (dados geograficamente distribuídos com transparência) · compartilhamento e controle distribuídos (autonomia) · **maior confiabilidade e disponibilidade** (réplicas) · **desempenho** (paralelismo, dados perto de quem usa) · **escalabilidade** (mais fácil adicionar nós do que trocar o servidor central).
- ❌ Custo de desenvolvimento · potencial para bugs sutis · **overhead** de mensagens e coordenação · projeto mais difícil (fragmentação, replicação) · dificuldade de obter **conhecimento global** (concorrência, deadlock).
- Problemas específicos: acompanhar a distribuição (catálogo) · consultas distribuídas minimizando rede · transações distribuídas (ACID) · consistência das réplicas · recuperação com falhas de nós e de comunicação · segurança (mais nós, mais pontos de ataque).

## Fragmentação
Uma relação é dividida em **fragmentos** armazenados em nós diferentes.
- **Horizontal**: subconjunto de **tuplas**, por **seleção**: $F_i = \sigma_{p_i}(R)$.
  - Ex.: $Rio.TopModels \leftarrow FragJovens \leftarrow \sigma_{age<25}(TopModels)$
- **Vertical**: subconjunto de **atributos**, por **projeção**, **sempre incluindo a chave** (para reconstruir com junção): $F_i = \pi_{chave, A_1..A_k}(R)$.
  - Ex.: $SP.TopModels \leftarrow \pi_{mid,age}(TopModels)$, $Rio.TopModels \leftarrow \pi_{mid,name,sal}(TopModels)$
- **Horizontal derivada**: fragmenta R conforme os fragmentos de **outra** tabela S relacionada por FK, via **semijunção**: $R_i = R \ltimes S_i = \pi_{R.*}(R \bowtie S_i)$.
  - Ex. (E4): $SegueComSeguidor_{SC} \leftarrow \pi_{Segue.*}(Pessoa_{SC} \bowtie_{idP=idSeguidor} Segue)$, e $SC.Segue = SegueComSeguidor_{SC} \cup SegueComSeguido_{SC}$
- **Mista / híbrida**: vertical + horizontal combinadas.

**Regras de correção:**
- **Completude**: todo dado de R está em algum fragmento.
- **Reconstrução**: R = ∪ dos fragmentos horizontais, ou ⋈ (pela chave) dos fragmentos verticais.
- **Disjunção**: fragmentos horizontais não se sobrepõem (a não ser que seja replicação de propósito). Os verticais só repetem a chave.

**Notação usada nas provas (especificar e alocar):**
```
Nodo BR:
BR.Fabricante ← FabBR ← σ idPaís='BR' (Fabricante)        -- horizontal
BR.Capacidade ← CapBR ← π C.* (FabBR ⋈ Capacidade C)      -- derivada
BR.Produto    ← Produto                                   -- replicação total
BR.Compra     ← CompraCliBR ∪ CompraFabBR                 -- união de derivadas
```
"Especificação de um fragmento" (`FabBR ← σ...`) + "**atribuição** do fragmento a uma tabela física" (`BR.Fabricante ← FabBR`).

## Replicação e alocação
- **Réplicas** em vários nós: mais **paralelismo** e **disponibilidade**, **leituras mais rápidas**, mas **overhead nas atualizações** (todas as cópias).
- Graus: **total** (BD inteiro em todo nó), **parcial**, **nenhuma** (cada fragmento em um nó só).
- **Síncrona**: todas as cópias são atualizadas **antes do commit**; a distribuição fica transparente.
- **Assíncrona**: as cópias são atualizadas **periodicamente** e podem ficar inconsistentes por um tempo; o usuário precisa saber disso. **É o que os produtos atuais fazem.**
- **Alocação**: decidir em que nó fica cada fragmento ou réplica (perto de quem mais usa, custo de atualização).

## Projeto de BDD
- **LAV (Local-As-View)**: 1) projeta o **esquema global**; 2) define os fragmentos como **visões** do global e aloca nos nós. Mais fácil quando **não há BDs legados**.
- **GAV (Global-As-View)**: 1) parte dos esquemas **locais** existentes (legados); 2) define o global como **visão integrada** deles. Aproveita legados, mas traz problemas de **integração**.
