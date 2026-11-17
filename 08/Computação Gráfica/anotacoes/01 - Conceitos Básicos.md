---
tags: [cg, modulo-1]
---
# 01 · Conceitos Básicos: Display File, Window e Viewport

[[Computação Gráfica|↑ Índice]] · próximo: [[02 - Transformações 2D e Coordenadas Homogêneas]]
Slides: [[02 - Conceitos Básicos - Window, Viewport e Display File.pdf]] · Apostila: [[Apostila 1.1 - Conceitos Básicos.pdf]] · Intro: [[01 - Introdução e Visão Geral da Disciplina.pdf]]

## O que é Computação Gráfica
Conjunto de métodos e técnicas computacionais para **representar graficamente**, com um computador, objetos de um mundo real ou virtual. Isso implica:
- um **modelo interno** do mundo a ser representado, e
- um **conjunto de transformações** que levam esse modelo a um dispositivo de saída (vídeo, plotter...).

Histórico: a CG começou substituindo a prancheta de desenho, com o **CAD** (Computer-Aided Design). Exemplos: IBM Catia, AutoCAD.

## Displays
| | **Vetorial (Random Scan)** | **Raster Scan** |
|---|---|---|
| Memória de vídeo | não tinha | **frame buffer** (matriz de pixels) |
| Como desenha | o canhão desenha **cada objeto** separadamente, sem conceito de pixel | varredura fixa da tela inteira, sempre igual |
| Redesenho | redesenha a cena inteira repetidamente (displays **caligráficos**) | a matriz é redesenhada num ritmo fixo, independente do conteúdo |
| Legado | motivou o **Display File** | |

**Display File**: a **lista de todos os objetos do mundo** representado.
- Nos random scan era percorrida em loop infinito.
- Ainda é usada para guardar os objetos em sistemas modernos.
- No SGI: cada objeto tem **nome**, **tipo** (ponto, reta, polígono/wireframe...) e **lista de coordenadas**.

Divisão de trabalho: o SO e o hardware escrevem e leem a memória de vídeo, fazem a aceleração e rasterizam. O **programa gráfico** faz a **transformada de viewport**.

## Window × Viewport
- **Window**: retângulo que é o **recorte do mundo** (em coordenadas do mundo, cartesianas) que vai aparecer na tela.
  - **Tamanho variável** → zoom
  - **Posição variável** → navegação (pan)
  - Estrutura: `Xwmin, Ywmin, Xwmax, Ywmax`
- **Viewport**: a **área do vídeo** onde se desenha.
  - Sistema de coordenadas **parcialmente invertido: o Y aponta para baixo**.
  - Tamanho fixo ou não controlado pela aplicação.
  - Estrutura: `Xvpmin, Yvpmin, Xvpmax, Yvpmax`

## Transformada de Viewport
$$
x_{vp} = \frac{x_w - x_{wmin}}{x_{wmax}-x_{wmin}}\,(x_{vpmax}-x_{vpmin}) \;(+\,x_{vpmin})
$$
$$
y_{vp} = \left(1 - \frac{y_w - y_{wmin}}{y_{wmax}-y_{wmin}}\right)(y_{vpmax}-y_{vpmin}) \;(+\,y_{vpmin})
$$
- O `1 −` no y existe porque o eixo y da viewport aponta **para baixo**.
- Se a viewport tem origem deslocada (ex.: (10,10)), some o offset. Isso caiu no [[Banco de Questões#2. Window, viewport e clipping|banco de questões]] (resposta 170).
- Se a window e a viewport tiverem **proporções diferentes**, o objeto distorce. O trabalho 1.1 exigia que um quadrado continuasse quadrado.

## Visão geral de um sistema gráfico
- **Modelo de aplicação**: objetos, dados, descrição geométrica/procedural, atributos, relações espaciais.
- **Programa aplicativo**: interface entre o modelo e o sistema gráfico; cria o modelo; trata a interação.
- **Sistema gráfico**: produz a imagem a partir do modelo (Display File + transformada de viewport + sub-rotinas).

Pipeline 2D do SGI (ver [[03 - Sistema de Coordenadas Normalizadas (SCN)]]):
`mundo → (transformações) → SCN (window normalizada) → clipping → viewport`

## APIs gráficas × Game Engines × Modeladores
Caiu no quiz de treino ([[Banco de Questões#6. APIs, engines e ferramentas|Q6]]).
- **API gráfica**: biblioteca de funções otimizadas para renderizar, gerando código executável em GPU. Exemplos: **OpenGL, WebGL, Direct3D** (e Vulkan, Metal).
  - **DirectX não é só gráfico**. É uma coleção (Direct3D, DirectSound, DirectInput...), então, se a pergunta é "API gráfica", a resposta é **Direct3D**.
- **Game Engine**: motor gráfico 2D/3D + física/colisão + animação + som + IA + rede + memória/arquivos/threads + **grafo de cena** + **linguagem de script**. Exemplos: Unity, Unreal.
- **Modelador 3D**: Blender, Moray. **Raytracer**: POV-Ray (ver [[10 - Visualização Realista - Raytracing, Raycasting e Radiosidade]]).
