---
tags: [cg, modulo-1, curvas]
---
# 06 · B-Splines e Forward Differences

[[Computação Gráfica|↑ Índice]] · anterior: [[05 - Curvas - Hermite e Bézier]] · próximo: [[07 - 3D - Transformações e Projeção Paralela]]
Slides: [[06.1 - Curvas Paramétricas - B-Splines.pdf]] · [[06.2 - Curvas Paramétricas - Forward Differences.pdf]] · [[06.3 - B-Splines e Forward Differences (corrigido).pdf]] · [[06.4 - B-Splines e Forward Differences (PDF novo).pdf]] · [[06.5 - Desempenho de Operações em Ponto Flutuante.pdf]]
Exemplo resolvido: [[Exemplo - Forward Differences com B-Splines 2D.pdf]] · Código do professor: [gist (Processing)](https://gist.github.com/awangenh/73983b81541abf2c71cc)

## Splines: origem do nome
- *Splines* eram **tiras de aço flexíveis** usadas na **construção naval** para dar forma ao casco, deformadas com pesos chamados **"ducks"**. (Daí os vídeos de drakkars e o link sobre têmpera no Moodle.)
- A não ser que fossem puxadas de forma extrema, mantinham **continuidade de 2ª ordem**.
- **Spline cúbica natural**: cúbica com **C0, C1 e C2** que **passa** pelos pontos de controle. É mais suave que Bézier/Hermite (que só garantem C1), **mas** os coeficientes dependem de **todos** os n pontos. Mover um ponto exige inverter uma matriz (n+1)×(n+1) e afeta a curva inteira, o que é caro.

## B-splines uniformes
- Segmentos cujo comportamento depende de **poucos pontos de controle**: **controle local**.
- Desenvolvidas entre **1960 e 1972** por **Carl de Boor** (GM).
- Uma B-spline com $P_0 \dots P_m$ ($m \ge 3$, ou seja m+1 pontos) tem **m − 2 segmentos cúbicos** $Q_3 \dots Q_m$. Em outras palavras, **n pontos → n − 3 segmentos**.
- O segmento $Q_i$ é definido por $P_{i-3}, P_{i-2}, P_{i-1}, P_i$, então segmentos vizinhos **compartilham 3 pontos**.
- Têm **C0, C1 e C2** automaticamente, sem precisar repetir pontos nem forçar colinearidade como em Bézier.
- **Não passam** pelos pontos de controle (aproximam, não interpolam). Ficam dentro do **fecho convexo**.

$$
M_{BS} = \frac{1}{6}\begin{bmatrix}-1&3&-3&1\\3&-6&3&0\\-3&0&3&0\\1&4&1&0\end{bmatrix},\qquad G_{BS_i} = [P_{i-3}\;P_{i-2}\;P_{i-1}\;P_i]^T
$$

## Três formas de desenhar uma cúbica
1. **Avaliar** x(t), y(t), z(t) a cada passo de t (blending functions). É preciso calcular $[t^3\;t^2\;t\;1]$ toda vez.
2. **Subdivisão recursiva** de ponto médio (de Casteljau): memória e recursão.
3. **Forward differences** (diferenças adiante): **a mais eficiente**. Depois da inicialização, cada ponto novo custa só **3 somas** por coordenada, nenhuma multiplicação.

## Forward Differences
Para $f(t) = at^3 + bt^2 + ct + d$ com passo δ:
$$
\Delta f(t) = f(t+\delta) - f(t),\quad \Delta^2 f = \Delta(\Delta f),\quad \Delta^3 f \text{ é constante (cúbica)}
$$
Condições iniciais (em t = 0):
$$
\begin{aligned}
f_0 &= d\\
\Delta f_0 &= a\delta^3 + b\delta^2 + c\delta\\
\Delta^2 f_0 &= 6a\delta^3 + 2b\delta^2\\
\Delta^3 f_0 &= 6a\delta^3
\end{aligned}
\qquad\Longleftrightarrow\qquad
D = E(\delta)\cdot C,\quad
E(\delta)=\begin{bmatrix}0&0&0&1\\\delta^3&\delta^2&\delta&0\\6\delta^3&2\delta^2&0&0\\6\delta^3&0&0&0\end{bmatrix}
$$
Coeficientes $C = [a\;b\;c\;d]^T$ conforme o tipo de curva:
$C_x^{hermite} = M_H G_H$, $\;C_x^{bézier} = M_B G_B$, $\;C_x^{b\text{-}spline} = M_{BS}G_{BS}$.

### Algoritmo (slides)
```
DesenhaCurvaFwdDiff(n, x, Dx, D2x, D3x, y, Dy, D2y, D3y, z, Dz, D2z, D3z)
  i = 1; xvelho = x; yvelho = y; zvelho = z
  enquanto i < n:
      i = i + 1
      x = x + Dx;  Dx = Dx + D2x;  D2x = D2x + D3x
      y = y + Dy;  Dy = Dy + D2y;  D2y = D2y + D3y
      z = z + Dz;  Dz = Dz + D2z;  D2z = D2z + D3z
      desenheLinha(xvelho, yvelho, zvelho, x, y, z)
      xvelho = x; yvelho = y; zvelho = z
```
Alto nível:
0. escolhe δ (ex. 0,001) e calcula δ², δ³ (constantes na curva toda);
1. calcula os coeficientes C = M·G para o segmento;
2. calcula $f_0, \Delta f_0, \Delta^2 f_0, \Delta^3 f_0$;
3. itera com o algoritmo acima ($n = 1/\delta$ passos).

> [!warning] Ponto fraco
> Erro **acumula** (somas sucessivas em ponto flutuante). Para δ muito pequeno e muitos passos, a curva pode "derivar". Por isso a aula 6.3 fala de desempenho e precisão de operações em ponto flutuante.

## Trabalho 1.6
B-spline com quantos pontos o usuário quiser (n > 3), desenhada com forward differences. Ver também [[09 - Superfícies Bicúbicas]], onde a mesma ideia vira matriz DD.
