---
tags: [cg, modulo-1, 3d]
---
# 07 · 3D: Estruturas, Transformações e Projeção Paralela

[[Computação Gráfica|↑ Índice]] · anterior: [[06 - B-Splines e Forward Differences]] · próximo: [[08 - Projeção em Perspectiva e Clipping 3D]]
Slides: [[07.1 - Rotação 3D Passo a Passo.pdf]] · [[07.2 - Exemplo Numérico de Projeção Paralela.pdf]] · Livro: [[Livro - Rotações em 2D e 3D.pdf]] · OBJ: [[Especificação OBJ v3.pdf]], [[Especificação OBJ com exemplos numéricos.pdf]]
Videoaula interativa (vem do banco): [Aula 7.3 Projeções Paralelas](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20786) · questões em [[Banco de Questões#3. 3D (projeções e estrutura de arame)]]

## Estruturas de dados 3D (modelo de arame / wireframe)
- **Ponto3D**: (x, y, z), em homogêneas `[x y z 1]`.
- **Objeto3D** (wireframe): lista de **segmentos de reta** (pares de Ponto3D), ou lista de vértices + lista de arestas/faces.
- Para o modelo de arame é preciso o **conjunto de vértices** e o **conjunto de pontos de cada face** (POSCOMP 2014).
- **Normal de uma face**: com 3 pontos $p_0, p_1, p_2$, $\vec n = (p_1 - p_0)\times(p_2 - p_0)$. É **produto vetorial**, não produto interno.
  - Produto vetorial: $(a_yb_z - a_zb_y,\; a_zb_x - a_xb_z,\; a_xb_y - a_yb_x)$.
  - O produto **interno** (escalar) serve para calcular **ângulos/cossenos** (Phong, backface), não para gerar a normal.

## Transformações 3D (4×4, vetor-linha como nos slides)
$$
T=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\D_x&D_y&D_z&1\end{bmatrix}\quad
S=\begin{bmatrix}S_x&0&0&0\\0&S_y&0&0\\0&0&S_z&0\\0&0&0&1\end{bmatrix}
$$
$$
R_x=\begin{bmatrix}1&0&0&0\\0&\cos&\sin&0\\0&-\sin&\cos&0\\0&0&0&1\end{bmatrix}\;
R_y=\begin{bmatrix}\cos&0&-\sin&0\\0&1&0&0\\\sin&0&\cos&0\\0&0&0&1\end{bmatrix}\;
R_z=\begin{bmatrix}\cos&\sin&0&0\\-\sin&\cos&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}
$$
- Escala 3D por [1 2 3] = **diag(1, 2, 3, 1)**, 4×4 (caiu no quiz).
- Rotações 3D em **eixos diferentes não comutam** (POSCOMP 2016, item III falso).

### Rotação em torno de um eixo arbitrário A (que passa por P)
1. **T**: translada por −P (P vai para a origem)
2. **Rx** por $\theta_x$: leva o eixo A para o **plano xy**
3. **Rz** por $\theta_z$: alinha A com o **eixo y**
4. **Ry** pelo **ângulo desejado**
5. **Rz⁻¹** (desfaz 3)
6. **Rx⁻¹** (desfaz 2)
7. **T⁻¹** (desfaz 1)

$M = T\cdot R_x\cdot R_z\cdot R_y(\theta)\cdot R_z^{-1}\cdot R_x^{-1}\cdot T^{-1}$

## Projeções: taxonomia **do professor**
- **Paralela**: raios de projeção **paralelos**. O campo de visão **não muda** com a distância, então o tamanho aparente **não varia** (objetos às vezes parecem distorcidos). Muito usada em engenharia e desenho técnico.
  - **Ortogonais ou Ortográficas**: raios ⟂ ao plano. **É a usada comumente em CG.**
  - **Oblíquas ou Pictóricas**:
    - **Axonométricas**: **Isométrica**, Dimétrica, Trimétrica (mantêm as dimensões sobre os eixos, por isso são usadas em desenho técnico)
    - **Cavaleira** (cavalier): profundidade em escala real
    - **Cabinet**: profundidade pela metade
- **Perspectiva**: raios convergem no **COP**; o tamanho aparente diminui com a distância. Ver [[08 - Projeção em Perspectiva e Clipping 3D]].

> [!warning] Divergência com o Foley
> No Foley, as axonométricas são subtipo das **ortográficas**. O professor (página do Moodle + gabarito H5P) coloca **isométrica = paralela oblíqua axonométrica**. **Na prova, use a do professor.** E "dois tipos de projeção" = **Paralela × Perspectiva** (não "Ortogonal × Perspectiva").

## Algoritmo da Projeção Paralela Ortogonal
Termos: **VRP** (View Reference Point, centro da window), **VPN** (View Plane Normal, normal do plano de projeção), **VUP** (view-up).
1. **Translade VRP para a origem**
2. **Determine a VPN** e decomponha para achar os ângulos dela com X e Y
3. **Rotacione o mundo** em torno de X e de Y para **alinhar a VPN com o eixo Z**
4. **Ignore todas as coordenadas Z** (isso é a projeção ortogonal)
5. **Normalize** o restante (coordenadas de window/SCN)
6. **Clippe** (2D)
7. Transforme para **coordenadas de viewport**

Passos 1 a 3 viram **uma matriz** $M = T\cdot R_x\cdot R_y$, aplicada a todos os pontos do mundo, **inclusive a window**.

### Exemplo numérico dos slides
Window: W1 = (0,5; 2; 2,5), W2 = (2,5; 2; 0,5), W3 = (3; 0; 1), W4 = (1; 0; 3).
- VRP = média = **(1,75; 1; 1,75)** → T com última linha (−1,75; −1; −1,75; 1)
- VPN = (vrp − w1) × (w2 − vrp) = **(2, 1, 2)**
- $\theta_x = \arctan(y/z) = \arctan(1/2) = 26{,}565°$ (projeção no plano yz)
- $\theta_y = \arctan(x/z) = \arctan(2/2) = 45°$ (projeção no plano xz)
- `transform = trans * rotx * roty` → multiplica todos os pontos → ignora z → normaliza → clip → viewport

> [!note] Rigor
> Para alinhar exatamente, o ângulo em Y deveria ser calculado **depois** da rotação em X: $\theta_y = \arctan\!\big(x/\sqrt{y^2+z^2}\big)$, o que dá ≈ 41,8° aqui. O slide usa a aproximação direta x/z. Se cair conta, siga o método do slide.

## Formato Wavefront OBJ (resumo)
- `v x y z` vértice · `vn` normal · `vt` textura
- `p i` ponto · `l i j ...` linha/polilinha · `f i j k ...` face (índices **começam em 1**; aceita `v/vt/vn`)
- `o nome` objeto · `g` grupo · `mtllib arq.mtl` / `usemtl mat` material (em `.mtl`: `Kd` difusa, `Ka` ambiente, `Ks` especular, `Ns` expoente, `d` transparência)
- Formas livres: `cstype bezier|bspline`, `deg 3 3`, `curv`, `surf u0 u1 v0 v1 <índices>`, `end`
