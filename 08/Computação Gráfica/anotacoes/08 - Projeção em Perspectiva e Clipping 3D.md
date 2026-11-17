---
tags: [cg, modulo-1, 3d]
---
# 08 · Projeção em Perspectiva e Clipping 3D

[[Computação Gráfica|↑ Índice]] · anterior: [[07 - 3D - Transformações e Projeção Paralela]] · próximo: [[09 - Superfícies Bicúbicas]]
Slides: [[08 - Projeção em Perspectiva.pdf]]
Videoaula interativa (vem do banco): [Aula 8.1 Perspectiva](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20787)

## Conceitos
- Raios de projeção **convergem** para o **COP** (*Center of Projection*), formando uma **pirâmide infinita de projeção**.
- Efeitos visuais: objetos **distantes aparecem menores**, "desvanecendo" à distância; objetos **distorcem** quando vistos obliquamente.
- **Tipos**: perspectiva de **1, 2 ou 3 pontos de fuga**, conforme quantos eixos principais cortam o plano de projeção.
- **VRC** (3D Viewing Reference Coordinates): plano de projeção **uv** (*view plane*), limitado por (Umin, Vmin)–(Umax, Vmax).
- **d** = distância do COP ao plano de projeção:
  - d pequeno → **grande angular** (perspectiva exagerada)
  - d grande → **teleobjetiva**; no limite d → ∞ vira **projeção paralela**

## Projeção de um ponto: caso especial
COP na **origem**, plano de projeção em **z = d**. Por semelhança de triângulos:
$$
x_p = \frac{x}{z/d} = \frac{x\,d}{z},\qquad y_p = \frac{y}{z/d} = \frac{y\,d}{z}
$$
Em coordenadas homogêneas (forma coluna, transponha para vetor-linha):
$$
M_{per}=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&1/d&0\end{bmatrix},\qquad
M_{per}\begin{bmatrix}x\\y\\z\\1\end{bmatrix} = \begin{bmatrix}x\\y\\z\\z/d\end{bmatrix}
\;\xrightarrow{\;\div W\;}\;\left(\frac{x}{z/d},\frac{y}{z/d},d\right)
$$
- É aqui que **W ≠ 1** aparece: a perspectiva é a transformação que exige a **divisão por W** (homogênea → cartesiana).
- **Caso geral ($M_{GER}$)**: COP em qualquer lugar, plano ⟂ a z, COP a uma distância Q de (0,0,zp) na direção (dx,dy,dz). Ver Foley & van Dam para a dedução.

## Algoritmo da Projeção em Perspectiva
1. **Translade o COP para a origem**
2. **Determine os ângulos da VPN** com X e Y
3. **Rotacione o mundo** em torno de X e Y para **alinhar a VPN com Z**
4. **Projete**: calcule $x_p$, $y_p$ (divide por z/d)
5. **Normalize** $x_p, y_p$ (coordenadas de window)
6. **Clippe 2D**
7. Transforme para **coordenadas de viewport**

Comparado à paralela ([[07 - 3D - Transformações e Projeção Paralela#Algoritmo da Projeção Paralela Ortogonal]]): o passo 1 translada o **COP** (não o VRP) e o passo 4 **divide por z/d** em vez de ignorar z.

> [!warning] Pegadinha recorrente
> "Para fazer uma **Perspectiva** basta ignorar Z" é **falso**. Ignorar Z é a **paralela ortogonal**.
> Antes de dividir por w é preciso descartar o que está **atrás do olho** (z ≤ 0), senão a imagem sai invertida.

## Clipping 3D (volume canônico)
Só com clipping 2D é preciso projetar o mundo **todo** antes, o que dá mais processamento. Para clipar em 3D define-se o **volume canônico**:
- **Paralela**: um **cubo/paralelepípedo** (dá para normalizar **antes** de projetar).
- **Perspectiva**: uma **pirâmide truncada** (frustum).

**Cohen-Sutherland 3D: 6 bits**
| bit | condição |
|---|---|
| 1 | acima, y > 1 |
| 2 | abaixo, y < −1 |
| 3 | direita, x > 1 |
| 4 | esquerda, x < −1 |
| 5 | à frente, z > 1 |
| 6 | atrás, z < −1 |

Na perspectiva, duas abordagens:
- clipar **direto na pirâmide** com **Cyrus-Beck / Liang-Barsky**, usando a interseção com os **planos** do volume (forma paramétrica) em vez de retas;
- **normalizar a pirâmide** (deformá-la num paralelepípedo, em coordenadas homogêneas) e então usar Cohen-Sutherland ou Liang-Barsky.
