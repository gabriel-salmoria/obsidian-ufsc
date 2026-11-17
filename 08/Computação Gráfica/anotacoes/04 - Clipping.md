---
tags: [cg, modulo-1]
---
# 04 · Clipping (Recorte)

[[Computação Gráfica|↑ Índice]] · anterior: [[03 - Sistema de Coordenadas Normalizadas (SCN)]] · próximo: [[05 - Curvas - Hermite e Bézier]]
Slides: [[04 - Clipping.pdf]] · Apostila: [[Apostila - Clipping.pdf]] · Exercícios: [[Revisão 1.3.3 - Exercícios de Clipping de Polígonos.pdf]] · Paper: [[Weiler & Atherton (1977) - Hidden Surface Removal Using Polygon Area Sorting.pdf]]
Videoaula interativa (vem do banco da prova): [Aula 4.2](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20785) · questões em [[Banco de Questões#2. Window, viewport e clipping]]

## O que é e por quê
- **Particionar primitivas geométricas**: saber se estão dentro ou fora de uma região (viewing frustum, picking frustum), detectar interseções, calcular sombras em 3D.
- É uma **otimização importante**, o pré-processamento de visibilidade. Remove boa parte da cena e garante que **só o potencialmente visível é rasterizado**.
- **Clip window**: a região/forma de recorte. O recorte é feito **em coordenadas da clip window** (SCN/PPC, ver [[03 - Sistema de Coordenadas Normalizadas (SCN)]]).
- Tipos: **ponto**, **linha**, **área (polígono)**, curva, texto.

## Ponto
Desenha se $x_{wmin} \le x \le x_{wmax}$ **e** $y_{wmin} \le y \le y_{wmax}$. Em SCN: $-1 \le x, y \le 1$.

## Retas: tabela-resumo (pergunta clássica: "qual algoritmo é...?")
| Algoritmo | Recorta | Ideia-chave |
|---|---|---|
| **Cohen-Sutherland** | retas | **region codes** de 4 bits + testes AND/OR |
| **Liang-Barsky** (reformula **Cyrus-Beck**, 1978 → 1984) | retas (e polígono/poliedro **convexo**) | equação **paramétrica** + parâmetros $p_k$, $q_k$ |
| **Nicholl-Lee-Nicholl** | retas, **só 2D** | regiões e **comparação de coeficientes angulares** com retas de P1 aos cantos; menos comparações e divisões que CS e LB |
| **Sutherland-Hodgeman** | **polígonos** | cada aresta da window recorta o polígono inteiro (4 passadas) |
| **Weiler-Atherton** | **polígonos** (inclusive côncavos, com buracos) | percorre as bordas trocando entre polígono e window nas interseções |
| Gauss-Seidel, Gauss-Jacobi, Runge-Kutta, Kruskal | ❌ **não são de CG** (sistemas lineares, EDOs, grafos) | distratores |

## Cohen-Sutherland
**Region Code (RC)**, 4 bits, na ordem do professor:
`RC[1] = acima`, `RC[2] = abaixo`, `RC[3] = direita`, `RC[4] = esquerda`

```
1001 | 1000 | 1010
-----+------+-----
0001 | 0000 | 0010      (0000 = dentro da window)
-----+------+-----
0101 | 0100 | 0110
```
Montagem:
- `x < xwesq → RC[4]=1`, `x > xwdir → RC[3]=1`
- `y < ywfundo → RC[2]=1`, `y > ywtopo → RC[1]=1`

Casos:
- **Totalmente dentro**: RC1 = RC2 = 0000 → desenha.
- **Totalmente fora**: RC1 **AND** RC2 ≠ 0000 (os dois do mesmo lado) → descarta.
- **Parcial**: RC1 ≠ RC2 e RC1 AND RC2 = 0000 → calcula interseções:
  - Esquerda/direita (x conhecido): $y = m(x_E - x_1) + y_1$
  - Topo/fundo (y conhecido): $x = x_1 + \frac{1}{m}(y_T - y_1)$
  - Se a interseção calculada cair **fora** do outro limite, ela não vale. Se o ponto é de canto (dois bits 1), calcula as duas e fica com a que cai sobre a window. Se nenhuma cai, a reta é descartada.

**Exemplo do slide**: window (10,10)–(25,20), R1 = (5,12)→(15,17). RC1 = 0001, RC2 = 0000. $m = 0{,}5$, $y = 0{,}5(10-5)+12 = 14{,}5$ → reta clipada **(10; 14,5)–(15,17)**.
R2 = (5,18)→(15,23): na esquerda dá y = 20,5 > 20 → fora → **descartada**.

## Liang-Barsky
Paramétrica: $x = x_1 + u\,\Delta x$, $y = y_1 + u\,\Delta y$, com $0\le u\le 1$.
$$
\begin{aligned}
p_1 &= -\Delta x, & q_1 &= x_1 - x_{wmin}\\
p_2 &= \Delta x, & q_2 &= x_{wmax} - x_1\\
p_3 &= -\Delta y, & q_3 &= y_1 - y_{wmin}\\
p_4 &= \Delta y, & q_4 &= y_{wmax} - y_1
\end{aligned}\qquad r_k = q_k/p_k
$$
- $p_k = 0$: reta **paralela** àquela borda. Se $q_k < 0$ está fora (descarta), se $q_k \ge 0$ está dentro.
- $p_k < 0$: a reta vai **de fora para dentro**, então entra em $\zeta_1 = \max(0, r_k)$.
- $p_k > 0$: vai **de dentro para fora**, então sai em $\zeta_2 = \min(1, r_k)$.
- Se $\zeta_1 > \zeta_2$ → **totalmente fora**. Senão os novos extremos são $P(\zeta_1)$ e $P(\zeta_2)$ (se $\zeta_1 = 0$ ou $\zeta_2 = 1$, aquele extremo não muda).
- **Exemplo**: R1 (5,12)→(15,17): p = (−10, 10, −5, 5), q = (−5, 20, 2, 8). $\zeta_1 = \max(0;\,0{,}5;\,-0{,}4) = 0{,}5$ → (10; 14,5). $\zeta_2 = \min(1;\,2;\,1{,}6) = 1$ → p2 fica igual.

## Nicholl-Lee-Nicholl
1. Classifica P1 em uma das 9 regiões. Só 3 casos são tratados (dentro, borda, canto); o resto vem por **simetria**.
2. Traça retas imaginárias de P1 aos **4 cantos** da window, o que divide o plano em regiões (L, T, R, B, LT, LR, LB, TR...).
3. Descobre a região de P2 **comparando inclinações**. Ex.: P1 à esquerda e P2 em LT se $m_{P_1 TR} < m_{P_1P_2} < m_{P_1 TL}$.
4. A região diz **quais bordas** cortam a reta, então só essas interseções são calculadas.

![[h5p-clip-nln-regioes.png]]

## Polígonos
- Clipar um polígono como várias retas **não serve**: o resultado precisa ser um polígono **fechado**, incluindo trechos das bordas da window. Um côncavo pode virar **2 polígonos** distintos.
- **Sutherland-Hodgeman**: recorta o polígono inteiro contra **uma aresta da window por vez** (esq → dir → baixo → cima). Para cada par de vértices (V1 → V2):
  - fora → dentro: salva **V1' (interseção) e V2**
  - dentro → dentro: salva **V2**
  - dentro → fora: salva **V1' (interseção)**
  - fora → fora: **nada**
  
  Funciona bem para **convexos**. Com côncavos pode gerar arestas "fantasmas" sobre a borda.
- **Weiler-Atherton**: anda pelas arestas do polígono. Ao **sair** da window, passa a andar pela **borda da window** até reencontrar o polígono. Lida com **côncavos** e gera múltiplos polígonos. (Origem: paper de 1977 sobre remoção de superfícies ocultas.)

## Polígonos côncavos e windows não retangulares
- Para **identificar** um côncavo, faça o produto vetorial das arestas consecutivas $(E_i \times E_{i+1})_z$ em sentido anti-horário. Uma **componente z negativa** no meio de positivas indica concavidade.
- Para **dividir**: método vetorial (corta ao longo da primeira aresta do par com z < 0) ou método da rotação (gira cada aresta para cima do eixo x; se o vértice seguinte fica abaixo, corta).
- Windows **convexas não retangulares**: Liang-Barsky/Cyrus-Beck com as equações de todas as bordas. Côncavas: divide em convexas. Círculos: usam o retângulo delimitador.

## Clipping de curvas (trabalho 1.5)
Gera a curva em pequenos segmentos de reta e faz clipping de **ponto** ou de reta em cada segmento. Ver [[05 - Curvas - Hermite e Bézier]].

## Clipping 3D
Ver [[08 - Projeção em Perspectiva e Clipping 3D#Clipping 3D (volume canônico)]]: Cohen-Sutherland com **6 bits**, Cyrus-Beck/Liang-Barsky contra planos.
