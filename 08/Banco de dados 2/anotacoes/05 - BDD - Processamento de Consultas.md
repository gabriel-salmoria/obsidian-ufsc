---
tags: [bd2, p2, bdd]
---
# 05 · BDs Distribuídos: Processamento de Consultas

[[Banco de dados 2|↑ Índice]] · anterior: [[04 - BDD - Conceitos, Fragmentação e Replicação]] · próximo: [[06 - BDD - Transações, 2PC e Deadlock]]
Slides: [[04b - Bancos de dados distribuídos.pdf]] (demonstrações 1, 2 e 3) · Exercícios: [[Exercícios 4.1 a 4.5 - BDD]]

> [!important] Provável formato da Parte 2 da P2
> Dado um esquema global, a fragmentação/alocação e uma consulta SQL **submetida a um nó X**:
> 1. **defina os fragmentos** em álgebra relacional;
> 2. escreva as **subconsultas SQL por nó**, usando só as tabelas materializadas em cada nó;
> 3. **estime o tráfego** em rede (atributos × nº de tuplas);
> 4. justifique por que a estratégia é a melhor.
> A Questão 3 da P1 (árvore otimizada + upload de PDF, 4 pontos) foi o equivalente na P1.

## O que considerar
- Onde estão as **réplicas** (escolher a cópia mais barata) e como **reconstruir** a relação a partir dos fragmentos.
- Custos de **processamento local** (CPU/I/O) **+ transmissão em rede**. Em WAN, **a rede domina**: o critério é **minimizar o tráfego**.
- O resultado tem que chegar ao **nó onde a consulta foi submetida**.
- **Toda referência a tabela ou visão de outro nó gera tráfego.** Indique sempre **em que nó roda cada subconsulta**.

## Técnicas
### 1. Eliminar fragmentos irrelevantes
Se o predicado da consulta contradiz o predicado do fragmento, o fragmento não precisa ser acessado. Ex. (4.2): `preco > 15 AND preco < 55` não toca B4 (preço > 100).

### 2. Agregação parcial (*push down* de agregados)
AVG global sobre fragmentos horizontais: **não** dá para fazer média de médias. Cada nó manda **SUM e COUNT**:
```sql
-- nodo Rio                                 -- nodo SP
CREATE VIEW Rio.Parc AS                     CREATE VIEW SP.Parc AS
  SELECT SUM(sal) AS s, COUNT(*) AS n         SELECT SUM(sal) AS s, COUNT(*) AS n
  FROM Rio.TopModels WHERE age > 20;          FROM SP.TopModels WHERE age < 35;
-- nodo onde a consulta foi submetida
SELECT SUM(s) / SUM(n) FROM (Rio.Parc UNION ALL SP.Parc);
```
Tráfego: só uma tupla `(s, n)` por nó.

### 3. Fragmentos verticais: mandar só as chaves filtradas
`AVG(sal) WHERE 20 < age < 35`, com `(mid, age)` em SP e `(mid, name, sal)` no Rio, submetida no Rio:
```sql
-- SP:  CREATE VIEW SP.Parc AS SELECT mid FROM SP.TopModels WHERE age > 20 AND age < 35;
-- Rio: SELECT AVG(sal) FROM Rio.TopModels T INNER JOIN SP.Parc P ON T.mid = P.mid;
```
Tráfego: k·|mid|. Se fosse submetida em SP, ainda precisaria mandar o resultado |avg| de volta.

### 4. Semijunção (semi-join)
Para juntar $R$ (em N1) com $S$ (em N2) sem mandar uma tabela inteira:
1. **N1** projeta só a **chave de junção** das tuplas relevantes: $N1.P \leftarrow \pi_{Key}(\sigma_{c1}(N1.R))$ e envia para N2;
2. **N2** filtra S por essas chaves: $N2.P \leftarrow \pi_{L2}(\sigma_{c2}(N2.S) \bowtie N1.P)$ e devolve só o necessário;
3. **N1** termina a junção: $\pi_{L1\cup L2}(N1.R \bowtie N2.P)$.

Compensa quando $|\pi_{key}|$ + o que volta for **menor** que mandar a tabela inteira. É a ferramenta principal das demonstrações 3 a 5.

### 5. Antijunção para "o que é de fora"
Com fragmentação derivada, "clientes de fora do país" = registros de `Compra` locais cujo cliente **não** está no `Cliente` local:
```sql
SELECT SUM(valor_total) FROM BR.Compra WHERE idC NOT IN (SELECT idC FROM BR.Cliente);
-- ou
SELECT SUM(Co.valor_total) FROM BR.Cliente C RIGHT JOIN BR.Compra Co ON C.idC = Co.idC WHERE C.idC IS NULL;
```
O E4 Q4 é exatamente isso: a consulta inteira roda **só no nó MG, sem tráfego**, porque `MG.Segue` já tem todo par em que o seguido é de MG, e "seguidor ≠ MG" é `idSeguidor NOT IN MG.Pessoa`.

## Exemplo das demonstrações (esquema Produto/Fabricante/Capacidade/Lote/Cliente/Compra, nós BR e US)
**Consulta 3**: soma das compras de clientes **US** de fabricantes **BR**, submetida em BR.
```sql
-- 1) BR: fabricantes BR que venderam para clientes de fora (só idF)     tráfego k_BR · |idF|
CREATE VIEW BR.FbrVendExt AS
  SELECT DISTINCT Co.idF FROM BR.Cliente C RIGHT JOIN BR.Compra Co ON C.idC = Co.idC
  WHERE C.idC IS NULL;
-- 2) US: soma das compras US desses fabricantes                          tráfego |valor_total|
CREATE VIEW US.Resultado AS
  SELECT SUM(Co.valor_total) FROM US.Compra Co NATURAL JOIN BR.FbrVendExt;
-- 3) BR: SELECT * FROM US.Resultado;
```

**Comparando alternativas** (demonstração da consulta 5): uma estratégia compensa quando o tráfego dela é menor, por exemplo
$k_{US}\cdot|F.*| < k_{BR\text{-}US}\cdot(|F.*|+|valor\_total|) + k_{BR}\cdot|idC|$.
Escreva sempre o tráfego como **nº de tuplas × tamanho dos atributos** em cada seta entre nós.

## Checklist para a resposta escrita
- [ ] Fragmentos definidos em AR (σ / π / ⋈ derivado / ∪) **e** alocados (`Nodo.Tabela ← Frag`)
- [ ] Cada subconsulta rotulada com o **nó** e usando **só tabelas daquele nó** (ou visões recebidas)
- [ ] Ordem numerada dos passos (1a, 1b, 2...)
- [ ] Tráfego estimado em cada passo
- [ ] Filtrar e agregar **antes** de transmitir; mandar **chaves**, não tuplas inteiras
- [ ] Discutir quando a estratégia deixa de ser a melhor (crescimento dos dados, novos nós; Ex. 4.3 d)
