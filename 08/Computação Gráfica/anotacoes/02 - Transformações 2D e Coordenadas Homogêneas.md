---
tags: [cg, modulo-1]
---
# 02 · Transformações 2D e Coordenadas Homogêneas

[[Computação Gráfica|↑ Índice]] · anterior: [[01 - Conceitos Básicos]] · próximo: [[03 - Sistema de Coordenadas Normalizadas (SCN)]]
Slides: [[03 - Transformações 2D e Coordenadas Homogêneas.pdf]] · Apostila: [[Apostila 1.2 - Transformações 2D.pdf]] · Exercícios: [[Exercícios de Transformações.pdf]]
Videoaula interativa (vem do banco da prova): [Aula 3.0](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20784)

As **3 transformações primitivas** (em 2D, 3D ou nD) são **translação, escalonamento e rotação**. Combinando essas três se obtém qualquer comportamento do objeto.

## As primitivas (forma "crua")
- **Translação** por $(D_x, D_y)$: $x' = x + D_x$, $y' = y + D_y$. É uma **soma** ($P' = P + T$), não uma multiplicação.
- **Escalonamento** por $(S_x, S_y)$: $x' = x\,S_x$, $y' = y\,S_y$, ou seja $P' = P\cdot S$. Ex.: (6,6) escalado por (1/2, 1/3) → (3,2).
- **Rotação** em torno da origem por θ: $x' = x\cos\theta - y\sin\theta$, $y' = x\sin\theta + y\cos\theta$. Ex.: (6,1) rotacionado 30° → (4,7; 3,9).

## Coordenadas homogêneas
- Ideia: todo problema em n dimensões tem um equivalente em **n+1 dimensões**. Resolve-se lá e projeta-se de volta.
- Um ponto $P(x,y)$ vira $P(W x, W y, W) = (X, Y, W)$ **para qualquer W ≠ 0**.
  - **W é o fator de escala**: $x = X/W$, $y = Y/W$.
  - **Usamos sempre W = 1**, e aí a divisão fica desnecessária.
  - W = 0 levaria a divisão por zero (W = 0 representa um *vetor*/direção, não um ponto).
- Ganho: **toda** operação geométrica 2D vira uma **matriz 3×3**, e a transformação vira *ponto × matriz*. Translação **também**, e é por isso que precisamos de coordenadas homogêneas (POSCOMP 2016: "necessárias para representar translação em matriz" = V).
- Em 3D: pontos `[x y z 1]`, matrizes 4×4. Ver [[07 - 3D - Transformações e Projeção Paralela]].

> [!important] Convenção do professor: vetor-linha
> $[x'\;y'\;1] = [x\;y\;1]\cdot M$, com a **translação na última linha**. Quando a convenção é vetor-coluna ($M\cdot P$), tudo aparece **transposto** e a ordem de multiplicação inverte. Nas questões a matriz aparece nas duas formas; reconheça pelo **padrão** (onde ficam cos/sen, a diagonal, os D).

### Matrizes (vetor-linha, como nos slides)
$$
T=\begin{bmatrix}1&0&0\\0&1&0\\D_x&D_y&1\end{bmatrix}\quad
S=\begin{bmatrix}S_x&0&0\\0&S_y&0\\0&0&1\end{bmatrix}\quad
R=\begin{bmatrix}\cos\theta&\sin\theta&0\\-\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}
$$
- Com vetor-linha, essa R dá $x' = x\cos - y\sin$, $y' = x\sin + y\cos$.
- A videoaula interativa mostra a R **transposta** (forma vetor-coluna): $\begin{bmatrix}\cos&-\sin&0\\\sin&\cos&0\\0&0&1\end{bmatrix}$. Para a prova importa **reconhecer**: 3×3 com cos/sen no bloco 2×2 e o resto identidade = **rotação 2D homogênea**.
- **Generalizada**: $M = \begin{bmatrix}a&d&0\\b&e&0\\c&f&1\end{bmatrix}$, onde a, b, d, e fazem rotação/escala/cisalhamento e **c, f fazem translação**.

## Concatenação (composição)
- Uma sequência de transformações é uma única matriz, o **produto** das matrizes **na ordem de aplicação** (com vetor-linha: $M = M_1 \cdot M_2 \cdot M_3$).
- Calcula-se **uma** matriz e transformam-se todos os pontos com ela, o que é eficiente.
- A **ordem importa** em geral: matrizes não comutam. Exceções: duas translações, duas escalas, duas rotações 2D, e **escala uniforme com rotação**.
- Exercício da lista: $T(a)\cdot T(b)$ com b = inverso de a dá a identidade; idem para escalas e rotações inversas. A **inversa** desfaz.

### Rotação em torno de um ponto qualquer (ex.: o centro do objeto)
1. Translada o ponto para a **origem** ($-c_x, -c_y$)
2. Rotaciona
3. Translada de volta ($+c_x, +c_y$)
$$M = T(-c)\cdot R(\theta)\cdot T(c)$$

### Escalonamento "natural" (em torno do centro)
Sozinho, um escalonamento **"incha" e "desloca"** o objeto, porque escala também a distância à origem. Concatenado com 2 translações, o objeto **apenas incha**:
$$
M = T_1\,S\,T_2 =
\begin{bmatrix}1&0&0\\0&1&0\\-x&-y&1\end{bmatrix}
\begin{bmatrix}a&0&0\\0&b&0\\0&0&1\end{bmatrix}
\begin{bmatrix}1&0&0\\0&1&0\\x&y&1\end{bmatrix}
=\begin{bmatrix}a&0&0\\0&b&0\\x(1-a)&y(1-b)&1\end{bmatrix}
$$
Essa é exatamente a questão da videoaula ([[Banco de Questões#1. Transformações 2D e coordenadas homogêneas|Q1.3]]: opção **(b)** + matriz **(1)**).

### Centro geométrico
Média aritmética das coordenadas dos vértices: $c = \left(\frac{1}{n}\sum x_i,\; \frac{1}{n}\sum y_i\right)$.

## Ponto × vetor (pergunta da lista)
- Ponto: W = 1, é afetado por translação.
- Vetor (direção): W = 0, **não** é afetado por translação; só rotação e escala mudam um vetor.
