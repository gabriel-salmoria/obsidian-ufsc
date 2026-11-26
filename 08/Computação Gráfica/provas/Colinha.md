---
tags: [cg, prova, colinha]
---
# Colinha CG (INE5420), prova de 26/11/2026

Voltar: [[Computação Gráfica]] · treino: [[Quiz de treino - banco do professor]] (versão interativa: `quiz-treino.html`, nesta pasta) · questões das videoaulas: [[Banco de Questões]] · POSCOMP: [[POSCOMP - Computação Gráfica]] · fórmulas: [[Formulário]]

**Prova**: quinta 26/11, 08:20–10:00, 3º andar do INE. Quiz no Moodle com senha, ~10 questões em 55 min (5 min de leitura + ~5 min por questão). Assine a lista de presença. Pode consultar a internet, menos rede social e chat.

O professor faz questões novas a cada ano, mas no mesmo molde: "qual algoritmo é este", "marque as verdadeiras" com alternativas que trocam uma palavra, conta de window/viewport/clipping com resposta inteira, "que matriz é esta", e questões tiradas do POSCOMP. Esta página tenta cobrir o conceito por trás de cada uma.

## Como achar as coisas (Ctrl+F)
- Busque a **raiz da palavra sem a parte acentuada**: `proje` acha projeção/projetar, `ilumina`, `rota`, `transla`, `normaliz`, `recort`.
- Cada seção começa com uma linha `busca:` com sinônimos em português e inglês. Ex.: `hidden surface` cai no z-buffer, `scan conversion` na rasterização.
- Busque `[S07]` para ir direto à seção 7 (índice abaixo).
- `PEGADINHA` marca confusão comum. `CONTA` marca exemplo resolvido (com números inventados ou dos slides).

## Índice
- [S00] Definições rápidas: descrição → nome
- [S01] Confusões clássicas (o certo × o que costuma ser confundido)
- [S02] Conceitos básicos, displays, frame buffer, APIs, engines
- [S03] Transformações 2D e coordenadas homogêneas
- [S04] Window, viewport e SCN (zoom, contas)
- [S05] Clipping (recorte)
- [S06] Curvas: Hermite, Bézier, de Casteljau, continuidade
- [S07] B-splines e forward differences
- [S08] Superfícies bicúbicas
- [S09] 3D: matrizes, eixo arbitrário, normal, plano, OBJ
- [S10] Projeções e pipeline 3D
- [S11] Rasterização: retas, círculos, preenchimento, aliasing, texturas
- [S12] Superfície oculta: z-buffer, pintor, backface, BSP
- [S13] Iluminação: Phong, Lambert, fontes de luz, shading
- [S14] Raytracing, raycasting e radiosidade
- [S15] GPU, shaders e pipeline do OpenGL
- [S16] Modelos hierárquicos e animação
- [S17] Cor
- [S18] Processamento de imagens: digitalização, histograma, filtros, frequência, segmentação, compressão
- [S19] Nomes e datas
- [S20] Distratores e dicas de prova
- [S21] Matemática que cai junto: produto escalar e vetorial, plano, reconhecer rotação/reflexão
- Mapa dos assuntos e de onde cada um está explicado: [[Mapa do que cai]]

---

## [S00] Definições rápidas (descrição → nome)
busca: qual algoritmo, qual técnica, como se chama, denomina, nome, estamos falando de

| Descrição | Nome |
|---|---|
| recorte de retas com **códigos de região** / region code / 4 bits / AND lógico | **Cohen-Sutherland** |
| recorte de retas com parâmetros **pk e qk** / equação **paramétrica** / u1 u2 (zeta) | **Liang-Barsky** (reformulação do **Cyrus-Beck**) |
| recorte comparando **coeficiente angular** (inclinação) com retas de P1 aos cantos | **Nicholl-Lee-Nicholl** (só 2D) |
| recorte que divide a reta ao meio recursivamente | **subdivisão do ponto médio** (midpoint subdivision) |
| recorte de **polígonos** | **Sutherland-Hodgeman** (Hodgman) e **Weiler-Atherton** |
| polígono côncavo, com buraco, que vira vários polígonos | **Weiler-Atherton** |
| recorta o polígono contra uma borda da window por vez | **Sutherland-Hodgeman** |
| recorte contra janela **convexa** qualquer / normais das bordas / produto escalar | **Cyrus-Beck** |
| traçar reta só com **inteiros** e variável de decisão | **Bresenham** |
| traçar reta somando m (ponto flutuante) e arredondando | **DDA** |
| círculo com simetria de 8 octantes | **ponto médio para círculo** (Bresenham de círculo) |
| preencher região a partir de um ponto semente até a cor da borda | **boundary-fill** (até a borda) / **flood-fill** (troca uma cor) |
| desenhar curva com **3 somas por ponto**, sem multiplicação | **forward differences** (diferenças adiante) |
| curva por **pontos médios recursivos** | **de Casteljau** |
| raios **de trás para frente**, do observador, **um por pixel** | **Ray Tracer** |
| raios dentro de **volume 3D denso**, **voxels**, tomografia, ressonância, radar | **Ray Caster volumétrico** |
| só a 1ª interseção, sem raio secundário | **Ray Casting** |
| cor e iluminação **por pixel**, roda na **GPU** | **Pixel Shader** (ou Ray Shader) |
| inter-reflexão **difusa**, interação luminosa entre objetos, color bleeding | **Radiosidade / Radiância** (iluminação global) |
| fator de forma, hemicubo (semicubo), analogia de Nusselt | **Radiosidade** |
| simular a propagação da luz e sua interação com as superfícies | **Ray Tracing** |
| buffer de **profundidade** por pixel, superfície visível | **Z-buffer** |
| ordena e pinta do **fundo para a frente** | **algoritmo do pintor** |
| descarta faces de costas (normal aponta para longe do olho) | **backface culling** |
| árvore de **partição binária do espaço** | **BSP** (subdivisão espacial) |
| interpola **cores/intensidades** dos vértices | **Gouraud** |
| interpola **normais**, iluminação por pixel | **Phong shading** |
| 1 cor por face | **flat shading** |
| 3 componentes **aditivas**: difusa, especular, ambiente | **modelo de Phong** |
| difusa proporcional ao cosseno entre N e L | **lei de Lambert** |
| luz no **infinito**, raios paralelos, como o Sol | **fonte direcional** |
| perturba a **normal** sem mudar a geometria | **bump mapping** |
| reflete o ambiente numa textura | **environment mapping** |
| pirâmide de texturas pré-filtradas (custa +33% de memória) | **mipmap** |
| várias amostras de cobertura por pixel, shading 1× por pixel | **MSAA** |
| motor gráfico + física + som + IA + rede + grafo de cena + script | **Game Engine** |
| entidades = IDs, componentes = dados, composição em vez de herança | **ECS** (Entity Component System) |
| API gráfica atual | **OpenGL, WebGL, Direct3D** (também Vulkan, Metal). **DirectX não** |
| lista de todos os objetos do mundo | **Display File** |
| memória com a matriz de pixels | **Frame buffer** |
| canhão desenha cada objeto, sem pixel | display **vetorial / random scan** (caligráfico) |
| tiras de aço da construção naval com pesos ("ducks") | origem do nome **spline** |
| controle local, C2, não passa pelos pontos | **B-spline** |
| passa no 1º e no 4º ponto, fecho convexo | **Bézier** |
| 2 pontos + 2 tangentes | **Hermite** |
| passa por todos os pontos, C2, controle global | **spline cúbica natural** |
| soma dupla de pontos de controle com funções de **Bernstein** em s e t | **superfície de Bézier** |
| 16 pontos de controle | **Bézier bicúbica** |
| cubo × pirâmide truncada | volume canônico **paralela × perspectiva** |
| região do mundo que será recortada e projetada | **volume de visão** (view volume) |
| 6 bits | **Cohen-Sutherland 3D** |
| W constante e ≠ 0, usamos W = 1 | **coordenadas homogêneas** |
| homogêneas são necessárias para... | representar **translação** como multiplicação de matriz |
| ignorar Z | **paralela ortogonal** (nunca perspectiva) |
| dividir x e y por z/d | **perspectiva** |
| isométrica | paralela **oblíqua axonométrica** (classificação do professor) |
| cavaleira, cabinet | paralela **oblíqua (pictórica)** |
| normal de face com 3 pontos | **produto vetorial** (não interno) |
| vetor perpendicular a outros dois | **produto vetorial** |
| ângulo entre vetores, cosseno | **produto escalar** (interno) |
| por que calcular normais | **difusa e especular** (não ambiente, sombra ou transparência) |
| transformação de instância | **T·R·S** (escala, gira, posiciona) |
| pilha de matrizes push/pop | percorrer **modelo hierárquico** |
| dados os ângulos, onde fica a mão | **cinemática direta** (a inversa faz o contrário) |
| esqueleto ligado à malha | **rigging / skinning** |
| modelo de cor subtrativo, gráfica, impressão | **CMYK** |
| aditivo, monitor, imita os cones | **RGB** |
| todas as cores visíveis num vetor 3D | **CIE 1931 (XYZ)** |
| tom, saturação, valor | **HSV / HSI** |
| capacidade de um monitor representar cores (polígono no CIE) | **gamut** |
| tabela de cores / paleta | **indexed color** |
| pouca luz, visão noturna, não vê cor | **bastonetes** |
| muita luz, 3 tipos, cor | **cones** (curto/azul, médio/verde, longo/vermelho) |
| calculam a segunda derivada do sinal | **células horizontais** da retina |
| "tela mental", só intensidade | **córtex visual primário** |
| integra a cor, não forma imagem | **córtex visual terciário** |
| filtro que suaviza / tira ruído | **passa-baixas** (média, gaussiano; mediana é não linear) |
| filtro que realça borda | **passa-altas** (Laplaciano, Sobel, Prewitt, Roberts) |
| agrupar pixels em regiões homogêneas | **segmentação** |
| discretizar as **coordenadas** da imagem | **amostragem** |
| discretizar a **amplitude** (níveis de cinza) | **quantização** |
| usa o histograma acumulado, espalha os níveis | **equalização de histograma** (aumenta contraste) |
| s = (L − 1) − r | **negativo** da imagem |
| tirar ruído sal e pimenta preservando bordas | **mediana** |
| máscara 2×2 / 3×3 com 1 / 3×3 com 2 / centro −4 | **Roberts / Prewitt / Sobel / Laplaciano** |
| [−1 2 −1] numa rampa dá zero | **Laplaciano** discreto (2ª derivada) |
| |F|² = R² + I² / arctan(I/R) | **espectro de potência / ângulo de fase** (Fourier) |
| multirresolução, localiza frequência e posição | **wavelet** |
| blocos 8×8 → DCT → quantização | **JPEG** |
| decompõe a imagem em várias imagens binárias | **codificação por planos de bits** |
| códigos curtos para os símbolos mais prováveis | **Huffman** (comprimento médio = Σ p·tamanho) |
| corridas de valores iguais, áreas uniformes | **RLE** |
| 4 vizinhos / 16 vizinhos / copia o vizinho | interpolação **bilinear / bicúbica / vizinho mais próximo** |
| recuperar imagem modelando a degradação e invertendo | **restauração** (realce é subjetivo) |
| duas câmeras, mapa de disparidade | **visão estéreo** |
| uma unidade, só linearmente separável | **perceptron** |
| menor distância ao vetor médio de cada classe | **classificador de distância mínima** |
| têmpera simulada (simulated annealing) | **não é técnica de PDI** (é otimização) |
| contraste da imagem colorida sem mudar o tom | RGB → **IHS**, mexe em I, volta |
| como normais se transformam | pela **inversa transposta** (M⁻¹)ᵀ ([S21]) |
| matriz ortogonal com det −1 | **reflexão** ([S21]) |
| testar caixa/esfera simples em volta do objeto antes | **volumes envolventes** (bounding volumes) |
| tamanho, textura, interposição, sombra, paralaxe | **pistas de profundidade** ([S10]) |

---

## [S01] Confusões clássicas (o certo e com o que costuma ser confundido)
busca: verdadeiro, falso, correto, incorreto, afirmar, assertivas, afirmativas, marque todas, confusão, cuidado

Resumo das trocas de palavra que mais derrubam. O detalhe de cada uma está na seção indicada.

**Homogêneas e transformações** ([S03], [S09], [S21])
- Em homogêneas **toda** transformação geométrica vira produto de matrizes, inclusive a translação. Não é só rotação ou só escala.
- W é o fator de escala: constante e diferente de zero, e usamos 1 por simplicidade. Não é 0, não é −1, não depende da norma do ponto, e o "1" é escolha, não obrigação. Homogêneas não são o mesmo que SCN e não exigem normalizar antes.
- 2D homogêneo é 3×3; 3D homogêneo é 4×4.
- Translação não é linear, por isso precisa da dimensão extra. Rotação e escala em torno da origem não precisariam.
- Escala uniforme comuta com rotação; rotações 3D em eixos diferentes não comutam.
- Ponto homogêneo → cartesiano: divide tudo por W.
- Rotação "pura" gira em torno da origem, não do centro do objeto.

**Window, viewport, clipping** ([S04], [S05])
- Window é do mundo; viewport é do dispositivo (tela). Não estão no mesmo sistema.
- Proporção diferente entre window e viewport = escala não uniforme (distorce).
- Window menor com a viewport fixa = zoom in; window maior = zoom out.
- O y da viewport cresce para baixo.
- Recorte pode ser feito no mundo, na tela ou em coordenadas normalizadas.

**Projeções** ([S10])
- "Dois tipos de projeção" (geral) = paralela e perspectiva. "Dois tipos de **paralela**" = ortogonal (ortográfica) e oblíqua (pictórica).
- Na classificação do professor a isométrica fica em paralela oblíqua axonométrica; cavaleira e cabinet também são oblíquas. Isométrica nunca é perspectiva.
- Ignorar Z depois de normalizar é a paralela **ortogonal**. A perspectiva exige dividir por z/d.
- Paralela: raios paralelos, tamanho aparente não muda com a distância (por isso às vezes parece distorcida), centro de projeção no infinito, volume de visão paralelepípedo. Perspectiva: raios convergem no COP (pirâmide), tamanho cai com a distância (inversamente proporcional), volume tronco de pirâmide, não preserva ângulos nem medidas, e cabe numa matriz 4×4.

**Rasterização e visibilidade** ([S11], [S12])
- Z-buffer: não ordena nada, calcula o z de forma incremental, tem um valor por pixel (mesmo tamanho do frame buffer), guarda o mais próximo e não é detecção de colisão. A ordem de desenho não muda a imagem.
- Aliasing aparece em qualquer rasterização, inclusive de triângulos 2D.
- Preenchimento com vizinhança 4 não garante preencher tudo (não atravessa diagonais).
- Ponto médio do círculo: o sinal de "dentro/fora" depende de como f foi escrita (x² + y² − r² ou r² − x² − y²).
- Piscar com cena complexa é problema do display vetorial (random scan), não do raster.
- Backface sozinho só resolve a visibilidade de **um** objeto convexo.
- Triângulo é sempre planar.

**Iluminação** ([S13], [S14])
- Phong (modelo): 3 componentes que se **somam**: difusa (direta), especular, ambiente (indireta). Não existe "componente transparente" e não são 4.
- A normal é usada na difusa e na especular. Ambiente não usa normal; sombra precisa de raio até a luz; transparência é outra coisa.
- Difusa não depende do observador; especular depende.
- Especular tem a cor da luz; difusa tem a cor do objeto.
- Gouraud interpola **cores** (suavidade depende do tamanho dos triângulos); Phong shading interpola **normais**.
- Gouraud e Phong são locais: não fazem sombra de um objeto no outro nem dependem da cor do vizinho.
- Ray tracing usa um modelo local (Phong) em cada ponto atingido e soma reflexão e refração; o número de raios depende da cena; depende da câmera; paraleliza fácil.
- Radiosidade independe do ponto de vista; ray tracing depende.

**Processamento de imagens e matemática** ([S18], [S21])
- Amostragem = coordenadas; quantização = amplitude.
- Equalização: não linear, usa histograma acumulado, **aumenta** o contraste; repetir não muda nada.
- Média: linear, borra contornos, ruído gaussiano. Mediana: não linear, ruído impulsivo, preserva bordas. Laplaciano é passa-altas.
- Média e mediana são filtros espaciais (vizinhança); passa-baixa/passa-alta/rejeita-banda são definidos na frequência. Passa-alta na frequência faz o papel do realce espacial.
- Fourier 2D tem núcleo separável e simétrico. JPEG usa DCT.
- Histograma diz se a imagem é clara ou escura, mas não se duas imagens são da mesma cena.
- RLE é sem perdas; JPEG é com perdas; BMP normalmente nem comprime.
- Produto vetorial é distributivo, mas não é comutativo nem associativo, e zero não implica vetores nulos.
- Afim leva convexo em convexo. Normais se transformam pela inversa transposta.

**APIs e engines** ([S02])
- API gráfica: OpenGL, WebGL, Direct3D (Vulkan, Metal). DirectX é a coleção inteira; Blender, Unity, Moray e POV-Ray não são APIs.
- ECS prefere composição (agregar componentes) a herança e polimorfismo.

---

## [S02] Conceitos básicos
busca: computação gráfica definição, display file, frame buffer, random scan, raster, vetorial, double buffer, API, engine, modelador, flicker, envelope circular, mouse, picking, distância euclidiana, API gráfica, biblioteca gráfica, pacote de software, ECS, entidade, componente, MeshSmooth, modificador

- **CG**: métodos e técnicas para representar graficamente, com computador, objetos de um mundo real ou virtual. Implica um **modelo interno** do mundo e **transformações** que levam esse modelo a um dispositivo de saída.
- **CG × processamento de imagens × visão computacional**: CG faz modelo → imagem (síntese); processamento de imagens faz imagem → imagem; visão computacional (análise) faz imagem → descrição/modelo.
- Começou com **CAD** (substituir a prancheta): IBM Catia, AutoCAD. **Sketchpad** (Ivan Sutherland, 1963) foi o primeiro sistema gráfico interativo.
- **Display vetorial (random scan, caligráfico)**: o canhão desenha cada objeto, não existe pixel nem frame buffer, e a cena é redesenhada em loop a partir da **display file**. Com cena complexa o redesenho demora e a imagem **pisca (flicker)**.
- **Raster scan**: varre a tela inteira a uma taxa fixa, a partir do **frame buffer** (matriz de pixels). A taxa de redesenho não depende da cena. TV antiga era **entrelaçada** (linhas pares e ímpares alternadas).
- **Display File**: lista de todos os objetos do mundo. No SGI cada objeto tem nome, tipo (ponto, reta, wireframe, curva...) e lista de coordenadas.
- **Frame buffer**, CONTA: memória = largura × altura × bits/8. 1024×768 a 24 bits = 2.359.296 bytes (2,25 MiB). 1920×1080 a 24 bits = 6.220.800 bytes. Nº de cores = 2^bits (24 bits = 16.777.216; 8 bits = 256).
- **Double buffering**: desenha no buffer de trás e troca com o da frente, para não mostrar a imagem pela metade.
- **API gráfica**: biblioteca de funções otimizadas de desenho que gera código para a GPU: **OpenGL, WebGL, Direct3D**, Vulkan, Metal. **DirectX** é uma coleção (Direct3D + som + entrada + ...), então não é a resposta para "API gráfica".
- **Game engine**: motor gráfico + física/colisão + animação + som + IA + rede + memória/arquivos/threads + grafo de cena + linguagem de script. Unity, Unreal, Godot.
- **ECS** (Entity Component System): entidade é só um ID, componentes guardam dados, sistemas processam. Composição em vez de herança.
- **Modelador 3D**: Blender, Moray (modelador para o POV-Ray), 3ds Max, Maya. **Raytracer**: POV-Ray, Radiance, Cycles (Blender), V-Ray, Mental Ray.
- **Picking com envelope circular** (clicar num objeto): calcula a distância euclidiana do mouse ao centro, dist = sqrt((xmouse − xc)² + (ymouse − yc)²), e compara com o raio (dentro se dist ≤ raio). Em C: `sqrt(pow(xm - xc, 2) + pow(ym - yc, 2))`.
- Termos de modelagem: **MeshSmooth** é modificador de malha, **bump map** é textura, **flat shading** é método de renderização.

---

## [S03] Transformações 2D e coordenadas homogêneas
busca: translação, translacao, escala, escalonamento, rotação, rotacao, cisalhamento, shear, reflexão, espelhamento, homogêneas, homogeneas, matriz, composição, concatenação, inversa, ordem, comutativa, W, matriz acima, reconhecer matriz, vetor-linha, vetor-coluna, centro de massa, pivô, mudança de base, pré-multiplicação, pós-multiplicação, comutativa, ordem das transformações

**Primitivas** (sem homogêneas):
- translação: x' = x + Dx, y' = y + Dy (é soma, não produto)
- escala: x' = x·Sx, y' = y·Sy
- rotação em torno da origem, anti-horária: x' = x·cosθ − y·senθ, y' = x·senθ + y·cosθ

**Homogêneas**: (x, y) vira (W·x, W·y, W) com W ≠ 0 e volta dividindo por W. Usamos W = 1. W = 0 representa direção (vetor, ponto no infinito), que não é afetada por translação. Com isso translação, escala e rotação viram todas uma matriz 3×3 (4×4 em 3D).

**Convenção do professor: vetor-linha**, [x' y' 1] = [x y 1]·M, translação na **última linha**:
```
T = | 1  0  0 |    S = | Sx 0  0 |    R = |  cos  sen  0 |
    | 0  1  0 |        | 0  Sy 0 |        | -sen  cos  0 |
    | Dx Dy 1 |        | 0  0  1 |        |  0    0   1 |
```
Em **vetor-coluna** (OpenGL, livros, POSCOMP) tudo aparece **transposto**: translação na última **coluna**, e a rotação fica [[cos, −sen], [sen, cos]]. Reconheça pela forma: cos/sen no bloco 2×2 = rotação; diagonal = escala; Dx, Dy fora da diagonal na borda = translação.

Genérica: `| a d 0 | b e 0 | c f 1 |` (a, b, d, e: rotação, escala, cisalhamento; c, f: translação).

Outras matrizes (vetor-linha; as diagonais servem para os dois):
- reflexão no eixo x (y → −y): diag(1, −1, 1); no eixo y: diag(−1, 1, 1); na origem: diag(−1, −1, 1); na reta y = x: troca x e y, `|0 1 0|1 0 0|0 0 1|`
- cisalhamento em x: x' = x + sh·y → `|1 0 0|sh 1 0|0 0 1|`

**Composição**: com vetor-linha a matriz final é o produto **na ordem de aplicação**, M = M1·M2·M3 (primeira à esquerda). Com vetor-coluna é o contrário, M = M3·M2·M1 (primeira à direita). PEGADINHA: veja qual convenção o enunciado usa. Ex.: girar em torno de um ponto p em vetor-coluna é T(p)·R·T(−p) (a primeira a agir, T(−p), fica à direita); em vetor-linha a mesma coisa é T(−p)·R·T(p).

**Comutam**: duas translações; duas escalas; duas rotações 2D; escala **uniforme** com rotação. **Não comutam**: translação com rotação ou escala; escala não uniforme com rotação; rotações 3D em eixos diferentes.

**Inversas**: T(Dx,Dy)⁻¹ = T(−Dx,−Dy); S(Sx,Sy)⁻¹ = S(1/Sx,1/Sy); R(θ)⁻¹ = R(−θ) = Rᵀ. (M1·M2)⁻¹ = M2⁻¹·M1⁻¹. M·M⁻¹ = identidade (é o que os exercícios g, h, i da lista mostram).

**Em torno de um ponto c** (centro do objeto = média dos vértices): leva c à origem, transforma, volta. Vetor-linha: M = T(−c)·X·T(c). Escala em torno de c:
```
| a        0        0 |
| 0        b        0 |
| cx(1-a)  cy(1-b)  1 |
```
Em **vetor-coluna**, girar θ em torno de P é M = T(P)·R(θ)·T(−P), e o resultado é o bloco de rotação com a translação **P − R·P** na última coluna. Ex.: 90° em torno de (1, 1): R·P = (−1, 1), então a translação é (1 − (−1), 1 − 1) = (2, 0).

Ler uma matriz composta em **vetor-coluna** (P' = M·P, "pré-multiplicação"):
- `|Ex 0 Tx| 0 Ey Ty| 0 0 1|` dá x' = Ex·x + Tx: **primeiro escala, depois translada** (se transladasse antes, seria Ex·(x + Tx)).
- Girar θ e depois transladar d: M = T(d)·R(θ) = `|cos −sen dx| sen cos dy| 0 0 1|`. Ex.: girar 45° e subir 3 → `|cos45 −sen45 0| sen45 cos45 3| 0 0 1|`.
- Em vetor-linha a mesma transformação aparece **transposta** (translação na última linha e sinais do seno trocados de lugar). Se uma alternativa tem a translação na linha de baixo e o enunciado usa coluna, desconfie.

**Mudança de base / de sistema de coordenadas** em 2D: é uma composição de translação, rotação e escala (exemplo direto: a transformação do mundo para o SCN em [S04], M = T(−WC)·R(−θ)·S(2/w, 2/h)).

Por que homogêneas: rotação e escala (em torno da origem) já são lineares e funcionam com matriz 2×2; **só a translação** obriga a usar a dimensão extra. Então "homogêneas são necessárias para a rotação" é falso; para a translação é verdadeiro.

Sem as translações a escala "incha e desloca" o objeto (escala também a distância à origem).

**Propriedades**: afim (translação, rotação, escala, cisalhamento, reflexão) preserva retas, paralelismo e razão entre comprimentos na mesma reta. Rígida (rotação + translação) preserva distâncias e ângulos. det(R) = 1, det(reflexão) = −1, det(S) = Sx·Sy (fator de área).

CONTA rotação: (6,1) girado 30° anti-horário = (6·0,866 − 1·0,5; 6·0,5 + 1·0,866) = (4,70; 3,87).
PEGADINHA de sentido: na lista de exercícios do professor, "(2; 2,5) rodado 30°" dá (2,98; 1,16), que é o sentido **horário**; o slide usa anti-horário. Se nenhuma alternativa bater, teste o outro sentido.
- anti-horário: (2; 2,5) → (0,48; 3,17). Horário: (2,98; 1,17).

Ponto × vetor: ponto tem W = 1 e sofre translação; vetor (direção) tem W = 0 e só sofre rotação e escala.

---

## [S04] Window, viewport e SCN
busca: window, janela, viewport, janela de visão, transformada de viewport, SCN, coordenadas normalizadas, sistema de coordenadas da window, WC, window center, zoom, pan, navegação, VUP, rotação da window, SRU, sistema de referência do universo, relação de aspecto, instanciamento, coordenadas de window, coordenadas de viewport, clipagem, mundo 2D, window center

- **Window**: retângulo do **mundo** que vai aparecer (coordenadas do mundo / SRU). Tamanho variável = **zoom**, posição variável = **pan**.
- **Viewport**: área da **tela** onde se desenha (coordenadas do dispositivo). O **y cresce para baixo**.
- **Zoom**: window menor (viewport fixa) = menos mundo na mesma tela = **zoom in** (aproxima). Window maior = **zoom out**. PEGADINHA frequente.
- Proporções diferentes entre window e viewport = escala diferente em x e y = **distorção** (quadrado vira retângulo).

**Transformada de viewport**:
```
xv = xvmin + (xw - xwmin) / (xwmax - xwmin) * (xvmax - xvmin)
yv = yvmin + (1 - (yw - ywmin) / (ywmax - ywmin)) * (yvmax - yvmin)
```
O `1 −` no y é porque o y da viewport aponta para baixo. Se a viewport tem origem deslocada, some a origem.

**SCN** (sistema de coordenadas normalizado, ou da window): origem no centro da window (WC), domínio [−1, 1]:
```
x_scn = 2 * (x - xwmin) / (xwmax - xwmin) - 1   =  (x - xc) / (largura/2)
y_scn = 2 * (y - ywmin) / (ywmax - ywmin) - 1   =  (y - yc) / (altura/2)
```
De SCN para a viewport: xv = (x_scn + 1)/2 · largura_vp; yv = (1 − (y_scn + 1)/2) · altura_vp (mais a origem da viewport).

**Gerar a descrição em SCN** (window que pode girar): 1) translada o mundo por −WC; 2) acha o ângulo θ entre o **VUP** (view-up) da window e o eixo Y; 3) gira o mundo por −θ; 4) escala por (2/largura, 2/altura); 5) guarda as coordenadas normalizadas em cada objeto (sem perder as de mundo); 6) recorta em SCN; 7) viewport. Tudo é uma matriz: M = T(−WC)·R(−θ)·S(2/w, 2/h). Zoom só muda S, pan só muda T, girar a window só muda R.

**CONTA (exemplo)**: window (20,10)–(28,22) → centro (24, 16), largura 8, altura 12, meia-largura 4, meia-altura 6. Viewport 400×300 com origem em (5,5).
- Ponto (22,19) em SCN: x = (22 − 24)/4 = −0,5; y = (19 − 16)/6 = 0,5.
- Reta horizontal (16,14)–(26,14): o ponto (16,14) está à esquerda (x < 20), então o novo extremo é (20,14), em cima da borda esquerda. Em SCN: x = (20 − 24)/4 = −1 e y = (14 − 16)/6 = −0,33 (se a questão pede inteiro, arredonda para 0). O outro extremo (26,14) já está dentro: x = 0,5.
- O mesmo ponto (26,14) na viewport: xv = 5 + (26 − 20)/8 · 400 = 305; yv = 5 + (1 − (14 − 10)/12)·300 = 5 + 200 = 205. Lembre que o y inverte e que a origem (5,5) soma.
- Receita: 1) acha o centro e as meias-dimensões da window; 2) recorta (descobre quem saiu e por qual borda); 3) aplica a fórmula pedida (SCN ou viewport) no ponto já recortado.

**CONTA (instanciamento na window)**: window (0,0)–(40,40), viewport (0,0)–(200,100), triângulo (5,0)–(5,10)–(15,0); aplica escala (2,1) e depois translação (0,5). Escala: (10,0), (10,10), (30,0). Translação: (10,5), (10,15), (30,5). Na window: o lado vertical fica em x = 10/40 = 1/4 da largura e vai de 1/8 a 3/8 da altura; o terceiro vértice fica a 3/4 da largura, embaixo. Como a viewport é 2:1 e a window 1:1, o desenho sai esticado na horizontal. Receita: aplica as transformações na ordem dada, depois vê a posição relativa de cada vértice na window (fração da largura e da altura).

**CONTA (aspecto e zoom)**: window (0,0)–(80,80) (1:1) numa viewport (0,0)–(400,200) (2:1): proporções diferentes, a imagem distorce. Trocar a window por (0,0)–(40,40) mostra metade do mundo na mesma viewport, ou seja zoom in (2×).

---

## [S05] Clipping (recorte)
busca: clipping, recorte, recortar, clipar, clipagem, Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl, NLN, Sutherland-Hodgeman, Sutherland-Hodgman, Weiler-Atherton, region code, RC, código de região, ponto médio, polígono côncavo, clipagem, RC, códigos de regiões, coeficientes angulares, parâmetros pk qk, recorte de retas, recorte de polígonos

Para que serve: descobrir o que está dentro da região visível e só rasterizar isso (pré-processamento de visibilidade). O professor recorta em **SCN**, contra o quadrado [−1, 1].

**Ponto**: desenha se xmin ≤ x ≤ xmax e ymin ≤ y ≤ ymax.

**Cohen-Sutherland (retas)**. Region code de 4 bits na ordem do professor: **[acima, abaixo, direita, esquerda]**, valores 8, 4, 2, 1.
```
1001 | 1000 | 1010
-----+------+-----
0001 | 0000 | 0010
-----+------+-----
0101 | 0100 | 0110
```
- os dois códigos 0000 → desenha inteira
- código1 AND código2 ≠ 0000 → os dois do mesmo lado de fora → descarta
- senão calcula interseções. Borda vertical (x conhecido): y = m·(x_borda − x1) + y1. Borda horizontal (y conhecido): x = x1 + (y_borda − y1)/m. Se o ponto calculado cai fora da outra faixa, não vale; se nenhuma interseção vale, a reta está fora.
- CONTAS (window (10,20)–(30,30), da revisão do professor):
  - (0,24)–(16,14): RCs 0001 e 0100, AND = 0; esquerda dá y = 17,75 (< 20, fora); baixo dá x = 6,4 (< 10, fora) → **fora**.
  - (0,26)–(16,26): esquerda dá y = 26 → **(10,26)–(16,26)**.
  - (22,24)–(38,24): direita → **(22,24)–(30,24)**.
  - (34,26)–(18,36): RCs 0010 e 1000; direita y = 28,5; topo x = 27,6 → **(30; 28,5)–(27,6; 30)**.
  - (−4,40)–(−4,24): 1001 AND 0001 = 0001 → **descarta**.
  - (6,22)–(36,12): RCs 0001 e 0110; esquerda y = 20,67 ✓; direita y = 14 ✗; baixo x = 12 ✓ → **(10; 20,67)–(12,20)**.
  - Slide: window (10,10)–(25,20), (5,12)–(15,17) → **(10; 14,5)–(15,17)**; (5,18)–(15,23) → fora (na esquerda y = 20,5).

**Liang-Barsky** (reformula Cyrus-Beck). Reta paramétrica x = x1 + u·Δx, y = y1 + u·Δy, 0 ≤ u ≤ 1.
```
p1 = -Δx   q1 = x1 - xmin
p2 =  Δx   q2 = xmax - x1
p3 = -Δy   q3 = y1 - ymin
p4 =  Δy   q4 = ymax - y1        r_k = q_k / p_k
```
- p_k = 0: paralela àquela borda; se q_k < 0, está fora (descarta).
- p_k < 0: entra (fora → dentro): ζ1 = max(0, esses r).
- p_k > 0: sai (dentro → fora): ζ2 = min(1, esses r).
- ζ1 > ζ2 → fora. Senão os novos extremos são P(ζ1) e P(ζ2); ζ1 = 0 ou ζ2 = 1 deixa aquele extremo como está.
- CONTA (5,12)–(15,17), window (10,10)–(25,20): p = (−10, 10, −5, 5), q = (−5, 20, 2, 8); ζ1 = max(0; 0,5) = 0,5 → (10; 14,5); ζ2 = min(1; 2; 1,6) = 1.
- CONTA (6,22)–(36,12), window (10,20)–(30,30): p = (−30, 30, 10, −10), q = (−4, 24, 2, 8); ζ1 = max(0; 0,133; −0,8) = 0,133 → (10; 20,67); ζ2 = min(1; 0,8; 0,2) = 0,2 → (12,20). (O PDF do professor tem q4 = 6 e r2 = 1,875 por erro de cópia; o resultado não muda.)
- CONTA (0,24)–(16,14): ζ1 = 0,625 > ζ2 = 0,4 → fora.

**Exercício em SCN** (window [−1,1], do Moodle):
- (−4; 0,5)–(−0,1; 2,5): RCs 0001 e 1000, AND = 0, mas esquerda dá y = 2,04 e topo dá x = −3,03 → **fora** (LB: ζ1 = 0,77 > ζ2 = 0,25).
- (−1,5; 0)–(0,9; 0,4): esquerda → **(−1; 0,083)–(0,9; 0,4)**.
- (−1,5; −1)–(1; 0,5): esquerda → **(−1; −0,7)–(1; 0,5)**.
- (0,4; −0,2)–(2,8; 1,5): RC de p2 = 1010; direita y = 0,225 ✓, topo x = 2,09 ✗ → **(0,4; −0,2)–(1; 0,225)**.

**Nicholl-Lee-Nicholl** (só 2D): classifica P1 em uma das 9 regiões (só 3 casos de verdade, o resto por simetria), traça retas de P1 aos 4 cantos e descobre por **comparação de inclinações** em qual região P2 cai. Isso diz quais bordas cortam a reta. Menos divisões que CS e LB. Heurística mais simples para escolher contra quais retas de referência comparar: olhe de que lado de P1 o P2 está (sinal de Δx e Δy, ou o region code de P2); só os cantos daquele lado importam.

**Subdivisão do ponto médio**: se CS não decide, divide a reta ao meio e repete nas metades até aceitar/descartar ou chegar ao tamanho de um pixel. Só soma e divisão por 2 (bom para hardware).

**Polígonos** (recortar como várias retas não serve, o resultado tem que ser fechado):
- **Sutherland-Hodgeman**: recorta o polígono inteiro contra uma borda da window por vez (4 passadas). Para cada aresta V1→V2: fora→dentro salva interseção e V2; dentro→dentro salva V2; dentro→fora salva a interseção; fora→fora nada. Bom para convexos; em côncavos pode deixar arestas "fantasma" na borda.
- **Weiler-Atherton**: anda pelo polígono e, ao sair da window, anda pela borda da window até voltar. Funciona com côncavos e buracos e pode gerar vários polígonos (paper de 1977 sobre remoção de superfície oculta).
- Côncavo: produto vetorial das arestas consecutivas; se um z sai com sinal diferente dos outros, é côncavo.
- Window não retangular convexa: Cyrus-Beck/LB com todas as bordas. Côncava: dividir em convexas.

**Curvas**: gera em segmentos de reta e recorta cada um (ou testa cada ponto).

**3D**: CS com **6 bits** (acima, abaixo, direita, esquerda, frente, trás) contra o volume canônico; LB/Cyrus-Beck contra planos.

---

## [S06] Curvas: Hermite, Bézier, de Casteljau, continuidade
busca: curva paramétrica, blending functions, funções de mistura, Hermite, Bézier, Bezier, Bernstein, de Casteljau, continuidade, G0, G1, C0, C1, C2, tangente, fecho convexo, convex hull

História: **de Casteljau** (Citroën, 1959) criou o algoritmo mas não pôde publicar; **Pierre Bézier** (Renault, ~1960) publicou, e a curva leva o nome dele. **Carl de Boor** (GM) desenvolveu as B-splines (1972).

**Forma matricial**: x(t) = T·M·Gx, com T = [t³ t² t 1], t ∈ [0,1]. M define o tipo, G é a geometria, C = M·G são os coeficientes [a b c d] de at³ + bt² + ct + d. As **blending functions** são T·M (quanto cada elemento de G pesa em cada t).

**Hermite**: G = [P1 P4 R1 R4] (2 pontos + 2 tangentes).
```
MH = |  2 -2  1  1 |      H1 = 2t³ - 3t² + 1
     | -3  3 -2 -1 |      H2 = -2t³ + 3t²
     |  0  0  1  0 |      H3 = t³ - 2t² + t
     |  1  0  0  0 |      H4 = t³ - t²
```

**Bézier**: G = [P1 P2 P3 P4]. Passa por P1 e P4; P2 e P3 só puxam.
```
MB = | -1  3 -3  1 |     Bernstein: (1-t)³, 3t(1-t)², 3t²(1-t), t³  (somam 1)
     |  3 -6  3  0 |
     | -3  3  0  0 |
     |  1  0  0  0 |
```
- Tangentes nas pontas: R1 = 3(P2 − P1), R4 = 3(P4 − P3) (converte Bézier ↔ Hermite).
- Fica dentro do **fecho convexo** dos pontos de controle; é invariante a transformações afins (transformar os pontos = transformar a curva); mexer um ponto mexe a curva toda (controle global). Com n+1 pontos o grau é n.
- P(0,5) = (P1 + 3P2 + 3P3 + P4)/8.
- CONTA (exercício 1.4.1): P1 (1,1), P2 (2,2), P3 (3,2), P4 (4,1) → x = 1 + 3t, y = 1 + 3t − 3t². Com δ = 0,2: (1,1), (1,6; 1,48), (2,2; 1,72), (2,8; 1,72), (3,4; 1,48), (4,1). P(0,5) = (2,5; 1,75).

**de Casteljau** (pontos médios recursivos): médio(P1P2), médio(P2P3), médio(P3P4), depois os médios desses, e o último médio está na curva. No exemplo: (1,5;1,5), (2,5;2), (3,5;1,5) → (2;1,75), (3;1,75) → **(2,5; 1,75)**. Prós: precisão ilimitada. Contras: muita conta, recursão gasta memória, não é incremental.

**Desenho por blending functions** (trabalho 1.5): passo δ, k segmentos de reta, recorte por ponto. Ruim: calcula T = [t³ t² t 1] e multiplica a cada passo (as forward differences resolvem).

**Continuidade na junção** de duas curvas:
- **G0/C0**: as curvas se encontram (mesmo ponto).
- **G1**: tangentes na mesma direção (módulos podem diferir).
- **C1**: tangentes iguais (direção e módulo).
- **C2**: segunda derivada igual também.
- Bézier [P1..P4] + [P4..P7]: compartilhar P4 dá C0; P3, P4, P5 colineares dá G1; com P4 no meio (|P3P4| = |P4P5|) dá C1. O slide chama de "C1" o caso colinear com k qualquer; pela definição isso é G1.
- 10 pontos em Bézier cúbica encadeada: 3 curvas (P1–P4, P4–P7, P7–P10). Em B-spline: 7 segmentos.

---

## [S07] B-splines e forward differences
busca: B-spline, bspline, spline, controle local, forward differences, diferenças adiante, diferencas, delta, E(δ), DesenhaCurvaFwdDiff, ponto flutuante

- **Spline**: tira de aço flexível da construção naval, curvada por pesos ("ducks"); mantinha continuidade de 2ª ordem.
- **Spline cúbica natural**: passa pelos pontos, C0+C1+C2, mas cada coeficiente depende de **todos** os pontos (controle global, inverter matriz (n+1)×(n+1)).
- **B-spline uniforme**: **controle local** (cada segmento depende de 4 pontos), **C2** automático, **não passa** pelos pontos (aproxima), fica no fecho convexo. **n pontos → n − 3 segmentos**; o segmento Qi usa P(i−3), P(i−2), P(i−1), Pi, e segmentos vizinhos compartilham 3 pontos.
```
MBS = 1/6 * | -1  3 -3  1 |
            |  3 -6  3  0 |
            | -3  0  3  0 |
            |  1  4  1  0 |
```
- Início do segmento: (P0 + 4P1 + P2)/6; fim: (P1 + 4P2 + P3)/6; tangente no início: (P2 − P0)/2.

**Três jeitos de desenhar uma cúbica**: avaliar o polinômio a cada t (blending), subdivisão recursiva (de Casteljau), **forward differences** (o mais eficiente: depois de inicializar, 3 somas por coordenada por ponto, nenhuma multiplicação).

Para f(t) = at³ + bt² + ct + d com passo δ:
```
f0    = d
Δf0   = aδ³ + bδ² + cδ
Δ²f0  = 6aδ³ + 2bδ²
Δ³f0  = 6aδ³                (constante na cúbica)

D = E(δ)·C,   E(δ) = | 0    0    0  1 |
                     | δ³   δ²   δ  0 |
                     | 6δ³  2δ²  0  0 |
                     | 6δ³  0    0  0 |
laço:  x += Δx;  Δx += Δ²x;  Δ²x += Δ³x     (n = 1/δ passos)
```
C = M·G conforme o tipo (MH·GH, MB·GB, MBS·GBS). Ponto fraco: o erro de arredondamento **acumula** a cada soma.

CONTA (exemplo B-spline 2D do professor, P = (1,1), (2,2), (3,2), (4,1), δ = 0,1): Cx = (0, 0, 1, 2) → x = t + 2; Cy = (0; −0,5; 0,5; 1,833) → y = −0,5t² + 0,5t + 1,833. Condições iniciais: x = 2, Δx = 0,1, Δ²x = 0; y = 1,833, Δy = 0,045, Δ²y = −0,01, Δ³ = 0. Pontos certos: y = 1,833 → 1,878 → 1,913 → 1,938 → 1,953 → 1,958 (t = 0,5) → 1,953 → 1,938 → 1,913 → 1,878 → 1,833. **A tabela do PDF do professor erra o y a partir da 2ª linha** (1,923, 1,958...); o Δy da tabela está certo.

CONTA (Bézier do exercício, y = 1 + 3t − 3t², δ = 0,2): y0 = 1, Δy = 0,48, Δ²y = −0,24 → 1,48; 1,72; 1,72; 1,48; 1.

Slide 6.5 (desempenho): em arquiteturas antigas (CISC) a soma em ponto flutuante era bem mais rápida que a multiplicação, por isso se preferiam algoritmos com somas (como as forward differences). Hoje a soma de PF é mais complicada que a multiplicação (precisa alinhar os expoentes em série), multiplicadores ficaram rápidos e existe FMA (a·x + b numa instrução), então a diferença quase sumiu.

---

## [S08] Superfícies bicúbicas
busca: superfície, superficie, retalho, patch, bicúbica, bicubica, Bézier 16 pontos, B-spline superfície, twist, malha, mesh, DD

- Ideia: se cada elemento de G de uma curva for ele mesmo uma curva em t, Q(s,t) varre uma **superfície** (retalho / patch).
- **x(s,t) = S·M·Gx·Mᵀ·Tᵀ**, S = [s³ s² s 1], T = [t³ t² t 1]; uma G 4×4 por coordenada (Gx, Gy, Gz).
- Forma com somatório: P(s,t) = Σi Σj Bij · Ji,n(s) · Jj,m(t), com J = funções de Bernstein → **superfície de Bézier**.
- **Hermite**: G com 4 cantos, tangentes em s e em t, e vetores de **torção** (twist, ∂²Q/∂s∂t).
- **Bézier**: **16 pontos de controle**, passa pelos **4 cantos**.
- **B-spline**: matriz de controle m×n, submatrizes 4×4 andando de 1 em 1 → **(m − 3)·(n − 3) retalhos**, C2 entre eles.
- Desenho: malha de curvas (s fixo variando t, e t fixo variando s).
  - Blending functions: avalia x(s,t) em cada (si, tj) (muita multiplicação; trabalho 1.9).
  - Forward differences (trabalho 1.10): **DDx = E(δs)·(M·Gx·Mᵀ)·E(δt)ᵀ**. A 1ª linha dá as condições iniciais da curva em t; para a próxima curva: linha1 += linha2; linha2 += linha3; linha3 += linha4. Depois transpõe para a outra família.

---

## [S09] 3D: matrizes, eixo arbitrário, normal, plano, OBJ
busca: 3D, tridimensional, Rx, Ry, Rz, rotação 3D, eixo arbitrário, produto vetorial, cross product, produto escalar, dot product, normal, plano, interseção, wireframe, arame, OBJ, Wavefront, projeção do ponto, direção de projeção, plano definido pelos pontos, matriz de transformação linear, mapeado para, rotação 3D de 90

**Matrizes 4×4 (vetor-linha)**:
```
T = | 1  0  0  0 |   S = | Sx 0  0  0 |
    | 0  1  0  0 |       | 0  Sy 0  0 |
    | 0  0  1  0 |       | 0  0  Sz 0 |
    | Dx Dy Dz 1 |       | 0  0  0  1 |

Rx = | 1   0    0   0 |   Ry = | cos 0 -sen 0 |   Rz = |  cos sen 0 0 |
     | 0  cos  sen  0 |        |  0  1   0  0 |        | -sen cos 0 0 |
     | 0 -sen  cos  0 |        | sen 0  cos 0 |        |  0   0  1 0 |
     | 0   0    0   1 |        |  0  0   0  1 |        |  0   0  0 1 |
```
- Note que em **Ry** o sinal do seno é o contrário de Rx e Rz.
- 90° (cos = 0, sen = 1): Rx → linhas [1 0 0 0], [0 0 1 0], [0 −1 0 0]; Ry → [0 0 −1 0], [0 1 0 0], [1 0 0 0]; Rz → [0 1 0 0], [−1 0 0 0], [0 0 1 0].
- Escala 3D por (a, b, c) = diag(a, b, c, 1), 4×4; ex.: por (2, 3, 4) dá diag(2, 3, 4, 1). Translação 3D por (dx, dy, dz): identidade 4×4 com [dx dy dz 1] na última linha (vetor-linha) ou na última coluna (vetor-coluna); a ordem dx, dy, dz importa. As versões 3×3 são de 2D.

**Rotação em torno de um eixo arbitrário** que passa por P: T(−P) → Rx (leva o eixo ao plano xy) → Rz (alinha com y) → **Ry(θ)** → Rz⁻¹ → Rx⁻¹ → T(P).

**Vetores**:
- Produto escalar a·b = axbx + ayby + azbz = |a||b|cosθ (ângulo; zero se perpendiculares).
- **Produto vetorial** a × b = (aybz − azby, azbx − axbz, axby − aybx), perpendicular aos dois. **Normal de uma face** com 3 pontos: n = (p1 − p0) × (p2 − p0). X × Y = Z.
- Estrutura de arame (wireframe): precisa dos vértices e de quais pontos formam cada face.

**Plano e projeção de ponto** (projeção do ponto D sobre um plano segundo uma direção de projeção U; CONTA com números inventados): plano por A(4,0,0), B(0,4,0), C(0,0,4): n = (B − A) × (C − A) = (−4,4,0) × (−4,0,4) = (16, 16, 16) ∝ (1,1,1); plano x + y + z = 4. Projetar D(4,4,4) na direção U = (−1,−1,−2): (4 − t) + (4 − t) + (4 − 2t) = 4 → t = 2 → ponto (2, 2, 0). Receita: n·(D + tU) = n·A → t = n·(A − D)/(n·U), depois substitui t.

**Matriz × vetor**: com vetor-coluna, A·(0,1,0) é a 2ª **coluna** de A. Ex.: A = [[2,0,1],[1,3,0],[0,1,4]] (linhas) leva (1,0,0) em (2,1,0), (0,1,0) em (0,3,1) e (0,0,1) em (1,0,4). Para um vetor qualquer, soma as colunas com os pesos: A·(1,1,0) = (2,1,0) + (0,3,1) = (2,4,1). Ler a linha em vez da coluna é o erro clássico.

**Homogêneo → cartesiano**: divide por W. Ex.: (4, 6, 2, 2) = (2, 3, 1); (3, 1, 6, 3) = (1; 0,33; 2).

**OBJ (Wavefront)**: `v x y z` vértice, `vn` normal, `vt` textura, `f i j k` face (índices começam em **1**, aceita `v/vt/vn`), `l` linha, `p` ponto, `o` objeto, `g` grupo, `mtllib`/`usemtl` material (no `.mtl`: Ka ambiente, Kd difusa, Ks especular, Ns expoente, d transparência).

---

## [S10] Projeções e pipeline 3D
busca: projeção, projecao, paralela, ortogonal, ortográfica, oblíqua, pictórica, isométrica, dimétrica, trimétrica, axonométrica, cavaleira, cavalier, cabinet, perspectiva, ponto de fuga, COP, VRP, VPN, VUP, volume de visão, frustum, pipeline de visualização, câmera, camera, pistas perceptuais, pistas de profundidade, displays, região do universo, câmera sintética, síntese de imagens, plano de recorte, transformação de projeção

**Classificação do professor** (difere do Foley; na prova vale a dele):
- **Paralela** (raios paralelos, tamanho não muda com a distância, às vezes parece distorcido; engenharia e desenho técnico):
  - **Ortogonais ou ortográficas**: raios ⟂ ao plano. A usada em CG.
  - **Oblíquas ou pictóricas**: **axonométricas** (**isométrica**, dimétrica, trimétrica), **cavaleira** (profundidade em escala real) e **cabinet** (profundidade pela metade).
- **Perspectiva**: raios convergem no **COP**; o que está longe fica menor (tamanho ∝ 1/distância).
- No Foley as axonométricas ficam dentro das ortográficas. "Dois tipos de projeção" (em geral) = paralela × perspectiva; "dois tipos de paralela" = ortogonal × oblíqua.
- Isométrica: os três eixos com o mesmo encurtamento, 120° entre eles na imagem. Dimétrica: dois iguais. Trimétrica: os três diferentes.
- Cavaleira: projetores a 45° do plano. Cabinet: ≈ 63,4° (tan = 2).
- Pontos de fuga: 1, 2 ou 3, conforme quantos eixos principais cortam o plano de projeção. Retas paralelas ao plano não convergem.
- Paralela preserva paralelismo; perspectiva não preserva paralelismo, ângulos nem medidas. Perspectiva pode ser escrita como matriz 4×4 em homogêneas.

**Paralela ortogonal (algoritmo do professor)**: 1) translada o **VRP** (centro da window) para a origem; 2) acha a **VPN** (normal do plano de projeção) e seus ângulos com X e Y; 3) gira o mundo em X e Y para alinhar a VPN com Z; 4) **ignora Z**; 5) normaliza; 6) recorta em 2D; 7) viewport. Passos 1–3 são uma matriz só, aplicada a tudo, inclusive à window.
- CONTA do slide: window W1 (0,5; 2; 2,5), W2 (2,5; 2; 0,5), W3 (3; 0; 1), W4 (1; 0; 3). VRP = (1,75; 1; 1,75). VPN = (2, 1, 2). θx = arctan(1/2) = 26,57°; θy = arctan(2/2) = 45°.

**Perspectiva**: COP na origem e plano em z = d: **xp = x·d/z, yp = y·d/z**. Matriz (vetor-coluna) com a última linha [0 0 1/d 0]: W vira z/d e a divisão por W faz a perspectiva. Algoritmo: translada o **COP** para a origem, alinha a VPN com Z, **divide por z/d**, normaliza, recorta, viewport. d pequeno = grande angular; d grande = teleobjetiva; d → ∞ vira paralela. Descarte o que está atrás do olho (z ≤ 0) antes de dividir.
- CONTA (exercício do Moodle): tetraedro (50,100,50), (70,20,30), (30,20,30), (50,20,100); window no plano y = 150 de x −10 a 110 e z 0 a 80; COP (50,250,40), olhando para −y, d = 100. Fator = 100/(250 − y): (50,100,50) → (50; 46,67) no plano; (70,20,30) → (58,70; 35,65); (30,20,30) → (41,30; 35,65); (50,20,100) → (50; 66,09). Em SCN (centro (50,40), meia-largura 60, meia-altura 40): (0; 0,17), (0,14; −0,11), (−0,14; −0,11), (0; 0,65). Se o x sai espelhado depende do sentido da rotação escolhida.

**Pistas de profundidade** (pistas perceptuais de profundidade; como mostrar 3D numa tela/display 2D): tamanho relativo, gradiente de textura, perspectiva linear, interposição (um objeto na frente do outro), sombra, contraste/claridade/brilho (perspectiva atmosférica: o que está longe fica mais claro e com menos contraste), paralaxe de movimento, estéreo (duas imagens) e foco. Todas valem.

**Volume de visão**: região do mundo que será recortada e projetada. Paralela: paralelepípedo (cubo canônico). Perspectiva: tronco de pirâmide (frustum).

**Pipeline 3D** (a ordem das etapas aparece descrita de jeitos diferentes; as três versões são coerentes):
- modelagem (objeto → mundo) → câmera/visualização (mundo → observador) → projeção → normalização e recorte → viewport
- transformação de câmera → recorte 3D → projeção → mapeamento para a tela → rasterização
- recorte → projeção → rasterização → visibilidade (z-buffer)
- Coordenadas no OpenGL: objeto → mundo (model) → câmera (view) → clip (projection) → NDC (divide por W) → tela (viewport).
- O pipeline trabalha com **primitivas geométricas** (pontos, linhas, polígonos/triângulos); os objetos não precisam ser sólidos. As coordenadas dos vértices são transformadas conforme a posição e a orientação do observador, e a última fase é a rasterização.
- **Transformação de câmera**: sequência de translações e rotações aplicada aos vértices, que deixa as coordenadas no sistema do observador (posição e orientação). Não projeta para 2D e não é a última etapa.

---

## [S11] Rasterização: retas, círculos, preenchimento, aliasing, texturas
busca: rasterização, rasterizacao, conversão por varredura, scan conversion, scanline, DDA, Bresenham, ponto médio, círculo, circulo, preenchimento, boundary fill, flood fill, vizinhança 4, vizinhança 8, aliasing, serrilhado, anti-aliasing, antisserrilhado, MSAA, supersampling, textura, mipmap, bump mapping, putpixel, plota, antisserrilhado, MSAA, multisampling, textura de superfície, textura procedural, textura sólida

**Rasterização**: dado um polígono no plano de projeção, achar quais pixels ele cobre. Método do professor: dividir em **trapézios** com topo e base horizontais; um **rastreador de bordas** segue cada lateral: próximo ponto = (x + xinc, y − 1, z + zinc), xinc = Δx/Δy, zinc = Δz/Δy. Em cada linha preenche da borda esquerda à direita incrementando z e manda para o z-buffer.

**Reta ingênua** (algoritmo "ingênuo"): y = yi + a·(x − xi), a = (yf − yi)/(xf − xi), putpixel para cada x → desenha uma **linha**.

**DDA**: passos = max(|Δx|, |Δy|); soma xinc e yinc (ponto flutuante) e arredonda.

**Bresenham** (0 ≤ m ≤ 1, só inteiros): p0 = 2Δy − Δx. Se p < 0: próximo (x+1, y), p += 2Δy. Senão: (x+1, y+1), p += 2Δy − 2Δx. Para |m| > 1 troca os papéis de x e y.
- CONTA (20,10)→(30,18): Δx = 10, Δy = 8, p0 = 6 → (21,11), (22,12), (23,12), (24,13), (25,14), (26,15), (27,16), (28,16), (29,17), (30,18).

**Círculo (ponto médio)**: p0 = 1 − r; se p < 0: (x+1, y), p += 2x + 1 (x já incrementado); senão (x+1, y−1), p += 2x + 1 − 2y. Simetria de 8 octantes. f(x,y) = x² + y² − r²: < 0 dentro, = 0 na circunferência, > 0 fora (com f = r² − x² − y² o sinal inverte).
- CONTA r = 10: (0,10) → (1,10), (2,10), (3,10), (4,9), (5,9), (6,8), (7,7).

**Preenchimento**:
- **Scanline**: para cada linha de varredura, acha as interseções com as arestas, ordena por x e pinta entre pares (regra **par-ímpar**). Tabela de arestas (ET) e tabela de arestas ativas (AET), x += 1/m por linha.
- **Boundary-fill**: a partir de uma semente, pinta até achar a cor da borda. **Flood-fill**: troca uma cor por outra. **Vizinhança 4** não atravessa diagonais (pode não preencher regiões ligadas só pela diagonal); **vizinhança 8** atravessa, e vaza por borda diagonal de 1 pixel.

**Aliasing** (serrilhado, "jaggies"): vem de amostrar pouco (Nyquist: amostrar a mais de 2× a maior frequência). Acontece em qualquer rasterização.
- **Supersampling (SSAA)**: várias amostras completas por pixel e média.
- **MSAA**: várias amostras de cobertura e profundidade por pixel, mas o shading é calculado uma vez por pixel e reaproveitado nas amostras (é a característica principal dele). Não suaviza o serrilhado de dentro das texturas.
- Filtragem por área (pré-filtragem), pós-filtragem.

**Texturas**:
- Mapeamento de textura (textura de superfície/imagem): usa um sistema de coordenadas **2D** (u,v) da imagem, mapeado na superfície. Dá realismo sem aumentar a geometria.
- **Bump mapping**: perturba a **normal**, sem mudar a geometria; só a iluminação muda.
- Displacement mapping: muda a geometria de verdade.
- **Environment mapping**: reflexo do ambiente numa textura (cube map, sphere map).
- Textura procedural: gerada por função na hora, então não precisa guardar imagens enormes na memória. Textura sólida (3D): a cor depende do ponto (x,y,z), como madeira ou mármore "esculpidos".
- PEGADINHA: bump mapping NÃO perturba a cor dos vértices, perturba a normal.
- **Mipmap**: pirâmide de versões reduzidas pela metade (cada nível tem 1/4 dos pixels). Reduz custo e aliasing de textura longe da câmera. Memória extra: 1/4 + 1/16 + ... = **1/3 ≈ 33%**.

---

## [S12] Superfície oculta: z-buffer, pintor, backface, BSP
busca: superfície oculta, superficie visivel, hidden surface, visible surface, z-buffer, zbuffer, buffer de profundidade, depth buffer, pintor, painter, backface, back-face culling, faces traseiras, BSP, Warnock, espaço do objeto, espaço da imagem, remoção de linhas ocultas, faces traseiras, back faces, volumes de delimitação, bounding volume, hemicubo, profundidade por pixel

**Z-buffer** (Catmull, 1974):
```
zbuffer = +∞ em todo pixel; cor = fundo
para cada polígono, para cada pixel (x,y) que ele cobre:
    z = profundidade do polígono em (x,y)
    se z < zbuffer[x][y]:  cor[x][y] = cor do polígono;  zbuffer[x][y] = z
```
- Mesma resolução do frame buffer (um z por pixel). Custa memória e tem precisão finita (z-fighting).
- **Não precisa ordenar**: a ordem dos polígonos não muda a imagem. Ex.: dois objetos, um escondendo o outro: em qualquer ordem o pixel fica com o mais próximo.
- z calculado **incrementalmente** na varredura (z += zinc).
- Espaço da imagem. Transparência é difícil.
- Sentido: nos slides "mais perto" = menor z; se o z aponta para o observador, troca o teste. A ideia é ficar com o mais próximo.

**Algoritmo do pintor** (Newell, 1972): ordena por profundidade e pinta do fundo para a frente. Problema: sobreposição cíclica e polígonos que se cruzam (tem que dividir).

**Backface culling**: descarta as faces cuja normal aponta para longe do observador: N·(olho − P) < 0 (olhando para −z: Nz < 0). Tira ~metade das faces de um objeto fechado. Resolve tudo **só para um único objeto convexo**; com vários objetos um ainda pode esconder o outro.

**BSP** (Fuchs, Kedem, Naylor, 1980): árvore de partição binária do espaço; dá a ordem de desenho de trás para frente a partir de qualquer ponto de vista.

**Warnock** (1969): subdivide a tela em quadrantes até cada região ficar simples.

**Técnicas usadas na remoção de linhas/superfícies ocultas**: backface culling, z-buffer, pintor, BSP, volumes envolventes (bounding volumes: testa primeiro uma caixa/esfera simples em volta do objeto para descartar rápido), scanline, Warnock, ray casting. **Hemicubo não é** dessa lista: é da radiosidade (calcula fator de forma, [S14]).
- PEGADINHA: o z-buffer guarda, por pixel, a profundidade do objeto **mais próximo**, não do mais distante. É técnica de rasterização em tempo real (GPU); o fotorrealismo de cinema vem de ray tracing/path tracing, não do z-buffer.

Espaço do objeto (compara objetos: backface, BSP) × espaço da imagem (por pixel: z-buffer, ray casting). O pintor mistura os dois.

---

## [S13] Iluminação: Phong, Lambert, fontes de luz, shading
busca: iluminação, iluminacao, Phong, Lambert, difusa, especular, ambiente, reflexão, coeficiente, expoente, Blinn, normal, fonte de luz, direcional, pontual, spot, shading, sombreamento, flat, Gouraud, Phong shading, tonalização, normais às facetas, tonalização, modelo de reflexão, fonte de luz no infinito, poliedro, esfera, superfície paramétrica, iluminação local

**Modelo de Phong** (Bui-Tuong Phong, 1975): **3 componentes que se somam** (aditivas): **difusa (direta)**, **especular**, **ambiente (indireta)**.
```
I = Ia·ka  +  Il·kd·(N·L)  +  Il·ks·(R·V)^n
    ambiente   difusa          especular
```
- **Difusa** (Lambert): reflete igual para todo lado, **não depende do observador**, ∝ cos do ângulo entre a normal N e a direção da luz L. kd carrega a **cor do objeto**.
- **Especular**: reflexo direcional (espelho, brilho), ∝ cosⁿ do ângulo entre a direção do observador V e a direção de reflexão R. Tem a **cor da luz** (bule vermelho com só especular = preto com reflexo branco). n grande = brilho pequeno e concentrado.
- **Ambiente**: aproxima a luz que vem das reflexões entre objetos e da atmosfera, como um termo constante (calcular de verdade é a radiosidade). Na Lua (sem atmosfera) as sombras são quase pretas.
- R = 2(N·L)N − L. **Blinn-Phong**: usa o vetor meio H = (L + V)/|L + V| e (N·H)ⁿ.
- Atenuação com a distância: f = 1/(c1 + c2·d + c3·d²). Várias luzes: soma as parcelas. Cor: calcula por canal R, G, B.
- CONTA: Ia = Il = 1, ka = 0,2, kd = 0,6, N·L = 0,8, ks = 0,3, R·V = 0,9, n = 2 → 0,2 + 0,48 + 0,243 = **0,923**.
- **Por que calcular normais** (às facetas/faces da superfície): para a difusa (N·L) e a especular (R depende de N). Não para a ambiente, sombra (precisa de raio até a luz), transparência, curvatura ou octree.
- **Normal de superfície paramétrica** p(u,v): n = ∂p/∂u × ∂p/∂v (derivada em u, derivada em v, produto vetorial). Ex.: cilindro p(u,v) = (cos u, sen u, v): ∂p/∂u = (−sen u, cos u, 0), ∂p/∂v = (0, 0, 1), n = (cos u, sen u, 0), que aponta para fora do eixo. Numa esfera centrada na origem a normal sai **paralela ao próprio p** (radial), multiplicada por um fator que depende da parametrização: faz as duas derivadas e o produto vetorial para achar esse fator.

**Fontes de luz**: ambiente (sem direção), **pontual** (de um ponto para todo lado), **direcional** (no infinito, raios paralelos, como o Sol), **spot** (pontual com cone), de área (sombra suave).

**Shading** (como aplicar a iluminação no polígono):
| técnica | calcula | resultado |
|---|---|---|
| **Flat** | resolve a iluminação 1 vez por polígono, face inteira com uma cor | facetado; o mais barato; só parece curvo se a malha for muito fina (muito tesselada), com malha grossa fica bem facetado |
| **Gouraud** | nos vértices e **interpola cores** | suave, mas perde brilho especular no meio da face; depende da resolução da malha; bandas de Mach |
| **Phong shading** | **interpola normais** e ilumina por pixel | brilho certo, mais caro |

PEGADINHA: Gouraud calcula a iluminação nos vértices e interpola as **cores/intensidades**; quem interpola os **vetores normais** é o Phong shading (que acerta o brilho especular, com custo maior).

Modelo de Phong (a equação) ≠ Phong shading (interpolar normais). Os dois, e Gouraud, são **locais**: não fazem sombra nem dependem da cor de outro objeto.

---

## [S14] Raytracing, raycasting e radiosidade
busca: ray tracing, raytracing, ray tracer, ray casting, ray caster, volumétrico, voxel, raios umbrais, shadow ray, reflexão, refração, Snell, radiosidade, radiância, iluminação global, inter-reflexão difusa, fator de forma, hemicubo, semicubo, Nusselt, color bleeding, POV-Ray, renderização fotorrealística, plano do filme, iluminação indireta, raios secundários, Ray Shader, tempo real, cinema

**Ray Tracer**: simula o caminho da luz **de trás para frente**: do observador, um raio **por pixel** da viewport passando pela window. Faz assim porque quase nenhum raio que sai da luz chega ao olho.
- No ponto atingido: **raios de sombra (umbrais)** até cada luz; se a superfície reflete ou é transparente, dispara raio **refletido** e **refratado**, recursivamente (Whitted, 1980).
- Em cada ponto usa um modelo **local** (Phong) para a luz direta.
- O nº de raios **depende da cena** (objetos refletores/transparentes e nº de luzes); transparência deixa mais lento. Depende da posição da câmera. Paraleliza fácil (pixels independentes). Sombras podem ser calculadas à parte.
- Bom para espelho, refração e sombra de contorno duro; **ruim/ineficiente para materiais difusos** (precisaria de muitíssimos raios; por isso existem radiosidade e path tracing).
- Os raios saem da câmera virtual em direção ao plano da imagem ("filme") e testam interseção com os objetos; a visibilidade sai da **interseção mais próxima**, então ray tracing **não usa z-buffer**.
- Reflexos e iluminação indireta especular vêm de **raios secundários** disparados na direção de reflexão (e de refração) no ponto atingido.
- É caro: tradicionalmente usado offline (cinema, renderizações fotorrealistas). Jogos em tempo real usam rasterização + z-buffer (hoje há ray tracing em hardware, mas como complemento). "Simular a propagação da luz e sua interação com as superfícies" é a definição de ray tracing.
- Interseção raio-esfera: |O + tD − C|² = r² (equação do 2º grau; menor t positivo). Raio-plano: t = (d − N·O)/(N·D). Refração: n1·senθ1 = n2·senθ2 (Snell).
- Raytracers: POV-Ray (linguagem de descrição de cena; Moray é o modelador dele), Radiance, Cycles, V-Ray, Mental Ray. São estáticos (lentos, qualidade alta).

**Ray Caster**: raio do olho, só a **1ª interseção**, sem raios secundários (Appel, 1968). **Ray Caster volumétrico**: raios atravessam um volume denso de **voxels** acumulando cor (tomografia, ressonância, radar).

**Radiosidade / radiância**: **iluminação global** que modela a **inter-reflexão difusa** entre superfícies (color bleeding: a parede vermelha tinge a branca). Veio da transferência de calor (Cornell, 1984). Supõe superfícies difusas e equilíbrio de energia.
- **Independe do ponto de vista** (o ray tracing depende): calcula uma vez e anda pela cena.
- Radiosidade de uma superfície = energia que **sai** dela por tempo e área (emitida + refletida): Bi = Ei + ρi·Σ Bj·Fij.
- **Fator de forma** Fij: fração da energia que sai de uma superfície e chega na outra; **só geometria** (distância e orientação). Ai·Fij = Aj·Fji; em cena fechada ΣFij = 1. A notação dos índices muda de autor para autor.
- **Analogia de Nusselt** (projeta no hemisfério e depois na base); **hemicubo** (meio cubo com células de fator pré-calculado, Cohen e Greenberg, 1985).
- **Radiosidade progressiva**: "dispara" a energia da superfície mais brilhante a cada passo, e a imagem melhora aos poucos.
- O sistema de equações costuma ser resolvido por métodos iterativos (Gauss-Seidel aparece aqui, mas nunca é resposta para "algoritmo de recorte").
- Com radiosidade as sombras ficam suaves e existe luz ambiente de verdade.

---

## [S15] GPU, shaders e pipeline do OpenGL
busca: GPU, shader, pixel shader, fragment shader, vertex shader, GLSL, HLSL, OpenGL, pipeline gráfico, rasterização × raytracing, pixel shading, rendering, etapa final, pipeline de computação gráfica, tonalização, sombreamento

- **Pixel shader** (fragment shader): programa que calcula cor e iluminação de cada pixel (e reflexo/transparência), rodando na GPU. O professor chama também de ray shader.
- **Pipeline do OpenGL**: vértices → **vertex shader** → (tesselação, geometry shader) → montagem de primitivas → recorte → **rasterização** → **fragment shader** → testes por fragmento (profundidade, stencil, blending) → frame buffer. Linguagens: GLSL (OpenGL), HLSL (Direct3D).
- Na etapa final do pipeline (rendering), a parte de **remoção de superfícies ocultas** e de **tonalização (shading)** usa z-buffer, Gouraud e Phong. Curvas de Bézier e transformações geométricas são modelagem/geometria; flood fill é preenchimento; Bresenham e Cohen-Sutherland são rasterização e recorte; mipmap é textura.
- Rasterização × ray tracing: a rasterização vai objeto por objeto e descobre os pixels de cada um; o ray tracing vai pixel por pixel e descobre o objeto de cada um.
- Pipeline do trabalho 3 (SGI): window → SCN → clipping → varredura → z-buffer → Phong por pixel → viewport.

---

## [S16] Modelos hierárquicos e animação
busca: hierárquico, hierarquico, árvore, grafo de cena, scene graph, instância, símbolo, pilha de matrizes, push, pop, glPushMatrix, cinemática direta, cinemática inversa, forward kinematics, rigging, skinning, key-frame, motion capture, MoCap, locomoção, bípede, quadrúpede, hexápode

- **Símbolo**: objeto modelado uma vez no próprio sistema de coordenadas. **Instância**: símbolo colocado na cena com a transformação de instância **M = T·R·S** (vetor-coluna; em vetor-linha S·R·T): escala, gira, posiciona. Tabela de instâncias não guarda relação entre as partes.
- **Modelo hierárquico**: as partes dependem umas das outras (mover o braço move a mão). Árvore (ou DAG, se partes iguais são reaproveitadas, como as 4 rodas). Cada nó guarda a geometria, a transformação **relativa ao pai** e os filhos. Transformação no mundo = produto das transformações dos ancestrais.
- Braço robótico: base Ry(θ); braço inferior Ry(θ)·T(0,h1,0)·Rz(φ); superior Ry(θ)·T(0,h1,0)·Rz(φ)·T(0,h2,0)·Rz(ψ).
- Percorre a árvore em pré-ordem com **pilha de matrizes**: push antes de descer num filho, pop ao voltar, para os irmãos partirem da matriz do pai (glPushMatrix/glPopMatrix). Representação filho-esquerdo, irmão-direito.
- **Cinemática direta**: dados os ângulos das juntas, onde fica o efetuador. **Inversa**: dada a posição desejada, quais ângulos (pode ter várias soluções ou nenhuma).
- Animação: **key-frames** + interpolação; **motion capture**; **rigging** (esqueleto) + **skinning** (ligar à malha).
- **Grafo de cena**: nós de geometria, transformação, material, luz, câmera, grupo (Open Scene Graph, engines).
- Trabalho de locomoção (página do professor): braço mecânico com esteira (sem deslocamento); **bípede**; **quadrúpede réptil** (pernas cruzadas, como o lagarto); **quadrúpede mamífero** (pernas alternadas; caminhada simétrica, corrida simétrica e assimétrica/galope); **hexápode** (inseto; coordenação trípode ou quadrípode). Base em biomecânica e cinesiologia.

---

## [S17] Cor
busca: cor, cores, espectro, comprimento de onda, nm, olho, retina, cones, bastonetes, córtex, tricromacia, Maxwell, RGB, CMY, CMYK, HSV, HSI, CIE, XYZ, Pantone, true color, indexed color, paleta, gamut, gama, luminância

- Cor = faixa de frequências que o olho percebe como semelhantes. Visível: ~**780 nm (vermelho) a ~350–380 nm (violeta)**, cerca de uma oitava.
- **Cor reflexiva** (reflexo seletivo, opaca ou especular) × **cor emissiva** (o objeto emite). **Em CG tudo é emissivo** (o monitor emite).
- Retina em campos receptivos **hexagonais**. **Bastonetes**: pouca luz, visão noturna, sem cor. **Cones**: muita luz, 3 tipos de opsina: ondas curtas (azul), médias (verde), longas (vermelho). **Células horizontais** interligam os campos e calculam a **2ª derivada** (realce de borda). **Ganglionares** levam ao cérebro.
- Córtex: **primário** = "tela mental", só intensidade (P&B); **terciário** integra a cor, não forma imagem (a cor é "pintada" depois); **secundário** detecta linhas retas.
- Qualquer cor sai de 3 componentes que dividem o espectro como o olho (tricromacia). Usado desde o séc. XVII (lanterna mágica, fantasmagoria), formalizado por **Maxwell** (séc. XIX).
- O amarelo do monitor não tem luz amarela: são subpixels vermelho e verde acesos.

**Modelos**:
| modelo | tipo | uso |
|---|---|---|
| CIE 1931 (XYZ) | toda cor visível como vetor 3D | referência, pouco intuitivo |
| RGB | **aditivo**, imita os cones, cubo de cores | monitores |
| HSV / HSI | tom (hue), saturação, valor/intensidade | escolher cor |
| CMYK | **subtrativo** (ciano, magenta, amarelo, preto) | impressão, gráfica |
| Pantone | tabelas proprietárias | gráfica, economia de tinta |

- Aditivo: R + G = amarelo, G + B = ciano, R + B = magenta, R + G + B = branco. Subtrativo: C + M = azul, M + Y = vermelho, C + Y = verde, C + M + Y = preto (na teoria; K existe porque esse preto sai ruim e caro).
- **CMY = 1 − RGB** (C = 1 − R, M = 1 − G, Y = 1 − B). K = min(C, M, Y).
- HSV: H em graus (0 vermelho, 60 amarelo, 120 verde, 180 ciano, 240 azul, 300 magenta); V = max(R,G,B); S = (max − min)/max.
- Cinza (luminância): Y = 0,299R + 0,587G + 0,114B (a média simples (R+G+B)/3 não respeita a percepção).
- Saturação e luminosidade são independentes: duas cores com saturações diferentes podem ter a mesma luminosidade.
- IHS/HSI = intensidade, matiz (hue), saturação. Para mudar o contraste sem mudar o tom, mexe só em I ([S18]).
- **True color**: o pixel guarda a cor (24 bits = 16,7 milhões). **Indexed color**: o pixel guarda um índice numa **tabela de cores** (paleta; 8 bits = 256 cores na tela).
- **Gamut**: as cores que um dispositivo consegue mostrar, um polígono dentro do diagrama CIE.
- Correção gama: o monitor não responde linearmente à tensão (I ∝ V^γ, γ ≈ 2,2).

---

## [S18] Processamento de imagens
busca: processamento de imagens, PDI, imagem digital, amostragem, quantização, quantizacao, histograma, equalização, equalizacao, negativo, contraste, brilho, filtro, passa-baixa, passa-alta, média, mediana, gaussiano, laplaciano, sobel, prewitt, roberts, convolução, máscara, núcleo, kernel, Fourier, espectro, fase, DCT, wavelet, Haar, Walsh, Slant, interpolação, vizinho mais próximo, bilinear, bicúbica, realce, restauração, segmentação, limiarização, threshold, componentes conexos, morfologia, erosão, dilatação, textura, co-ocorrência, Gabor, reconhecimento de padrões, classificador, distância mínima, perceptron, estéreo, disparidade, compressão, Huffman, RLE, JPEG, BMP, planos de bits, Golomb, aritmética, IHS, gradiente, diferença, realce de imagem, codificação, codificador, decodificador, ruído, sal e pimenta, desborramento, modelos de cor, DOI, análise de imagens, monocromática

Não tem slide na disciplina, mas o assunto aparece nas questões de treino (filtros, histograma, segmentação, compressão). Base: Gonzalez & Woods, Processamento Digital de Imagens.

**Imagem digital e digitalização**
- Imagem = função f(x, y) de intensidade (brilho) em cada ponto. Para ir pro computador tem que discretizar duas coisas:
  - **amostragem**: discretiza as **coordenadas** (x, y), ou seja, o domínio espacial. Define a resolução espacial (quantos pixels);
  - **quantização**: discretiza a **amplitude** (o valor/brilho de cada amostra). Define quantos níveis de cinza (L = 2^k níveis com k bits).
- PEGADINHA: é sempre "amostragem = coordenadas, quantização = amplitude", nunca o contrário. Quantização às vezes aparece descrita como "converter cada amostra num valor discreto".
- Modelos de representação: escala de cinza, RGB, CMY(K), HSV/HSI/IHS, YIQ/YCbCr. "DOI" (Digital Object Identifier) é identificador de documento, não é modelo de cor.

**Etapas de um sistema de análise de imagens** (nessa ordem): aquisição → pré-processamento → segmentação → representação e descrição → reconhecimento e interpretação. Uma base de conhecimento acompanha todas as etapas.

**O que é técnica de PDI**: realce, restauração, amostragem e quantização, limiarização, segmentação, morfologia, compressão, transformadas, representação e descrição, reconhecimento. **Têmpera simulada** (simulated annealing) não é de PDI, é método de otimização/busca.

**Histograma**
- h(r_k) = n_k: quantas vezes cada nível r_k aparece. Normalizado, p(r_k) = n_k / n é uma função discreta que dá a probabilidade de cada nível.
- Diz se a imagem é escura (concentrado nos níveis baixos), clara (níveis altos), de baixo contraste (concentrado numa faixa estreita) ou de alto contraste (espalhado).
- Não diz se duas imagens são da mesma cena: cenas diferentes podem ter o mesmo histograma (ele perde a posição dos pixels).

**Equalização de histograma**
- Usa o histograma **acumulado** (CDF): s_k = (L − 1) · Σ_{j ≤ k} p(r_j).
- É **não linear** e **específica** de cada imagem (depende do histograma dela).
- Espalha os níveis tentando deixar o histograma uniforme: **aumenta o contraste** (principalmente nas faixas com mais pixels) e aumenta a variância/entropia do histograma. "Reduzir o contraste" é falso.
- Equalizar de novo uma imagem já equalizada não muda nada.
- Em imagem colorida: equalizar cada canal RGB separado muda as cores; o certo é equalizar só a intensidade. A equalização de cores serve para realçar diferenças de tonalidade.

**Transformações de intensidade (ponto a ponto)**
- Negativo: s = (L − 1) − r (com níveis de 0 a L−1). Com valores normalizados em [0,1], s = 1 − r.
- Logaritmo: s = c·log(1 + |r|), expande os escuros (usado para mostrar espectro de Fourier).
- Potência (gama): s = c·r^γ.
- Alargamento de contraste (contrast stretching), limiarização (threshold), fatiamento.
- Brilho e contraste: s = a·r + b, são operações **lineares**.
- Tudo isso depende só do valor do próprio pixel, então pode ser aplicado em todos os pixels em paralelo.

**Cor em PDI**
- Cinza a partir de RGB: a média (R + G + B)/3 não bate com a percepção. Luminância: **Y = 0,299R + 0,587G + 0,114B** (o verde pesa mais, o azul menos).
- Mudar o contraste sem mudar o tom: converter RGB → IHS (intensidade, matiz, saturação), mexer só em **I** e voltar IHS → RGB. Mexer direto em R muda a cor.

**Filtragem espacial** (convolução da imagem com uma máscara/núcleo)
- Para que serve um filtro digital em PDI: **corrigir, suavizar ou realçar** informações da imagem. Suavizar e aguçar dá para fazer **tanto no domínio espacial quanto no da frequência** (não é "suavização só no espacial e aguçamento só na frequência").
- **Passa-baixas / suavização**: borra, tira ruído, atenua as altas frequências (transições bruscas).
  - **Média** (box): linear, m(f + g) = m(f) + m(g); é convolução; bom para ruído **gaussiano**; borra os contornos. Quanto maior a máscara M×M, mais borra.
  - **Gaussiano**: média ponderada, borra mais suave. Gaussiano é passa-baixas.
  - Imagem constante (ex.: toda preta) continua igual depois de qualquer média, e o tamanho da imagem não muda.
- Componentes pequenos (um pontinho, uma linha fina): a **média não elimina**, só espalha e borra, ou seja, "preserva" o componente pequeno de forma borrada; a **mediana elimina** o que é menor que metade da janela. Já os contornos (bordas de regiões grandes): a média borra, a mediana preserva.
- **Mediana**: **não linear** (filtro de estatística de ordem): M(f + g) ≠ M(f) + M(g). Ótimo para ruído **impulsivo** (sal e pimenta), **preserva bordas/contornos** e elimina pontos isolados menores que metade da janela. Se a pergunta é "tirar pontinhos e preservar a forma", é mediana.
- **Passa-altas / aguçamento / realce**: realça bordas e detalhes finos.
  - 1ª derivada (gradiente): **Roberts**, **Prewitt**, **Sobel**.
  - 2ª derivada: **Laplaciano**. O Laplaciano é passa-altas, não passa-baixas.
  - Realce costuma usar passa-altas e depende da aplicação e da interpretação subjetiva de quem olha.

Máscaras (para reconhecer na alternativa):
```
Roberts (2x2)      Prewitt (3x3)        Sobel (3x3)          Laplaciano (3x3)
| 1  0|  | 0  1|   |-1 -1 -1| |-1 0 1|  |-1 -2 -1| |-1 0 1|  | 0  1  0|   | 1  1  1|
| 0 -1|  |-1  0|   | 0  0  0| |-1 0 1|  | 0  0  0| |-2 0 2|  | 1 -4  1|   | 1 -8  1|
                   | 1  1  1| |-1 0 1|  | 1  2  1| |-1 0 1|  | 0  1  0|   | 1  1  1|
```
- Como reconhecer: 2×2 é Roberts; 3×3 só com 1 e −1 é Prewitt; 3×3 com 2 no meio da linha/coluna é Sobel; centro grande com sinal oposto aos vizinhos e soma zero é Laplaciano (às vezes com os sinais trocados).
- Em 1D, a máscara [−1 2 −1] (ou [1 −2 1]) é o Laplaciano discreto. Numa rampa (3 4 5 6 7 ...) dá 0 em tudo: a 2ª derivada de uma reta é zero. Ex.: em [... 2 4 6 8 ...] também dá 0; em [... 0 0 5 5 ...] dá picos na borda.
- Filtro de diferença direcional (gradiente numa direção; filtro definido por fórmula com |soma de um lado − soma do outro|): compara os vizinhos de um lado com os do outro, então responde às bordas **perpendiculares** a essa direção. Se compara (baixo, direita, baixo-direita) com (cima, esquerda, cima-esquerda), a direção é a diagonal principal e as bordas detectadas ficam ao longo da outra diagonal.
- Média × mediana em janela 3×3 (como pensar): monte a janela, conte os valores. Ex.: num xadrez de 0 e 10, a janela centrada num 0 tem quatro 10 e cinco 0 (média 40/9, mediana 0) e a centrada num 10 tem cinco 10 (média 50/9, mediana 10); a mediana devolve o próprio xadrez e a média não fica constante. Num padrão que repete 3 valores em diagonal, toda janela 3×3 tem três de cada, então média e mediana dão o valor do meio em todo lugar.

**Domínio da frequência**
- Fourier: F(u) = ∫ f(x) e^(−j2πux) dx, complexo F(u) = R(u) + jI(u).
  - Espectro (magnitude) |F(u)| = √(R² + I²); **espectro de potência** P(u) = |F(u)|² = R² + I².
  - **Ângulo de fase** φ(u) = arctan(I(u)/R(u)).
  - O núcleo 2D é **separável e simétrico**: faz a 1D nas linhas e depois nas colunas (é o que permite a FFT 2D).
  - Baixa frequência = regiões homogêneas; alta frequência = bordas, detalhes e ruído.
- Filtros na frequência: passa-baixa (ideal, Butterworth, gaussiano) atenua as altas e suaviza; **passa-alta** atenua as baixas e realça, tem a mesma função do realce/aguçamento espacial; rejeita-banda e notch tiram ruído periódico. Convolução no espaço = multiplicação na frequência.
  - PEGADINHA: média e mediana são filtros espaciais (olham a vizinhança), não são a definição de passa-baixa ou rejeita-banda na frequência. Passa-alta deixa passar as altas e corta as baixas, nunca o contrário.
- Outras transformadas: **DCT** (cosseno, usada no JPEG), Walsh, Hadamard, **Haar**, Slant: todas com núcleo separável e simétrico. **Wavelet**: análise em **multirresolução**, localiza a frequência e também a posição (Fourier perde a localização), base do JPEG2000.

**Interpolação** (ampliar, girar, reamostrar)
- Vizinho mais próximo: copia o valor do vizinho mais perto; rápido, mas serrilha bordas retas e distorce detalhes finos.
- Bilinear: usa os **4** vizinhos mais próximos (média ponderada pela distância); suaviza e borra um pouco.
- Bicúbica: usa os **16** vizinhos (4×4); preserva melhor os detalhes, é a mais cara.

**Realce × restauração**
- Realce: deixar a imagem "melhor" para uma aplicação ou observador; é subjetivo (passa-altas, equalização, alargamento de contraste).
- Restauração: recuperar a imagem corrompida modelando a degradação e aplicando o processo inverso (filtro inverso, Wiener); é objetiva. Pode ser interativa (o usuário ajusta parâmetros até ficar bom). Transformações geométricas usadas na restauração mudam as relações espaciais entre os pixels. Alargamento de contraste é realce, não restauração. Ninguém tem "conhecimento total" da percepção visual.

**Segmentação**
- Dividir a imagem em regiões homogêneas por algum critério (brilho, cor, textura; similaridade, continuidade). As regiões não precisam ter o mesmo tamanho.
- Abordagens: por descontinuidade (detecção de bordas, que é só uma das técnicas) e por similaridade (limiarização/threshold, Otsu, crescimento de regiões, split and merge, watershed, k-means). Rotular **componentes conexos** agrupa pixels adjacentes e conta como segmentação.
- Não é compressão, não mexe em gamut, e identificar o objeto a partir de uma descrição já é reconhecimento.

**Morfologia matemática** (imagens binárias, com elemento estruturante)
- Erosão: encolhe objetos, some com pontos pequenos. Dilatação: engorda, fecha buracos pequenos.
- Abertura = erosão seguida de dilatação (tira ruído pequeno). Fechamento = dilatação seguida de erosão (fecha buracos).

**Textura** (descritores): matriz de co-ocorrência (Haralick), densidade local de bordas, energia nas sub-bandas de filtros de Gabor, espectro de Fourier, LBP. Todos servem para imagens monocromáticas.

**Reconhecimento de padrões**
- Cada objeto vira um **vetor de características** (descritores escolhidos com cuidado).
- **Classificador de distância mínima**: calcula o vetor médio (protótipo) de cada classe e coloca o objeto desconhecido na classe de menor distância. Funciona bem quando as médias das classes estão longe em relação à dispersão de cada classe. Não é o classificador estatístico de Bayes.
- **Perceptron**: uma unidade só, saída binária, resolve apenas problemas **linearmente separáveis**. Perceptron multicamadas (com retropropagação) resolve os não lineares; convolucional é o usado em imagens hoje.
- **Visão estéreo**: duas câmeras/pontos de vista da mesma cena; acha os pontos correspondentes e monta o **mapa de disparidade**, que dá a profundidade (quanto maior a disparidade, mais perto).

**Compressão de imagens**
- Redundâncias: de codificação, interpixel (espacial) e psicovisual. Compressão rende mais quando a imagem tem grandes áreas da mesma cor.
- Sem perdas: **Huffman** (códigos curtos para os símbolos mais prováveis), aritmética, LZW, **RLE** (guarda corridas de valores iguais, ótimo para áreas uniformes e padrões simples, ruim em foto), Golomb, **planos de bits** (decompõe a imagem em várias imagens binárias, uma por bit, e comprime cada uma).
- Com perdas: **JPEG** (blocos 8×8 → **DCT** → quantização que joga fora alta frequência → zigue-zague → Huffman); wavelet (JPEG2000). Com perdas não reconstrói exatamente a original.
- BMP: normalmente sem compressão (no máximo RLE), suporta alta resolução e profundidade de cor, mas o arquivo é grande e não serve para a web. PNG: sem perdas.
- Comprimento médio de um código: L = Σ p_i · (tamanho do código i). Ex.: probabilidades 0,5; 0,3; 0,2 com códigos 0, 10, 11 dão 0,5·1 + 0,3·2 + 0,2·2 = 1,5 bits/símbolo.

---

## [S19] Nomes e datas
busca: quem inventou, autor, ano, história, historia

| nome | o quê | quando |
|---|---|---|
| Ivan Sutherland | Sketchpad | 1963 |
| Cohen e Sutherland | recorte de retas por region code | 1967 |
| Sutherland e Hodgman | recorte de polígonos | 1974 |
| Weiler e Atherton | recorte de polígonos / superfície oculta | 1977 |
| Cyrus e Beck | recorte paramétrico | 1978 |
| Liang e Barsky | recorte paramétrico (pk, qk) | 1984 |
| Nicholl, Lee e Nicholl | recorte por inclinações | 1987 |
| Bresenham | retas só com inteiros (IBM) | 1965 |
| de Casteljau | algoritmo de curvas (Citroën, não publicou) | 1959 |
| Pierre Bézier | curvas (Renault, publicou) | ~1960 |
| Carl de Boor | B-splines (GM) | 1972 |
| Gouraud | interpolação de cor | 1971 |
| Bui-Tuong Phong | modelo de iluminação e interpolação de normais | 1975 |
| Blinn | Blinn-Phong (vetor meio) | 1977 |
| Catmull | z-buffer | 1974 |
| Newell, Newell e Sancha | algoritmo do pintor | 1972 |
| Warnock | subdivisão de área | 1969 |
| Fuchs, Kedem e Naylor | árvore BSP | 1980 |
| Appel | ray casting | 1968 |
| Whitted | ray tracing recursivo | 1980 |
| Goral et al. (Cornell) | radiosidade | 1984 |
| Cohen e Greenberg | hemicubo | 1985 |
| Maxwell | mistura de 3 cores | séc. XIX |

---

## [S20] Distratores e dicas de prova
busca: dica, distrator, Gauss-Seidel, Gauss-Jacobi, Runge-Kutta, Kruskal, Boundary-Fill

- Em "qual algoritmo é", os nomes de fora de CG são sempre os mesmos: **Gauss-Seidel, Gauss-Jacobi** (sistemas lineares), **Runge-Kutta** (EDO), **Kruskal** (árvore geradora mínima). Nunca são a resposta.
- "Marque todas": as alternativas erradas trocam **uma palavra** (aditiva × multiplicativa, 3 × 4 componentes, paralela × perspectiva, ortogonal × oblíqua, vetorial × interno, 2D × 3D, in × out). Leia devagar.
- Matriz em imagem: 3×3 é mundo 2D, 4×4 é 3D. Veja se o enunciado usa vetor-linha ([x y 1]·M, translação na última linha) ou vetor-coluna (M·[x y 1]ᵀ, translação na última coluna). As duas aparecem.
- Numérica: resposta inteira; arredonde (−0,33 vira 0). Desenhe a window e a reta antes de calcular. Lembre do y invertido na viewport e da origem deslocada.
- Questões de outros exames (POSCOMP) costumam aparecer com o enunciado original.
- Se nenhuma alternativa estiver exatamente certa, escolha a mais próxima e siga em frente.
- Treino: [[Quiz de treino - banco do professor]] (77 questões de 2021 com explicação) e [[Banco de Questões]] (videoaulas interativas e quiz de 2026).

---

## [S21] Matemática que cai junto: vetores e transformações lineares
busca: produto escalar, produto interno, produto vetorial, vetorial, ângulo entre vetores, angulo, norma, normal, vetor normal, plano, equação do plano, paramétrica, transformação linear, matriz, coluna, reflexão, reflexao, rotação, cisalhamento, expansão, contração, determinante, ortogonal, autovetor, inversa transposta, convexo, projeção ortogonal, vetor normal a um triângulo, linearmente independente, plano π

O POSCOMP põe essas na parte de Matemática, mas são as contas de CG (normal, ângulo, rotação).

**Produto escalar (interno)**: u·v = u1v1 + u2v2 (+ u3v3) = |u||v|cos θ.
- θ = arccos(u·v / (|u||v|)). Se u·v < 0, o ângulo passa de 90°; se = 0, são perpendiculares.
- Ex.: u = (1, 2), v = (3, −1): u·v = 1, |u| = √5, |v| = √10, cos θ = 1/√50 ≈ 0,141, θ ≈ 81,9°.

**Produto vetorial** (só em 3D): u × v = (u2v3 − u3v2, u3v1 − u1v3, u1v2 − u2v1).
- Dá um vetor perpendicular aos dois; |u × v| = |u||v| sen θ = área do paralelogramo.
- Propriedades: **anticomutativo** (u × v = −v × u), **não é associativo**, **é distributivo** sobre a soma (u × (v + w) = u×v + u×w), (k·u) × v = k(u × v), **não vale cancelamento**. u × v = 0 quando são paralelos (ou um é nulo), não precisa os dois serem nulos.
- Ex.: (1, 0, 2) × (0, 1, 1) = (0·1 − 2·1, 2·0 − 1·1, 1·1 − 0·0) = (−2, −1, 1).

**Normal de um triângulo/polígono** ABC: n = (B − A) × (C − A). Qualquer múltiplo também é normal; a ordem dos vértices define o sentido (anti-horário aponta para fora). Ex.: A (0,0,0), B (1,0,0), C (0,1,0) → (1,0,0) × (0,1,0) = (0,0,1).

**Plano**
- Equação geral: n·(X − P) = 0, ou seja ax + by + cz = d, com n = (a, b, c).
- Equação vetorial/paramétrica: X = P + a·u + b·v, com u e v linearmente independentes no plano; n = u × v.
- Vetores LI: não paralelos (produto vetorial ≠ 0).
- Reta P + tU furando o plano: t = n·(A − P) / (n·U), com A um ponto do plano.

**Matriz × vetor**: com vetor-coluna, A·(1,0,0) é a 1ª **coluna** de A, A·(0,1,0) a 2ª, e assim por diante. Com vetor-linha, (1,0,0)·A é a 1ª linha. PEGADINHA: alternativa que "lê a linha" quando a convenção é coluna.

**Reconhecer a transformação linear 2D pela matriz**
- Rotação: colunas unitárias e perpendiculares (ortogonal), det = +1, forma [[cos, −sen], [sen, cos]] (vetor-coluna).
- Reflexão (reflexão através de uma reta, espelhamento): ortogonal, **det = −1**, simétrica. A reta de reflexão é feita dos pontos que não mudam: resolve (A − I)v = 0. Reflexão na reta que faz ângulo α com x: [[cos 2α, sen 2α], [sen 2α, −cos 2α]].
  - Ex.: (1/5)·[[3, 4], [4, −3]]: colunas unitárias e perpendiculares, det = −1 → reflexão; (3/5 − 1)x + (4/5)y = 0 → reta y = x/2.
- Escala uniforme: k·I (expansão se k > 1, contração se k < 1).
- Cisalhamento horizontal: [[1, k], [0, 1]], det = 1, não é ortogonal.
- Translação não é linear (leva 0 em algo ≠ 0), não existe matriz 2×2 para ela (por isso as homogêneas, [S03]).
- Rotação dada por um par: se T(v) = w com |v| = |w|, o ângulo é a diferença das direções. Ex.: (3, 1) → (−1, 3): produto escalar 0 e mesmo módulo, rotação de 90° (π/2) anti-horária.

**Transformar normais**: pontos vão com M, mas normais vão com a **inversa transposta** (M⁻¹)ᵀ. Com escala não uniforme, M·n deixa de ser perpendicular à superfície. Para rotação pura (ortogonal) as duas coincidem.

**O que a transformação afim preserva**: retas, paralelismo, razão entre comprimentos na mesma reta e convexidade (objeto convexo continua convexo). Em geral não preserva ângulos nem medidas.
