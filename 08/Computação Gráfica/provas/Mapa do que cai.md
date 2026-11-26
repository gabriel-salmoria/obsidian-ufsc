---
tags: [cg, prova, mapa]
---
# Mapa do que cai (e onde está explicado)

Voltar: [[Computação Gráfica]] · [[Colinha v1]] · [[Quiz de treino - banco do professor]] · [[POSCOMP - Computação Gráfica]]

Este mapa junta tudo o que aparece nas questões de treino (quiz do professor de 2021 = **Q01–Q77**; POSCOMP 2002–2026 = **P01–P105**) e diz onde estudar cada coisa na [[Colinha v1]]. Os códigos `[S..]` são as seções da Colinha: busque o código com Ctrl+F para ir direto. Na coluna "buscar" está a palavra que eu usaria no Ctrl+F para cair no lugar certo.

Como usar na prova: lê a questão, identifica o assunto aqui (ou direto na tabela [S00] da Colinha), busca a palavra e lê o parágrafo. As contas têm receita e exemplo com outros números.

## Computação gráfica 2D

### `[S02]` Conceitos básicos

O que precisa saber: diferença entre API gráfica, DirectX, game engine e modelador; ECS (composição × herança); display vetorial × raster; termos de modelagem (modificador, textura, método de renderização); distância euclidiana para picking.

| assunto da questão | buscar | questões |
|---|---|---|
| MeshSmooth, bump map, flat shading | `meshsmooth` | Q65, P33 |
| ECS | `ecs` | Q69 |
| Pacote com motor gráfico, física, som... | `engine` | Q70 |
| Exemplos de API gráfica | `api` | Q71 |
| Distância do mouse ao centro | `envelope` | Q72, P14 |

### `[S03]` Transformações 2D e coordenadas homogêneas

O que precisa saber: homogêneas (W, 3×3 e 4×4, por que existem); reconhecer translação, escala e rotação pela forma da matriz; vetor-linha × vetor-coluna; composição e ordem (quem comuta); girar/escalar em torno de um ponto; ler uma matriz composta (escala antes ou depois da translação); mudança de base.

| assunto da questão | buscar | questões |
|---|---|---|
| Reconhecer matriz de translação 2D | `translação` | Q17 |
| Sx e Sy: escala 2D | `diagonal` | Q18 |
| Expressão [x y 1]·M: homogêneas e W | `homogêneas` | Q20 |
| Reconhecer matriz de rotação 2D | `rotação` | Q22 |
| Homogêneas 3D: pontos 4D e W | `homogêneas` | Q24 |
| Reconhecer matriz de escala 2D | `diagonal` | Q25 |
| Homogêneas e comutatividade | `comutam` | Q29, P34 |
| Girar em torno do centro de massa | `em torno` | Q30, P20 |
| Ler matrizes A e B (ordem, centro, mudança de base) | `primeiro escala / mudança de base` | Q31 |
| Identificar a matriz de uma rotação + translação | `vetor-coluna` | Q32, P17 |
| Ler matrizes A e B | `primeiro escala / mudança de base` | P30 |
| Matrizes A e B: centro, ordem, homogêneas | `só a translação / primeiro escala` | P46 |
| Matriz de rotação em torno de um ponto (números) | `em torno` | P50 |

### `[S04]` Window, viewport e SCN

O que precisa saber: window (mundo) × viewport (dispositivo); fórmula da transformada de viewport com y invertido e origem deslocada; SCN com origem no centro e domínio [−1,1]; zoom in/out; relação de aspecto; instanciamento (aplicar transformações e ver a posição relativa).

| assunto da questão | buscar | questões |
|---|---|---|
| Ponto na viewport (coordenada y, y invertido) | `viewport` | Q02 |
| Ponto recortado em SCN (coordenada y) | `scn` | Q03 |
| Ponto em SCN (coordenada y) | `scn` | Q05 |
| Ponto recortado na viewport (coordenada y) | `viewport / recorta` | Q06 |
| Ponto recortado em SCN (coordenada x) | `scn` | Q07 |
| Ponto em SCN (coordenada x) | `scn` | Q09 |
| Ponto na viewport (coordenada x) | `viewport` | Q11 |
| Window × viewport: sistema, aspecto, zoom | `zoom` | Q14, P01 |
| Window, viewport, aspecto, onde recortar | `viewport` | Q15, P36 |
| Instanciamento e posição na window | `instanciamento` | Q16, P05 |

### `[S05]` Clipping (recorte)

O que precisa saber: nomes dos algoritmos (Cohen-Sutherland, Liang-Barsky, Nicholl-Lee-Nicholl, Sutherland-Hodgeman, Weiler-Atherton) e os distratores; montar region codes; achar o ponto recortado.

| assunto da questão | buscar | questões |
|---|---|---|
| Algoritmos de recorte de polígonos | `polígonos / Gauss` | Q01 |
| Nome do algoritmo por códigos de região | `region code` | Q04 |
| Region codes de dois pontos | `region code` | Q08, Q12 |
| Nome do algoritmo com pk e qk | `pk` | Q10 |
| Nome do algoritmo por coeficientes angulares | `coeficiente angular` | Q13 |

## Curvas e superfícies

### `[S06]` Curvas: Hermite, Bézier, de Casteljau, continuidade

O que precisa saber: Hermite, Bézier (Bernstein, fecho convexo, tangentes), de Casteljau, continuidade.

(nenhuma questão de treino caiu direto aqui, mas o assunto está no programa)

### `[S07]` B-splines e forward differences

O que precisa saber: B-spline (controle local, C2), forward differences.

(nenhuma questão de treino caiu direto aqui, mas o assunto está no programa)

### `[S08]` Superfícies bicúbicas

O que precisa saber: superfície bicúbica; soma dupla com Bernstein = superfície de Bézier.

| assunto da questão | buscar | questões |
|---|---|---|
| Superfície pela soma com Bernstein | `bernstein` | Q46, P32 |

## 3D, projeções e pipeline

### `[S09]` 3D: matrizes, eixo arbitrário, normal, plano, OBJ

O que precisa saber: matrizes 3D (translação, escala, Rx/Ry/Rz de 90°); matriz aplicada a vetor (colunas); normal por produto vetorial e estrutura de arame; projeção de ponto num plano numa direção.

| assunto da questão | buscar | questões |
|---|---|---|
| Matriz de translação 3D | `translação 3d` | Q19 |
| Matriz de escala 3D | `escala 3d` | Q21 |
| Rotação 3D de 90° em Z | `rz` | Q23 |
| Rotação 3D de 90° em X | `rx` | Q26 |
| Escolher a matriz de translação 3D | `translação 3d` | Q27 |
| Rotação 3D de 90° em Y | `ry` | Q28 |
| Matriz aplicada a um vetor | `coluna` | Q33, P53 |
| Estrutura de arame e normal | `arame` | Q34, P29 |
| Vetor perpendicular a dois | `perpendicular` | Q35, P40 |
| Projeção de ponto num plano por direção | `plano` | Q38, P11, P13 |

### `[S10]` Projeções e pipeline 3D

O que precisa saber: classificação das projeções (do professor); paralela × perspectiva (tamanho, volume de visão, matriz 4×4); as ordens do pipeline 3D; transformação de câmera; volume de visão; pistas de profundidade.

| assunto da questão | buscar | questões |
|---|---|---|
| Projeção paralela (marque as verdadeiras) | `oblíqua / ignora Z` | Q36 |
| Características das projeções | `perspectiva` | Q37, P35 |
| Associar etapas da síntese de imagens | `volume de visão / Gouraud` | Q39, P22 |
| Afirmações sobre o pipeline 3D | `pipeline` | Q40, P03 |
| Ordem: recorte, projeção, rasterização, visibilidade | `pipeline` | Q41, P18 |
| Ordem: câmera, recorte 3D, projeção, tela, rasterização | `pipeline` | Q42, P04 |
| Nome da região recortada e projetada | `volume de visão` | Q43, P37 |
| Ordem das 5 transformações do pipeline | `pipeline` | Q44, P38 |
| Transformação de câmera | `câmera` | Q45, P06 |
| Pistas de profundidade | `profundidade` | P09 |

### `[S15]` GPU, shaders e pipeline do OpenGL

O que precisa saber: pixel shader; pipeline do OpenGL; o que pertence à etapa de rendering.

| assunto da questão | buscar | questões |
|---|---|---|
| Nome: cor e iluminação por pixel na GPU | `pixel shader` | Q51 |
| Tarefas da etapa de rendering | `rendering` | P48 |

## Rasterização e visibilidade

### `[S11]` Rasterização: retas, círculos, preenchimento, aliasing, texturas

O que precisa saber: reta ingênua/DDA/Bresenham; ponto médio do círculo; preenchimento (vizinhança 4/8); aliasing e MSAA; texturas (2D, procedural, bump, mipmap).

| assunto da questão | buscar | questões |
|---|---|---|
| MSAA | `msaa` | Q60, P25 |
| Textura que perturba a normal | `bump` | Q63, P39 |
| Função em C que desenha | `putpixel` | Q66, P15 |
| Memória extra do mipmap | `mipmap` | Q67, P28 |
| Texturas: 2D, procedural, bump | `textura` | P42 |
| O que é mipmapping | `mipmap` | P49 |

### `[S12]` Superfície oculta: z-buffer, pintor, backface, BSP

O que precisa saber: z-buffer (incremental, um valor por pixel, guarda o mais próximo, ordem não importa); pintor; backface (só 1 convexo); BSP; o que é e o que não é técnica de superfície oculta.

| assunto da questão | buscar | questões |
|---|---|---|
| Propriedades do z-buffer | `z-buffer` | Q61, P02 |
| Duas esferas, uma escondendo a outra | `z-buffer` | Q64, P24 |
| O que não é técnica de superfície oculta | `ocultas` | P45 |

## Iluminação e visualização realista

### `[S13]` Iluminação: Phong, Lambert, fontes de luz, shading

O que precisa saber: modelo de Phong (3 componentes aditivas), Lambert, especular, ambiente; por que calcular normais; fontes de luz; flat × Gouraud × Phong shading; normal de superfície paramétrica.

| assunto da questão | buscar | questões |
|---|---|---|
| Componentes do modelo de Phong | `phong` | Q47 |
| Para que servem as normais | `normais` | Q48 |
| Normal de superfície paramétrica | `paramétrica` | Q55, P21 |
| Modelos de iluminação locais | `lambert` | Q56, P23 |
| Fonte de luz no infinito | `direcional` | Q57, P41 |
| Gouraud, volume paralelo, Bresenham, aliasing | `gouraud` | Q62, P26 |
| Tonalização que interpola normais | `phong shading` | P43 |
| Flat, Gouraud e Phong (afirmações) | `flat` | P51 |

### `[S14]` Raytracing, raycasting e radiosidade

O que precisa saber: ray tracer × ray caster × ray caster volumétrico; o que o ray tracing faz e não faz (z-buffer, difuso, número de raios, modelo local); radiosidade.

| assunto da questão | buscar | questões |
|---|---|---|
| Radiância e radiosidade | `radiosidade` | Q49 |
| Nome: raios num volume de voxels | `voxel` | Q50 |
| Nome: raios de trás para frente | `trás para frente` | Q52 |
| O que o ray tracing faz | `ray tracing` | Q53, P07 |
| Afirmações sobre ray tracing | `ray tracing` | Q58, P08 |
| Simular a propagação da luz | `propagação` | Q59, P31 |
| Afirmações sobre ray tracing (z-buffer, difuso, secundários) | `ray tracing` | P44 |
| Ray tracing, z-buffer e Phong (afirmações) | `ray tracing` | P47 |

### `[S17]` Cor

O que precisa saber: modelos de cor, luminância, saturação × luminosidade, IHS.

(nenhuma questão de treino caiu direto aqui, mas o assunto está no programa)

## Processamento de imagens

### `[S18]` Processamento de imagens

O que precisa saber: digitalização (amostragem × quantização); etapas da análise de imagens; histograma e equalização; negativo e transformações de intensidade; filtros espaciais (média, mediana, passa-baixas/altas, máscaras); Fourier, DCT, wavelet, outras transformadas; interpolação; realce × restauração; segmentação; textura; reconhecimento (distância mínima, perceptron, estéreo); compressão (Huffman, RLE, JPEG, BMP, planos de bits).

| assunto da questão | buscar | questões |
|---|---|---|
| Filtros: qual afirmação é incorreta | `laplaciano` | Q74, P63 |
| Histograma, brilho/contraste, negativo | `equalização` | Q75, P64 |
| Definição de segmentação | `segmentação` | Q76, P75 |
| Passa-baixas numa imagem toda preta | `passa-baixa` | Q77, P69 |
| Definição de histograma | `histograma` | P60 |
| Para que serve a mediana | `mediana` | P61 |
| Descritores de textura | `co-ocorrência` | P62 |
| Ordem das etapas da análise de imagens | `análise de imagens` | P65 |
| Discretizar espaço e amplitude | `amostragem` | P66 |
| Média × mediana (características) | `mediana` | P67 |
| Convolução de [−1 2 −1] numa rampa | `[−1 2 −1]` | P68 |
| Técnicas de realce | `realce` | P70 |
| Comprimento médio de código Huffman | `huffman` | P71 |
| Contraste em cor sem mudar o tom | `ihs` | P72 |
| Média e mediana 3×3 em padrões | `mediana` | P73 |
| Filtro de diferença e orientação das bordas | `direcional` | P74 |
| Transformação do negativo | `negativo` | P76 |
| O que é e o que não é segmentação | `segmentação` | P77 |
| Luminância a partir de RGB | `luminância` | P78 |
| Classificador de distância mínima | `distância mínima` | P79 |
| Transformadas: núcleo separável e simétrico | `separável` | P80 |
| Filtro para tirar pontos preservando forma | `mediana` | P81 |
| Histograma e equalização (afirmações) | `histograma` | P82 |
| Associar máscaras às matrizes | `sobel` | P83 |
| Fourier: espectro, fase, separabilidade | `fourier` | P84 |
| Objetivo de um filtro digital | `filtro` | P85 |
| O que não é modelo de imagem | `doi` | P86 |
| Objetivo da equalização | `equalização` | P87 |
| Resultado do passa-baixa | `passa-baixa` | P88 |
| O que não é técnica de PDI | `têmpera` | P89 |
| Wavelet | `wavelet` | P90 |
| Equalização de cores | `equalização` | P91 |
| Definição de quantização | `quantização` | P92 |
| Resultado da equalização | `equalização` | P93 |
| Visão estéreo | `estéreo` | P94 |
| Restauração de imagens (afirmações) | `restauração` | P95 |
| Codificação por planos de bits | `planos de bits` | P96 |
| Interpolação: vizinho, bilinear, bicúbica | `interpolação` | P97 |
| Rede neural de uma unidade | `perceptron` | P98 |
| Amostragem e quantização (lacunas) | `amostragem` | P99 |
| Filtragem: média, passa-baixa, laplaciano, domínios | `laplaciano` | P100 |
| Compressão: RLE, lossy, BMP | `rle` | P101 |
| Tamanho da máscara da média | `M×M` | P102 |
| JPEG | `jpeg` | P103 |
| Amostragem × quantização | `amostragem` | P104 |
| Filtros na frequência | `passa-alta` | P105 |

## Matemática (vetores e transformações lineares)

### `[S21]` Matemática que cai junto: vetores e transformações lineares

O que precisa saber: produto escalar e ângulo; produto vetorial e propriedades; normal de triângulo; equações do plano; reconhecer reflexão/rotação pela matriz; transformar normais; o que a afim preserva.

| assunto da questão | buscar | questões |
|---|---|---|
| Normais, compressão, iluminação local, cor, afim | `inversa transposta / saturação / mesma cor / sombra` | P16 |
| Reconhecer reflexão pela matriz | `reflexão através` | P52 |
| Normal de um triângulo por 3 pontos | `normal de um triângulo` | P54 |
| Ângulo de uma rotação dada por um par | `rotação dada por um par` | P55 |
| Propriedades do produto vetorial | `produto vetorial` | P56 |
| Plano por 3 pontos: equações, LI, normal | `equação geral` | P57 |
| Produto escalar e ângulo | `produto escalar` | P58 |
| Produto escalar e vetorial numéricos | `produto vetorial` | P59 |

## Resumos transversais

### `[S00]` Definições rápidas (descrição → nome)

O que precisa saber: tabela "descrição → nome" para as questões do tipo "estamos falando de um...".

| assunto da questão | buscar | questões |
|---|---|---|
| Associar técnicas às funções | `BSP / Cohen-Sutherland` | Q73, P27 |

### `[S01]` Confusões clássicas (o certo e com o que costuma ser confundido)

O que precisa saber: lista das confusões mais comuns, separadas por tema.

| assunto da questão | buscar | questões |
|---|---|---|
| Phong × Gouraud, z-buffer, homogêneo, malha triangular | `Gouraud / divide tudo por W / planar` | Q54, P19 |
| Raster, preenchimento, círculo, backface, zoom | `pisca` | Q68, P10 |
| Raster, backface, ponto médio do círculo | `pisca` | P12 |

## Índice por questão

Para treinar um assunto, abra a questão no [[Quiz de treino - banco do professor]] (Q..) ou no [[POSCOMP - Computação Gráfica]] (P..).

| questão | assunto | seção | buscar |
|---|---|---|---|
| Q01 | Algoritmos de recorte de polígonos | `[S05]` | `polígonos / Gauss` |
| Q02 | Ponto na viewport (coordenada y, y invertido) | `[S04]` | `viewport` |
| Q03 | Ponto recortado em SCN (coordenada y) | `[S04]` | `scn` |
| Q04 | Nome do algoritmo por códigos de região | `[S05]` | `region code` |
| Q05 | Ponto em SCN (coordenada y) | `[S04]` | `scn` |
| Q06 | Ponto recortado na viewport (coordenada y) | `[S04]` | `viewport / recorta` |
| Q07 | Ponto recortado em SCN (coordenada x) | `[S04]` | `scn` |
| Q08 | Region codes de dois pontos | `[S05]` | `region code` |
| Q09 | Ponto em SCN (coordenada x) | `[S04]` | `scn` |
| Q10 | Nome do algoritmo com pk e qk | `[S05]` | `pk` |
| Q11 | Ponto na viewport (coordenada x) | `[S04]` | `viewport` |
| Q12 | Region codes de dois pontos | `[S05]` | `region code` |
| Q13 | Nome do algoritmo por coeficientes angulares | `[S05]` | `coeficiente angular` |
| Q14 | Window × viewport: sistema, aspecto, zoom | `[S04]` | `zoom` |
| Q15 | Window, viewport, aspecto, onde recortar | `[S04]` | `viewport` |
| Q16 | Instanciamento e posição na window | `[S04]` | `instanciamento` |
| Q17 | Reconhecer matriz de translação 2D | `[S03]` | `translação` |
| Q18 | Sx e Sy: escala 2D | `[S03]` | `diagonal` |
| Q19 | Matriz de translação 3D | `[S09]` | `translação 3d` |
| Q20 | Expressão [x y 1]·M: homogêneas e W | `[S03]` | `homogêneas` |
| Q21 | Matriz de escala 3D | `[S09]` | `escala 3d` |
| Q22 | Reconhecer matriz de rotação 2D | `[S03]` | `rotação` |
| Q23 | Rotação 3D de 90° em Z | `[S09]` | `rz` |
| Q24 | Homogêneas 3D: pontos 4D e W | `[S03]` | `homogêneas` |
| Q25 | Reconhecer matriz de escala 2D | `[S03]` | `diagonal` |
| Q26 | Rotação 3D de 90° em X | `[S09]` | `rx` |
| Q27 | Escolher a matriz de translação 3D | `[S09]` | `translação 3d` |
| Q28 | Rotação 3D de 90° em Y | `[S09]` | `ry` |
| Q29 | Homogêneas e comutatividade | `[S03]` | `comutam` |
| Q30 | Girar em torno do centro de massa | `[S03]` | `em torno` |
| Q31 | Ler matrizes A e B (ordem, centro, mudança de base) | `[S03]` | `primeiro escala / mudança de base` |
| Q32 | Identificar a matriz de uma rotação + translação | `[S03]` | `vetor-coluna` |
| Q33 | Matriz aplicada a um vetor | `[S09]` | `coluna` |
| Q34 | Estrutura de arame e normal | `[S09]` | `arame` |
| Q35 | Vetor perpendicular a dois | `[S09]` | `perpendicular` |
| Q36 | Projeção paralela (marque as verdadeiras) | `[S10]` | `oblíqua / ignora Z` |
| Q37 | Características das projeções | `[S10]` | `perspectiva` |
| Q38 | Projeção de ponto num plano por direção | `[S09]` | `plano` |
| Q39 | Associar etapas da síntese de imagens | `[S10]` | `volume de visão / Gouraud` |
| Q40 | Afirmações sobre o pipeline 3D | `[S10]` | `pipeline` |
| Q41 | Ordem: recorte, projeção, rasterização, visibilidade | `[S10]` | `pipeline` |
| Q42 | Ordem: câmera, recorte 3D, projeção, tela, rasterização | `[S10]` | `pipeline` |
| Q43 | Nome da região recortada e projetada | `[S10]` | `volume de visão` |
| Q44 | Ordem das 5 transformações do pipeline | `[S10]` | `pipeline` |
| Q45 | Transformação de câmera | `[S10]` | `câmera` |
| Q46 | Superfície pela soma com Bernstein | `[S08]` | `bernstein` |
| Q47 | Componentes do modelo de Phong | `[S13]` | `phong` |
| Q48 | Para que servem as normais | `[S13]` | `normais` |
| Q49 | Radiância e radiosidade | `[S14]` | `radiosidade` |
| Q50 | Nome: raios num volume de voxels | `[S14]` | `voxel` |
| Q51 | Nome: cor e iluminação por pixel na GPU | `[S15]` | `pixel shader` |
| Q52 | Nome: raios de trás para frente | `[S14]` | `trás para frente` |
| Q53 | O que o ray tracing faz | `[S14]` | `ray tracing` |
| Q54 | Phong × Gouraud, z-buffer, homogêneo, malha triangular | `[S01]` | `Gouraud / divide tudo por W / planar` |
| Q55 | Normal de superfície paramétrica | `[S13]` | `paramétrica` |
| Q56 | Modelos de iluminação locais | `[S13]` | `lambert` |
| Q57 | Fonte de luz no infinito | `[S13]` | `direcional` |
| Q58 | Afirmações sobre ray tracing | `[S14]` | `ray tracing` |
| Q59 | Simular a propagação da luz | `[S14]` | `propagação` |
| Q60 | MSAA | `[S11]` | `msaa` |
| Q61 | Propriedades do z-buffer | `[S12]` | `z-buffer` |
| Q62 | Gouraud, volume paralelo, Bresenham, aliasing | `[S13]` | `gouraud` |
| Q63 | Textura que perturba a normal | `[S11]` | `bump` |
| Q64 | Duas esferas, uma escondendo a outra | `[S12]` | `z-buffer` |
| Q65 | MeshSmooth, bump map, flat shading | `[S02]` | `meshsmooth` |
| Q66 | Função em C que desenha | `[S11]` | `putpixel` |
| Q67 | Memória extra do mipmap | `[S11]` | `mipmap` |
| Q68 | Raster, preenchimento, círculo, backface, zoom | `[S01]` | `pisca` |
| Q69 | ECS | `[S02]` | `ecs` |
| Q70 | Pacote com motor gráfico, física, som... | `[S02]` | `engine` |
| Q71 | Exemplos de API gráfica | `[S02]` | `api` |
| Q72 | Distância do mouse ao centro | `[S02]` | `envelope` |
| Q73 | Associar técnicas às funções | `[S00]` | `BSP / Cohen-Sutherland` |
| Q74 | Filtros: qual afirmação é incorreta | `[S18]` | `laplaciano` |
| Q75 | Histograma, brilho/contraste, negativo | `[S18]` | `equalização` |
| Q76 | Definição de segmentação | `[S18]` | `segmentação` |
| Q77 | Passa-baixas numa imagem toda preta | `[S18]` | `passa-baixa` |
| P01 | Window × viewport: sistema, aspecto, zoom | `[S04]` | `zoom` |
| P02 | Propriedades do z-buffer | `[S12]` | `z-buffer` |
| P03 | Afirmações sobre o pipeline 3D | `[S10]` | `pipeline` |
| P04 | Ordem: câmera, recorte 3D, projeção, tela, rasterização | `[S10]` | `pipeline` |
| P05 | Instanciamento e posição na window | `[S04]` | `instanciamento` |
| P06 | Transformação de câmera | `[S10]` | `câmera` |
| P07 | O que o ray tracing faz | `[S14]` | `ray tracing` |
| P08 | Afirmações sobre ray tracing | `[S14]` | `ray tracing` |
| P09 | Pistas de profundidade | `[S10]` | `profundidade` |
| P10 | Raster, preenchimento, círculo, backface, zoom | `[S01]` | `pisca` |
| P11 | Projeção de ponto num plano por direção | `[S09]` | `plano` |
| P12 | Raster, backface, ponto médio do círculo | `[S01]` | `pisca` |
| P13 | Projeção de ponto num plano por direção | `[S09]` | `plano` |
| P14 | Distância do mouse ao centro | `[S02]` | `envelope` |
| P15 | Função em C que desenha | `[S11]` | `putpixel` |
| P16 | Normais, compressão, iluminação local, cor, afim | `[S21]` | `inversa transposta / saturação / mesma cor / sombra` |
| P17 | Identificar a matriz de uma rotação + translação | `[S03]` | `vetor-coluna` |
| P18 | Ordem: recorte, projeção, rasterização, visibilidade | `[S10]` | `pipeline` |
| P19 | Phong × Gouraud, z-buffer, homogêneo, malha triangular | `[S01]` | `Gouraud / divide tudo por W / planar` |
| P20 | Girar em torno do centro de massa | `[S03]` | `em torno` |
| P21 | Normal de superfície paramétrica | `[S13]` | `paramétrica` |
| P22 | Associar etapas da síntese de imagens | `[S10]` | `volume de visão / Gouraud` |
| P23 | Modelos de iluminação locais | `[S13]` | `lambert` |
| P24 | Duas esferas, uma escondendo a outra | `[S12]` | `z-buffer` |
| P25 | MSAA | `[S11]` | `msaa` |
| P26 | Gouraud, volume paralelo, Bresenham, aliasing | `[S13]` | `gouraud` |
| P27 | Associar técnicas às funções | `[S00]` | `BSP / Cohen-Sutherland` |
| P28 | Memória extra do mipmap | `[S11]` | `mipmap` |
| P29 | Estrutura de arame e normal | `[S09]` | `arame` |
| P30 | Ler matrizes A e B | `[S03]` | `primeiro escala / mudança de base` |
| P31 | Simular a propagação da luz | `[S14]` | `propagação` |
| P32 | Superfície pela soma com Bernstein | `[S08]` | `bernstein` |
| P33 | MeshSmooth, bump map, flat shading | `[S02]` | `meshsmooth` |
| P34 | Homogêneas e comutatividade | `[S03]` | `comutam` |
| P35 | Características das projeções | `[S10]` | `perspectiva` |
| P36 | Window, viewport, aspecto, onde recortar | `[S04]` | `viewport` |
| P37 | Nome da região recortada e projetada | `[S10]` | `volume de visão` |
| P38 | Ordem das 5 transformações do pipeline | `[S10]` | `pipeline` |
| P39 | Textura que perturba a normal | `[S11]` | `bump` |
| P40 | Vetor perpendicular a dois | `[S09]` | `perpendicular` |
| P41 | Fonte de luz no infinito | `[S13]` | `direcional` |
| P42 | Texturas: 2D, procedural, bump | `[S11]` | `textura` |
| P43 | Tonalização que interpola normais | `[S13]` | `phong shading` |
| P44 | Afirmações sobre ray tracing (z-buffer, difuso, secundários) | `[S14]` | `ray tracing` |
| P45 | O que não é técnica de superfície oculta | `[S12]` | `ocultas` |
| P46 | Matrizes A e B: centro, ordem, homogêneas | `[S03]` | `só a translação / primeiro escala` |
| P47 | Ray tracing, z-buffer e Phong (afirmações) | `[S14]` | `ray tracing` |
| P48 | Tarefas da etapa de rendering | `[S15]` | `rendering` |
| P49 | O que é mipmapping | `[S11]` | `mipmap` |
| P50 | Matriz de rotação em torno de um ponto (números) | `[S03]` | `em torno` |
| P51 | Flat, Gouraud e Phong (afirmações) | `[S13]` | `flat` |
| P52 | Reconhecer reflexão pela matriz | `[S21]` | `reflexão através` |
| P53 | Matriz aplicada a um vetor | `[S09]` | `coluna` |
| P54 | Normal de um triângulo por 3 pontos | `[S21]` | `normal de um triângulo` |
| P55 | Ângulo de uma rotação dada por um par | `[S21]` | `rotação dada por um par` |
| P56 | Propriedades do produto vetorial | `[S21]` | `produto vetorial` |
| P57 | Plano por 3 pontos: equações, LI, normal | `[S21]` | `equação geral` |
| P58 | Produto escalar e ângulo | `[S21]` | `produto escalar` |
| P59 | Produto escalar e vetorial numéricos | `[S21]` | `produto vetorial` |
| P60 | Definição de histograma | `[S18]` | `histograma` |
| P61 | Para que serve a mediana | `[S18]` | `mediana` |
| P62 | Descritores de textura | `[S18]` | `co-ocorrência` |
| P63 | Filtros: qual afirmação é incorreta | `[S18]` | `laplaciano` |
| P64 | Histograma, brilho/contraste, negativo | `[S18]` | `equalização` |
| P65 | Ordem das etapas da análise de imagens | `[S18]` | `análise de imagens` |
| P66 | Discretizar espaço e amplitude | `[S18]` | `amostragem` |
| P67 | Média × mediana (características) | `[S18]` | `mediana` |
| P68 | Convolução de [−1 2 −1] numa rampa | `[S18]` | `[−1 2 −1]` |
| P69 | Passa-baixas numa imagem toda preta | `[S18]` | `passa-baixa` |
| P70 | Técnicas de realce | `[S18]` | `realce` |
| P71 | Comprimento médio de código Huffman | `[S18]` | `huffman` |
| P72 | Contraste em cor sem mudar o tom | `[S18]` | `ihs` |
| P73 | Média e mediana 3×3 em padrões | `[S18]` | `mediana` |
| P74 | Filtro de diferença e orientação das bordas | `[S18]` | `direcional` |
| P75 | Definição de segmentação | `[S18]` | `segmentação` |
| P76 | Transformação do negativo | `[S18]` | `negativo` |
| P77 | O que é e o que não é segmentação | `[S18]` | `segmentação` |
| P78 | Luminância a partir de RGB | `[S18]` | `luminância` |
| P79 | Classificador de distância mínima | `[S18]` | `distância mínima` |
| P80 | Transformadas: núcleo separável e simétrico | `[S18]` | `separável` |
| P81 | Filtro para tirar pontos preservando forma | `[S18]` | `mediana` |
| P82 | Histograma e equalização (afirmações) | `[S18]` | `histograma` |
| P83 | Associar máscaras às matrizes | `[S18]` | `sobel` |
| P84 | Fourier: espectro, fase, separabilidade | `[S18]` | `fourier` |
| P85 | Objetivo de um filtro digital | `[S18]` | `filtro` |
| P86 | O que não é modelo de imagem | `[S18]` | `doi` |
| P87 | Objetivo da equalização | `[S18]` | `equalização` |
| P88 | Resultado do passa-baixa | `[S18]` | `passa-baixa` |
| P89 | O que não é técnica de PDI | `[S18]` | `têmpera` |
| P90 | Wavelet | `[S18]` | `wavelet` |
| P91 | Equalização de cores | `[S18]` | `equalização` |
| P92 | Definição de quantização | `[S18]` | `quantização` |
| P93 | Resultado da equalização | `[S18]` | `equalização` |
| P94 | Visão estéreo | `[S18]` | `estéreo` |
| P95 | Restauração de imagens (afirmações) | `[S18]` | `restauração` |
| P96 | Codificação por planos de bits | `[S18]` | `planos de bits` |
| P97 | Interpolação: vizinho, bilinear, bicúbica | `[S18]` | `interpolação` |
| P98 | Rede neural de uma unidade | `[S18]` | `perceptron` |
| P99 | Amostragem e quantização (lacunas) | `[S18]` | `amostragem` |
| P100 | Filtragem: média, passa-baixa, laplaciano, domínios | `[S18]` | `laplaciano` |
| P101 | Compressão: RLE, lossy, BMP | `[S18]` | `rle` |
| P102 | Tamanho da máscara da média | `[S18]` | `M×M` |
| P103 | JPEG | `[S18]` | `jpeg` |
| P104 | Amostragem × quantização | `[S18]` | `amostragem` |
| P105 | Filtros na frequência | `[S18]` | `passa-alta` |
