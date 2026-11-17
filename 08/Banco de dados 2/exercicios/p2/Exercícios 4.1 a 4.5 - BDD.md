---
tags: [bd2, p2, exercicios, bdd]
---
# Exercícios 4.1 a 4.5: Bancos de Dados Distribuídos

[[Banco de dados 2|↑ Índice]] · teoria: [[04 - BDD - Conceitos, Fragmentação e Replicação]], [[05 - BDD - Processamento de Consultas]], [[06 - BDD - Transações, 2PC e Deadlock]]

Enunciados copiados do Moodle, com roteiro de resolução meu. São **adaptados de provas anteriores e do Elmasri**, o tipo de coisa que deve aparecer na Parte 2 da P2.

---

## 4.1: Fragmentação (Elmasri)
`LIVRO(Num_livro, Autor_principal, Assunto, Estoque_total, preco)` · `LIVRARIA(Num_livraria, Cidade, Estado, CEP, Valor_estoque_total)` · `ESTOQUE(Num_livraria, Num_livro, Qtd)`
Em álgebra relacional:
- a) dois predicados simples para fragmentar `LIVRARIA` horizontalmente;
- b) fragmentos de `ESTOQUE` derivados de (a);
- c) predicados para fragmentar `LIVRO` por `assunto`;
- d) fragmentação ainda maior de `ESTOQUE` combinando (b) e (c).

**Roteiro:**
- a) $LIV_1 = \sigma_{Estado='SC'}(LIVRARIA)$, $LIV_2 = \sigma_{Estado\neq'SC'}(LIVRARIA)$. Ou por valor: `Valor_estoque_total < 100000` / `>= 100000`. Os predicados têm que ser **completos e disjuntos**.
- b) $EST_i = \pi_{ESTOQUE.*}(ESTOQUE \bowtie_{Num\_livraria} LIV_i)$, ou seja $ESTOQUE \ltimes LIV_i$.
- c) $LVR_k = \sigma_{Assunto = a_k}(LIVRO)$ para cada assunto $a_k$ (mais um fragmento "outros" para garantir completude).
- d) $EST_{ik} = \pi_{ESTOQUE.*}(ESTOQUE \bowtie LIV_i \bowtie LVR_k)$: estoque da região i **e** do assunto k.

## 4.2: Consultas e atualizações com fragmentos (Elmasri)
Nós LESTE, CENTRO, OESTE. `LIVRO` por preço: B1 ≤ 20; B2 20,01–50; B3 50,01–100; B4 > 100. `LIVRARIA` por CEP: S1 (LESTE) ≤ 35.000; S2 (CENTRO) 35.001–70.000; S3 (OESTE) 70.001–99.999. `ESTOQUE` derivado de `LIVRARIA`.
Alocação de LIVRO: LESTE {B1, B4}, CENTRO {B1, B2}, OESTE {B1, B2, B3, B4}.
- a) `SELECT Num_livro, Estoque_total FROM Livro WHERE preco > 15 AND preco < 55` submetida em **LESTE**: que subconsultas remotas?
- b) Livro 1234 muda de R$45 para R$55 no CENTRO: que atualizações?
- c) Uma consulta em OESTE que necessariamente gera subconsulta no CENTRO.

**Roteiro:**
- a) Fragmentos relevantes: **B1** (parte com preco > 15), **B2** (inteiro), **B3** (parte com preco < 55). **B4 é eliminado.** B1 é **local**. B2 e B3 vêm do **OESTE**, o único nó com B3, então um nó remoto só:
  ```sql
  -- OESTE (remota):
  SELECT Num_livro, Estoque_total FROM B2
  UNION ALL
  SELECT Num_livro, Estoque_total FROM B3 WHERE preco < 55;
  -- LESTE (local) + união com o resultado remoto:
  SELECT Num_livro, Estoque_total FROM B1 WHERE preco > 15;
  ```
- b) O livro **migra de B2 para B3**: `DELETE FROM B2 WHERE Num_livro = 1234` em **todas as réplicas de B2** (CENTRO e OESTE) e `INSERT INTO B3 (...) VALUES (1234, ..., 55.00)` em **OESTE** (único nó com B3). `ESTOQUE` não muda (é derivado de LIVRARIA, não de LIVRO).
- c) Qualquer coisa que dependa de **S2** ou do **ESTOQUE derivado de S2**, que só existem no CENTRO (sem réplica). Ex.: `SELECT * FROM LIVRARIA WHERE CEP BETWEEN 35001 AND 70000;` ou o estoque total das livrarias do centro.

## 4.3: Estratégia frente à distribuição (prof. Ronaldo Mello)
`Funcionário` no **nodo1**. `Filial` fragmentada por cidade: 20 filiais de Florianópolis no **nodo2**, 10 de Blumenau no **nodo3**. Consulta submetida no **nodo2**:
```sql
SELECT F.codF, F.nome, F.nroFilial
FROM Funcionário F INNER JOIN Filial Fi ON F.nroFilial = Fi.nroFilial
WHERE Fi.cidade IN ('Florianópolis', 'Blumenau');
```
Alternativas:
1. filtrar os funcionários no nodo1 com os códigos de filial vindos de nodo2 e nodo3, e mandar o resultado para o nodo2;
2. trazer os atributos de **todos** os funcionários + os códigos de filial de Blumenau para o nodo2.

**Roteiro:**
- (a) $N1.Funcionario \leftarrow Funcionario$; $N2.Filial \leftarrow \sigma_{cidade='Florianópolis'}(Filial)$; $N3.Filial \leftarrow \sigma_{cidade='Blumenau'}(Filial)$
- (b) **Alt. 1**:
  ```sql
  -- nodo2: CREATE VIEW N2.Fil AS SELECT nroFilial FROM N2.Filial;          -- 20 · |nroFilial| → nodo1
  -- nodo3: CREATE VIEW N3.Fil AS SELECT nroFilial FROM N3.Filial;          -- 10 · |nroFilial| → nodo1
  -- nodo1: CREATE VIEW N1.Res AS SELECT codF, nome, nroFilial FROM N1.Funcionario
  --          WHERE nroFilial IN (SELECT nroFilial FROM N2.Fil UNION SELECT nroFilial FROM N3.Fil);
  -- nodo2: SELECT * FROM N1.Res;                                            -- k · (|codF|+|nome|+|nroFilial|) → nodo2
  ```
  **Alt. 2**:
  ```sql
  -- nodo1: CREATE VIEW N1.Todos AS SELECT codF, nome, nroFilial FROM N1.Funcionario;  -- N · (...) → nodo2
  -- nodo3: CREATE VIEW N3.Fil AS SELECT nroFilial FROM N3.Filial;                     -- 10 · |nroFilial| → nodo2
  -- nodo2: SELECT * FROM N1.Todos WHERE nroFilial IN (SELECT nroFilial FROM N2.Filial
  --                                                   UNION SELECT nroFilial FROM N3.Fil);
  ```
- (c) Alt. 1: $30\cdot|nroFilial| + k\cdot(|codF|+|nome|+|nroFilial|)$, com k = funcionários dessas 30 filiais. Alt. 2: $10\cdot|nroFilial| + N\cdot(|codF|+|nome|+|nroFilial|)$, com N = **todos** os funcionários.
- (d) A **alt. 1** é mais barata sempre que $k \ll N$, o que é o caso normal e piora para a alt. 2 conforme a rede cresce para outras cidades e países. A alt. 2 só empata quando quase todos os funcionários são de Floripa e Blumenau ($k \approx N$). Nesse caso a alt. 1 paga só as 20 chaves extras.

## 4.4: Recuperação em BDD com 2PC (quiz no Moodle, ainda não feito)
3 nós; T1 em RJ, SP e SC; T2 só em SP e SC (coordenador = **SC**).
| Nodo RJ | Nodo SP | Nodo SC (coord.) |
|---|---|---|
| `<START T1>` | `<START T1>` | `<START T1>` |
| `RL1(A)` | `<START T2>` | `<START T2>` |
| `R1(A)` | `RL2(C)` | `RL2(D)` |
| `WL1(B)` | `R2(C)` | `R2(D)` |
| `UL1(A)` | `WL2(C)` | `UL2(D)` |
| `W1(B)` | `W2(C)` | `<PREPARE T2>` |
| `UL1(B)` | `UL2(C)` | `WL1(D)` |
| `<READY T1>` | `<READY T2>` | `W1(D)` |

As perguntas só aparecem ao abrir o quiz. Para aplicar a receita de [[06 - BDD - Transações, 2PC e Deadlock#Como resolver as questões de log (E4 e Exercício 4.4)]], observe:
- **T2**: o coordenador SC tem `<PREPARE T2>`, SP tem `<READY T2>` ⇒ todos prontos ⇒ **COMMIT**. Se SP cair agora, ao voltar ele precisa perguntar ao coordenador.
- **T1**: no trecho mostrado, o coordenador **ainda não** gravou `<PREPARE T1>`, mas RJ já tem `<READY T1>`. SP **não tem READY T1**. Se SP falhar por mais que o timeout da votação ⇒ **ABORT**. RJ, que está READY, não pode abortar sozinho e espera a decisão do coordenador.
- Variante de 2PL: RJ faz `UL1(A)` **antes** de `W1(B)` (libera cedo) e `UL1(B)` antes do READY/commit ⇒ **não estrito**. Os locks de T1 em RJ vêm antes das operações (`RL1(A)` antes de `R1(A)`, mas `WL1(B)` vem **depois** de `R1(A)`) ⇒ **não conservativo**. Confira com cuidado na hora.

## 4.5: Fragmentos formais + otimização (adaptado de prova anterior)
`Aluno(idA, nomeA, uf, foto)` · `Cursa(idA, idD, dataIn, dataFim, nota)` · `Disciplina(idD, nomeD, descrição, conteúdo, siteWeb)`
- a) Fragmentos e alocação em **SC** e **RS**: Aluno horizontal por `uf` (exceto RS, RJ, PE, DF); Cursa derivada de Aluno (idem); Disciplina **replicada em todos os nós**; Aluno e Cursa **inteiras replicadas** em RS, RJ, PE e DF.
- b) SQL por nó (SC e RS) para a consulta abaixo, submetida em SC, minimizando tráfego:
```sql
SELECT D.*, COUNT(DISTINCT A.*) AS nAlunos, AVG(nota) AS mNotas
FROM Aluno A NATURAL JOIN Cursa C NATURAL JOIN Disciplina D
GROUP BY D.* HAVING nAlunos > 1000 AND mNotas < 7
ORDER BY mNotas ASC, nAlunos DESC;
```
**Roteiro:**
- a)
  ```
  Nodo SC:  AlunoSC ← σ uf='SC' (Aluno)              SC.Aluno ← AlunoSC
            CursaSC ← π C.* (AlunoSC ⋈ Cursa C)      SC.Cursa ← CursaSC
            SC.Disciplina ← Disciplina
  Nodo RS:  RS.Aluno ← Aluno   RS.Cursa ← Cursa   RS.Disciplina ← Disciplina
  ```
- b) O agregado é sobre **todos** os alunos, e só **RS** tem tudo. Agrega em RS e manda **só os grupos que passam no HAVING** (poucos). `D.*` **não** precisa trafegar, porque Disciplina está replicada em SC. A junção com Aluno pode sair: Cursa já tem idA, e `COUNT(DISTINCT idA)` basta (integridade referencial).
  ```sql
  -- RS:
  CREATE VIEW RS.Res AS
    SELECT idD, COUNT(DISTINCT idA) AS nAlunos, AVG(nota) AS mNotas
    FROM RS.Cursa GROUP BY idD
    HAVING COUNT(DISTINCT idA) > 1000 AND AVG(nota) < 7;     -- tráfego k · (|idD|+|nAlunos|+|mNotas|)
  -- SC (onde o resultado é esperado):
  SELECT D.*, R.nAlunos, R.mNotas
  FROM SC.Disciplina D NATURAL JOIN RS.Res R
  ORDER BY R.mNotas ASC, R.nAlunos DESC;
  ```
  Usar SC.Cursa + parciais de RS daria contagem dupla (RS já contém os alunos de SC) e mais tráfego.
