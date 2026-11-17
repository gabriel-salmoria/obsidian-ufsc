---
tags: [cg, modulo-1, superficies]
---
# 09 · Superfícies Paramétricas Bicúbicas

[[Computação Gráfica|↑ Índice]] · anterior: [[08 - Projeção em Perspectiva e Clipping 3D]] · próximo: [[10 - Visualização Realista - Raytracing, Raycasting e Radiosidade]]
Slides: [[09.1 - Superfícies Bicúbicas.pdf]] · [[09.2 - Forward Differences em Superfícies Bicúbicas.pdf]] · Livros: [[Foley - Cap. 11 - Curvas e Superfícies.pdf]], [[Salomon - Curves and Surfaces for Computer Graphics.pdf]], [[Salomon - Forward Differences em Superfícies Bicúbicas.pdf]]
Colab de exemplos: [Superfícies de Bézier](https://colab.research.google.com/drive/1_xeGlpLo1GDImLPXfzdSviq-9LolQXDZ?usp=sharing) · Gist: [FD em retalho bicúbico](https://gist.github.com/awangenh/73983b81541abf2c71cc)

## Ideia
Uma curva é $Q(s) = S\cdot M\cdot G$. Se a **geometria G variar** com um segundo parâmetro t, isto é se cada elemento de G for **ele mesmo uma curva** $G_i(t)$, então:
- para t fixo, $Q(s, t_1)$ é uma curva 3D;
- variando t um pouco, $Q(s, t_2)$ é uma curva levemente diferente;
- a família de curvas varre uma **superfície** ("**retalho**", *patch*).

$$
x(s,t) = S\cdot M\cdot G_x\cdot M^T\cdot T^T,\qquad S = [s^3\;s^2\;s\;1],\;T = [t^3\;t^2\;t\;1],\quad s,t\in[0,1]
$$
- Uma **matriz de geometria 4×4 por coordenada** ($G_x, G_y, G_z$).
- M é a mesma das curvas ($M_H$, $M_B$, $M_{BS}$), ver [[05 - Curvas - Hermite e Bézier]] e [[06 - B-Splines e Forward Differences]].

## Tipos
- **Hermite**: $G_H$ 4×4 com os **4 cantos**, as **tangentes em s** e **em t** nos cantos e os **vetores de torção** (*twist*, $\partial^2 Q/\partial s\,\partial t$).
- **Bézier**: **16 pontos de controle** (4×4). O retalho passa pelos **4 cantos**; os outros 12 "puxam" a superfície. Trabalho 1.9: cada 4 linhas de 4 pontos formam um retalho.
- **B-spline**: matriz de controle **m×n** (4×4 até 20×20 no trabalho 1.10), cortada em submatrizes 4×4 que se sobrepõem andando de 1 em 1 → **(m−3)·(n−3) retalhos**, com continuidade **C2** entre eles.

## Desenhando: malha de curvas
Desenha-se uma **malha** (*mesh*) de curvas:
- **s fixo** e t variando de 0 a 1 → uma família de curvas;
- **t fixo** e s variando → a outra família.

### 1) Blending functions (trabalho 1.9)
Para cada $s_i$ e cada $t_j$ avalia $x(s_i,t_j)$ com a fórmula acima. Custa muitas multiplicações.

### 2) Forward differences (trabalho 1.10)
$$
C_x = M\cdot G_x\cdot M^T \qquad DD_x = E(\delta_s)\cdot C_x\cdot E(\delta_t)^T
$$
(E(δ) é a mesma matriz das curvas, ver [[06 - B-Splines e Forward Differences#Forward Differences]].)
- A **1ª linha** de $DD_x$ = $[x,\;\Delta_t x,\;\Delta_t^2 x,\;\Delta_t^3 x]$ são as condições iniciais da curva em t para o s atual. Desenha com `DesenhaCurvaFwdDiff`.
- Para **avançar s** de δs (próxima curva da família), atualiza as linhas:
  `linha1 += linha2; linha2 += linha3; linha3 += linha4`
- Depois **transpõe** $DD$ (recalculado com os papéis de s e t trocados) para desenhar a **outra família**.
- Vantagem: depois da inicialização, cada ponto custa só **somas**.
