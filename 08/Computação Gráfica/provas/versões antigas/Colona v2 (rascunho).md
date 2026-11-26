---
tags: [cg, prova, colona, rascunho]
---
# Colona CG v2 (rascunho, em construção)

Versão grande da [[Colinha v1]]. Por enquanto só o capítulo de recorte está pronto, no formato que os outros vão seguir (explicação completa, contas, exercícios com resolução escondida).

## [S05] Clipping (recorte)
busca: clipping, recorte, recortar, clipar, clipagem, Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl, NLN, Sutherland-Hodgeman, Sutherland-Hodgman, Weiler-Atherton, region code, RC, código de região, códigos de regiões, ponto médio, polígono côncavo, coeficientes angulares, parâmetros pk qk, recorte de retas, recorte de polígonos

### Para que serve e onde entra no pipeline

O recorte decide o que da cena cai dentro da região visível (a window em 2D, o volume de visão em 3D) e joga fora ou corta o resto antes de rasterizar. Sem ele a gente gastaria tempo rasterizando coisas que nunca aparecem, e pior, coordenadas fora da viewport podem estourar a memória do frame buffer. No SGI do trabalho o recorte é feito em **SCN**, contra o quadrado fixo [−1, 1] × [−1, 1], porque aí a window pode girar e mudar de tamanho e o recorte continua igual ([S04]).

Tipos de recorte: ponto, reta (segmento), polígono (área), curva e texto. Em 3D: contra os 6 planos do volume canônico.

### Recorte de ponto

Um ponto (x, y) fica se xmin ≤ x ≤ xmax **e** ymin ≤ y ≤ ymax. Em SCN: −1 ≤ x ≤ 1 e −1 ≤ y ≤ 1. É o que se usa para recortar curvas desenhadas por pontos ou por segmentos muito pequenos.

### Cohen-Sutherland (retas)

Ideia: classificar cada extremo da reta numa das 9 regiões ao redor da window com um código de 4 bits e decidir rápido os casos fáceis.

Ordem dos bits usada na disciplina: **[acima, abaixo, direita, esquerda]** (valores 8, 4, 2, 1).
```
1001 | 1000 | 1010        acima:    y > ymax
-----+------+-----        abaixo:   y < ymin
0001 | 0000 | 0010        direita:  x > xmax
-----+------+-----        esquerda: x < xmin
0101 | 0100 | 0110
```
Casos:
- os dois códigos 0000 → reta toda dentro, desenha;
- código1 AND código2 ≠ 0000 → os dois do mesmo lado de fora, descarta sem calcular nada;
- senão → pode cruzar a window: calcula a interseção com uma das bordas indicadas pelos bits ligados, troca o extremo de fora pelo ponto da interseção e repete.

Interseções (m = Δy/Δx):
- borda vertical x = xb (esquerda ou direita): y = y1 + m·(xb − x1);
- borda horizontal y = yb (topo ou fundo): x = x1 + (yb − y1)/m.
Se a interseção cair fora do intervalo da outra coordenada, ela não serve; tenta a outra borda. Se nenhuma serve, a reta está toda fora mesmo com AND = 0 (caso do canto).

**CONTA**: window (0,0)–(10,8), reta A(−4, 2) → B(6, 12).
- Códigos: A está à esquerda (x < 0) → 0001. B está acima (y > 8) → 1000. AND = 0000, precisa calcular.
- m = (12 − 2)/(6 + 4) = 1.
- Borda esquerda (x = 0): y = 2 + 1·(0 + 4) = 6, dentro de [0, 8] → A' = (0, 6).
- Borda de cima (y = 8): x = −4 + (8 − 2)/1 = 2, dentro de [0, 10] → B' = (2, 8).
- Reta recortada: (0, 6) → (2, 8).

> [!example]- Exercício 5.1: window (2,2)–(12,10). Classifique e recorte P(0, 4) → Q(8, 14) e R(14, 0) → S(16, 6).
> - P: x < 2 → 0001. Q: y > 10 → 1000. AND = 0. m = 10/8 = 1,25.
>   - esquerda x = 2: y = 4 + 1,25·2 = 6,5 ✓ → (2; 6,5).
>   - topo y = 10: x = 0 + 6/1,25 = 4,8 ✓ → (4,8; 10).
>   - resultado (2; 6,5) → (4,8; 10).
> - R: x > 12 e y < 2 → 0110. S: x > 12 → 0010. AND = 0010 ≠ 0 → descarta direto (os dois à direita).

> [!example]- Exercício 5.2: por que Cohen-Sutherland pode fazer contas à toa?
> Porque escolhe uma borda pelo bit ligado e calcula a interseção mesmo que a reta esteja toda fora (caso do canto: AND = 0 mas a reta passa pelo canto sem entrar). Só depois de calcular percebe que o ponto cai fora do outro limite. Liang-Barsky resolve isso calculando os parâmetros de entrada e saída de uma vez.

### Liang-Barsky (retas)

Ideia: escrever a reta na forma paramétrica P(u) = P1 + u·(Δx, Δy), com u de 0 a 1, e descobrir em que u ela entra e sai da window.

Para cada uma das 4 bordas:
```
k = 1 (esquerda):  p1 = −Δx   q1 = x1 − xmin
k = 2 (direita):   p2 =  Δx   q2 = xmax − x1
k = 3 (fundo):     p3 = −Δy   q3 = y1 − ymin
k = 4 (topo):      p4 =  Δy   q4 = ymax − y1
```
- p_k = 0: reta paralela àquela borda; se q_k < 0 está fora (descarta tudo), senão ignora essa borda.
- p_k < 0: a reta vai de fora para dentro naquela borda → candidata a **entrada**: u1 = max(0, q_k/p_k, ...).
- p_k > 0: vai de dentro para fora → candidata a **saída**: u2 = min(1, q_k/p_k, ...).
- Se u1 > u2: a reta está fora. Senão, os novos extremos são P(u1) e P(u2).

**CONTA** (mesma reta do exemplo anterior): window (0,0)–(10,8), A(−4, 2) → B(6, 12), Δx = 10, Δy = 10.
- p = (−10, 10, −10, 10); q = (−4 − 0, 10 + 4, 2 − 0, 8 − 2) = (−4, 14, 2, 6).
- entradas (p < 0): k = 1: r = −4/−10 = 0,4; k = 3: r = 2/−10 = −0,2 → u1 = max(0; 0,4; −0,2) = 0,4.
- saídas (p > 0): k = 2: r = 14/10 = 1,4; k = 4: r = 6/10 = 0,6 → u2 = min(1; 1,4; 0,6) = 0,6.
- P(0,4) = (−4 + 4, 2 + 4) = (0, 6); P(0,6) = (−4 + 6, 2 + 6) = (2, 8). Mesmo resultado do Cohen-Sutherland.

> [!example]- Exercício 5.3: window (0,0)–(10,10), reta (−5, 12) → (5, 20). Liang-Barsky.
> Δx = 10, Δy = 8. p = (−10, 10, −8, 8); q = (−5, 15, 12, −2).
> Entradas: k = 1: 0,5; k = 3: 12/−8 = −1,5 → u1 = 0,5. Saídas: k = 2: 1,5; k = 4: −2/8 = −0,25 → u2 = min(1; 1,5; −0,25) = −0,25.
> u1 > u2 → fora (a reta passa toda acima da window).

### Cyrus-Beck

Generaliza o Liang-Barsky para qualquer polígono convexo: para cada borda com normal interna N e um ponto E da borda, o u de interseção é u = N·(E − P1) / N·(P2 − P1). O sinal de N·(P2 − P1) diz se é entrada ou saída. Liang-Barsky é o caso com as 4 normais alinhadas aos eixos.

### Nicholl-Lee-Nicholl (só 2D)

Ideia: com P1 numa região (dentro, borda ou canto), traçar retas de P1 até os 4 cantos da window. Elas dividem o plano em setores, e cada setor diz exatamente quais bordas a reta P1P2 cruza. Para saber em que setor P2 está, compara a **inclinação** de P1P2 com a das retas até os cantos. Por simetria basta tratar 3 casos de P1 (dentro, à esquerda, no canto inferior esquerdo); os outros se reduzem a esses girando/espelhando. É o que faz menos divisões, mas tem muitos casos para programar. Heurística simples para saber com quais retas comparar: olhar de que lado de P1 o P2 está (sinal de Δx e Δy).

### Subdivisão do ponto médio

Usa os códigos do Cohen-Sutherland: se não dá para aceitar nem rejeitar, divide a reta no ponto médio e repete em cada metade, até a metade ser aceita, rejeitada ou ficar do tamanho de um pixel. Só soma e divide por 2 (shift), por isso era usado em hardware.

### Recorte de polígonos

Recortar polígono como um monte de retas soltas não serve: o resultado tem que ser um polígono fechado, que às vezes inclui pedaços da borda da window, e um polígono côncavo pode virar vários.

**Sutherland-Hodgeman** (Hodgman): recorta o polígono inteiro contra uma borda de cada vez (esquerda, direita, baixo, cima); a lista de saída de uma borda é a entrada da próxima. Para cada aresta V1 → V2:

| caso | o que sai |
|---|---|
| fora → dentro | interseção e V2 |
| dentro → dentro | V2 |
| dentro → fora | interseção |
| fora → fora | nada |

**CONTA** (só a borda esquerda x = 0): triângulo A(−2, 2), B(4, 2), C(4, 6).
- A → B: fora → dentro: interseção (0, 2) e B(4, 2).
- B → C: dentro → dentro: C(4, 6).
- C → A: dentro → fora: interseção com x = 0 na reta C(4,6)–A(−2,2): m = 4/6, y = 6 + (2/3)(0 − 4) = 3,33 → (0; 3,33).
- Saída: (0,2), (4,2), (4,6), (0; 3,33): virou um quadrilátero.

Funciona bem com convexos; com côncavos pode deixar arestas "fantasma" correndo sobre a borda da window.

**Weiler-Atherton**: anda pela borda do polígono no sentido horário; quando sai da window, passa a andar pela borda da window até reencontrar o polígono entrando, e fecha a figura. Lida com côncavos e buracos e devolve vários polígonos quando o recorte os separa. Veio do paper de 1977 sobre remoção de superfícies ocultas.

> [!example]- Exercício 5.4: um polígono em forma de "U" é recortado por uma window que corta o fundo do U. Qual algoritmo dá dois polígonos separados?
> Weiler-Atherton. O Sutherland-Hodgeman devolve uma lista só de vértices, ligando as duas partes por uma aresta sobre a borda da window (aresta fantasma).

### Polígonos côncavos e windows não retangulares

- Identificar côncavo: produto vetorial das arestas consecutivas (componente z); se um sinal é diferente dos outros, é côncavo.
- Window convexa qualquer: Cyrus-Beck. Window côncava: divide em convexas.

### Recorte de curvas e em 3D

- Curva desenhada por segmentos pequenos: recorta cada segmento (ou testa os pontos).
- 3D: Cohen-Sutherland com 6 bits (acima, abaixo, direita, esquerda, frente, trás) contra o volume canônico; Liang-Barsky/Cyrus-Beck contra os planos. Na perspectiva, ou recorta contra o tronco de pirâmide, ou deforma ele num paralelepípedo antes.

### Resumo para reconhecer pelo enunciado

| se a questão fala de... | é |
|---|---|
| códigos de região, 4 bits, AND | Cohen-Sutherland |
| parâmetros pk e qk, forma paramétrica, u1/u2 | Liang-Barsky |
| inclinações comparadas com retas até os cantos | Nicholl-Lee-Nicholl |
| normal das bordas e produto escalar, janela convexa | Cyrus-Beck |
| recorta polígono borda por borda | Sutherland-Hodgeman |
| polígono côncavo, vários pedaços | Weiler-Atherton |
| Gauss-Seidel, Gauss-Jacobi, Runge-Kutta, Kruskal | não são de recorte (são de sistemas lineares, EDO e grafos) |
