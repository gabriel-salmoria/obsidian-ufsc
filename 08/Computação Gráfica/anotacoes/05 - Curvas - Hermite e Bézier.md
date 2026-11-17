---
tags: [cg, modulo-1, curvas]
---
# 05 · Curvas Paramétricas 2D: Hermite e Bézier

[[Computação Gráfica|↑ Índice]] · anterior: [[04 - Clipping]] · próximo: [[06 - B-Splines e Forward Differences]]
Slides: [[05.1 - Curvas Paramétricas - Conceitos Básicos e Hermite.pdf]] · [[05.2 - Curvas Paramétricas - Bézier.pdf]] · Apostila: [[Apostila antiga - Curvas Paramétricas (CG4).pdf]] · Exercício: [[Exercício 1.4.1 - Plote uma curva com Hermite e Bézier.pdf]] · Livro: [[Foley - Cap. 11 - Curvas e Superfícies.pdf]]
Extras: [Simulador de Bézier (Desmos)](https://www.desmos.com/calculator/d1ofwre0fr) · [[de Casteljau (1999) - Autobiografia.pdf]]

## Contexto histórico (cai como cultura geral)
- Problema: design automotivo no fim dos anos 50 (modelos de argila e madeira). Era preciso representar curvas **fiéis, rápidas e compactas**, com posição de qualquer ponto calculável a qualquer momento (zoom).
- Descobertas **independentemente**:
  - **Paul de Faget de Casteljau**, Citroën, **1959**. **Não publicou**: a Citroën não deixou. Inventou o **algoritmo** básico de desenho.
  - **Pierre Bézier**, Renault, **1960**. A Renault, empresa pública, **deixou publicar**, e por isso o modelo leva o nome dele.
  - Aperfeiçoadas por **Carl de Boor**, General Motors (**B-spline, 1972**).
- Em 1999 a revista *Computer Aided Geometric Design* fez uma edição especial em homenagem a de Casteljau.

## Algoritmo de de Casteljau (divisão e conquista)
- P0 e P2 são os extremos; P1 é o **ponto de controle** (curvatura).
- Pontos médios recursivos: $P_1^{(1)} = \text{médio}(P_0P_1)$, $P_2^{(1)} = \text{médio}(P_1P_2)$, $P_2^{(2)} = \text{médio}(P_1^{(1)}P_2^{(1)})$, que está **na curva**. Recursão nas duas metades.
- ✅ Precisão ilimitada, suporta zoom.
- ❌ Muitos cálculos de ponto médio. A **recursão** consome muita memória. **Não é incremental**: não dá para saber onde fica o ponto a uma certa distância do início sem desenhar a curva toda.

## Forma matricial geral (cúbicas)
$$
x(t) = T\cdot M\cdot G_x,\qquad T = [t^3\;\;t^2\;\;t\;\;1],\quad t\in[0,1]
$$
- **M** é constante e define o tipo da curva (Hermite, Bézier, B-spline). **G** é o vetor de **geometria**.
- $C = M\cdot G = [a\;b\;c\;d]^T$ são os **coeficientes** do polinômio $x(t) = at^3+bt^2+ct+d$.
- **Blending functions** (funções de suavização/mistura) são $T\cdot M$: dizem **quanto cada elemento de G pesa** em cada t.

### Hermite
Geometria: **2 pontos extremos + 2 vetores tangentes**, $G_H = [P_1\;P_4\;R_1\;R_4]^T$
$$
M_H=\begin{bmatrix}2&-2&1&1\\-3&3&-2&-1\\0&0&1&0\\1&0&0&0\end{bmatrix}
$$
Blending: $H_1 = 2t^3-3t^2+1$, $H_2 = -2t^3+3t^2$, $H_3 = t^3-2t^2+t$, $H_4 = t^3-t^2$.

### Bézier
Geometria: **4 pontos de controle**, $G_B = [P_1\;P_2\;P_3\;P_4]^T$. A curva **passa por P1 e P4**; P2 e P3 "puxam" a curva.
$$
M_B=\begin{bmatrix}-1&3&-3&1\\3&-6&3&0\\-3&3&0&0\\1&0&0&0\end{bmatrix}
$$
Blending (Bernstein): $(1-t)^3$, $3t(1-t)^2$, $3t^2(1-t)$, $t^3$, que **somam 1**.
- Tangentes nas pontas: $R_1 = 3(P_2-P_1)$, $R_4 = 3(P_4-P_3)$. É assim que se converte Bézier ↔ Hermite.
- **Fecho convexo**: a curva fica dentro do polígono de controle.

## Continuidade
Para modelar formas complexas se juntam várias cúbicas, e a **junção** precisa ser contínua:
- **G0 / C0**: as curvas se **encontram** (compartilham o ponto).
- **G1**: as tangentes na junção têm a **mesma direção** (colineares), magnitudes podem diferir.
- **C1**: as tangentes são **iguais** (direção **e** magnitude).
- **C2**: segunda derivada igual também (B-splines têm isso, ver [[06 - B-Splines e Forward Differences]]).

Para Bézier, curvas [P1..P4] e [P4..P7]:
- **compartilham P4** → C0;
- **P3, P4, P5 colineares**, isto é $\overline{P_3P_4} = k\,\overline{P_4P_5}$ → G1; com **k = 1** → C1.

> [!note] O slide do professor chama de "C(1)" a condição com k qualquer. Pela definição estrita isso é **G1**, e só com k = 1 é C1. Se aparecer na prova, leia com cuidado o que estão perguntando.

## Desenho incremental com blending functions (método do trabalho 1.5)
- ✅ **Incremental**: dá para gerar a curva até onde se quiser.
- ✅ **Precisão e passo variáveis**: passo $\delta = 1/k$ gera a curva como k segmentos de reta.
- ✅ **Resolve o clipping**: basta testar se o fim do próximo segmento está dentro da window (clipping de **ponto**).
- ❌ A cada passo tem que calcular $T = [t^3\;t^2\;t\;1]$ e multiplicar. As [[06 - B-Splines e Forward Differences#Forward Differences|forward differences]] resolvem isso.

## Exercício 1.4.1 (resolvido)
P1=(1,1), P2=(2,2), P3=(3,2), P4=(4,1), Bézier, δ = 0,2:
- $x(t) = 1 + 3t$ (pontos igualmente espaçados em x, então x é linear)
- $y(t) = (1-t)^3 + 6t(1-t)^2 + 6t^2(1-t) + t^3 = 1 + 3t - 3t^2$

| t | 0 | 0,2 | 0,4 | 0,6 | 0,8 | 1 |
|---|---|---|---|---|---|---|
| x | 1 | 1,6 | 2,2 | 2,8 | 3,4 | 4 |
| y | 1 | 1,48 | 1,72 | 1,72 | 1,48 | 1 |

Para a mesma curva em Hermite: $R_1 = 3(P_2-P_1) = (3,3)$, $R_4 = 3(P_4-P_3) = (3,-3)$.
