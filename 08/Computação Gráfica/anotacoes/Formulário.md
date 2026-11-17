---
tags: [cg, prova, formulario]
---
# Formulário (para consulta rápida durante a prova)

[[Computação Gráfica|↑ Índice]] · [[Banco de Questões]]

## Window → Viewport
$$x_v = x_{vmin} + \frac{x_w - x_{wmin}}{x_{wmax}-x_{wmin}}(x_{vmax}-x_{vmin})\qquad
y_v = y_{vmin} + \left(1-\frac{y_w - y_{wmin}}{y_{wmax}-y_{wmin}}\right)(y_{vmax}-y_{vmin})$$
**y da viewport aponta para baixo.** SCN [−1,1] com origem no centro da window: $x_{scn} = 2\frac{x-x_{wmin}}{x_{wmax}-x_{wmin}}-1$.
Detalhes: [[01 - Conceitos Básicos]], [[03 - Sistema de Coordenadas Normalizadas (SCN)]]

## Homogêneas 2D (vetor-linha: $[x\,y\,1]\cdot M$, translação na última linha)
$$T=\begin{bmatrix}1&0&0\\0&1&0\\D_x&D_y&1\end{bmatrix}\;
S=\begin{bmatrix}S_x&0&0\\0&S_y&0\\0&0&1\end{bmatrix}\;
R=\begin{bmatrix}\cos&\sin&0\\-\sin&\cos&0\\0&0&1\end{bmatrix}$$
(em vetor-coluna tudo é transposto; o H5P mostra R como $\begin{bmatrix}\cos&-\sin\\\sin&\cos\end{bmatrix}$)
- Em torno de um ponto c: $T(-c)\,X\,T(c)$ → escala vira $\begin{bmatrix}a&0&0\\0&b&0\\c_x(1-a)&c_y(1-b)&1\end{bmatrix}$
- Centro = média dos vértices. W ≠ 0, usamos W = 1.

## Clipping
- **CS**: RC = [acima, abaixo, direita, esquerda]; dentro se ambos 0000; fora se AND ≠ 0.
  $y = m(x_E-x_1)+y_1$ (bordas verticais), $x = x_1 + (y_T-y_1)/m$ (bordas horizontais)
- **LB**: $p=(-\Delta x, \Delta x, -\Delta y, \Delta y)$, $q=(x_1-x_{min}, x_{max}-x_1, y_1-y_{min}, y_{max}-y_1)$, $r=q/p$
  $\zeta_1=\max(0, r_k|_{p_k<0})$, $\zeta_2=\min(1, r_k|_{p_k>0})$, $\zeta_1>\zeta_2$ → fora
- Retas: CS, LB (Cyrus-Beck), NLN (só 2D, inclinações). **Polígonos: Sutherland-Hodgeman, Weiler-Atherton.**
Detalhes: [[04 - Clipping]]

## Curvas: $x(t) = T\,M\,G_x$, $T=[t^3\;t^2\;t\;1]$
$$M_H=\begin{bmatrix}2&-2&1&1\\-3&3&-2&-1\\0&0&1&0\\1&0&0&0\end{bmatrix}G=\begin{bmatrix}P_1\\P_4\\R_1\\R_4\end{bmatrix}\quad
M_B=\begin{bmatrix}-1&3&-3&1\\3&-6&3&0\\-3&3&0&0\\1&0&0&0\end{bmatrix}\quad
M_{BS}=\tfrac16\begin{bmatrix}-1&3&-3&1\\3&-6&3&0\\-3&0&3&0\\1&4&1&0\end{bmatrix}$$
- Bézier: passa em P1, P4; $R_1 = 3(P_2-P_1)$, $R_4=3(P_4-P_3)$; fecho convexo.
- B-spline: n pontos → n−3 segmentos; C2; controle local; não interpola.
- Continuidade: G0 (encontro) · G1 (mesma direção) · C1 (mesma direção e módulo) · C2.
Detalhes: [[05 - Curvas - Hermite e Bézier]], [[06 - B-Splines e Forward Differences]]

## Forward differences
$$E(\delta)=\begin{bmatrix}0&0&0&1\\\delta^3&\delta^2&\delta&0\\6\delta^3&2\delta^2&0&0\\6\delta^3&0&0&0\end{bmatrix},\quad D = E\,C,\quad C = M\,G$$
Loop: `x+=Dx; Dx+=D2x; D2x+=D3x` (D3x constante).
Superfície: $DD = E(\delta_s)\,(M G M^T)\,E(\delta_t)^T$; próxima curva: `L1+=L2; L2+=L3; L3+=L4`.
Detalhes: [[09 - Superfícies Bicúbicas]]

## Superfícies
$x(s,t) = S\,M\,G_x\,M^T\,T^T$ · Bézier: 16 pts, passa nos 4 cantos · B-spline m×n → (m−3)(n−3) retalhos.

## 3D
- Rotação em eixo arbitrário: $T \to R_x \to R_z \to R_y(\theta) \to R_z^{-1} \to R_x^{-1} \to T^{-1}$
- **Paralela ortogonal**: translada **VRP**→origem; acha VPN; roda em X e Y alinhando VPN com Z; **ignora Z**; normaliza; clip; viewport.
- **Perspectiva**: translada **COP**→origem; idem; **$x_p = x\,d/z$, $y_p = y\,d/z$**; normaliza; clip; viewport.
- Normal = **produto vetorial** de 2 arestas: $(a_yb_z-a_zb_y,\;a_zb_x-a_xb_z,\;a_xb_y-a_yb_x)$.
- Volume canônico: cubo (paralela) / pirâmide truncada (perspectiva); CS 3D = 6 bits.
Detalhes: [[07 - 3D - Transformações e Projeção Paralela]], [[08 - Projeção em Perspectiva e Clipping 3D]]

## Phong
$$I = I_a k_a + I_l k_d (\hat N\cdot \hat L) + I_l k_s (\hat R\cdot\hat V)^n$$
3 componentes **aditivas**: ambiente (indireta), difusa (direta), especular. Especular tem a cor da luz.
Shading: Flat (por face) · Gouraud (interpola **intensidade**) · Phong (interpola **normal**).
Detalhes: [[12 - Iluminação - Modelo de Phong e Shading]]

## Z-buffer
Inicia z = +∞, cor = fundo; se z < zbuf: atualiza cor e zbuf. A ordem dos polígonos não importa.
Detalhes: [[11 - Rasterização e Z-Buffer]]
