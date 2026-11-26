---
tags: [cg, prova, colinha]
---
# gabs-graphics · Computação Gráfica (INE5420)

Voltar: [[Computação Gráfica]]

**Como achar as coisas**

1. **Caixa de busca** (no HTML e no site): a caixa no topo (atalho `/`). Cole um pedaço do enunciado ou as palavras-chave ("códigos de região", "pk qk", "rotação eixo Y 90") e dê Enter. Ela não procura a palavra solta: ela ranqueia os **blocos** pelo assunto e mostra os 10 melhores com a linha que bateu. Setas escolhem, Enter pula.
2. **Ctrl+F por tag**: cada bloco tem uma tag (arroba + nome) no título, e cada tag aparece **uma vez só** no arquivo inteiro. Ctrl+F com arroba seguido de `cs` cai direto no Cohen-Sutherland, sem passar por mais nada. A tabela abaixo diz qual tag procurar.
3. Cada bloco começa com **termos**: palavras-chave, sinônimos e nomes alternativos do assunto (a busca dá mais peso a eles). As contas estão em LaTeX, passo a passo, com números inventados.

**Índice (assunto → tag para o Ctrl+F)**


**Parte 1. Window, viewport e recorte**

| tag | assunto |
|---|---|
| `win` | Window e viewport: o que são, zoom, pan, aspecto |
| `wv` | Fórmula da transformada de viewport (com origem deslocada e y invertido) |
| `scn` | SCN: sistema de coordenadas normalizado (coordenadas da window) |
| `contaclip` | Conta completa: recortar e levar para SCN e para a viewport |
| `clipint` | Interseção da reta com as bordas da window |
| `clipp` | Recorte de ponto |
| `cs` | Cohen-Sutherland: recorte de retas por códigos de região (RC) |
| `lb` | Liang-Barsky: recorte paramétrico com pk e qk |
| `cb` | Cyrus-Beck: recorte paramétrico contra polígono convexo |
| `nln` | Nicholl-Lee-Nicholl: recorte por coeficientes angulares |
| `subdiv` | Subdivisão do ponto médio (midpoint subdivision) |
| `suth` | Sutherland-Hodgeman: recorte de polígonos borda a borda |
| `weiler` | Weiler-Atherton: recorte de polígonos côncavos |
| `clipq` | Qual algoritmo de recorte é qual (reconhecer pela descrição) |

**Parte 2. Transformações e coordenadas homogêneas**

| tag | assunto |
|---|---|
| `homog` | Coordenadas homogêneas: o W |
| `t2c` | Convenção vetor-linha × vetor-coluna (de onde vem a transposta) |
| `t2d` | Matrizes 2D em homogêneas: translação, escala, rotação |
| `tgen` | Matriz genérica 2D e mapeamento de vetores da base |
| `refl` | Reflexão (espelhamento) e cisalhamento (shear) |
| `comp` | Composição de transformações e ordem |
| `comuta` | Quais transformações comutam |
| `pivo` | Girar/escalar em torno de um ponto (centro do objeto, pivô) |
| `inv` | Inversas das transformações |
| `t3d` | Translação e escala 3D (4×4) |
| `r3d` | Rotação 3D em torno dos eixos X, Y e Z (geral e 90°) |
| `eixoarb` | Rotação em torno de um eixo arbitrário |
| `mudbase` | Mudança de base / mudança de sistema de coordenadas |

**Parte 3. Vetores, planos e malhas**

| tag | assunto |
|---|---|
| `dot` | Produto escalar (interno, dot product) |
| `cross` | Produto vetorial (cross product) e normal de uma face |
| `plano` | Equação do plano, distância e interseção reta-plano |
| `dist` | Distância entre pontos, norma, normalizar |
| `normesf` | Normal de superfícies: esfera, superfície paramétrica, normal de vértice |
| `malha` | Malhas poligonais, B-rep, OBJ |

**Parte 4. Projeções, câmera e pipeline 3D**

| tag | assunto |
|---|---|
| `projtipos` | Tipos de projeção (classificação) |
| `projprop` | Propriedades: paralela × perspectiva, volume de visão |
| `projmat` | Matrizes de projeção (ortogonal, perspectiva) com exemplo |
| `camera` | Transformação de câmera (de visualização): VRP, VPN, VUP, u v n |
| `pipe3d` | Pipeline de visualização 3D: ordem das etapas |
| `canon` | Volume canônico e normalização |

**Parte 5. Curvas e superfícies**

| tag | assunto |
|---|---|
| `curvparam` | Curvas paramétricas: forma geral e matricial |
| `hermite` | Hermite |
| `bezier` | Bézier: Bernstein, matriz, propriedades |
| `casteljau` | Algoritmo de de Casteljau |
| `continuidade` | Continuidade entre segmentos (G0, G1, C0, C1, C2) |
| `bspline` | B-spline cúbica uniforme |
| `fwddiff` | Forward differences (diferenças adiante) |
| `superf` | Superfícies bicúbicas (Bézier, B-spline, Hermite) |

**Parte 6. Rasterização, preenchimento, aliasing e texturas**

| tag | assunto |
|---|---|
| `rastconc` | Rasterização: o que é |
| `dda` | DDA (Digital Differential Analyzer) para retas |
| `bres` | Bresenham para retas (só inteiros) |
| `circ` | Círculo pelo ponto médio (e elipse) |
| `fill` | Preenchimento: scanline de polígonos, flood fill, boundary fill |
| `alias` | Aliasing (serrilhado) e anti-aliasing (SSAA, MSAA, FXAA) |
| `textura` | Mapeamento de textura: coordenadas, filtragem, perspectiva |
| `mipmap` | Mipmap e o custo de memória (1/3) |
| `bump` | Bump, normal, displacement, environment e outras texturas |

**Parte 7. Visibilidade (superfícies ocultas)**

| tag | assunto |
|---|---|
| `visconc` | Remoção de superfícies ocultas: classificação |
| `backface` | Backface culling (remoção de faces traseiras) |
| `zbuf` | Z-buffer (buffer de profundidade) |
| `pintor` | Algoritmo do pintor (ordenação por profundidade) |
| `arvbsp` | Árvore BSP (Binary Space Partitioning) |
| `warnock` | Scanline, Warnock e ray casting para visibilidade |

**Parte 8. Iluminação e tonalização (shading)**

| tag | assunto |
|---|---|
| `luzes` | Fontes de luz: ambiente, direcional, pontual, spot, extensa |
| `phong` | Modelo de iluminação de Phong (ambiente + difusa + especular) |
| `lambert` | Lei de Lambert (reflexão difusa) |
| `espec` | Reflexão especular: Phong e Blinn-Phong |
| `normuso` | Para que servem as normais na renderização |
| `shading` | Tonalização: flat, Gouraud e Phong shading |

**Parte 9. Visualização realista, GPU, APIs e engines**

| tag | assunto |
|---|---|
| `raytrace` | Ray tracing (traçado de raios, Whitted 1980) |
| `raycast` | Ray casting e ray casting volumétrico |
| `radios` | Radiosidade e radiância (iluminação global) |
| `shader` | Shaders e GPU: vertex, pixel/fragment, linguagens |
| `glpipe` | Pipeline do OpenGL (gráfico moderno) |
| `apis` | APIs gráficas, game engines, modeladores |
| `ecs` | Entity Component System (ECS) |
| `tecnfunc` | Técnica → para que serve (relacionar colunas) |

**Parte 10. Hierarquia, animação, cor e dispositivos**

| tag | assunto |
|---|---|
| `hier` | Modelos hierárquicos, grafo de cena, pilha de matrizes |
| `anim` | Animação: keyframes, interpolação, cinemática, partículas |
| `luzcor` | Cor: luz, espectro, olho |
| `modcor` | Modelos de cor: RGB, CMY(K), HSV, CIE, YIQ (com conversões) |
| `display` | Dispositivos: vetorial × raster, frame buffer, memória |

**Parte 11. Processamento de imagens**

| tag | assunto |
|---|---|
| `imgdig` | Imagem digital: amostragem, quantização, vizinhança |
| `histo` | Histograma, operações pontuais (negativo, brilho, contraste, limiar) |
| `equal` | Equalização de histograma (com exemplo) |
| `conv` | Filtragem espacial: convolução e máscaras |
| `filtros` | Passa-baixa, passa-alta, mediana, detectores de borda |
| `fourier` | Domínio da frequência (Fourier) |
| `segm` | Segmentação (e o que ela não é) |
| `morfo` | Morfologia matemática |
| `zipimg` | Compressão e formatos de imagem |

# Parte 1. Window, viewport e recorte

## @win Window e viewport: o que são, zoom, pan, aspecto
termos: window, janela, viewport, janela de visão, mundo 2D, SRU, sistema de referência do universo, coordenadas de mundo, coordenadas de dispositivo, zoom in, zoom out, pan, relação de aspecto, distorção, escala não uniforme, mapeamento window-viewport

- **Window**: retângulo do **mundo** (coordenadas do mundo, SRU) que a gente quer mostrar. Unidade qualquer (metros, km...). Só o que está dentro dela aparece.
- **Viewport**: retângulo da **tela/janela do programa** (coordenadas de dispositivo, em pixels) onde a window é desenhada. A origem do dispositivo fica **em cima à esquerda** e o **y cresce para baixo**. Por isso a fórmula do y tem o "1 −" (ver **→wv**).
- **Mapeamento window → viewport**: é uma escala + translação. Escala em x: $s_x = \dfrac{W_{vp}}{W_{win}}$; em y: $s_y = \dfrac{H_{vp}}{H_{win}}$.
- **Relação de aspecto** = largura / altura. Se $\dfrac{W_{win}}{H_{win}} \neq \dfrac{W_{vp}}{H_{vp}}$ então $s_x \neq s_y$: escala **não uniforme**, a imagem **distorce** (círculo vira elipse, quadrado vira retângulo). Se as razões são iguais, não distorce.

**Zoom e pan (viewport fixa)**

| mexe na window | efeito na tela |
|---|---|
| diminui a window | **zoom in** (aproxima, vê menos mundo, objetos maiores) |
| aumenta a window | **zoom out** (afasta, vê mais mundo, objetos menores) |
| desloca a window para a direita | **pan**: os objetos andam para a **esquerda** na tela |
| gira a window de θ (VUP) | os objetos giram de −θ na tela |

> [!warning] Pegadinha clássica
> Viewport fixa e window **maior** = mais mundo na mesma área = **zoom out** (e não zoom in).
> Mudar o tamanho da **viewport** com a mesma window não é zoom de navegação: só muda o tamanho do desenho na tela.

**Exemplo (aspecto)**: window $(0,0)$–$(60,30)$, razão $60/30 = 2$. Viewport $(0,0)$–$(300,300)$, razão $1$. Razões diferentes, então $s_x = 300/60 = 5$ e $s_y = 300/30 = 10$: tudo fica esticado 2× na vertical. Trocar a window por $(0,0)$–$(30,15)$ (metade de cada lado) é **zoom in 2×**, e ainda distorce (razão continua 2).

**Recorte (clipping) pode ser feito** no mundo (contra a window), no SCN (contra $[-1,1]$, o que o SGI faz) ou no dispositivo (contra a viewport). As três versões dão o mesmo desenho. Fazer no SCN tem a vantagem de os limites serem sempre $-1$ e $1$, mesmo com a window girada.

## @wv Fórmula da transformada de viewport (com origem deslocada e y invertido)
termos: transformada de viewport, coordenadas de viewport, sistema de coordenadas de viewport, eixos da viewport, y para baixo, y invertido, origem da viewport, largura e altura da viewport, pixels, resultado inteiro, arredondar, xvp, yvp

Window $[x_{wmin}, x_{wmax}] \times [y_{wmin}, y_{wmax}]$ e viewport com canto $(x_{vmin}, y_{vmin})$ e tamanho $W \times H$ (então $x_{vmax} = x_{vmin}+W$, $y_{vmax} = y_{vmin}+H$):

$$x_v = x_{vmin} + \frac{x_w - x_{wmin}}{x_{wmax}-x_{wmin}}\,(x_{vmax}-x_{vmin})$$

$$y_v = y_{vmin} + \left(1 - \frac{y_w - y_{wmin}}{y_{wmax}-y_{wmin}}\right)(y_{vmax}-y_{vmin})$$

- O **"1 −"** existe porque na viewport o y aponta para baixo: o **topo da window** ($y_w = y_{wmax}$) vai para $y_v = y_{vmin}$ (topo da tela) e a **base** ($y_w = y_{wmin}$) vai para $y_v = y_{vmin} + H$.
- Se a viewport "começa em $(o_x, o_y)$", isso é o $(x_{vmin}, y_{vmin})$: soma no fim.
- Se o ponto já está em **SCN** ($x_s, y_s \in [-1,1]$), a mesma coisa fica:

$$x_v = o_x + \frac{x_s + 1}{2}\,W \qquad y_v = o_y + \left(1 - \frac{y_s + 1}{2}\right) H$$

**Tabela de cantos** (serve para conferir resposta rápido), viewport origem $(o_x,o_y)$, tamanho $W\times H$:

| ponto da window | SCN | viewport |
|---|---|---|
| canto inferior esquerdo | $(-1,-1)$ | $(o_x,\ o_y+H)$ |
| canto superior esquerdo | $(-1,1)$ | $(o_x,\ o_y)$ |
| canto superior direito | $(1,1)$ | $(o_x+W,\ o_y)$ |
| canto inferior direito | $(1,-1)$ | $(o_x+W,\ o_y+H)$ |
| centro da window | $(0,0)$ | $(o_x+W/2,\ o_y+H/2)$ |
| meio da borda esquerda | $(-1,0)$ | $(o_x,\ o_y+H/2)$ |
| meio da borda de cima | $(0,1)$ | $(o_x+W/2,\ o_y)$ |

**Exemplo**: viewport $400 \times 200$ com origem $(20,15)$; ponto no SCN $(0.5,\,-0.5)$:

$$x_v = 20 + \frac{0.5+1}{2}\cdot 400 = 20 + 300 = 320 \qquad y_v = 15 + \left(1-\frac{-0.5+1}{2}\right)\cdot 200 = 15 + 0.75\cdot 200 = 165$$

> [!warning] Cuidado
> - Esquecer a origem $(o_x, o_y)$ é o erro mais comum. Esquecer o "1 −" é o segundo.
> - Se pedirem resposta inteira: faça a conta exata e arredonde só no fim. Em questão bem feita o resultado já sai inteiro; se sair 0,33 a resposta inteira é 0.
> - Se a questão disser explicitamente que o y da viewport **cresce para cima**, aí não tem o "1 −".

## @scn SCN: sistema de coordenadas normalizado (coordenadas da window)
termos: SCN, coordenadas normalizadas, sistema de coordenadas de window, window center, WC, domínio [-1, 1], origem no centro da window, normalizar, VUP, view up, rotação da window, gerar descrição, PPC

O SCN tem **origem no centro da window (WC)** e a window inteira vira o quadrado $[-1,1]\times[-1,1]$. Borda esquerda $x=-1$, direita $x=1$, baixo $y=-1$, cima $y=1$.

Window com centro $(x_c, y_c)$, largura $w$ e altura $h$ (sem rotação):

$$x_{s} = \frac{x - x_c}{w/2} = 2\,\frac{x - x_{wmin}}{x_{wmax}-x_{wmin}} - 1 \qquad y_{s} = \frac{y - y_c}{h/2} = 2\,\frac{y - y_{wmin}}{y_{wmax}-y_{wmin}} - 1$$

**Window girada (VUP)**: o vetor *view-up* diz para onde é o "cima" da window. Para gerar a descrição em SCN:

1. translada o mundo por $-WC$ (centro da window vai para a origem);
2. acha o ângulo $\theta$ entre o VUP e o eixo $Y$ do mundo;
3. gira o mundo por $-\theta$ (a window fica alinhada aos eixos);
4. escala por $\left(\frac{2}{w},\frac{2}{h}\right)$;
5. guarda as coordenadas normalizadas em cada objeto (sem perder as de mundo);
6. recorta contra $[-1,1]$;
7. transformada de viewport.

Em uma matriz só (convenção vetor-linha, **→t2c**): $M_{scn} = T(-x_c,-y_c)\cdot R(-\theta)\cdot S\!\left(\tfrac{2}{w},\tfrac{2}{h}\right)$. Zoom muda só o $S$, pan muda só o $T$, girar a window muda só o $R$. A cada navegação recalcula $M_{scn}$ e reaplica em todos os objetos.

**Exemplo**: window $(-10,0)$–$(30,20)$: $x_c = 10$, $y_c = 10$, $w/2 = 20$, $h/2 = 10$.

$$(25,\ 4)\ \to\ \left(\frac{25-10}{20},\ \frac{4-10}{10}\right) = (0.75,\ -0.6) \qquad (-10,\ 20)\ \to\ (-1,\ 1)\ \text{(canto superior esquerdo)}$$

## @contaclip Conta completa: recortar e levar para SCN e para a viewport
termos: mundo 2D, segmento de reta, window, clipagem, recortar e converter, extremo recortado, p1', p2', novo ponto, reta clipada, coordenadas X e Y depois do recorte, coordenadas de window, coordenadas de viewport, conta completa

**Receita**

1. Lê da figura: limites da window e os pontos $p_1$, $p_2$ da reta (em mundo).
2. Acha centro e meias-dimensões da window.
3. **Recorta**: para cada extremo fora, descobre por qual borda ele sai e calcula a interseção (**→clipint**). O extremo que estava fora vira $p'$. O que já estava dentro não muda.
4. Leva o ponto pedido para o sistema pedido: SCN (**→scn**) ou viewport (**→wv**).
5. Confere com a tabela de cantos do **→wv**: ponto em cima da borda esquerda tem $x_s=-1$, na borda de cima $y_s=1$ etc.

**Exemplo resolvido (números inventados)**. Window $(-10,0)$–$(30,20)$. Viewport $400\times200$ com origem $(20,15)$. Reta de $p_1=(-20,5)$ a $p_2=(20,25)$.

- $p_1$ tem $x=-20 < -10$: fora pela **esquerda**. $p_2$ tem $y = 25 > 20$: fora por **cima**.
- Inclinação: $m = \dfrac{25-5}{20-(-20)} = \dfrac{20}{40} = 0.5$.
- Borda esquerda $x=-10$: $y = 5 + 0.5\,(-10-(-20)) = 10$, então $p_1' = (-10,\ 10)$. Está entre $y=0$ e $y=20$: interseção válida.
- Borda de cima $y = 20$: $x = -20 + \dfrac{20-5}{0.5} = 10$, então $p_2' = (10,\ 20)$. Está entre $x=-10$ e $x=30$: válida.

Em SCN ($x_c=10,\ y_c=10,\ w/2=20,\ h/2=10$):

$$p_1' = \left(\frac{-10-10}{20},\ \frac{10-10}{10}\right) = (-1,\ 0) \qquad p_2' = \left(\frac{10-10}{20},\ \frac{20-10}{10}\right) = (0,\ 1)$$

Na viewport:

$$p_1':\ x_v = 20 + \tfrac{-1+1}{2}\cdot400 = 20,\quad y_v = 15 + \left(1-\tfrac{0+1}{2}\right)\cdot200 = 115$$

$$p_2':\ x_v = 20 + \tfrac{0+1}{2}\cdot400 = 220,\quad y_v = 15 + \left(1-\tfrac{1+1}{2}\right)\cdot200 = 15$$

Leitura rápida: $p_2'$ está na borda de **cima** da window, então $y_v$ é a própria origem $o_y = 15$; $p_1'$ está na borda **esquerda**, então $x_v = o_x = 20$.

> [!example]- Exercício 1: window (0,0)–(40,40), viewport 200×100 com origem (5,5), reta (−10,30)–(20,10). Ache p1' em SCN e na viewport.
> $p_1=(-10,30)$ está fora pela esquerda. $m = \frac{10-30}{20+10} = -\frac{2}{3}$. Em $x=0$: $y = 30 - \frac{2}{3}\cdot10 = 23.33$. $p_1' = (0,\ 23.33)$.
> SCN: $x_c = 20$, $y_c=20$, meias = 20. $x_s = -1$, $y_s = 3.33/20 = 0.167$ (inteiro: 0).
> Viewport: $x_v = 5 + 0 = 5$; $y_v = 5 + (1 - 23.33/40)\cdot100 = 5 + 41.67 = 46.67$ (≈ 47).

> [!example]- Exercício 2: mesma window e viewport, ponto (40, 0). Onde cai?
> É o canto inferior direito: SCN $(1,-1)$; viewport $(5+200,\ 5+100) = (205,\ 105)$.

## @clipint Interseção da reta com as bordas da window
termos: calcular interseção, ponto de interseção, coeficiente angular, inclinação, m, borda esquerda, borda direita, borda superior, borda inferior, x = xmin, y = ymax

Reta de $(x_1,y_1)$ a $(x_2,y_2)$, $m = \dfrac{y_2-y_1}{x_2-x_1}$:

| borda | conta | vale se |
|---|---|---|
| esquerda $x = x_{min}$ | $y = m\,(x_{min} - x_1) + y_1$ | $y_{min} \le y \le y_{max}$ |
| direita $x = x_{max}$ | $y = m\,(x_{max} - x_1) + y_1$ | $y_{min} \le y \le y_{max}$ |
| cima $y = y_{max}$ | $x = x_1 + \dfrac{y_{max} - y_1}{m}$ | $x_{min} \le x \le x_{max}$ |
| baixo $y = y_{min}$ | $x = x_1 + \dfrac{y_{min} - y_1}{m}$ | $x_{min} \le x \le x_{max}$ |

- Reta **vertical** ($x_1 = x_2$): não tem $m$; só corta cima/baixo e $x$ fica igual.
- Reta **horizontal** ($m=0$): só corta esquerda/direita e $y$ fica igual.
- Ponto num **canto** (código com dois bits, ex. cima+esquerda): testa uma borda; se o resultado cair fora do intervalo, a interseção certa é com a outra borda. Se nenhuma vale, a reta não passa pela window (rejeita).

## @clipp Recorte de ponto
termos: recorte de pontos, clipping de ponto, ponto dentro da window, ponto visível

Um ponto $(x,y)$ é desenhado se $x_{min} \le x \le x_{max}$ e $y_{min} \le y \le y_{max}$ (em SCN: $-1 \le x,y \le 1$). Ponto **na borda conta como dentro**. Não tem interseção para calcular: ou desenha ou não.

## @cs Cohen-Sutherland: recorte de retas por códigos de região (RC)
termos: códigos de região, region codes, RC, outcode, 4 bits, nove regiões, acima, abaixo, direita, esquerda, AND lógico, trivialmente aceita, trivialmente rejeitada, 0000, recorte de retas

**Ideia**: o plano é dividido em 9 regiões pelas 4 retas das bordas. Cada extremo da reta ganha um código de 4 bits; um bit vale 1 se o ponto está daquele lado de fora.

Ordem mais usada (e a que a questão costuma dar): **RC = [cima, baixo, direita, esquerda]**

- bit cima $= 1$ se $y > y_{max}$
- bit baixo $= 1$ se $y < y_{min}$
- bit direita $= 1$ se $x > x_{max}$
- bit esquerda $= 1$ se $x < x_{min}$

Mapa das 9 regiões nessa ordem:

| | esquerda | meio | direita |
|---|---|---|---|
| **cima** | `1001` | `1000` | `1010` |
| **meio** | `0001` | `0000` (window) | `0010` |
| **baixo** | `0101` | `0100` | `0110` |

> [!warning] Se a ordem dos bits for outra
> Não decore o mapa, decore o **método**: escreve 1 para cada lado em que o ponto está fora, na ordem que o enunciado der. Ex.: ordem [esquerda, direita, baixo, cima]: canto superior esquerdo = `1001`, canto inferior direito = `0110`, só acima = `0001`.
> Nunca existe `1100` (cima e baixo ao mesmo tempo) nem `0011`. Um código `1111` também nunca aparece.
> Ponto em cima da borda: bit 0 (é dentro).

**Algoritmo**

1. Calcula RC1 e RC2.
2. `RC1 == RC2 == 0000` → **totalmente dentro**, desenha sem conta.
3. `RC1 AND RC2 ≠ 0000` (têm um 1 na mesma posição) → os dois estão do mesmo lado de fora → **totalmente fora**, descarta.
4. Senão: **parcial**. Pega um extremo de fora, olha um bit 1 dele, calcula a interseção com aquela borda (**→clipint**), troca o extremo pela interseção, recalcula o código e volta ao passo 2.

```
enquanto verdade:
  se (c1 | c2) == 0: aceita; sai
  se (c1 & c2) != 0: rejeita; sai
  c = c1 se c1 != 0 senão c2
  se c & CIMA:     x = x1 + (ymax - y1)/m ; y = ymax
  senao se BAIXO:  x = x1 + (ymin - y1)/m ; y = ymin
  senao se DIREITA:y = y1 + m*(xmax - x1); x = xmax
  senao ESQUERDA:  y = y1 + m*(xmin - x1); x = xmin
  troca o ponto de código c por (x,y) e recalcula o código
```

**Exemplo** (window $(-10,0)$–$(30,20)$, ordem [cima, baixo, direita, esquerda]):

| ponto | testes | RC |
|---|---|---|
| $(-20,5)$ | $x<-10$ | `0001` |
| $(20,25)$ | $y>20$ | `1000` |
| $(40,-5)$ | $x>30$, $y<0$ | `0110` |
| $(0,10)$ | dentro | `0000` |
| $(-15,30)$ | $x<-10$, $y>20$ | `1001` |

- $(-20,5)$–$(20,25)$: `0001 AND 1000 = 0000`, não rejeita trivialmente; calcula interseções (deu $(-10,10)$ e $(10,20)$ no **→contaclip**).
- $(-15,30)$–$(-20,5)$: `1001 AND 0001 = 0001` → os dois à esquerda → rejeita sem conta.
- Caso chato: `AND = 0000` não garante que a reta passa pela window (ex.: reta cortando só a região do canto). O algoritmo descobre isso ao recalcular os códigos.

**Características**: bom quando a maioria das retas está toda dentro ou toda fora (testes triviais baratos). Só funciona para window **retangular**. Pode calcular interseções desnecessárias (até 4 por reta).

## @lb Liang-Barsky: recorte paramétrico com pk e qk
termos: parâmetros pk e qk, p1 p2 p3 p4, q1 q2 q3 q4, u1 u2, forma paramétrica, r = q/p, entrando, saindo, recorte de retas paramétrico

Reta paramétrica: $x = x_1 + u\,\Delta x$, $y = y_1 + u\,\Delta y$, $0 \le u \le 1$, com $\Delta x = x_2-x_1$, $\Delta y = y_2-y_1$. O ponto está dentro se $p_k\,u \le q_k$ para $k=1..4$:

$$\begin{aligned}
p_1 &= -\Delta x, & q_1 &= x_1 - x_{min} &\text{(esquerda)}\\
p_2 &= \Delta x, & q_2 &= x_{max} - x_1 &\text{(direita)}\\
p_3 &= -\Delta y, & q_3 &= y_1 - y_{min} &\text{(baixo)}\\
p_4 &= \Delta y, & q_4 &= y_{max} - y_1 &\text{(cima)}
\end{aligned}$$

**Regras**

- $p_k = 0$: reta **paralela** àquela borda. Se $q_k < 0$ está fora → **rejeita**. Se $q_k \ge 0$, ignora essa borda.
- $p_k < 0$: a reta **entra** por essa borda. $r_k = q_k/p_k$ e $u_1 = \max(0,\ r_k\ \text{dos que entram})$.
- $p_k > 0$: a reta **sai** por essa borda. $r_k = q_k/p_k$ e $u_2 = \min(1,\ r_k\ \text{dos que saem})$.
- Se $u_1 > u_2$ → **rejeita** (totalmente fora). Senão os novos extremos são $u_1$ e $u_2$ na equação paramétrica.

**Exemplo** (mesma reta $(-20,5)$–$(20,25)$, window $(-10,0)$–$(30,20)$; $\Delta x = 40$, $\Delta y = 20$):

| k | $p_k$ | $q_k$ | $r_k$ | tipo |
|---|---|---|---|---|
| 1 | $-40$ | $-20-(-10) = -10$ | $0.25$ | entra |
| 2 | $40$ | $30-(-20) = 50$ | $1.25$ | sai |
| 3 | $-20$ | $5 - 0 = 5$ | $-0.25$ | entra |
| 4 | $20$ | $20 - 5 = 15$ | $0.75$ | sai |

$$u_1 = \max(0,\ 0.25,\ -0.25) = 0.25 \qquad u_2 = \min(1,\ 1.25,\ 0.75) = 0.75$$

$$u_1:\ (-20 + 0.25\cdot40,\ 5 + 0.25\cdot20) = (-10,\ 10) \qquad u_2:\ (-20+0.75\cdot40,\ 5+0.75\cdot20) = (10,\ 20)$$

Mesmo resultado do Cohen-Sutherland, como tinha que ser.

**Características**: mais eficiente que Cohen-Sutherland (calcula no máximo as 2 interseções que importam, decide antes de calcular). É o Cyrus-Beck especializado para window retangular alinhada aos eixos. Generaliza fácil para 3D (6 desigualdades).

## @cb Cyrus-Beck: recorte paramétrico contra polígono convexo
termos: Cyrus-Beck, normal da aresta, produto escalar, polígono convexo, janela convexa qualquer, potencialmente entrando, potencialmente saindo, tE, tL

Mesma ideia paramétrica do Liang-Barsky, mas a janela pode ser **qualquer polígono convexo**. Para cada aresta $i$, com normal **para fora** $N_i$ e um ponto $P_{Ei}$ sobre ela, e a reta $P(t) = P_0 + t\,D$, $D = P_1 - P_0$:

$$t_i = \frac{N_i \cdot (P_0 - P_{Ei})}{-\,N_i \cdot D}$$

- $N_i\cdot D < 0$: **potencialmente entrando** (PE); $t_E = \max(0,\ t_i)$.
- $N_i\cdot D > 0$: **potencialmente saindo** (PL); $t_L = \min(1,\ t_i)$.
- $N_i \cdot D = 0$: paralela; se $N_i\cdot(P_0 - P_{Ei}) > 0$ está fora, rejeita.
- $t_E > t_L$ → rejeita. Senão desenha de $P(t_E)$ a $P(t_L)$.

## @nln Nicholl-Lee-Nicholl: recorte por coeficientes angulares
termos: Nicholl-Lee-Nicholl, NLN, coeficientes angulares, inclinação, retas de referência, cantos da window, regiões, menos interseções, comparar inclinações

**Ideia**: evita calcular interseções à toa. Com $P_1$ numa de 3 posições (dentro da window, numa região de borda, ou numa região de canto; os outros casos saem por simetria), traça **retas de referência** de $P_1$ até os **4 cantos** da window. Essas retas dividem o plano em regiões. Comparando o **coeficiente angular** de $P_1P_2$ com os coeficientes angulares dessas retas de referência, descobre em qual região $P_2$ está, e com isso **por qual borda a reta entra e sai**, antes de calcular qualquer interseção. Aí calcula só as interseções que interessam.

- Exemplo de teste: $P_1$ à esquerda da window; se a inclinação de $P_1P_2$ está entre as inclinações de $P_1$ até o canto superior esquerdo e $P_1$ até o canto inferior esquerdo, a reta entra pela borda esquerda.
- Faz menos divisões e comparações que Cohen-Sutherland e Liang-Barsky.
- Só serve para **2D** e window **retangular** (é muito caso para generalizar).

## @subdiv Subdivisão do ponto médio (midpoint subdivision)
termos: subdivisão do ponto médio, midpoint subdivision, busca binária, dividir a reta ao meio

Variante do Cohen-Sutherland que não calcula interseção com divisão: divide a reta no **ponto médio** e aplica os testes triviais a cada metade, recursivamente, até as partes serem aceitas, rejeitadas ou do tamanho de um pixel. Só usa soma e divisão por 2 (shift), por isso era bom em hardware.

## @suth Sutherland-Hodgeman: recorte de polígonos borda a borda
termos: recorte de polígonos, polygon clipping, Sutherland-Hodgman, Sutherland-Hodgeman, aresta por aresta, lista de vértices de saída, dentro-fora, fora-dentro, reentrante, janela convexa

**Ideia**: recorta o polígono inteiro contra **uma borda da janela de cada vez** (esquerda, direita, baixo, cima). A saída de uma etapa (lista de vértices) é a entrada da próxima. Para cada aresta $S \to P$ do polígono (S = vértice anterior, P = atual):

| S | P | o que vai para a saída |
|---|---|---|
| dentro | dentro | $P$ |
| dentro | fora | a interseção $I$ |
| fora | fora | nada |
| fora | dentro | $I$ e depois $P$ |

**Exemplo**: triângulo $A(0,0)$, $B(8,0)$, $C(4,8)$ recortado só pela borda direita $x = 6$.

- $A\to B$: $A$ dentro, $B$ fora ($8>6$): sai $I_1 = (6,0)$.
- $B\to C$: $B$ fora, $C$ dentro: interseção em $x=6$. $B + t(C-B) = (8-4t,\ 8t)$, $8-4t=6 \Rightarrow t = 0.5$, $I_2 = (6,4)$. Sai $I_2$ e $C$.
- $C\to A$: os dois dentro: sai $A$.

Resultado: $(6,0),\ (6,4),\ (4,8),\ (0,0)$, um quadrilátero.

**Características**: a **janela de recorte tem que ser convexa**. O polígono recortado pode ser côncavo, mas se ele se partir em vários pedaços o algoritmo devolve **um polígono só** ligado por arestas extras sobre a borda (arestas fantasma). Para isso existe o Weiler-Atherton.

## @weiler Weiler-Atherton: recorte de polígonos côncavos
termos: Weiler-Atherton, polígonos côncavos, janela côncava, percorrer, entrando, saindo, lista de interseções, vários polígonos, buracos

**Ideia**: anda pelo contorno do polígono e, ao chegar numa interseção onde o polígono **sai** da janela, passa a andar pelo **contorno da janela** até a próxima interseção, aí volta para o polígono. Cada volta fechada vira um polígono de saída.

1. Calcula todas as interseções do polígono com a janela e marca cada uma como **entrando** ou **saindo**.
2. Monta duas listas circulares (vértices do polígono e vértices da janela) com as interseções inseridas nas duas.
3. Começa num ponto de entrada, segue o polígono até um ponto de saída, troca para a lista da janela, segue até a próxima entrada, troca de novo, até voltar ao início.

**Características**: funciona com polígono **côncavo** e com **janela côncava** (até com buracos) e devolve **vários polígonos separados**, sem arestas fantasma. Mais caro e mais chato de implementar que Sutherland-Hodgeman.

## @clipq Qual algoritmo de recorte é qual (reconhecer pela descrição)
termos: identificar o algoritmo de recorte, algoritmo de recorte baseado em, recorte de retas, recorte de polígonos, nomes que não são de recorte, Gauss-Seidel, Gauss-Jacobi, Runge-Kutta, Kruskal

| a questão descreve | algoritmo |
|---|---|
| códigos de região, 4 bits, AND, 9 regiões | **Cohen-Sutherland** (retas) |
| parâmetros $p_k$, $q_k$, $u_1$, $u_2$, forma paramétrica | **Liang-Barsky** (retas) |
| normais das arestas, polígono convexo qualquer, $t_E$/$t_L$ | **Cyrus-Beck** (retas) |
| coeficientes angulares, retas de referência até os cantos | **Nicholl-Lee-Nicholl** (retas) |
| divide ao meio até aceitar/rejeitar | **Subdivisão do ponto médio** (retas) |
| uma borda de cada vez, lista de vértices, 4 casos dentro/fora | **Sutherland-Hodgeman** (polígonos) |
| polígonos côncavos, alterna entre contorno do polígono e da janela | **Weiler-Atherton** (polígonos) |

- **Recorte de polígonos**: Sutherland-Hodgeman e Weiler-Atherton. Os outros (CS, LB, CB, NLN) são de **retas**.
- Nomes que **não são** de recorte: Gauss-Seidel e Gauss-Jacobi (sistemas lineares), Runge-Kutta (EDOs), Kruskal (árvore geradora mínima), Bresenham e DDA (rasterização de retas), Boundary-fill / Flood-fill (preenchimento), algoritmo do pintor (visibilidade).

**Recorte de curvas**: no SGI a curva vira uma sequência de segmentos de reta; recorta cada segmento com o algoritmo de reta (ou recorta ponto a ponto).

# Parte 2. Transformações e coordenadas homogêneas

## @homog Coordenadas homogêneas: o W
termos: coordenadas homogêneas, mapeamento das coordenadas 3D para homogêneas, sistema de referência homogêneo, representação homogênea, W, dimensão adicional, fator de escala, W diferente de zero, W = 1, [x y W], [X Y Z W], ponto 4D, dividir por W, converter para cartesianas, ponto no infinito, vetor

**Para que serve**: sem homogêneas a translação é uma **soma** ($x' = x + D_x$) e a escala/rotação são **produtos**; não dá para juntar tudo numa matriz só. Acrescentando **uma** coordenada a mais (o W), **toda** transformação geométrica (translação, escala, rotação, cisalhamento, reflexão e até a projeção perspectiva) vira **multiplicação de matriz**, e várias transformações em sequência viram **uma** matriz (composição).

- 2D: $(x, y) \to [x\ \ y\ \ W]$ , matrizes $3\times3$.  3D: $(x,y,z) \to [x\ \ y\ \ z\ \ W]$ , matrizes $4\times4$. Sempre **só uma** dimensão a mais.
- O W é chamado de **fator de escala** da coordenada homogênea. Ele tem que ser **constante e diferente de 0** (W = 0 daria divisão por zero ao voltar para cartesiano). Por simplicidade **usa-se W = 1**, que não altera x e y.
- Voltar para cartesiano: **divide tudo por W**. $[X\ Y\ Z\ W] \to \left(\frac{X}{W},\frac{Y}{W},\frac{Z}{W}\right)$.
- Um mesmo ponto tem infinitas representações: $(2,1) = [2\ 1\ 1] = [4\ 2\ 2] = [-6\ -3\ -3]$.
- $W = 0$: não é ponto, é **direção** (vetor, ou ponto no infinito). Translação não afeta direções.

**Exemplo**: o ponto homogêneo $[6\ \ 3\ \ 9\ \ 3]$ é o cartesiano $\left(\frac{6}{3},\frac{3}{3},\frac{9}{3}\right) = (2,\ 1,\ 3)$. E $[5\ \ -2\ \ 4\ \ 2] = (2.5,\ -1,\ 2)$.

> [!warning] Erros comuns sobre homogêneas
> - O W não é fixo em 0, nem em −1, nem "obrigatoriamente 1", nem calculado a partir do ponto: é **qualquer constante ≠ 0** (1 por conveniência).
> - Homogêneas **não** é o mesmo que SCN/coordenadas normalizadas (SCN é a window virando $[-1,1]$) e não exige normalizar nada antes.
> - **Todas** as transformações viram produto de matriz, não só rotação ou só escala.
> - É **uma** dimensão a mais, não o dobro.
> - Matriz $3\times3$ com W é **2D**; matriz $4\times4$ é **3D**.

## @t2c Convenção vetor-linha × vetor-coluna (de onde vem a transposta)
termos: vetor-linha, vetor-coluna, pré-multiplicação, pós-multiplicação, transposta, última linha, última coluna, [x' y' 1] = [x y 1] M, OpenGL, convenção

Tem duas formas de escrever a mesma coisa:

| | vetor-**linha** | vetor-**coluna** |
|---|---|---|
| produto | $[x'\ y'\ 1] = [x\ y\ 1]\cdot M$ | $\begin{bmatrix}x'\\y'\\1\end{bmatrix} = M \cdot \begin{bmatrix}x\\y\\1\end{bmatrix}$ |
| translação fica | na **última linha** | na **última coluna** |
| composição (aplica $M_1$, depois $M_2$, depois $M_3$) | $M = M_1 M_2 M_3$ (primeira à **esquerda**) | $M = M_3 M_2 M_1$ (primeira à **direita**) |
| quem usa | material do professor / SGI, livros antigos (Foley 1ª ed.) | OpenGL, GLM, maioria dos livros novos, POSCOMP |

Uma é a **transposta** da outra: $M_{col} = M_{lin}^T$. Na prova, olhe onde está a translação (ou o sinal do seno) para saber qual convenção a matriz usa.

## @t2d Matrizes 2D em homogêneas: translação, escala, rotação
termos: matriz de translação 2D, matriz de escalonamento 2D, matriz de rotação 2D, Dx Dy, Sx Sy, cos sen, identificar a matriz, mundo 2D, 3x3, reconhecer matriz, fatores de escala

**Equações** (valem nas duas convenções):

$$\text{translação: } x' = x + D_x,\ \ y' = y + D_y \qquad \text{escala: } x' = S_x\,x,\ \ y' = S_y\,y$$

$$\text{rotação anti-horária de } \theta \text{ em torno da origem: } x' = x\cos\theta - y\,\mathrm{sen}\,\theta,\ \ y' = x\,\mathrm{sen}\,\theta + y\cos\theta$$

**Vetor-linha** ($[x\ y\ 1]\cdot M$):

$$T = \begin{bmatrix}1&0&0\\0&1&0\\D_x&D_y&1\end{bmatrix} \quad S = \begin{bmatrix}S_x&0&0\\0&S_y&0\\0&0&1\end{bmatrix} \quad R = \begin{bmatrix}\cos\theta&\mathrm{sen}\,\theta&0\\-\mathrm{sen}\,\theta&\cos\theta&0\\0&0&1\end{bmatrix}$$

**Vetor-coluna** ($M \cdot [x\ y\ 1]^T$), as mesmas transpostas:

$$T = \begin{bmatrix}1&0&D_x\\0&1&D_y\\0&0&1\end{bmatrix} \quad S = \begin{bmatrix}S_x&0&0\\0&S_y&0\\0&0&1\end{bmatrix} \quad R = \begin{bmatrix}\cos\theta&-\mathrm{sen}\,\theta&0\\\mathrm{sen}\,\theta&\cos\theta&0\\0&0&1\end{bmatrix}$$

**Reconhecer "a matriz acima é"**

| forma | é |
|---|---|
| $3\times3$, identidade com 2 números na última linha (ou coluna) | **translação 2D** em homogêneas |
| $3\times3$, só diagonal $S_x, S_y, 1$ | **escala 2D** em homogêneas ($S_x$, $S_y$ = fatores de escala em x e y) |
| $3\times3$, bloco $2\times2$ com cos e sen, resto identidade | **rotação 2D** em homogêneas |
| $4\times4$, identidade com 3 números na última linha/coluna | **translação 3D** |
| $4\times4$, diagonal $S_x,S_y,S_z,1$ | **escala 3D** |
| $4\times4$ com cos/sen e uma linha+coluna de identidade | **rotação 3D** em torno do eixo da linha/coluna identidade (**→r3d**) |

- Escala com $S_x = S_y$: **uniforme** (não deforma). $S_x \neq S_y$: não uniforme. $0<S<1$ diminui, $S>1$ aumenta, $S<0$ espelha.
- Escala e rotação "puras" são **em torno da origem**: um objeto fora da origem também **anda** quando escala ou gira. Para escalar/girar no lugar, ver **→pivo**.

**Exemplo**: girar $(4,\ 2)$ de $90°$ anti-horário em torno da origem: $x' = 4\cdot0 - 2\cdot1 = -2$, $y' = 4\cdot1 + 2\cdot0 = 4$, fica $(-2,\ 4)$. Com $30°$ ($\cos = 0.866$, $\mathrm{sen} = 0.5$): $(4\cdot0.866 - 2\cdot0.5,\ 4\cdot0.5+2\cdot0.866) = (2.46,\ 3.73)$.

## @tgen Matriz genérica 2D e mapeamento de vetores da base
termos: transformação genérica, matriz genérica, a b c d, transformação linear, para onde vai cada vetor, imagem de um vetor, imagem de (1,0,0), colunas da matriz, base canônica

Vetor-linha, a forma geral de uma transformação afim 2D:

$$[x'\ \ y'\ \ 1] = [x\ \ y\ \ 1]\begin{bmatrix}a&b&0\\c&d&0\\m&n&1\end{bmatrix} \Rightarrow \begin{cases}x' = a\,x + c\,y + m\\ y' = b\,x + d\,y + n\end{cases}$$

$a, b, c, d$: rotação, escala, cisalhamento, reflexão (a parte linear). $m, n$: translação. A última coluna $[0\ 0\ 1]^T$ fixa (a última **linha** na versão coluna). Se ela não for $0,0,1$ a transformação é projetiva (perspectiva).

**Para onde vai cada vetor da base** (transformação linear $v' = M v$, vetor-coluna): a imagem de $e_1 = (1,0,0)$ é a **1ª coluna** de $M$, de $e_2 = (0,1,0)$ a **2ª coluna**, de $e_3$ a **3ª coluna**. Imagem de uma soma = soma das colunas. (Em vetor-linha é a mesma coisa com **linhas**.)

**Exemplo** (vetor-coluna): $M = \begin{bmatrix}2&4&0\\1&-1&3\\0&5&1\end{bmatrix}$.

$$M\begin{bmatrix}0\\1\\0\end{bmatrix} = \begin{bmatrix}4\\-1\\5\end{bmatrix}\ (\text{coluna 2}) \qquad M\begin{bmatrix}1\\0\\1\end{bmatrix} = \begin{bmatrix}2+0\\1+3\\0+1\end{bmatrix} = \begin{bmatrix}2\\4\\1\end{bmatrix}\ (\text{colunas 1 + 3})$$

## @refl Reflexão (espelhamento) e cisalhamento (shear)
termos: reflexão, espelhamento, espelhar, eixo x, eixo y, origem, reta y = x, cisalhamento, shear, inclinar, achar a matriz pela figura antes e depois

Matrizes $2\times2$ (põe no canto de uma identidade $3\times3$; as diagonais são iguais nas duas convenções):

| transformação | efeito | matriz (parte linear) |
|---|---|---|
| reflexão no eixo x | $(x,y)\to(x,-y)$ | $\mathrm{diag}(1,-1)$ |
| reflexão no eixo y | $(x,y)\to(-x,y)$ | $\mathrm{diag}(-1,1)$ |
| reflexão na origem | $(x,y)\to(-x,-y)$ | $\mathrm{diag}(-1,-1)$ = rotação de 180° |
| reflexão na reta $y=x$ | $(x,y)\to(y,x)$ | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ |
| reflexão na reta $y=-x$ | $(x,y)\to(-y,-x)$ | $\begin{bmatrix}0&-1\\-1&0\end{bmatrix}$ |
| cisalhamento em x | $x' = x + sh\,y$ | coluna: $\begin{bmatrix}1&sh\\0&1\end{bmatrix}$; linha: $\begin{bmatrix}1&0\\sh&1\end{bmatrix}$ |
| cisalhamento em y | $y' = y + sh\,x$ | coluna: $\begin{bmatrix}1&0\\sh&1\end{bmatrix}$; linha: $\begin{bmatrix}1&sh\\0&1\end{bmatrix}$ |

**Descobrir a matriz a partir de uma figura** (questão "T mapeia a figura da esquerda na da direita"): pegue 2 ou 3 pontos fáceis (cantos), veja para onde foram e monte as equações $x' = ax + cy + m$, $y' = bx + dy + n$. Ex.: quadrado unitário em que $(1,0)\to(1,0)$, $(0,1)\to(0.5,1)$ e $(0,0)\to(0,0)$: $x' = x + 0.5y$, $y' = y$, cisalhamento em x com $sh = 0.5$. Lembre que **pode haver mais de uma matriz certa** (ex.: uma rotação de 180° é igual a reflexão na origem; a mesma transformação escrita nas duas convenções).

## @comp Composição de transformações e ordem
termos: composição, concatenação, ordem das transformações, primeiro escala e depois translada, primeiro translada e depois escala, matriz composta, multiplicação de matrizes não é comutativa, sequência de transformações

- Aplicar $A$, depois $B$: em **vetor-coluna** a matriz é $B\cdot A$ (lê da direita para a esquerda); em **vetor-linha** é $A\cdot B$ (lê da esquerda para a direita).
- Multiplicar as matrizes antes e aplicar uma só em todos os pontos é mais barato que aplicar cada uma em cada ponto. É o porquê de homogêneas.

**Ler uma matriz composta: escalou antes ou transladou antes?** (vetor-coluna, escala $S$ e translação $T$)

$$T\cdot S = \begin{bmatrix}S_x&0&D_x\\0&S_y&D_y\\0&0&1\end{bmatrix}\ \ \text{(escala primeiro, depois translada: a translação aparece "pura")}$$

$$S\cdot T = \begin{bmatrix}S_x&0&S_xD_x\\0&S_y&S_yD_y\\0&0&1\end{bmatrix}\ \ \text{(translada primeiro, depois escala: a translação sai multiplicada pela escala)}$$

**Exemplo numérico**: ponto $(1,1)$, escala 2 e translação $(3,0)$.
- Escala e depois translada: $(2,2) \to (5,2)$.
- Translada e depois escala: $(4,1) \to (8,2)$. Resultados diferentes: ordem importa.

## @comuta Quais transformações comutam
termos: comutativa, a ordem altera o resultado, a ordem não altera, duas rotações, rotação e escala, rotação em torno de eixos diferentes, comutam

| par | comuta? |
|---|---|
| translação + translação | **sim** |
| escala + escala | **sim** |
| rotação 2D + rotação 2D (mesmo centro) | **sim** (somam os ângulos) |
| rotação 3D + rotação 3D **no mesmo eixo** | **sim** |
| rotação 3D + rotação 3D em **eixos diferentes** (ex. 90° em X e 90° em Z) | **não** |
| escala **uniforme** + rotação | **sim** |
| escala **não uniforme** + rotação | **não** |
| translação + rotação | **não** |
| translação + escala | **não** |

Teste rápido de "rotações 3D em eixos diferentes não comutam": $R_x(90°)$ depois $R_z(90°)$ leva o eixo $y$ para $z$ e depois $z$ fica $z$: $y\to z$. Na outra ordem, $R_z(90°)$ leva $y \to -x$ e $R_x$ não mexe em $x$: $y \to -x$. Diferente.

## @pivo Girar/escalar em torno de um ponto (centro do objeto, pivô)
termos: em torno de um ponto, centro de massa, centro do objeto, pivô, girar no lugar, manter a posição, rotação em torno de ponto arbitrário, escala em relação ao centro, T(p) R T(-p), ancorado

Rotação e escala básicas são em torno da **origem**. Para fazer em torno de um ponto $p = (x_c, y_c[, z_c])$:

1. translada por $-p$ (o ponto vai para a origem);
2. gira/escala;
3. translada de volta por $+p$.

$$\text{vetor-coluna: } M = T(p)\cdot R(\theta)\cdot T(-p) \qquad \text{vetor-linha: } M = T(-p)\cdot R(\theta)\cdot T(p)$$

Em 3D, "girar o objeto em torno do eixo x passando pelo seu centro" é igual: $T(p)\,R_x(\theta)\,T(-p)$ (coluna). O centro do objeto (centro geométrico) é a média dos vértices.

**Exemplo** (2D): girar $(6,3)$ de $90°$ em torno de $p=(4,3)$. $(6,3)-(4,3) = (2,0)$; gira: $(0,2)$; volta: $(4,5)$.

> [!warning] Ordens erradas
> $T(-p)\,R\,T(p)$ em vetor-coluna (ordem trocada), $T(p)\,R\,T(p)$ (sinal errado), $T(-p)\,R$ (esqueceu de voltar), $R\,T(-p)$. Só uma tem o $-p$ agindo **primeiro** e o $+p$ por **último**.

## @inv Inversas das transformações
termos: inversa, desfazer transformação, matriz inversa, transposta da rotação, ortogonal

$$T(D_x,D_y)^{-1} = T(-D_x,-D_y) \qquad S(S_x,S_y)^{-1} = S\!\left(\tfrac{1}{S_x},\tfrac{1}{S_y}\right) \qquad R(\theta)^{-1} = R(-\theta) = R(\theta)^T$$

A matriz de rotação é **ortogonal** (inversa = transposta, determinante 1). Inversa de composição inverte a ordem: $(AB)^{-1} = B^{-1}A^{-1}$.

## @t3d Translação e escala 3D (4×4)
termos: translação 3D, escalonamento 3D, deslocamento Dx Dy Dz, fatores de escala Sx Sy Sz, matriz 4x4, coordenadas homogêneas 3D

Vetor-linha ($[x\ y\ z\ 1]\cdot M$) e vetor-coluna, deslocamento $D = [D_x\ D_y\ D_z]$ e escala $S = [S_x\ S_y\ S_z]$:

$$T_{lin} = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\D_x&D_y&D_z&1\end{bmatrix} \qquad T_{col} = \begin{bmatrix}1&0&0&D_x\\0&1&0&D_y\\0&0&1&D_z\\0&0&0&1\end{bmatrix} \qquad S = \begin{bmatrix}S_x&0&0&0\\0&S_y&0&0\\0&0&S_z&0\\0&0&0&1\end{bmatrix}$$

**Exemplo**: translação por $D = [4\ \ {-1}\ \ 2]$ e escala por $S = [2\ \ 3\ \ 0.5]$:

$$T_{lin} = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\4&-1&2&1\end{bmatrix} \quad T_{col} = \begin{bmatrix}1&0&0&4\\0&1&0&-1\\0&0&1&2\\0&0&0&1\end{bmatrix} \quad S = \begin{bmatrix}2&0&0&0\\0&3&0&0\\0&0&0.5&0\\0&0&0&1\end{bmatrix}$$

Aplicando no ponto $(1,1,1)$: translação dá $(5,0,3)$; escala dá $(2,3,0.5)$.

> [!warning] Matrizes parecidas que **não** são essas
> - Escala com os fatores **na última linha/coluna** (isso é translação).
> - Translação com os números **na diagonal** (isso é escala).
> - Translação com $1$ na diagonal mas os $D$ espalhados (fora da última linha/coluna).
> - Matriz de escala com o último elemento diferente de 1 (o $W$ seria escalado).

## @r3d Rotação 3D em torno dos eixos X, Y e Z (geral e 90°)
termos: rotação 3D, matriz homogênea de rotação de um objeto em torno de um eixo, rotação em torno do eixo X, em torno do eixo Y, em torno do eixo Z, Rx, Ry, Rz, seno e cosseno de 90, rotação de 90 graus, regra da mão direita, anti-horário

Regra: a linha e a coluna do **eixo de rotação** ficam como identidade (o eixo não muda). Os outros dois eixos formam a rotação 2D. Sentido positivo = **anti-horário olhando do lado positivo do eixo para a origem** (mão direita).

**Vetor-coluna** ($M\cdot v$), $c = \cos\theta$, $s = \mathrm{sen}\,\theta$:

$$R_x = \begin{bmatrix}1&0&0&0\\0&c&-s&0\\0&s&c&0\\0&0&0&1\end{bmatrix} \quad R_y = \begin{bmatrix}c&0&s&0\\0&1&0&0\\-s&0&c&0\\0&0&0&1\end{bmatrix} \quad R_z = \begin{bmatrix}c&-s&0&0\\s&c&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$$

**Vetor-linha** ($v\cdot M$) = transpostas (o sinal de menos troca de lugar):

$$R_x = \begin{bmatrix}1&0&0&0\\0&c&s&0\\0&-s&c&0\\0&0&0&1\end{bmatrix} \quad R_y = \begin{bmatrix}c&0&-s&0\\0&1&0&0\\s&0&c&0\\0&0&0&1\end{bmatrix} \quad R_z = \begin{bmatrix}c&s&0&0\\-s&c&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$$

O $R_y$ é o "estranho": o $-s$ fica **embaixo** à esquerda (coluna), ao contrário de $R_x$ e $R_z$. Motivo: o ciclo é $x\to y\to z\to x$, e para Y o plano girado é $z\text{–}x$ (não $x\text{–}z$).

**Com 90°** ($\cos = 0$, $\mathrm{sen} = 1$):

| | vetor-coluna | vetor-linha |
|---|---|---|
| $R_x(90°)$ | $\begin{bmatrix}1&0&0&0\\0&0&-1&0\\0&1&0&0\\0&0&0&1\end{bmatrix}$ | $\begin{bmatrix}1&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&1\end{bmatrix}$ |
| $R_y(90°)$ | $\begin{bmatrix}0&0&1&0\\0&1&0&0\\-1&0&0&0\\0&0&0&1\end{bmatrix}$ | $\begin{bmatrix}0&0&-1&0\\0&1&0&0\\1&0&0&0\\0&0&0&1\end{bmatrix}$ |
| $R_z(90°)$ | $\begin{bmatrix}0&-1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$ | $\begin{bmatrix}0&1&0&0\\-1&0&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$ |

Efeito de 90° (vale nas duas convenções): $R_x$: $y\to z$, $z\to -y$. $R_y$: $z \to x$, $x\to -z$. $R_z$: $x \to y$, $y\to -x$.

**Como reconhecer qual rotação é**: (1) é $4\times4$? (2) qual linha/coluna é identidade? Esse é o eixo. (3) o $-1$ (ou $-\mathrm{sen}$) está acima ou abaixo da diagonal? Compare com a tabela acima na convenção que as outras matrizes da questão usam.

**Com 180°** ($\cos=-1$, $\mathrm{sen}=0$): $R_z(180°) = \mathrm{diag}(-1,-1,1,1)$, igual nas duas convenções.

> [!example]- Exercício: aplique Rx(90°) no ponto (2, 3, 5).
> $y' = y\cos - z\,\mathrm{sen} = -5$, $z' = y\,\mathrm{sen} + z\cos = 3$. Fica $(2,\ -5,\ 3)$.

## @eixoarb Rotação em torno de um eixo arbitrário
termos: eixo arbitrário, eixo qualquer, rotação em torno de uma reta qualquer, alinhar com o eixo z, ângulos de Euler

Eixo passando por $P_1$ com direção $u$ (unitária). Sequência (cada passo é uma matriz, e no fim desfaz na ordem inversa):

1. $T(-P_1)$: leva o eixo para passar pela origem.
2. Gira em torno de $x$ até o eixo cair no plano $xz$ (ângulo $\alpha$, com $\cos\alpha = \frac{u_z}{\sqrt{u_y^2+u_z^2}}$).
3. Gira em torno de $y$ até o eixo coincidir com $z$ (ângulo $\beta$).
4. $R_z(\theta)$: a rotação pedida.
5. Desfaz: $R_y(-\beta)$, $R_x(-\alpha)$, $T(P_1)$.

Vetor-coluna: $M = T(P_1)\,R_x^{-1}(\alpha)\,R_y^{-1}(\beta)\,R_z(\theta)\,R_y(\beta)\,R_x(\alpha)\,T(-P_1)$. No SGI 3D a mesma ideia com ângulos para alinhar o eixo ao $y$ ou $z$.

**Casos que caem**: girar em torno do centro do objeto (eixo paralelo a X, Y ou Z passando pelo centro) é só $T(c)\,R\,T(-c)$, sem os passos 2, 3 e 5.

## @mudbase Mudança de base / mudança de sistema de coordenadas
termos: mudança de base, mudança de sistema de coordenadas, matriz de mudança de base, composição de translação rotação e escala, sistema local, sistema da câmera

Passar de um sistema de coordenadas para outro (mundo → câmera, mundo → window, objeto → mundo) é uma composição de **translação, rotação e escala** em homogêneas. Ex.: mundo → SCN é $T(-WC)\,R(-\theta)\,S(2/w,2/h)$ (vetor-linha), visto no **→scn**. Se os novos eixos são vetores unitários ortogonais $u, v, w$ e a nova origem é $O$, a matriz é rotação com $u,v,w$ nas linhas (vetor-coluna) vezes $T(-O)$ (ver **→camera**).

# Parte 3. Vetores, planos e malhas

## @dot Produto escalar (interno, dot product)
termos: produto escalar, produto interno, dot product, ângulo entre vetores, cosseno, perpendicular, ortogonal, projeção de vetor, Lambert usa

$$a\cdot b = a_xb_x + a_yb_y + a_zb_z = |a|\,|b|\cos\theta$$

- Resultado é um **número** (escalar). $a\cdot b = 0$ → perpendiculares. $>0$ → ângulo agudo (mesmo lado). $<0$ → obtuso.
- Ângulo: $\cos\theta = \dfrac{a\cdot b}{|a|\,|b|}$. Com vetores unitários, $\cos\theta = a\cdot b$ direto (é o que a iluminação usa: $N\cdot L$, $R\cdot V$).
- Projeção de $a$ sobre $b$: $\dfrac{a\cdot b}{|b|^2}\,b$.

**Exemplo**: $a = (1,0,1)$, $b=(0,1,1)$: $a\cdot b = 1$, $|a| = |b| = \sqrt2$, $\cos\theta = \frac{1}{2}$, $\theta = 60°$.

## @cross Produto vetorial (cross product) e normal de uma face
termos: produto vetorial, cross product, vetor perpendicular aos outros dois, normal da face, normal a partir de 3 pontos, eixo Z a partir de X e Y, regra da mão direita, área do triângulo

$$a\times b = \begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\a_x&a_y&a_z\\b_x&b_y&b_z\end{vmatrix} = \big(a_yb_z - a_zb_y,\ \ a_zb_x - a_xb_z,\ \ a_xb_y - a_yb_x\big)$$

- Resultado é um **vetor perpendicular aos dois**. Sentido pela mão direita. $b\times a = -(a\times b)$ (não comuta).
- $|a\times b| = |a||b|\,\mathrm{sen}\,\theta$ = área do paralelogramo (metade = área do triângulo).
- Eixos: $X \times Y = Z$, $Y\times Z = X$, $Z \times X = Y$. É **a** operação que dá o terceiro eixo de um sistema a partir de dois (a câmera faz isso: **→camera**).

**Normal de uma face com 3 pontos** $P_0, P_1, P_2$ (é **produto vetorial**, não escalar):

$$N = (P_1 - P_0)\times(P_2 - P_0) \qquad \hat N = \frac{N}{|N|}$$

A ordem dos vértices decide o sentido: vértices em ordem **anti-horária** vistos de fora → normal para **fora**.

**Exemplo**: $P_0 = (1,0,0)$, $P_1 = (0,2,0)$, $P_2 = (0,0,3)$. $e_1 = (-1,2,0)$, $e_2 = (-1,0,3)$:

$$e_1\times e_2 = \big(2\cdot3 - 0\cdot0,\ \ 0\cdot(-1) - (-1)\cdot3,\ \ (-1)\cdot0 - 2\cdot(-1)\big) = (6,\ 3,\ 2)$$

Confere: $(6,3,2)\cdot e_1 = -6+6+0 = 0$ e $(6,3,2)\cdot e_2 = -6+0+6=0$. $|N| = 7$, $\hat N = (6/7,\ 3/7,\ 2/7)$.

## @plano Equação do plano, distância e interseção reta-plano
termos: equação do plano, plano definido por três pontos, ax + by + cz + d = 0, distância de ponto a plano, interseção de reta com plano, projetar um ponto no plano ao longo de uma direção, direção de projeção

**Plano** com normal $N = (a,b,c)$ passando por $P_0$: $\ a x + b y + c z + d = 0$ com $d = -N\cdot P_0$.

Do exemplo do **→cross**: $6x + 3y + 2z + d = 0$ em $(1,0,0)$: $d = -6$, plano $6x+3y+2z = 6$.

**Distância** de $Q$ ao plano: $\ \dfrac{|aQ_x + bQ_y + cQ_z + d|}{\sqrt{a^2+b^2+c^2}}$. O sinal de $aQ_x+bQ_y+cQ_z+d$ diz de que lado do plano $Q$ está (é o teste da BSP e do backface).

**Projetar um ponto $D$ sobre o plano na direção $U$** (projeção paralela oblíqua de um ponto; também é a interseção de um raio com um plano no ray tracing):

$$P(t) = D + t\,U, \qquad N\cdot P(t) + d = 0 \ \Rightarrow\ t = -\frac{N\cdot D + d}{N\cdot U}$$

Se $N\cdot U = 0$ a direção é paralela ao plano (não intercepta).

**Exemplo**: plano por $A(4,0,0)$, $B(0,4,0)$, $C(0,0,4)$: normal $(1,1,1)$, plano $x+y+z = 4$. Projetar $D = (3,2,5)$ na direção $U = (-1,-1,-2)$:

$$P(t) = (3-t,\ 2-t,\ 5-2t),\quad (3-t)+(2-t)+(5-2t) = 4 \Rightarrow 10 - 4t = 4 \Rightarrow t = 1.5$$

$$P = (1.5,\ 0.5,\ 2) \quad\text{(confere: } 1.5+0.5+2 = 4\text{)}$$

Com frações: se aparecer denominador estranho (tipo /13), faça a conta com $t$ em fração e só no fim distribua; alternativas costumam diferir em uma coordenada só, então confira cada uma no plano (a soma/equação tem que bater).

## @dist Distância entre pontos, norma, normalizar
termos: distância entre dois pontos, sqrt, pow, norma, módulo, comprimento, normalizar vetor, vetor unitário, mouse sobre o objeto, pick, seleção

$$|P - Q| = \sqrt{(x_P - x_Q)^2 + (y_P - y_Q)^2\ [+ (z_P - z_Q)^2]}$$

Em C: `sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))`. Erros comuns: somar/subtrair as diferenças sem elevar ao quadrado, ou **subtrair** os quadrados.

Seleção (pick) de um objeto com o mouse: calcula a distância do clique até o centro (ou até o objeto) e seleciona se for menor que um raio/tolerância.

**Normalizar**: $\hat v = v/|v|$. Ex.: $v=(3,4,0)$, $|v|=5$, $\hat v = (0.6,\ 0.8,\ 0)$.

## @normesf Normal de superfícies: esfera, superfície paramétrica, normal de vértice
termos: normal de uma esfera, superfície paramétrica, derivadas parciais, p(u, v), n(u, v), normal no vértice, média das normais das faces, tonalizar poliedro

- **Esfera** de centro $C$ e raio $r$: a normal em $P$ é $\dfrac{P - C}{r}$. Centro na origem e raio 1: a normal **é o próprio ponto** $p$ (a menos de um fator).
- **Superfície paramétrica** $p(u,v)$: $\ n = \dfrac{\partial p}{\partial u}\times\dfrac{\partial p}{\partial v}$.

**Exemplo** (esfera unitária com a minha parametrização $p(a,b) = (\cos a\cos b,\ \cos a\,\mathrm{sen}\, b,\ \mathrm{sen}\, a)$, $a$ = latitude):

$$\frac{\partial p}{\partial a} = (-\mathrm{sen}\,a\cos b,\ -\mathrm{sen}\,a\,\mathrm{sen}\,b,\ \cos a) \qquad \frac{\partial p}{\partial b} = (-\cos a\,\mathrm{sen}\,b,\ \cos a\cos b,\ 0)$$

$$\frac{\partial p}{\partial b}\times\frac{\partial p}{\partial a} = \cos a\,(\cos a\cos b,\ \cos a\,\mathrm{sen}\,b,\ \mathrm{sen}\,a) = \cos(a)\;p(a,b)$$

Resultado: a normal é um **múltiplo do próprio ponto**, $n = \cos(\text{latitude})\cdot p$ (a outra ordem do produto dá $-\cos(a)\,p$, apontando para dentro). O fator $\cos$ da latitude zera nos polos. Então, numa questão desse tipo, a resposta é "cosseno do ângulo de latitude vezes $p$".

- **Normal de vértice** (para Gouraud/Phong): média das normais das faces que tocam o vértice, normalizada: $N_v = \dfrac{\sum N_i}{|\sum N_i|}$.

## @malha Malhas poligonais, B-rep, OBJ
termos: malha poligonal, mesh, malha de triângulos, representação por fronteira, B-rep, lista de vértices, lista de arestas, lista de faces, wireframe, arquivo OBJ, faces planares, winged-edge, Wavefront

**B-rep** (boundary representation): o sólido é representado pela sua **superfície** (fronteira): vértices, arestas, faces.

| estrutura | guarda | prós e contras |
|---|---|---|
| lista de vértices explícita por face | cada face com as coordenadas | simples, repete vértice, difícil achar vizinhos |
| lista de vértices + faces por índice | vértices uma vez; face = índices | sem repetição, mudar um vértice muda todas as faces (é o OBJ) |
| lista de arestas | arestas como pares de vértices, faces como lista de arestas | bom para wireframe (cada aresta desenhada uma vez) |
| winged-edge (aresta alada) | cada aresta aponta para 2 vértices, 2 faces e arestas vizinhas | consulta de vizinhança rápida, mais memória |

- Para construir: lista de **vértices**, lista de **arestas** (ligam vértices), e para cada **face** a lista dos seus pontos/arestas. A **normal da face** sai de 3 pontos com **produto vetorial** (não produto interno).
- **Malha de triângulos**: vantagem principal = toda face é **planar** garantido (3 pontos sempre definem um plano). Quadrilátero pode ficar torto. GPU só desenha triângulos.
- **Wavefront OBJ** (texto): `v x y z` (vértice), `vt u v` (coordenada de textura), `vn x y z` (normal), `f 1 2 3` ou `f 1/1/1 2/2/2 3/3/3` (face com índices **começando em 1**: v/vt/vn), `o`/`g` (objeto/grupo), `mtllib`/`usemtl` (material em `.mtl`: `Ka`, `Kd`, `Ks`, `Ns`, `map_Kd`), `l` (linha).

**Exemplo OBJ** (um quadrado com 2 triângulos):
```
v 0 0 0
v 1 0 0
v 1 1 0
v 0 1 0
f 1 2 3
f 1 3 4
```

**Outras representações de sólidos** (aparecem como alternativa): CSG (sólido = árvore de união/interseção/diferença de primitivas), enumeração espacial (voxels), octree (subdivisão recursiva em 8), varredura (sweep: extrusão/revolução), superfícies paramétricas (Bézier, B-spline).

# Parte 4. Projeções, câmera e pipeline 3D

## @projtipos Tipos de projeção (classificação)
termos: tipos de projeção, projeção paralela, projeção perspectiva, ortogonal, ortográfica, oblíqua, pictórica, axonométrica, isométrica, dimétrica, trimétrica, cavaleira, cavalier, cabinet, gabinete, multivistas, pontos de fuga, desenho técnico, engenharia

Projeção = levar o 3D para um plano (plano de projeção) usando **projetores** (raios).

```
Projeções geométricas planas
├── Paralela (projetores paralelos, centro de projeção no infinito)
│   ├── Ortogonal / Ortográfica (projetores perpendiculares ao plano)
│   │   ├── multivistas: frontal, topo, lateral (plano paralelo a uma face)
│   │   └── axonométricas: isométrica, dimétrica, trimétrica
│   └── Oblíqua / Pictórica (projetores inclinados em relação ao plano)
│       ├── cavaleira (cavalier)
│       └── cabinet (gabinete)
└── Perspectiva (projetores saem de um ponto: o centro de projeção / olho)
    └── 1, 2 ou 3 pontos de fuga
```

> [!warning] Classificação no material da disciplina
> O material da disciplina divide as paralelas em **ortogonais (ortográficas)** e **oblíquas (pictóricas)** e coloca a **isométrica** junto das oblíquas, como axonométrica (mantém as dimensões sobre os eixos, por isso é usada em desenho técnico e engenharia). Nos livros (Foley, Hearn) a axonométrica é **ortográfica** (projetores perpendiculares, plano inclinado em relação ao objeto). Na dúvida, siga o material da disciplina. A isométrica **nunca** é perspectiva.

**Axonométricas** (o plano de projeção não é paralelo a nenhuma face principal):

| tipo | eixos encurtados | ângulos entre os eixos projetados |
|---|---|---|
| isométrica | os 3 igualmente (fator ≈ 0,816) | 120°, 120°, 120° |
| dimétrica | 2 iguais | 2 ângulos iguais |
| trimétrica | os 3 diferentes | todos diferentes |

**Oblíquas**: a face paralela ao plano aparece em verdadeira grandeza; a profundidade vai num ângulo $\phi$ (normalmente 30° ou 45°) com fator $L$:

$$x_p = x + z\,L\cos\phi \qquad y_p = y + z\,L\,\mathrm{sen}\,\phi$$

| | fator $L$ da profundidade | ângulo dos projetores com o plano |
|---|---|---|
| **cavaleira** | $1$ (profundidade em verdadeira grandeza, parece esticada) | 45° |
| **cabinet** | $1/2$ (profundidade pela metade, parece mais real) | $\approx 63{,}4°$ ($\tan = 2$) |

**Perspectiva**: retas paralelas que **não** são paralelas ao plano convergem para um **ponto de fuga**. Quantos eixos principais cortam o plano = quantos pontos de fuga (1, 2 ou 3).

## @projprop Propriedades: paralela × perspectiva, volume de visão
termos: propriedades das transformações de projeção, tamanho aparente, distância ao plano de projeção, preserva paralelismo, preserva medidas, encurtamento perspectivo, volume de visualização, paralelepípedo, tronco de pirâmide, frustum, campo de visão, realismo, matriz 4x4 de projeção

| | paralela | perspectiva |
|---|---|---|
| projetores | paralelos entre si | partem de um ponto (centro de projeção) |
| tamanho aparente | **não varia** com a distância | **diminui** com a distância (encurtamento perspectivo) |
| retas paralelas | continuam paralelas | convergem (pontos de fuga), exceto as paralelas ao plano |
| medidas/ângulos | preservados nas faces paralelas ao plano (bom para engenharia) | não preservados |
| realismo | menor, objetos às vezes parecem distorcidos | maior (é como o olho vê) |
| **volume de visão** | **paralelepípedo** (caixa retangular) | **tronco de pirâmide** (frustum) |
| campo de visão | amplitude **não muda** com a distância | amplitude cresce com a distância (cortes da pirâmide) |
| matriz | $4\times4$ afim | $4\times4$ com última linha $\neq [0\ 0\ 0\ 1]$ (usa W) |

- **Volume de visão** (view volume) = região do universo que será **recortada e projetada**. Limitado lateralmente pela window e na frente/atrás pelos planos de recorte **frontal (near)** e **traseiro (far)**.
- Toda projeção usada em CG (paralela **e** perspectiva) é representável por matriz $4\times4$ em homogêneas. A perspectiva **não** preserva distâncias nem ângulos; o tamanho projetado é **inversamente** proporcional à distância.
- Paralela ortogonal no SGI: depois de levar tudo para o sistema da window (SCN) com o VPN alinhado ao $z$, **basta ignorar o z**. Na **perspectiva** ignorar o z **não** basta: tem que dividir por z.

## @projmat Matrizes de projeção (ortogonal, perspectiva) com exemplo
termos: matriz de projeção, projeção ortogonal matriz, projeção perspectiva matriz, centro de projeção, COP, distância focal, d, divisão perspectiva, x d / z, W = z/d

**Ortogonal no plano $z = 0$**: $(x,y,z)\to(x,y,0)$:

$$M_{ort} = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&0\\0&0&0&1\end{bmatrix}$$

**Perspectiva** com o centro de projeção na origem e plano de projeção em $z = d$ (semelhança de triângulos):

$$x_p = \frac{x\,d}{z} = \frac{x}{z/d} \qquad y_p = \frac{y\,d}{z} \qquad z_p = d$$

Vetor-coluna (em vetor-linha é a transposta, o $1/d$ vai para a última **coluna**, terceira linha):

$$M_{per} = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&1/d&0\end{bmatrix} \ \Rightarrow\ M_{per}\begin{bmatrix}x\\y\\z\\1\end{bmatrix} = \begin{bmatrix}x\\y\\z\\z/d\end{bmatrix} \xrightarrow{\ \div W\ } \left(\frac{x d}{z},\ \frac{y d}{z},\ d\right)$$

O $W$ deixa de ser 1: é a **divisão perspectiva** (divide por W) que faz o objeto longe ficar pequeno.

**Exemplo**: $d = 2$, ponto $(4,\ 2,\ 8)$: $W = 8/2 = 4$, projetado $= (1,\ 0.5,\ 2)$. O mesmo objeto com $z = 16$ ficaria metade do tamanho: $(0.5,\ 0.25)$.

Variante comum: centro de projeção em $z = -d$ e plano em $z=0$: $x_p = \dfrac{x}{1 + z/d}$, $y_p = \dfrac{y}{1+z/d}$.

**No SGI (perspectiva)**: translada o COP para a origem, gira o mundo para alinhar o VPN com o eixo $z$, aplica $x' = x\,d/z$, $y' = y\,d/z$, depois normaliza (SCN), recorta e manda para a viewport.

## @camera Transformação de câmera (de visualização): VRP, VPN, VUP, u v n
termos: transformação de câmera, câmera sintética, transformação de visualização, view transformation, posição e orientação do observador, VRP, VPN, VUP, PRP, COP, look-at, eye, sistema de referência da câmera, base u v w

A **câmera sintética** é definida por: posição (**VRP** / eye / COP), direção para onde olha (**VPN**, normal ao plano de visão, ou um ponto alvo), e o **VUP** (o "cima" da câmera). Mais a window no plano de visão e os planos near/far.

**Base da câmera** (com eye $E$ e alvo $A$):

$$n = \frac{E - A}{|E - A|} \qquad u = \frac{VUP \times n}{|VUP\times n|} \qquad v = n\times u$$

($u$ = direita, $v$ = cima, $n$ = para trás; a câmera olha para $-n$. O terceiro eixo sai com **produto vetorial**, **→cross**.)

**A transformação de câmera** leva as coordenadas do mundo (SRU) para o sistema da câmera. É uma **sequência de transformações geométricas** (translação + rotações) aplicada aos vértices da cena:

$$M_{cam} = R\cdot T(-E),\qquad R = \begin{bmatrix}u_x&u_y&u_z&0\\v_x&v_y&v_z&0\\n_x&n_y&n_z&0\\0&0&0&1\end{bmatrix}\ \text{(vetor-coluna)}$$

1. translada a câmera para a origem;
2. gira para alinhar $u, v, n$ com $x, y, z$.

> [!warning] Cuidado com a câmera
> - Quem leva o 3D para o 2D é a **projeção**, não a transformação de câmera.
> - A transformação de câmera é uma das **primeiras** etapas; as últimas são viewport e rasterização.
> - O eixo $n$ (ou $w$) sai da posição da câmera e do **ponto para onde ela olha**, não da origem do SRU (só coincide se ela olhar para a origem).
> - Depois dela as coordenadas ficam no **sistema** da câmera (posição **e** orientação, eixos $u,v,n$), não só relativas à posição do observador.

## @pipe3d Pipeline de visualização 3D: ordem das etapas
termos: pipeline de visualização, processo de síntese de imagens, etapas e suas funções, ordem das etapas, sequência do pipeline, transformação de modelagem, transformação de visualização, transformação normalizante, recorte 3D, mapeamento para coordenadas de tela, transformação de viewport, rasterização, visibilidade, síntese de imagem, rendering pipeline

**Ordem (a que cai)**:

| # | etapa | sai em |
|---|---|---|
| 1 | **transformação de modelagem** (objeto → mundo: posiciona/escala/gira cada objeto) | coordenadas do mundo (SRU) |
| 2 | **transformação de câmera / visualização** (mundo → câmera) | coordenadas da câmera |
| 3 | **projeção** (paralela ou perspectiva; define o volume de visão) | coordenadas de projeção / clip |
| 4 | **transformação normalizante e recorte** (volume de visão vira volume canônico, recorta 3D contra ele) | coordenadas normalizadas (SCN/NDC) |
| 5 | **transformação de viewport** (mapeamento para coordenadas de tela/dispositivo) | coordenadas de dispositivo |
| 6 | **rasterização** (vira pixels) + **visibilidade** (z-buffer) + tonalização | frame buffer |

Atenção, a ordem aparece em mais de uma forma, todas compatíveis com a tabela:

- "modelagem → câmera → projeção → normalização e recorte → viewport".
- "transformação de câmera → recorte 3D → projeção → mapeamento para coordenadas de tela" (aqui o recorte é contra o volume de visão, antes da divisão perspectiva achatar o z).
- "recorte → projeção → rasterização → visibilidade" (visibilidade por z-buffer acontece **por pixel**, junto/depois da rasterização).
- Etapas finais sempre: viewport e **rasterização**. A **primeira** é modelagem (ou câmera, se a questão não lista modelagem).

**Termo × função**:

| termo | função |
|---|---|
| projeção perspectiva | mapeia coordenadas do espaço 3D para um espaço 2D |
| volume de visualização | define a porção **visível** da cena |
| modelagem (transformação de modelagem) | posiciona os objetos na cena (objeto → mundo) |
| câmera / visualização | coloca a cena no referencial do observador |
| recorte | elimina o que está fora do volume de visão |
| rasterização | encontra os **pixels** (coordenadas de tela) que cada primitiva ocupa |
| z-buffer / visibilidade | decide qual superfície aparece em cada pixel |
| tonalização / iluminação | calcula a cor de cada vértice ou pixel |

## @canon Volume canônico e normalização
termos: volume canônico, transformação normalizante, NDC, coordenadas normalizadas de dispositivo, cubo [-1, 1], recorte 3D, near far, plano de recorte frontal, plano de recorte traseiro

- A **transformação normalizante** leva o volume de visão (caixa ou tronco de pirâmide) para um **volume canônico** (no OpenGL, o cubo $[-1,1]^3$; em alguns livros $[0,1]$ em z). Vantagem: o recorte 3D vira comparação com constantes, igual o SCN em 2D.
- Recorte 3D: Cohen-Sutherland com **6 bits** (esq, dir, baixo, cima, frente, trás) ou Liang-Barsky com 6 desigualdades.
- Na perspectiva, o tronco de pirâmide vira cubo: depois disso uma projeção paralela simples resolve.
- **Near e far**: o que está mais perto que o near ou mais longe que o far é recortado. A precisão do z-buffer depende da razão far/near (near muito perto da câmera = z-fighting).

# Parte 5. Curvas e superfícies

## @curvparam Curvas paramétricas: forma geral e matricial
termos: curva paramétrica, polinômio cúbico, cúbica paramétrica, matriz base, vetor geometria, blending functions, funções de mistura, funções de base, T M G, interpolação, aproximação

Curva cúbica paramétrica: $x(t) = a_xt^3 + b_xt^2 + c_xt + d_x$ (igual para $y$, $z$), $t \in [0,1]$. Forma matricial:

$$P(t) = T\cdot M\cdot G, \qquad T = [t^3\ \ t^2\ \ t\ \ 1]$$

$M$ = **matriz base** (define o tipo: Hermite, Bézier, B-spline), $G$ = **vetor geometria** (pontos/tangentes de controle). $T\cdot M$ = **funções de mistura (blending functions)**: dizem quanto cada elemento de $G$ pesa em cada $t$.

- **Interpola**: a curva passa pelos pontos de controle (Hermite, Catmull-Rom, spline natural).
- **Aproxima**: a curva só é "puxada" pelos pontos (Bézier passa só pelos extremos; B-spline não passa por nenhum, em geral).
- Por que cúbica: é o menor grau que permite continuidade $C^1$/$C^2$ e curvas espaciais não planas, sem as oscilações de grau alto.

## @hermite Hermite
termos: Hermite, tangentes nos extremos, R1 R4, vetores tangentes, matriz de Hermite, interpola extremos

Geometria: $G_H = [P_1\ \ P_4\ \ R_1\ \ R_4]^T$ (2 pontos extremos + 2 vetores tangente neles).

$$M_H = \begin{bmatrix}2&-2&1&1\\-3&3&-2&-1\\0&0&1&0\\1&0&0&0\end{bmatrix}$$

Funções de mistura: $H_1 = 2t^3 - 3t^2 + 1$, $H_2 = -2t^3+3t^2$, $H_3 = t^3 - 2t^2 + t$, $H_4 = t^3 - t^2$.

Relação com Bézier (mesma curva): $R_1 = 3(P_2 - P_1)$ e $R_4 = 3(P_4 - P_3)$, onde $P_1..P_4$ são os pontos de controle Bézier.

## @bezier Bézier: Bernstein, matriz, propriedades
termos: Bézier, Bezier, polinômios de Bernstein, funções de Bernstein, pontos de controle, fecho convexo, convex hull, controle global, grau n, interpola o primeiro e o último, matriz de Bézier

Com $n+1$ pontos de controle $P_0..P_n$ (grau $n$):

$$P(t) = \sum_{i=0}^{n}\binom{n}{i}(1-t)^{n-i}t^{i}\,P_i \qquad B_{i,n}(t) = \binom{n}{i}(1-t)^{n-i}t^i\ \ \text{(Bernstein)}$$

Cúbica ($n=3$, 4 pontos):

$$P(t) = (1-t)^3P_0 + 3t(1-t)^2P_1 + 3t^2(1-t)P_2 + t^3P_3 \qquad M_B = \begin{bmatrix}-1&3&-3&1\\3&-6&3&0\\-3&3&0&0\\1&0&0&0\end{bmatrix}$$

**Propriedades** (as que caem):
- passa pelo **primeiro e pelo último** ponto; os do meio só atraem;
- tangente no início na direção $P_0P_1$ e no fim na direção $P_2P_3$: $P'(0) = 3(P_1-P_0)$, $P'(1) = 3(P_3 - P_2)$;
- a curva fica dentro do **fecho convexo** (convex hull) dos pontos de controle;
- **controle global**: mexer um ponto muda a curva inteira (todo $B_i(t) > 0$ para $0<t<1$);
- grau = nº de pontos − 1 (muitos pontos = grau alto, por isso se emendam várias cúbicas);
- as funções de Bernstein somam 1 em todo $t$ (invariância afim: transformar os pontos de controle = transformar a curva).

**Exemplo cúbica** $P_0=(0,0)$, $P_1=(2,4)$, $P_2=(6,4)$, $P_3=(8,0)$, $t=0.5$: pesos $\frac18, \frac38, \frac38, \frac18$:

$$P(0.5) = \tfrac18(0,0) + \tfrac38(2,4) + \tfrac38(6,4) + \tfrac18(8,0) = (0.75 + 2.25 + 1,\ 1.5+1.5) = (4,\ 3)$$

**Exemplo grau 2** (3 pontos) $P_0=(0,0)$, $P_1=(2,4)$, $P_2=(4,0)$: $P(t) = (1-t)^2P_0 + 2t(1-t)P_1 + t^2P_2$. Em $t = 0.5$: $0.25(0,0) + 0.5(2,4) + 0.25(4,0) = (2,\ 2)$.

## @casteljau Algoritmo de de Casteljau
termos: de Casteljau, interpolação linear repetida, subdivisão da curva, lerp, construção geométrica

Calcula um ponto da Bézier (e divide a curva em duas) só com interpolação linear: em cada nível, troca cada par de pontos vizinhos por $(1-t)P_i + tP_{i+1}$, até sobrar 1 ponto.

Exemplo, mesmos pontos, $t = 0.5$ (média de vizinhos):

$$\begin{aligned}
&\text{nível 1: } (1,2),\ (4,4),\ (7,2)\\
&\text{nível 2: } (2.5,3),\ (5.5,3)\\
&\text{nível 3: } (4,3) = P(0.5)
\end{aligned}$$

Os pontos $(0,0),(1,2),(2.5,3),(4,3)$ são os controles da metade esquerda e $(4,3),(5.5,3),(7,2),(8,0)$ os da direita (subdivisão). Numericamente estável; usado para desenhar subdividindo até ficar "reto".

## @continuidade Continuidade entre segmentos (G0, G1, C0, C1, C2)
termos: continuidade, G0, G1, C0, C1, C2, paramétrica, geométrica, emendar curvas, colineares, tangente igual, derivada igual

| tipo | condição | Bézier $P$ emendada com $Q$ |
|---|---|---|
| $G^0 = C^0$ | as pontas se encontram | $P_3 = Q_0$ |
| $G^1$ | tangentes na **mesma direção** (módulos podem diferir) | $P_2,\ P_3 = Q_0,\ Q_1$ **colineares** |
| $C^1$ | tangentes **iguais** (direção e módulo) | $P_3 - P_2 = Q_1 - Q_0$ ($P_3$ é o ponto médio de $P_2Q_1$) |
| $C^2$ | segunda derivada igual também | B-spline cúbica uniforme tem $C^2$ automático |

$C^1$ implica $G^1$ (se a tangente não for nula), não o contrário. Paramétrica (C) olha as derivadas; geométrica (G) só a forma.

## @bspline B-spline cúbica uniforme
termos: B-spline, bspline, controle local, não interpola, C2, 4 pontos por segmento, matriz B-spline, nós, NURBS, Catmull-Rom

$$M_{BS} = \frac{1}{6}\begin{bmatrix}-1&3&-3&1\\3&-6&3&0\\-3&0&3&0\\1&4&1&0\end{bmatrix} \qquad \text{segmento } i: G = [P_{i-3}\ P_{i-2}\ P_{i-1}\ P_i]^T$$

- Cada segmento usa **4 pontos consecutivos**; com $m+1$ pontos ($P_0..P_m$) dá $m-2$ segmentos. Ex.: 6 pontos → 3 segmentos.
- **Controle local**: um ponto só afeta 4 segmentos vizinhos.
- Continuidade $C^2$ entre segmentos (automática, Bézier não tem).
- **Não passa** pelos pontos de controle (aproxima). Fica no fecho convexo de cada 4 pontos.
- Início do segmento: $P(0) = \frac{P_{i-3} + 4P_{i-2} + P_{i-1}}{6}$.
- **NURBS**: B-spline **N**ão-**U**niforme **R**acional: nós não uniformes e pesos; representa cônicas (círculo) exatamente; invariante a projeção perspectiva.
- **Catmull-Rom**: spline que **interpola** os pontos, $C^1$.

## @fwddiff Forward differences (diferenças adiante)
termos: forward differences, diferenças adiante, diferenças progressivas, E(δ), delta, incremental, somas em vez de multiplicações, DesenhaCurvaFwdDiff, erro de ponto flutuante

Calcular a cúbica em passos de $\delta$ só com **somas** (sem multiplicar a cada ponto). Para $f(t) = at^3+bt^2+ct+d$:

$$f_0 = d \quad \Delta f_0 = a\delta^3 + b\delta^2 + c\delta \quad \Delta^2 f_0 = 6a\delta^3 + 2b\delta^2 \quad \Delta^3 f_0 = 6a\delta^3$$

Em matriz: $[f_0\ \Delta f_0\ \Delta^2f_0\ \Delta^3f_0]^T = E(\delta)\cdot C$, com $C = M\cdot G = [a\ b\ c\ d]^T$:

$$E(\delta) = \begin{bmatrix}0&0&0&1\\\delta^3&\delta^2&\delta&0\\6\delta^3&2\delta^2&0&0\\6\delta^3&0&0&0\end{bmatrix}$$

```
para i = 1..n   (n = 1/δ passos)
  x   += Δx ;   Δx  += Δ²x ;   Δ²x += Δ³x      (idem y, z)
  desenha reta do ponto anterior até (x, y)
```

**Exemplo**: $f(t) = t^3$ ($a=1$), $\delta = 0.5$: $f_0 = 0$, $\Delta = 0.125$, $\Delta^2 = 0.75$, $\Delta^3 = 0.75$. Passo 1: $f = 0.125$ ($=0.5^3$ ✓), $\Delta = 0.875$, $\Delta^2 = 1.5$. Passo 2: $f = 1$ ($=1^3$ ✓).

Desvantagem: o erro de ponto flutuante **acumula** a cada soma (com $\delta$ muito pequeno a curva desvia no fim).

## @superf Superfícies bicúbicas (Bézier, B-spline, Hermite)
termos: superfície de Bézier, superfície bicúbica, retalho, patch, 16 pontos de controle, funções de Bernstein nas direções s e t, superfície B-spline, superfície de Hermite, twist, produto tensorial, malha de controle

Superfície = curva cujos pontos de controle andam numa segunda curva (**produto tensorial**). Parâmetros $s, t \in [0,1]$:

$$P(s,t) = \sum_{i=0}^{3}\sum_{j=0}^{3} B_i(s)\,B_j(t)\,P_{ij} \qquad\text{ou}\qquad P(s,t) = S\cdot M\cdot G\cdot M^T\cdot T^T$$

com $S = [s^3\ s^2\ s\ 1]$, $T = [t^3\ t^2\ t\ 1]$ e $G$ uma matriz $4\times4$ de pontos (uma para x, uma para y, uma para z).

| superfície | reconhece por | detalhes |
|---|---|---|
| **Bézier** | funções de **Bernstein** em $s$ e em $t$, 16 pontos | passa pelos **4 cantos**; bordas são curvas de Bézier |
| **B-spline** | matriz $M_{BS}$, controle local | não passa pelos pontos; $C^2$ entre retalhos |
| **Hermite** | cantos + tangentes em $s$ e $t$ + **vetores twist** ($\partial^2P/\partial s\partial t$) | interpola os cantos |

- Desenhar: fixa $s$ e varia $t$ (e vice-versa), desenhando uma família de curvas em cada direção (wireframe), ou subdivide em triângulos.
- Com forward differences, usa $DD_x = E(\delta_s)\,C_x\,E(\delta_t)^T$ e anda nas duas direções.
- Retalhos são emendados com as mesmas regras de continuidade das curvas.

# Parte 6. Rasterização, preenchimento, aliasing e texturas

## @rastconc Rasterização: o que é
termos: rasterização, conversão por varredura, scan conversion, discretização, encontrar os pixels, coordenadas de pixel na tela, primitiva vira pixels, fragmentos

**Rasterização** = descobrir **quais pixels** cada primitiva (ponto, reta, triângulo) ocupa na tela e gerar um fragmento para cada um (com cor, profundidade, coordenada de textura interpoladas). É a etapa que vem depois da viewport no pipeline. Os algoritmos clássicos trabalham **incrementalmente** (o pixel seguinte sai do anterior com somas), e o Bresenham faz isso só com **inteiros**.

## @dda DDA (Digital Differential Analyzer) para retas
termos: DDA, analisador diferencial digital, código C com putpixel, desenhar pixel a pixel, modo gráfico, reconhecer o que um código desenha, incremento, xinc, yinc, steps, arredondamento, round, ponto flutuante, putpixel em laço

```c
void dda(int x1, int y1, int x2, int y2, int cor) {
    int dx = x2 - x1, dy = y2 - y1;
    int passos = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    float xinc = dx / (float) passos, yinc = dy / (float) passos;
    float x = x1, y = y1;
    putpixel(round(x), round(y), cor);
    for (int k = 0; k < passos; k++) {
        x += xinc; y += yinc;
        putpixel(round(x), round(y), cor);
    }
}
```

- Anda 1 pixel no eixo que **varia mais** e soma a fração no outro. Usa **ponto flutuante** e arredondamento a cada pixel (mais lento que Bresenham, e o erro acumula em retas longas).
- **Reconhecer código**: um único laço, um `putpixel` por iteração, `x += algo; y += algo` constantes → é uma **reta**. Com `abs(dx) > abs(dy)` escolhendo o número de passos é DDA.

**Exemplo**: $(2,1)$ a $(8,4)$: $dx = 6$, $dy=3$, 6 passos, $x_{inc} = 1$, $y_{inc} = 0.5$. Pontos: $(2,1),(3,1.5\to2),(4,2),(5,2.5\to3),(6,3),(7,3.5\to4),(8,4)$ (arredondando .5 para cima).

## @bres Bresenham para retas (só inteiros)
termos: Bresenham, ponto médio para retas, parâmetro de decisão, p0 = 2dy - dx, aritmética inteira, erro, rasterização de linhas, algoritmo de linhas

Para $0 \le m \le 1$ (os outros octantes por simetria/troca de eixos), $\Delta x = x_2-x_1$, $\Delta y = y_2-y_1$:

$$p_0 = 2\Delta y - \Delta x$$

$$\text{se } p_k < 0:\ (x_k+1,\ y_k),\ \ p_{k+1} = p_k + 2\Delta y \qquad \text{se } p_k \ge 0:\ (x_k+1,\ y_k+1),\ \ p_{k+1} = p_k + 2\Delta y - 2\Delta x$$

$p_k$ é (proporcional a) a diferença entre as distâncias do pixel de baixo e do de cima até a reta verdadeira: diz qual dos dois está mais perto. Tudo com **soma de inteiros**.

**Exemplo** $(0,0)$ a $(6,4)$: $\Delta x=6$, $\Delta y=4$, $2\Delta y = 8$, $2\Delta y-2\Delta x = -4$, $p_0 = 2$.

| k | $p_k$ | próximo pixel |
|---|---|---|
| 0 | 2 (≥0) | (1,1) |
| 1 | 2−4 = −2 (<0) | (2,1) |
| 2 | −2+8 = 6 | (3,2) |
| 3 | 6−4 = 2 | (4,3) |
| 4 | 2−4 = −2 | (5,3) |
| 5 | −2+8 = 6 | (6,4) |

Confere com $y = \tfrac{2}{3}x$ arredondado: 0, 0.67→1, 1.33→1, 2, 2.67→3, 3.33→3, 4.

```c
void bresenham(int x1, int y1, int x2, int y2, int cor) {   // 0 <= m <= 1, x1 < x2
    int dx = x2 - x1, dy = y2 - y1, p = 2*dy - dx, y = y1;
    for (int x = x1; x <= x2; x++) {
        putpixel(x, y, cor);
        if (p >= 0) { y++; p += 2*dy - 2*dx; } else p += 2*dy;
    }
}
```

## @circ Círculo pelo ponto médio (e elipse)
termos: círculo, circunferência, algoritmo do ponto médio para círculos, simetria de 8, oito octantes, f(x,y) = x² + y² - r², interior, exterior, p0 = 1 - r, elipse, simetria de 4

$f(x,y) = x^2 + y^2 - r^2$: **$< 0$ dentro**, $= 0$ na circunferência, **$>0$ fora**. Calcula só um octante (de $(0,r)$ até $x \ge y$) e espelha nos 8 (simetria de 8 pontos).

> [!warning] Sinal invertido
> Se escreverem $f = r^2 - x^2 - y^2$, o sinal vira: aí $f<0$ significa **fora** e $f>0$ significa dentro.

$$p_0 = 1 - r \qquad p<0:\ (x+1,\ y),\ p \mathrel{+}= 2x_{novo} + 1 \qquad p \ge 0:\ (x+1,\ y-1),\ p \mathrel{+}= 2x_{novo} + 1 - 2y_{novo}$$

**Exemplo** $r = 5$: $(0,5)$, $p_0 = -4$ → $(1,5)$, $p = -4+3 = -1$ → $(2,5)$, $p = -1+5 = 4$ → $(3,4)$, $p = 4 + 7 - 8 = 3$ → $(4,3)$ já passou de $x\ge y$, para. Octante: $(0,5),(1,5),(2,5),(3,4)$; o resto por simetria.

**Reconhecer código**: círculo tem **8 `putpixel`** por iteração com $(\pm x, \pm y)$ e $(\pm y, \pm x)$. **Elipse** tem **4** (simetria só nos quadrantes) e duas regiões (antes e depois da inclinação −1). Retângulo = 4 laços retos. Reta = 1 `putpixel` por iteração.

```c
void circulo(int xc, int yc, int r, int cor) {
    int x = 0, y = r, p = 1 - r;
    while (x <= y) {
        putpixel(xc+x, yc+y, cor); putpixel(xc-x, yc+y, cor);
        putpixel(xc+x, yc-y, cor); putpixel(xc-x, yc-y, cor);
        putpixel(xc+y, yc+x, cor); putpixel(xc-y, yc+x, cor);
        putpixel(xc+y, yc-x, cor); putpixel(xc-y, yc-x, cor);
        x++;
        if (p < 0) p += 2*x + 1; else { y--; p += 2*x + 1 - 2*y; }
    }
}
```

## @fill Preenchimento: scanline de polígonos, flood fill, boundary fill
termos: preenchimento, scanline, varredura, tabela de arestas, lista de arestas ativas, par-ímpar, regra do número de voltas, flood fill, boundary fill, boundary-fill, vizinhança 4, vizinhança 8, 4-conectado, 8-conectado, semente, seed

**Scanline (polígono definido por vértices)**: para cada linha $y$ da tela: acha as interseções da linha com as arestas, **ordena** por $x$ e pinta entre os pares (1º–2º, 3º–4º...). Usa a **tabela de arestas** (ET, arestas ordenadas por $y_{min}$) e a **lista de arestas ativas** (AET); de uma linha para outra o $x$ da interseção anda $1/m$ (coerência). Vértice que é máximo ou mínimo local conta duas vezes; vértice "de passagem" conta uma.

**Teste dentro/fora**: **par-ímpar** (raio a partir do ponto cruza um número ímpar de arestas → dentro) ou **número de voltas (winding, não-zero)** (difere em polígonos que se cruzam).

**Por semente (região definida por pixels)**, começa de um pixel interno e espalha recursivamente:

| | para quando | troca |
|---|---|---|
| **boundary fill** | encontra a **cor da borda** | pinta tudo até a borda |
| **flood fill** | o pixel **não tem a cor interior antiga** | troca a cor interior por outra (ex. balde de tinta) |

- **Vizinhança 4** (cima, baixo, esq., dir.): não atravessa diagonais. Uma região interna ligada só pela diagonal **não é preenchida** inteira. Borda mais grossa (ex. 2 pixels) **não** garante nada sobre isso.
- **Vizinhança 8** (inclui diagonais): preenche tudo, mas **vaza** por borda 4-conectada (fresta na diagonal). Regra: região 8-conectada pede borda 4-conectada e vice-versa.
- Recursivo direto estoura a pilha; a versão boa preenche **spans** (trechos horizontais) de cada vez.

## @alias Aliasing (serrilhado) e anti-aliasing (SSAA, MSAA, FXAA)
termos: aliasing, serrilhado, jaggies, escada, anti-aliasing, antisserrilhado, superamostragem, supersampling, SSAA, MSAA, multi sampling, amostras, Nyquist, subamostragem, área, FXAA, TAA, moiré

**Aliasing** = artefato de **subamostragem**: a tela tem resolução finita e a cena tem frequências (bordas) mais altas que a metade da taxa de amostragem (**Nyquist**: tem que amostrar a pelo menos o **dobro** da maior frequência). Aparece como: bordas em **escada** (jaggies) em retas e **triângulos** (malha 2D também serrilha), **moiré** em texturas, objetos pequenos que somem/piscam, roda girando ao contrário (aliasing temporal).

| técnica | como faz | custo |
|---|---|---|
| **SSAA** (superamostragem) | renderiza em resolução maior (ex. 4 amostras por pixel) e faz a média | caro: tonaliza **todas** as amostras |
| **MSAA** (multisample) | testa **cobertura e profundidade** em várias amostras por pixel, mas calcula a **cor/tonalização uma vez por pixel** e **reaproveita** para as amostras cobertas | mais barato; age nas **bordas** das primitivas |
| amostragem por área (área ponderada/não ponderada) | intensidade proporcional à fração do pixel coberta pela primitiva | (reta com "espessura") |
| **FXAA / SMAA** | pós-processamento: detecta bordas na imagem pronta e borra | baratíssimo, borra um pouco |
| **TAA** (temporal) | mistura amostras de quadros anteriores com jitter | barato, pode dar rastro |
| mipmap / filtragem de textura | aliasing **de textura** (minificação) | ver **→mipmap** |

> [!warning] Sobre MSAA
> - É feito **numa passada** de rasterização (não precisa de duas).
> - Não exige ordenar as primitivas (isso é o pintor).
> - As amostras **não** precisam estar em grade regular; padrões rotacionados/esparsos funcionam melhor.
> - O que define a técnica: a informação calculada para uma amostra (iluminação/cor) é **reutilizada** pelas outras do mesmo pixel.

## @textura Mapeamento de textura: coordenadas, filtragem, perspectiva
termos: mapeamento de textura, texture mapping, texel, coordenadas de textura, (u, v), (s, t), UV, magnificação, minificação, vizinho mais próximo, nearest, bilinear, trilinear, anisotrópica, correção perspectiva, wrap, repeat, clamp

- Cada vértice recebe coordenadas $(u,v) \in [0,1]^2$ na imagem da textura; na rasterização o $(u,v)$ é **interpolado** para cada pixel e busca o **texel** (pixel da textura) correspondente.
- **Correção perspectiva**: interpolar $u,v$ linearmente na tela deforma a textura em perspectiva; o certo é interpolar $u/w$, $v/w$ e $1/w$ e dividir no pixel.
- **Magnificação** (texel maior que pixel, textura esticada): **vizinho mais próximo** (fica quadriculado) ou **bilinear** (média ponderada dos 4 texels vizinhos, fica borrado suave).
- **Minificação** (vários texels num pixel, textura longe): dá aliasing/moiré → **mipmap** (**→mipmap**).
- **Trilinear** = bilinear em dois níveis de mipmap vizinhos + interpolação entre eles. **Anisotrópica** = várias amostras ao longo da direção em que a textura está esticada (chão em ângulo raso).
- Fora de $[0,1]$: **repeat** (ladrilha), **clamp** (repete a borda), **mirror**.

**Exemplo bilinear**: texels vizinhos $a=10$ (esq. baixo), $b=30$ (dir. baixo), $c=50$ (esq. cima), $d=70$ (dir. cima), posição fracionária $(0.25,\ 0.5)$:

$$\text{baixo} = 10 + 0.25(30-10) = 15 \quad \text{cima} = 50 + 0.25(70-50) = 55 \quad \text{valor} = 15 + 0.5(55-15) = 35$$

## @mipmap Mipmap e o custo de memória (1/3)
termos: mipmap, MIP map, pirâmide de texturas, níveis de detalhe, LOD, memória extra do mipmap, um terço a mais, multum in parvo, minificação

**Mipmap** (*multum in parvo*, Williams 1983): guarda a textura em vários níveis, cada um com **metade da largura e metade da altura** do anterior (1/4 dos texels), até $1\times1$. Na renderização escolhe o nível em que 1 texel ≈ 1 pixel: menos aliasing na minificação e mais rápido (menos cache miss).

**Memória extra**: o nível 1 tem $1/4$, o 2 tem $1/16$...

$$\frac14 + \frac1{16} + \frac1{64} + \dots = \frac{1/4}{1 - 1/4} = \frac13 \approx 33\%\ \text{a mais que a textura original}$$

(total = $4/3$ da original). **Exemplo**: textura $1024\times1024$ RGBA (4 bytes) = 4 MB; com mipmap ≈ 5,33 MB.

## @bump Bump, normal, displacement, environment e outras texturas
termos: bump mapping, perturbação da normal, normal map, displacement mapping, environment mapping, mapeamento de ambiente, reflection mapping, cube map, textura procedural, textura sólida, textura 3D, light map, shadow map, alpha map, opacidade

| técnica | o que faz | detalhe que cai |
|---|---|---|
| **bump mapping** (Blinn 1978) | aplica uma **função de perturbação no vetor normal** (a partir de um mapa de alturas) e com isso muda a **iluminação** | a geometria **não muda**: a silhueta continua lisa |
| **normal mapping** | a textura guarda a própria normal (RGB = xyz) | versão moderna do bump |
| **displacement mapping** | **move os vértices** de verdade conforme o mapa de altura | muda a silhueta; precisa de malha densa/tesselação |
| **environment / reflection mapping** | reflexo do ambiente via textura (cube map de 6 faces ou sphere map), indexada pelo vetor refletido | reflexo "falso", barato, sem ray tracing |
| **textura procedural** | a cor vem de uma **função** (ex. ruído de Perlin, xadrez) e não de uma imagem | resolução infinita, pouca memória |
| **textura sólida (3D)** | função ou volume indexado por $(x,y,z)$, o objeto é "esculpido" dentro dela | madeira, mármore: os veios continuam através do objeto |
| **light map** | iluminação pré-calculada guardada em textura | jogos, cena estática |
| **shadow map** | profundidade vista da luz; ponto mais longe que o guardado está na sombra | sombra em tempo real |
| **alpha / opacity map** | transparência por texel | folhas, grades |

# Parte 7. Visibilidade (superfícies ocultas)

## @visconc Remoção de superfícies ocultas: classificação
termos: remoção de superfícies ocultas, oclusão, objeto encoberto por outro, cena com vários objetos no volume de visualização, objetos escondidos atrás de outros dentro do volume de visão, superfícies visíveis, hidden surface removal, visible surface determination, espaço do objeto, espaço da imagem, precisão de objeto, precisão de imagem, determinação de visibilidade

Problema: com vários objetos dentro do volume de visão, decidir **o que fica na frente** em cada pixel. Mesmo com tudo dentro do volume de visão o problema existe (estar dentro do volume não quer dizer estar visível).

| classe | trabalha | exemplos |
|---|---|---|
| **espaço do objeto** (precisão de objeto) | compara objetos/polígonos entre si | backface culling, pintor (parte), BSP |
| **espaço da imagem** (precisão de imagem) | decide pixel a pixel | **z-buffer**, scanline, Warnock, ray casting |

## @backface Backface culling (remoção de faces traseiras)
termos: backface culling, faces traseiras, back faces, faces posteriores, normal apontando para longe, produto escalar normal e vista, objeto convexo, ordem dos vértices

Face cuja **normal aponta para longe do observador** não pode ser vista (num objeto fechado). Teste com $V$ = vetor do ponto da face até o observador:

$$N\cdot V \le 0 \Rightarrow \text{face traseira (descarta)} \qquad N\cdot V > 0 \Rightarrow \text{pode ser visível}$$

No sistema da câmera olhando para $-z$, basta olhar o sinal de $N_z$. Na tela, dá para usar a **ordem dos vértices**: anti-horária = de frente, horária = de costas (é o `glCullFace`).

- Remove em média **metade** das faces, barato, por isso é o primeiro passo.
- Para **um único objeto convexo** ele resolve a visibilidade sozinho. Com **vários** objetos (mesmo todos convexos) um pode esconder o outro, então **não basta**: precisa de z-buffer/pintor. Em objeto côncavo também não basta (uma face de frente pode esconder outra de frente).

**Exemplo**: face com normal $N = (0,0.6,0.8)$, observador na direção $V = (0,0,1)$: $N\cdot V = 0.8 > 0$, visível. Com $N = (0,0.6,-0.8)$: $-0.8$, descarta.

## @zbuf Z-buffer (buffer de profundidade)
termos: z-buffer, zbuffer, oclusão, objeto encoberto, objeto na frente de outro, qualquer ordem de rasterização dá a mesma imagem, buffer de profundidade, depth buffer, Catmull 1974, profundidade de cada pixel, teste de profundidade, incremental, não precisa ordenar, mesma resolução do frame buffer, z-fighting

```
para cada pixel (x,y): zbuf[x][y] = +infinito (o mais longe); cor[x][y] = fundo
para cada polígono (em QUALQUER ordem):
  para cada pixel (x,y) coberto pelo polígono:
    z = profundidade do polígono em (x,y)
    se z < zbuf[x][y]:          (mais perto)
        zbuf[x][y] = z
        cor[x][y]  = cor do polígono em (x,y)
```

- **Não precisa ordenar** as primitivas; o resultado é **o mesmo em qualquer ordem** de rasterização (exceto empate exato e transparência).
- Tem **o mesmo tamanho (resolução) do frame buffer**: um valor de profundidade por pixel.
- O $z$ é calculado **incrementalmente**: no plano $Ax + By + Cz + D = 0$, $z = \dfrac{-Ax - By - D}{C}$; andando um pixel em $x$: $z_{x+1} = z_x - \dfrac{A}{C}$; descendo uma linha: $z - \dfrac{B}{C}$.
- Prós: simples, em hardware em toda GPU, qualquer tipo de primitiva. Contras: memória extra, **z-fighting** (precisão limitada, near muito perto), **transparência** precisa de ordenar mesmo assim, desenha pixels que depois são cobertos (overdraw).
- Não é técnica de detecção de colisão e não faz sombra.

**Exemplo incremental**: plano $2x + y + 4z - 20 = 0$. Em $(1,2)$: $z = (20 - 2 - 2)/4 = 4$. Próximo pixel $(2,2)$: $4 - \tfrac{2}{4} = 3.5$ (confere: $(20-4-2)/4 = 3.5$).

## @pintor Algoritmo do pintor (ordenação por profundidade)
termos: algoritmo do pintor, painter, ordenação por profundidade, depth sort, de trás para frente, Newell, sobreposição cíclica, polígonos que se interpenetram, dividir polígonos

1. **Ordena** os polígonos pela profundidade (do mais **longe** para o mais **perto**).
2. Desenha nessa ordem: o que vem depois pinta por cima (como um pintor fazendo fundo antes).

- Problemas: **sobreposição cíclica** (A na frente de B, B de C, C de A) e polígonos que **se atravessam**: nenhuma ordem serve, tem que **dividir** polígonos. O algoritmo de Newell-Newell-Sancha faz os testes (extensões em z, x, y, lados dos planos) e divide quando precisa.
- Desenha tudo, até o que fica escondido (overdraw). Bom para transparência (desenha de trás para frente).

## @arvbsp Árvore BSP (Binary Space Partitioning)
termos: BSP, binary space partitioning, partição binária do espaço, subdivisão espacial, árvore, plano divisor, frente e trás, cena estática, percurso, Doom

Pré-processamento: escolhe um polígono, o plano dele divide o espaço em **frente** e **trás**; os outros polígonos vão para um dos lados (os que cruzam o plano são **divididos**); repete recursivamente → árvore binária.

Na hora de desenhar (pintor sem ordenar): para cada nó, vê de que lado do plano está o **observador**:
```
desenha(no):
  se observador está na FRENTE do plano do no:
      desenha(no.tras); desenha o polígono do no; desenha(no.frente)
  senão:
      desenha(no.frente); desenha o polígono do no; desenha(no.tras)
```
Isso dá a ordem **de trás para frente** para **qualquer** posição da câmera, sem reordenar.

- A árvore depende só da geometria, **não da câmera**: ótima para **cenas estáticas** com câmera andando (Doom, Quake). Mudou a geometria, reconstrói.
- Também usada para colisão e ray tracing (é uma **subdivisão espacial**).

## @warnock Scanline, Warnock e ray casting para visibilidade
termos: scanline visibilidade, coerência, Warnock, subdivisão de área, quadtree, área homogênea, ray casting visibilidade, A-buffer, octree

- **Scanline (visibilidade)**: processa linha a linha da tela com a lista de arestas ativas; em cada trecho (span) entre arestas, compara as profundidades só dos polígonos ativos. Usa **coerência** (de um pixel para o seguinte quase nada muda).
- **Warnock (subdivisão de área)**: olha uma região da tela; se é "simples" (vazia, um polígono só cobrindo tudo, ou um polígono claramente na frente) desenha; senão **divide em 4** (quadtree) e repete até o tamanho de um pixel.
- **Ray casting**: um raio do olho por pixel; o primeiro objeto atingido é o visível (é a parte de visibilidade do ray tracing).
- **A-buffer**: z-buffer que guarda uma lista de fragmentos por pixel (transparência e anti-aliasing).
- **Octree / BSP / BVH**: estruturas de subdivisão espacial que aceleram visibilidade, colisão e ray tracing.

# Parte 8. Iluminação e tonalização (shading)

## @luzes Fontes de luz: ambiente, direcional, pontual, spot, extensa
termos: fonte de luz, luz direcional, fonte no infinito, sol, raios paralelos, luz pontual, puntual, spot, holofote, cone, luz ambiente, fonte extensa, luz de área, penumbra, atenuação

| fonte | definida por | como ilumina |
|---|---|---|
| **ambiente** | só intensidade $I_a$ | igual em tudo, sem direção (aproxima as múltiplas reflexões da cena) |
| **direcional** | só uma **direção** | fonte a **distância infinita** (tipo o **Sol**): raios paralelos, $L$ é o mesmo em todo ponto, sem atenuação |
| **pontual** | uma **posição** | irradia para todos os lados (lâmpada); $L$ muda de ponto a ponto; atenua com a distância |
| **spot** (holofote) | posição + direção + ângulo de abertura (+ expoente de queda) | só dentro de um **cone** |
| **extensa / de área** | uma superfície que emite | gera sombra com **penumbra** (sombra suave); pontual/direcional dão sombra dura |

**Atenuação** (pontual/spot): $f(d) = \dfrac{1}{a + b\,d + c\,d^2}$ (física seria $1/d^2$, mas fica escuro rápido demais; as constantes ajustam).

## @phong Modelo de iluminação de Phong (ambiente + difusa + especular)
termos: modelo de Phong, modelo de iluminação, modelo de iluminação local, cor de um ponto a partir do material, da geometria e da luz, três componentes aditivas, luz ambiente, luz difusa, luz direta, luz especular, coeficientes ka kd ks, expoente de brilho, n, shininess, Bui Tuong Phong 1975, iluminação local

O modelo de iluminação de Phong (1975) é **local** e soma **3 componentes** (aditivas):

$$I = \underbrace{I_a\,k_a}_{\text{ambiente}} + f(d)\,I_l\Big[\underbrace{k_d\,(N\cdot L)}_{\text{difusa}} + \underbrace{k_s\,(R\cdot V)^{n}}_{\text{especular}}\Big]$$

| componente | outro nome | depende de | não depende de |
|---|---|---|---|
| ambiente ($k_a$) | luz indireta | nada (constante) | posição da luz, do observador, normal |
| **difusa** ($k_d$) | luz **direta**, lambertiana | ângulo entre **$N$ e $L$** | **posição do observador** |
| **especular** ($k_s$, $n$) | brilho, reflexo | ângulo entre **$R$ e $V$** (observador!) | |

- $N$ normal, $L$ direção **para a luz**, $V$ direção **para o observador**, $R$ = reflexo de $L$ em $N$: $\ R = 2(N\cdot L)\,N - L$. Todos **unitários**.
- $k_a, k_d, k_s \in [0,1]$ = propriedades do **material**. $n$ = expoente de brilho: grande (100+) = brilho pequeno e forte (metal, plástico polido); pequeno (1–10) = brilho espalhado.
- Se $N\cdot L < 0$ a luz está atrás: difusa e especular = 0.
- Com cor: faz a conta **por canal** (R, G, B), cada um com seu $k_d$; a especular costuma usar a cor da luz (brilho branco).
- Várias luzes: soma a parte entre colchetes para cada luz.
- É **local**: a cor de um objeto **não depende dos outros objetos** (nada de sombra, reflexo de outro objeto ou cor de outro objeto). Sombras e inter-reflexões precisam de técnicas globais (**→raytrace**, **→radios**).

> [!warning] Quantas componentes
> São **3**, **somadas**: ambiente (indireta), difusa (direta) e especular. Difusa e direta são a **mesma** componente; transparência não faz parte do modelo; não são 4 nem multiplicativas.

**Exemplo**: $N = (0,0,1)$, $L = (0,\ 0.6,\ 0.8)$, $V = (0,0,1)$, $I_a = 0.2$, $I_l = 1$, $k_a = 0.5$, $k_d = 0.7$, $k_s = 0.4$, $n = 10$, sem atenuação.

$$N\cdot L = 0.8 \qquad R = 2(0.8)(0,0,1) - (0,0.6,0.8) = (0,\ -0.6,\ 0.8) \qquad R\cdot V = 0.8$$

$$I = 0.2\cdot0.5 + 0.7\cdot0.8 + 0.4\cdot0.8^{10} = 0.1 + 0.56 + 0.4\cdot0.107 = 0.703$$

## @lambert Lei de Lambert (reflexão difusa)
termos: Lambert, lei do cosseno, reflexão difusa ideal, superfície fosca, mate, cosseno do ângulo entre a normal e a luz, independe do observador

Superfície difusa ideal (fosca) espalha a luz igual para **todas as direções**, então o brilho que você vê **não depende de onde você está**. Ela recebe mais luz quanto mais de frente a luz bate:

$$I_d = I_l\,k_d\cos\theta = I_l\,k_d\,(N\cdot L)$$

$\theta$ = ângulo entre a **normal** e a **direção da luz**. Luz perpendicular à superfície ($\theta = 0$) → máximo; rasante ($\theta = 90°$) → zero. Ex.: $\theta = 60°$ → metade da intensidade.

## @espec Reflexão especular: Phong e Blinn-Phong
termos: especular, reflexo especular, brilho, highlight, vetor refletido, half vector, vetor intermediário, Blinn, cosseno elevado a n, depende do observador

**Phong**: $I_s = I_l\,k_s\,(R\cdot V)^n = I_l\,k_s\cos^n\alpha$, $\alpha$ = ângulo entre o **raio refletido** $R$ e a direção do **observador** $V$. Muda quando o observador se move.

**Blinn-Phong** (o do OpenGL fixo): troca $R\cdot V$ por $N\cdot H$, com o **vetor intermediário**

$$H = \frac{L + V}{|L+V|} \qquad I_s = I_l\,k_s\,(N\cdot H)^{n'}$$

Mais barato quando luz e observador estão no infinito ($H$ constante). Para o mesmo brilho, o expoente $n'$ precisa ser ~4× maior.

Ex. (números do **→phong**): $L+V = (0,\ 0.6,\ 1.8)$, $|L+V| = \sqrt{3.6} = 1.897$, $H = (0,\ 0.316,\ 0.949)$, $N\cdot H = 0.949$.

## @normuso Para que servem as normais na renderização
termos: normal da faceta, para que serve a normal, vetor normal, intensidade da iluminação difusa, intensidade do reflexo especular, orientação da face

A normal é o que diz **como a superfície está virada** em relação à luz e ao observador. Ela entra em:

- **difusa**: $N\cdot L$ → quanta luz direta o ponto recebe (Lambert);
- **especular**: $R = 2(N\cdot L)N - L$ (ou $N\cdot H$) → quão brilhante/espelhado o ponto fica;
- **backface culling**: $N\cdot V$;
- tonalização suave (Gouraud/Phong interpolam a partir das normais dos vértices);
- reflexão e refração no ray tracing.

Não é com a normal sozinha que se decide sombra (precisa saber se **outro objeto** bloqueia a luz: shadow ray / shadow map), nem transparência/translucência (propriedades do material), nem a luz **ambiente** (que é constante).

## @shading Tonalização: flat, Gouraud e Phong shading
termos: tonalização, shading, sombreamento, flat shading, constante, facetado, Gouraud, interpolação de intensidades, interpolação de cores, Phong shading, interpolação de normais, bandas de Mach, resolução da malha, suavidade

Modelo de **iluminação** (**→phong**) = a fórmula da cor num ponto. Modelo de **tonalização** (shading) = **onde** aplicar a fórmula e como preencher o resto do polígono.

| método | calcula a iluminação | interpola | resultado |
|---|---|---|---|
| **flat** (constante) | 1 vez por **polígono** (normal da face) | nada | facetado; bandas de Mach nas arestas |
| **Gouraud** (1971) | nos **vértices** (normal do vértice = média das faces) | as **cores/intensidades** ao longo das arestas e da scanline | suave, mas **perde/borra o brilho especular** no meio do polígono; brilho "pisca" entre vértices na animação |
| **Phong shading** (1975) | em **cada pixel** | as **normais** (renormaliza em cada pixel) | brilho especular correto; mais caro |

- No Gouraud a suavidade **depende da resolução da malha** (esfera com poucos triângulos ainda mostra os vértices).
- **Pegadinha**: quem interpola as **cores** dos vértices é o **Gouraud**; o Phong (shading) interpola **normais**.
- Nenhum dos três faz **sombra projetada** de um objeto no outro (são locais).
- Flat é exato só se luz e observador estão no infinito e a superfície é de fato plana.

**Exemplo Gouraud** (interpolação numa scanline): numa linha, aresta esquerda com intensidade $0.2$ em $x = 10$ e direita com $0.8$ em $x = 30$. Em $x = 15$:

$$I = 0.2 + \frac{15 - 10}{30-10}(0.8 - 0.2) = 0.2 + 0.25\cdot0.6 = 0.35$$

(incremental: soma $\Delta I = 0.6/20 = 0.03$ por pixel.) As intensidades das arestas vêm, do mesmo jeito, interpolando entre os vértices em $y$.

# Parte 9. Visualização realista, GPU, APIs e engines

## @raytrace Ray tracing (traçado de raios, Whitted 1980)
termos: ray tracing, raytracing, ray tracer, traçado de raios, renderização de imagens 3D, raio do observador para cada pixel da viewport, caminho inverso ao da luz real, raios secundários, reflexão, refração, sombra, shadow ray, recursivo, simular a propagação da luz, iluminação global, Snell

Simula a propagação da luz **ao contrário**: em vez de seguir os raios que saem da luz (quase nenhum chega ao olho), lança **do observador um raio para cada pixel** da viewport e vê o que ele atinge.

```
cor traca(raio, profundidade):
  acha a interseção MAIS PRÓXIMA do raio com os objetos (se nenhuma: cor de fundo)
  cor = luz ambiente
  para cada luz:
     lança um RAIO DE SOMBRA do ponto até a luz
     se nada bloqueia: cor += difusa + especular (modelo LOCAL de Phong)
  se profundidade < max:
     se o material reflete: cor += kr * traca(raio refletido, profundidade+1)
     se é transparente:     cor += kt * traca(raio refratado (Snell), profundidade+1)
  devolve cor
```

- **Usa o modelo local de Phong** em cada ponto atingido e soma as contribuições recursivas (reflexão e refração). Trata **sombras, reflexos especulares e transparência/refração**.
- **Raios primários**: um por pixel (dependem da câmera e da resolução). **Secundários** (sombra, reflexão, refração): dependem do **número de objetos e de luzes** atingidos. Então o total de raios **depende** da cena.
- Depende do **observador**: a câmera mexeu, recalcula tudo.
- Cada pixel é independente → **fácil de paralelizar** (GPU, várias máquinas).
- Caro: o custo está nos **testes de interseção**; acelera com volumes envolventes, grades, octree, BSP/kd-tree, BVH.
- Não modela bem a **inter-reflexão difusa** (luz que quica em paredes foscas): isso é radiosidade / path tracing. Mais transparência = **mais** raios = mais lento.
- Aliasing: um raio por pixel serrilha; lança vários (superamostragem/distribuído).
- **Refração (Snell)**: $\ n_1\,\mathrm{sen}\,\theta_1 = n_2\,\mathrm{sen}\,\theta_2$. Ex.: ar ($1.0$) para vidro ($1.5$) com $30°$: $\mathrm{sen}\,\theta_2 = 0.5/1.5 = 0.333$, $\theta_2 \approx 19.5°$ (dobra em direção à normal).
- **Interseção raio-esfera**: $P(t) = O + tD$ em $|P - C|^2 = r^2$ dá uma equação do 2º grau em $t$; o menor $t > 0$ é o ponto visível. Raio-plano: **→plano**.

## @raycast Ray casting e ray casting volumétrico
termos: ray casting, ray caster, Appel 1968, só raios primários, sem recursão, volumétrico, voxel, dados volumétricos, tomografia, ressonância magnética, radar, acumula cores dos voxels, renderização volumétrica, transferência

- **Ray casting** (Appel 1968): igual ao ray tracing **sem a recursão**: um raio por pixel, acha o primeiro objeto e calcula a cor local (no máximo um raio de sombra). Serve para **visibilidade**; jogos 2,5D (Wolfenstein 3D) usam ray casting numa grade.
- **Ray casting volumétrico** (volume ray casting): o dado não é uma superfície, é um **volume de voxels** (tomografia, ressonância, radar, simulação). Para cada pixel lança um raio através do volume, **amostra ao longo do raio** e **acumula (compõe) a cor e a opacidade dos voxels** por onde passa (função de transferência: densidade → cor/opacidade). Resultado: uma visualização 2D do dado 3D, dá para "ver dentro".
- Diferença de nome que cai: **ray tracer** = recursivo, superfícies, reflexo/refração; **ray caster volumétrico** = atravessa dados volumétricos acumulando voxels.

## @radios Radiosidade e radiância (iluminação global)
termos: radiosidade, radiosity, radiância, radiance, iluminação global, inter-reflexão difusa, interação entre objetos, fator de forma, patches, independente do observador, color bleeding, sombra suave, equação de renderização, path tracing, Goral 1984

- **Iluminação global** = a cor de um ponto considera a luz que chega **de outros objetos** (reflexos, inter-reflexões), não só da fonte. Local = só fonte + o próprio ponto.
- **Radiosidade** (Goral et al. 1984, vem da transferência de calor): modela a **inter-reflexão difusa** entre todas as superfícies. Divide a cena em **patches**, calcula **fatores de forma** (quanto um patch "vê" do outro) e resolve um **sistema linear** (por Gauss-Seidel/Jacobi ou refinamento progressivo):

$$B_i = E_i + \rho_i \sum_j F_{ij}\,B_j$$

($B$ radiosidade, $E$ emissão, $\rho$ refletividade, $F_{ij}$ fator de forma).
- É **independente do observador**: pré-processamento caro, mas depois a câmera anda à vontade sem recalcular (só se luz/objeto mexer). Dá **sombras suaves** e **color bleeding** (parede branca fica avermelhada perto de um tapete vermelho). **Não** faz reflexo especular/espelho.
- **Radiância**: grandeza física da luz numa direção (W/(sr·m²)); é o que a **equação de renderização** (Kajiya 1986) calcula. "Radiance" também é nome de renderizador de iluminação global. No material da disciplina, radiância e radiosidade aparecem como métodos de **iluminação global** que modelam a **inter-reflexão difusa** entre os objetos.
- Não confundir com emissão de luz (corpo negro, temperatura de cor) nem com espalhamento em meios participantes (névoa, fumaça, céu).
- Ray tracing + radiosidade se complementam (especular + difuso). **Path tracing** e **photon mapping** resolvem os dois juntos (Monte Carlo).

## @shader Shaders e GPU: vertex, pixel/fragment, linguagens
termos: shader, pixel shader, fragment shader, ray shader, vertex shader, geometry shader, compute shader, GPU, programa da GPU, cor e iluminação por pixel, efeitos de reflexo e transparência, GLSL, HLSL

**Shader** = pequeno programa que roda **na GPU**, em paralelo, num estágio programável do pipeline.

| shader | roda para cada | faz |
|---|---|---|
| **vertex shader** | vértice | transforma (modelo/câmera/projeção), passa normal e $(u,v)$, iluminação por vértice |
| tessellation / geometry | patch / primitiva | subdivide, cria ou descarta primitivas |
| **pixel shader / fragment shader** ("ray shader" no material do professor) | fragmento (pixel candidato) | calcula a **cor e iluminação** do pixel: textura, Phong por pixel, **reflexos, transparência**, efeitos |
| compute shader | item de trabalho | cálculo geral (física, partículas, pós-processamento) |

Linguagens: **GLSL** (OpenGL/Vulkan), **HLSL** (Direct3D), MSL (Metal), WGSL (WebGPU); Cg (antiga, NVIDIA).

**GPU**: milhares de núcleos simples (SIMD/SIMT) → ótima para o que é igual em muitos dados (vértices, pixels). Tem rasterizador, z-buffer e unidades de textura em hardware. GPUs novas têm núcleo de ray tracing (RTX/DXR).

## @glpipe Pipeline do OpenGL (gráfico moderno)
termos: pipeline gráfico, pipeline do OpenGL, estágios, programável, fixo, primitive assembly, clipping, divisão perspectiva, rasterização, testes por fragmento, blending, frame buffer, double buffering, VBO, VAO, glBegin

1. dados dos vértices (VBO/VAO) →
2. **vertex shader** →
3. (tesselação, geometry shader) →
4. **montagem de primitivas** →
5. **recorte** (no espaço de clip) → **divisão perspectiva** (÷W) → NDC → **viewport** →
6. **rasterização** (gera fragmentos) →
7. **fragment shader** →
8. testes por fragmento (**scissor, stencil, profundidade/z-buffer**), **blending** (transparência) →
9. **frame buffer**.

- Pipeline **fixo** (OpenGL 1.x, `glBegin/glEnd`, `glLight`, `glRotate`, pilha de matrizes) × **programável** (3.x+ core: tudo por shaders, matrizes passadas como uniform, GLM).
- **Double buffering**: desenha no buffer de trás e troca (`swap`) → sem flicker/tearing; com vsync espera o retraço.

## @apis APIs gráficas, game engines, modeladores
termos: API gráfica, biblioteca gráfica, OpenGL, WebGL, Direct3D, DirectX, Vulkan, Metal, game engine, motor de jogo, Unity, Unreal, Godot, Blender, POV-Ray, pacote de modelagem, renderizador

**API gráfica** = biblioteca de baixo nível para mandar desenhar na GPU (funções otimizadas, gera código para a GPU):

| API | de quem / onde |
|---|---|
| **OpenGL** | Khronos, multiplataforma (1992) |
| **OpenGL ES** | versão para celular/embarcado |
| **WebGL** | OpenGL ES no **navegador**, via JavaScript |
| **Direct3D** | Microsoft (Windows, Xbox). É a parte 3D do **DirectX** |
| **Vulkan** | Khronos, baixo nível (sucessor "explícito" do OpenGL) |
| **Metal** | Apple |
| **WebGPU** | sucessor do WebGL |

- **DirectX** é uma **coleção** de APIs (Direct3D, DirectSound, DirectInput, DirectPlay...), não só gráfica. Então, numa lista de APIs gráficas, o nome exato é **Direct3D** (DirectX é o pacote).
- **Não** são APIs gráficas: **Blender**, 3ds Max, Maya (modeladores/animação/render), **Unity, Unreal, Godot** (engines), **POV-Ray** (ray tracer), Moray (modelador para POV-Ray).

**Game engine (motor de jogo)** = pacote de software que junta: **motor gráfico** (render 2D/3D), **motor de física** (ou só detecção de colisão), **animação**, **som**, **IA**, **rede**, gerência de memória, de arquivos e de threads, **grafo de cena** e entidades, e uma **linguagem de script**. Ex.: Unity (C#), Unreal (C++/Blueprints), Godot (GDScript).

**Pacote de modelagem 3D** (Blender, 3ds Max, Maya): cria malhas, materiais, animação. Termos: **modificador** (MeshSmooth/TurboSmooth/Subdivision Surface suavizam a malha subdividindo; Bend, Twist, Mirror), **textura/mapa** (bump map, diffuse map), **método de renderização** (flat shading, Gouraud, wireframe).

## @ecs Entity Component System (ECS)
termos: ECS, entity component system, entidade, componente, sistema, composição sobre herança, agregação, padrão de arquitetura, game engine, orientado a dados

Padrão de **arquitetura/modelagem de dados** de game engines:

- **Entidade**: só um **ID** (não tem código nem dados).
- **Componente**: só **dados** (Posição, Velocidade, Sprite, Vida).
- **Sistema**: a **lógica**, roda sobre todas as entidades que têm certos componentes (ex. sistema de movimento: todas com Posição + Velocidade).

Prefere **composição/agregação** (montar a entidade juntando componentes) **em vez de herança e polimorfismo** (hierarquia `Inimigo extends Personagem extends ...`). Vantagens: flexível (adiciona/remove comportamento em tempo de execução), dados contíguos na memória (cache), fácil de paralelizar. Ex.: Unity DOTS, Bevy, EnTT.

## @tecnfunc Técnica → para que serve (relacionar colunas)
termos: técnica e função, para que serve cada algoritmo, tabela de técnicas, associar técnica e uso

| técnica | serve para |
|---|---|
| Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, NLN | **recorte** de retas |
| Sutherland-Hodgeman, Weiler-Atherton | **recorte** de polígonos |
| Bézier, B-spline, Hermite | **curvas/superfícies** (Bézier: aproximação de curvas) |
| de Casteljau | calcular/subdividir Bézier |
| DDA, Bresenham | **rasterização de retas** |
| ponto médio (círculo) | rasterização de círculos |
| scanline, flood fill, boundary fill | **preenchimento** |
| z-buffer, pintor, Warnock, scanline | **remoção de superfícies ocultas** |
| BSP, octree, kd-tree, quadtree | **subdivisão espacial** |
| backface culling | descartar faces traseiras |
| Phong, Lambert, Blinn | **iluminação** |
| flat, Gouraud, Phong shading | **tonalização** |
| ray tracing | iluminação global especular, sombras, reflexo/refração |
| radiosidade | iluminação global difusa |
| mipmap, SSAA, MSAA | anti-aliasing |
| bump, normal, environment mapping | texturas/detalhe |
| Gauss-Seidel / Jacobi | resolver sistema linear (aparece na radiosidade; distrator em recorte) |
| Runge-Kutta | EDO (simulação física); distrator |
| Kruskal | árvore geradora mínima; distrator |

# Parte 10. Hierarquia, animação, cor e dispositivos

## @hier Modelos hierárquicos, grafo de cena, pilha de matrizes
termos: modelo hierárquico, hierarquia, grafo de cena, scene graph, árvore, nó pai, nó filho, instância, instanciamento, símbolo, pilha de matrizes, push, pop, glPushMatrix, glPopMatrix, braço de robô, transformação relativa ao pai

- Objeto articulado (braço de robô, corpo, sistema solar) = **árvore**: cada nó tem uma transformação **relativa ao pai**. A transformação de um nó no mundo é o **produto das matrizes do caminho** da raiz até ele: mexeu no pai, os filhos vão junto.
- Vetor-coluna: $M_{mão} = M_{base}\,M_{braço}\,M_{antebraço}\,M_{mão,local}$.
- **Pilha de matrizes**: ao descer para um filho, `push` (salva a matriz atual); desenha o filho multiplicando a transformação dele; ao voltar, `pop` (restaura a do pai) para o irmão seguinte não herdar a transformação do filho.

```
desenha(no, M):
  M = M * no.local
  desenha a geometria do no com M
  para cada filho: push; desenha(filho, M); pop
```

- **Instância / símbolo**: um modelo só guardado uma vez (ex. roda) e usado várias vezes com transformações diferentes (4 rodas). Economiza memória; mudou o símbolo, mudam todas.
- **Grafo de cena** (scene graph) generaliza: nós de grupo, de transformação, de geometria, de luz, de câmera; pode ser DAG (instância compartilhada).

**Exemplo** (2D): base na origem; elo 1 de comprimento 4 girado $90°$; elo 2 de comprimento 2 girado $-90°$ **em relação ao elo 1**. Fim do elo 1: $(0,4)$. O elo 2 fica com ângulo absoluto $90° - 90° = 0°$: fim em $(0+2,\ 4) = (2,\ 4)$. (Isso é cinemática direta.)

## @anim Animação: keyframes, interpolação, cinemática, partículas
termos: animação, quadros-chave, keyframes, interpolação, in-betweening, tweening, lerp, slerp, quaternion, gimbal lock, cinemática direta, cinemática inversa, forward kinematics, inverse kinematics, sistema de partículas, morphing, captura de movimento, motion capture, esqueleto, skinning, easing

- **Keyframes (quadros-chave)**: o animador define poses em alguns quadros; o computador gera os intermediários (**in-betweening / tweening**) por interpolação: linear (**lerp**: $P = (1-t)A + tB$), por spline (movimento suave, ver curvas), com **easing** (acelera/desacelera).
- Rotação: interpolar ângulos de Euler dá **gimbal lock** e caminhos estranhos; usa-se **quaternion** com **slerp** (interpolação esférica).
- **Cinemática direta** (FK): dados os **ângulos** das juntas, calcula a **posição** da ponta (multiplica as matrizes da hierarquia). Fácil, uma resposta.
- **Cinemática inversa** (IK): dada a **posição desejada** da ponta (mão no copo, pé no chão), calcula os **ângulos**. Pode ter **várias soluções ou nenhuma**; resolve por métodos numéricos (Jacobiano, CCD).
- **Sistema de partículas** (Reeves 1983, Star Trek II): muitas partículas com posição, velocidade, tempo de vida, emitidas e atualizadas por regras/física → fogo, fumaça, explosão, chuva.
- **Morphing**: transforma uma forma/imagem em outra (interpola vértices ou deforma + dissolve imagens).
- **Animação esquelética + skinning**: malha "pendurada" num esqueleto; cada vértice segue os ossos com pesos.
- **Motion capture**: grava o movimento de um ator (marcadores) e aplica no esqueleto.
- Animação **procedural / por física**: posição vem de simulação (integra com Euler/Runge-Kutta: aqui o Runge-Kutta é legítimo).
- Taxa de quadros: cinema 24 fps, TV 30 (NTSC)/25 (PAL), jogos 30–60+.

## @luzcor Cor: luz, espectro, olho
termos: cor, espectro visível, comprimento de onda, nm, nanômetros, olho humano, retina, cones, bastonetes, tricromacia, Young-Helmholtz, fóvea, metamerismo, matiz, saturação, brilho, luminância

- Luz visível: comprimento de onda de ~**380 nm (violeta)** a ~**780 nm (vermelho)** (muitos livros: 400–700 nm). Ordem: violeta, azul, verde, amarelo, laranja, vermelho. Abaixo: ultravioleta; acima: infravermelho.
- **Retina**: **bastonetes** (~120 milhões, visão no escuro, **não** distinguem cor, periferia) e **cones** (~6 milhões, **cor**, concentrados na **fóvea**). 3 tipos de cone: S (azul, ~420 nm), M (verde, ~530 nm), L (vermelho, ~560 nm) → **tricromacia** (teoria de Young-Helmholtz): qualquer cor percebida é uma combinação de 3 estímulos. Por isso 3 primárias bastam na tela.
- **Metamerismo**: espectros diferentes que o olho vê como a mesma cor.
- Atributos: **matiz** (hue, comprimento de onda dominante), **saturação** (pureza, quanto branco misturado), **brilho/luminância** (intensidade).

## @modcor Modelos de cor: RGB, CMY(K), HSV, CIE, YIQ (com conversões)
termos: modelo de cor, RGB, aditivo, CMY, CMYK, subtrativo, HSV, HSL, HSI, CIE, XYZ, diagrama de cromaticidade, gamut, gama de cores, YIQ, YUV, YCbCr, Pantone, converter RGB para CMY, tons de cinza

| modelo | tipo | onde |
|---|---|---|
| **RGB** | **aditivo** (luz somando; preto = (0,0,0), branco = (1,1,1)); cubo | monitores, câmeras |
| **CMY / CMYK** | **subtrativo** (tinta absorvendo; branco = papel) | impressão. K (preto) porque C+M+Y real dá marrom escuro e gasta tinta |
| **HSV / HSL** | matiz (ângulo 0–360°), saturação, valor/luminosidade; hexcone | seletor de cor, intuitivo para pessoas |
| **CIE XYZ** (1931) | padrão baseado na visão humana com primárias imaginárias; **diagrama de cromaticidade** em forma de ferradura | comparar e converter; **gamut** de um dispositivo = triângulo dentro dele (nenhum trio de primárias reais cobre todas as cores visíveis) |
| **YIQ** / **YUV** / **YCbCr** | Y = luminância separada da cor | TV (NTSC), vídeo, JPEG (comprime mais a cor que o brilho) |
| **Pantone** | catálogo de cores prontas (spot colors) | gráfica, marcas |

Aditivo: $R+G$ = amarelo, $G+B$ = ciano, $R+B$ = magenta, $R+G+B$ = branco. Subtrativo: $C+M$ = azul, $M+Y$ = vermelho, $C+Y$ = verde, $C+M+Y$ = preto.

**Conversões** (valores em $[0,1]$), exemplo $RGB = (0.2,\ 0.6,\ 0.4)$:

$$CMY = (1-R,\ 1-G,\ 1-B) = (0.8,\ 0.4,\ 0.6)$$

$$K = \min(C,M,Y) = 0.4 \qquad C' = \frac{C-K}{1-K} = \frac{0.4}{0.6} = 0.667,\ \ M' = 0,\ \ Y' = \frac{0.2}{0.6} = 0.333$$

HSV: $V = \max = 0.6$; $S = \dfrac{\max-\min}{\max} = \dfrac{0.4}{0.6} = 0.667$; como o máximo é o **G**: $H = 60°\cdot\dfrac{B-R}{\max-\min} + 120° = 60\cdot0.5 + 120 = 150°$. (Máximo em R: $H = 60\frac{G-B}{\Delta}$ (mod 360); em B: $H = 60\frac{R-G}{\Delta} + 240$.)

Tons de cinza (luminância): $Y = 0.299R + 0.587G + 0.114B = 0.06 + 0.352 + 0.046 = 0.458$ (o verde pesa mais porque o olho é mais sensível a ele).

## @display Dispositivos: vetorial × raster, frame buffer, memória
termos: dispositivo de saída, display, vetorial, random scan, raster, matricial, frame buffer, memória de vídeo, refresh, taxa de atualização, flicker, pisca-pisca, retraço, entrelaçado, CRT, LCD, OLED, plasma, resolução, profundidade de cor, bits por pixel, tabela de cores, lookup table, display file

| | **vetorial** (random scan, caligráfico) | **raster** (matricial) |
|---|---|---|
| como desenha | o feixe vai direto de ponto a ponto desenhando **linhas** (lista de comandos: *display file*) | varre a tela **inteira**, linha por linha, lendo o **frame buffer** |
| tempo de refresh | depende de **quantas linhas** a cena tem → cena complexa demais dá **flicker** (pisca-pisca) | **independe** da complexidade da cena (sempre varre todos os pixels) |
| linhas | perfeitas, sem serrilhado | serrilhado (aliasing) |
| áreas preenchidas, imagens | não (só contorno) | sim |
| custo de memória | pequeno | frame buffer grande |

- Ou seja: flicker por cena complexa é problema do **vetorial**, não do raster.
- **CRT**: canhão de elétrons, fósforo (persistência curta → refresh ≥ 60 Hz), **retraço horizontal** (volta ao início da linha) e **vertical** (volta ao topo); **entrelaçado** = linhas pares num quadro, ímpares no outro (menos flicker com menos banda).
- **LCD**: cristal líquido + polarizadores + luz de fundo (não emite luz). **LED/OLED**: cada pixel emite. Plasma: células de gás.
- **Frame buffer**: memória com a cor de cada pixel. Tamanho = largura × altura × bits por pixel.

**Exemplo**: $1920\times1080$ com 24 bits (8 por canal) $= 1920\cdot1080\cdot3 = 6\,220\,800$ bytes $\approx 5{,}9$ MB; com double buffering, o dobro. 24 bits = $2^{24} \approx 16{,}7$ milhões de cores.

**Tabela de cores (lookup table / paleta)**: o frame buffer guarda um índice de 8 bits por pixel e uma tabela traduz para uma cor de 24 bits: $2^8 = 256$ cores ao mesmo tempo, escolhidas entre $2^{24}$.

# Parte 11. Processamento de imagens

## @imgdig Imagem digital: amostragem, quantização, vizinhança
termos: imagem digital, amostragem, quantização, resolução espacial, níveis de cinza, bits por pixel, vizinhança 4, vizinhança 8, conectividade, pixel, matriz de intensidades

- Imagem digital = matriz $M\times N$ de **pixels**, cada um com uma intensidade (cinza) ou 3 (RGB).
- **Amostragem**: discretiza o **espaço** (quantos pixels: resolução espacial). Pouca amostragem → aliasing, blocos.
- **Quantização**: discretiza a **intensidade** (quantos níveis: $k$ bits → $2^k$ níveis, ex. 8 bits = 256 tons de cinza). Pouca quantização → **falso contorno** (faixas).
- Vizinhança **4** (cima, baixo, esq., dir.) e **8** (inclui diagonais). Memória: $M\cdot N\cdot k$ bits.

## @histo Histograma, operações pontuais (negativo, brilho, contraste, limiar)
termos: histograma, operação pontual, transformação de intensidade, negativo, brilho, contraste, limiarização, threshold, binarização, gama, logaritmo, linear, paralelo

**Histograma**: quantos pixels há em cada nível de cinza. Imagem escura → concentrado à esquerda; clara → à direita; **baixo contraste** → concentrado num trecho estreito; alto contraste → espalhado.

**Operações pontuais** (cada pixel de saída depende **só do pixel de entrada** na mesma posição → podem ser feitas **em paralelo** em todos os pixels). $r$ = entrada, $s$ = saída, $L$ níveis:

| operação | fórmula | efeito |
|---|---|---|
| **negativo** | $s = L-1-r$ | inverte (255 → 0) |
| **brilho** | $s = r + b$ | desloca o histograma (linear) |
| **contraste** | $s = a\,r$ (ou $a(r - m) + m$) | estica/comprime o histograma (linear) |
| **limiar** (threshold) | $s = L-1$ se $r > T$, senão $0$ | binariza |
| **gama** | $s = c\,r^{\gamma}$ | $\gamma<1$ clareia escuros; $\gamma>1$ escurece |
| **log** | $s = c\log(1+r)$ | realça escuros (ex. espectro de Fourier) |

Brilho e contraste são **lineares**; a equalização **não** (próximo bloco).

## @equal Equalização de histograma (com exemplo)
termos: equalização de histograma, histograma acumulado, cumulativo, função de distribuição acumulada, CDF, aumentar o contraste, não linear, específica para cada imagem, espalhar os níveis

**Objetivo**: deixar o histograma o mais **uniforme** possível → **aumenta o contraste** justamente nas faixas onde há **muitos pixels** (os níveis concentrados são espalhados); níveis com poucos pixels são comprimidos/juntados.

$$s_k = (L-1)\sum_{j=0}^{k}\frac{n_j}{n} \qquad \text{(arredonda)}$$

Usa o **histograma acumulado** (CDF). É **não linear** e **específica de cada imagem** (a curva sai do histograma dela). Aplicar duas vezes não muda mais nada.

**Exemplo**: 8 níveis (0–7), 100 pixels, imagem escura:

| $r$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $n_r$ | 20 | 30 | 25 | 15 | 5 | 3 | 1 | 1 |
| acumulado | 0.20 | 0.50 | 0.75 | 0.90 | 0.95 | 0.98 | 0.99 | 1.00 |
| $7\times$acum. | 1.4 | 3.5 | 5.25 | 6.3 | 6.65 | 6.86 | 6.93 | 7 |
| $s$ | 1 | 4 | 5 | 6 | 7 | 7 | 7 | 7 |

Os níveis 0–3, que tinham 90% dos pixels, foram **espalhados** para 1, 4, 5, 6 (mais contraste ali); os níveis 4–7, quase vazios, foram juntados no 7.

> [!warning] Cuidado
> Equalizar **aumenta** o contraste onde o histograma tem mais pixels (nunca reduz).

## @conv Filtragem espacial: convolução e máscaras
termos: filtragem no domínio espacial, convolução, máscara, kernel, janela 3x3, vizinhança, correlação, borda da imagem, padding

**Convolução**: para cada pixel, coloca a **máscara** (kernel, ex. $3\times3$) centrada nele, multiplica cada peso pelo pixel embaixo e **soma**; o resultado é o novo pixel. (Convolução de verdade espelha a máscara; para máscaras simétricas dá igual à correlação.)

- A imagem de saída tem **as mesmas dimensões** da entrada (nas bordas: replica, zera ou espelha os pixels de fora).
- Pesos que **somam 1** → preserva o brilho médio (passa-baixa). Pesos que **somam 0** → resposta zero em região uniforme (passa-alta, detector de borda).
- Consequência: um passa-baixa numa imagem **toda de uma cor só** (ex. toda preta) devolve **a mesma imagem**, mesmo tamanho, mesma cor. Um passa-alta nela devolve tudo 0.

**Exemplo** com a vizinhança (um ponto de ruído no meio):

$$\begin{bmatrix}10&10&10\\10&90&10\\10&10&10\end{bmatrix}$$

- **Média** $3\times3$ (todos os pesos $1/9$): $(8\cdot10 + 90)/9 = 170/9 \approx 19$ → o ruído é atenuado, não sumiu.
- **Mediana**: ordenando, 8 valores 10 e um 90 → mediana **10** → o ruído **some**.
- **Laplaciano** $\begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\end{bmatrix}$: $4\cdot10 - 4\cdot90 = -320$ → resposta **forte** no ponto (detecta).

## @filtros Passa-baixa, passa-alta, mediana, detectores de borda
termos: filtro passa-baixa, passa-baixas, low-pass, suavização, borramento, média, Gaussiano, filtro da mediana, ruído sal e pimenta, passa-alta, passa-altas, high-pass, realce, nitidez, Laplaciano, Sobel, Prewitt, Roberts, Canny, gradiente, detecção de bordas

| filtro | tipo | uso |
|---|---|---|
| **média** (box) | **passa-baixa**, linear | suaviza, reduz ruído, borra bordas |
| **Gaussiano** | **passa-baixa**, linear (pesos de uma gaussiana) | suaviza com menos artefato que a média |
| **mediana** | **não linear** (ordena e pega o do meio) | remove ruído **sal e pimenta** preservando bordas |
| **Laplaciano** | **passa-alta** (2ª derivada) | realça detalhes/bordas, nitidez (somado à imagem) |
| **Sobel, Prewitt, Roberts** | **passa-alta** (gradiente, 1ª derivada) | **detecção de bordas** com direção |
| **Canny** | gaussiano + gradiente + supressão de não-máximos + histerese | detector de bordas "ótimo" |
| **unsharp masking / high-boost** | imagem + (imagem − borrada) | nitidez |

> [!warning] Pegadinha
> **Gaussiano é passa-baixa, Laplaciano é passa-alta.** Passa-**alta** = bordas/detalhes; passa-**baixa** = suavizar/ruído.

Sobel:

$$G_x = \begin{bmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{bmatrix} \qquad G_y = \begin{bmatrix}-1&-2&-1\\0&0&0\\1&2&1\end{bmatrix} \qquad |G| = \sqrt{G_x^2 + G_y^2} \approx |G_x| + |G_y|$$

Prewitt = igual com 1 no lugar dos 2. Exemplo: numa borda vertical com coluna esquerda 0 e direita 100, $G_x = 100 + 200 + 100 = 400$ e $G_y = 0$: borda forte, vertical.

## @fourier Domínio da frequência (Fourier)
termos: transformada de Fourier, DFT, FFT, domínio da frequência, altas frequências, baixas frequências, teorema da convolução, espectro

- A **transformada discreta de Fourier (DFT)**, calculada pela **FFT**, leva a imagem para o **domínio da frequência**: baixas frequências = regiões suaves/variação lenta; **altas** frequências = **bordas, detalhes e ruído**.
- **Teorema da convolução**: convolução no espaço = **multiplicação** na frequência. Filtrar = multiplicar o espectro por uma máscara (zerar altas = passa-baixa; zerar baixas = passa-alta) e voltar com a inversa. Para máscaras grandes é mais rápido.
- Filtro ideal (corte seco) gera "anéis" (ringing); Butterworth e Gaussiano são suaves.

## @segm Segmentação (e o que ela não é)
termos: segmentação, regiões homogêneas, agrupar, limiarização, Otsu, crescimento de regiões, split and merge, divisão e fusão, watershed, k-means, características, brilho, textura

**Segmentação** = **agrupar** partes da imagem em **regiões homogêneas** com respeito a uma ou mais características (brilho, nível de cinza, cor, textura). É o passo antes de reconhecer objetos.

| método | ideia |
|---|---|
| **limiarização** (threshold, Otsu escolhe o limiar automático) | separa por intensidade |
| **crescimento de regiões** | começa de sementes e agrega vizinhos parecidos |
| **divisão e fusão** (split and merge, quadtree) | divide o que não é homogêneo, junta vizinhos parecidos |
| **watershed** | imagem como relevo, "inunda" a partir dos mínimos |
| **por bordas** | detecta bordas e fecha contornos |
| **agrupamento** (k-means) | agrupa pixels por cor/característica |

O que **não** é: dividir a imagem em regiões de **mesmo tamanho** (isso é só particionar em blocos); **identificar/reconhecer** objetos a partir de uma descrição prévia (isso é **reconhecimento/classificação**, vem depois); e não é a mesma coisa que **detecção de bordas** (borda é um dos meios de segmentar).

## @morfo Morfologia matemática
termos: morfologia, erosão, dilatação, abertura, fechamento, elemento estruturante, imagem binária, esqueletização

Opera com um **elemento estruturante** (ex. quadrado $3\times3$) sobre imagem binária (ou cinza):

- **Erosão**: o pixel fica 1 só se o elemento **inteiro** cabe no objeto → objeto **encolhe**, some com pontinhos.
- **Dilatação**: fica 1 se o elemento **toca** o objeto → objeto **cresce**, fecha buracos pequenos.
- **Abertura** = erosão e depois dilatação → remove ruído/objetos pequenos, mantém o tamanho do resto.
- **Fechamento** = dilatação e depois erosão → fecha buracos e frestas pequenas.
- Borda do objeto = imagem − erosão. Esqueletização, afinamento, hit-or-miss também são morfológicos.

## @zipimg Compressão e formatos de imagem
termos: compressão, com perdas, sem perdas, JPEG, PNG, GIF, BMP, RLE, Huffman, LZW, DCT, redundância

- **Sem perdas**: RLE (corridas iguais: "10 brancos, 3 pretos"), **Huffman** (códigos curtos para símbolos frequentes), **LZW** (dicionário; GIF), DEFLATE (**PNG**). Volta exatamente.
- **Com perdas**: **JPEG** = converte para YCbCr, subamostra a cor, blocos $8\times8$ com **DCT**, **quantiza** (onde perde), Huffman. Bom para fotos; ruim para texto/desenho (artefatos de bloco).
- BMP: sem compressão (ou RLE). GIF: 256 cores (paleta), animação. PNG: sem perdas, transparência.
