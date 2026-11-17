---
tags: [cg, prova, questoes]
---
# Banco de Questões — INE5420

Voltar: [[Computação Gráfica]] · Formulário: [[Formulário]]

Duas fontes, as duas com gabarito oficial:

1. **Quiz de Treino para Prova** (Moodle). A minha tentativa de 15/11/2026 tirou 10/10. Cada tentativa sorteia questões do banco, então fazer outras tentativas mostra questões novas. O quiz fica aberto até 14/12.
2. **Videoaulas interativas (H5P)**. Segundo o professor, *"as questões dos quizes e exercícios das videoaulas interativas são extraídas diretamente do Banco de Questões da prova teórica"*. Os links estão em cada seção.

> [!tip] Padrão das questões
> - Muitas são **"marque todas as verdadeiras"**, com alternativas quase iguais que mudam uma palavra (ex.: *oblíqua* × *ortogonal*, *aditivas* × *multiplicativas*, *3* × *4 componentes*).
> - Nas questões de **nome de algoritmo**, a lista de distratores é sempre a mesma: Gauss-Seidel, Gauss-Jacobi, Runge-Kutta, Kruskal (nenhum deles é de CG).
> - Nas questões **numéricas** (clipping + window/viewport) a resposta é um inteiro.
> - Algumas vêm do POSCOMP (2004, 2012, 2014, 2016).

---

## 1. Transformações 2D e coordenadas homogêneas
Videoaula: [Aula 3.0 interativa](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20784) · [YouTube](https://youtu.be/HYRbRAc2eQI) · nota: [[02 - Transformações 2D e Coordenadas Homogêneas]]

**Q1.1** Sobre o mapeamento de um mundo **3D** para coordenadas homogêneas:
- ✅ Adicionamos **uma** dimensão: pontos 4D `[X Y Z W]`, com **W constante e ≠ 0**. Por simplicidade usamos **W = 1**.
- ❌ W = −1 constante · ❌ W = 0 · ❌ W é função da norma de [x y z] · ❌ "W **só pode** ser 1" · ❌ "Coordenadas homogêneas é outro nome para Sistema de Coordenadas Normalizado" · ❌ duplicar para 6D · ❌ "só depois de normalizar para [0,1]"

**Q1.2** Dada a expressão abaixo, marque as verdadeiras:

![[h5p-transf-expressao.png]]

- ✅ Com coordenadas homogêneas **toda** operação geométrica sobre um ponto vira multiplicação de matrizes (ponto × matriz).
- ✅ A expressão descreve uma transformação genérica de um **mundo 2D** em coordenadas homogêneas.
- ✅ W = 1 está correto: W é o **fator de escala**, e W = 1 não altera x e y.
- ✅ W = 1 está correto: W deve ser **constante e ≠ 0** (W = 0 daria divisão por zero).
- ❌ "apenas Rotação" / "apenas Escalonamento" como multiplicação de matrizes · ❌ "mundo 3D" · ❌ "W deve ser sempre 0"

**Q1.3** Escalonar um objeto 2D em torno do seu centro geométrico `[x y]` pelos fatores `[a b]`. A composta é `M = T1 · S · T2`.

![[h5p-transf-escala-centro.png]]

- ✅ **Matrizes da opção (b), M da opção (1).**
- Por quê: o professor usa **vetor-linha** (`[x y 1]·M`, translação na **última linha**). Primeiro levamos o centro à origem (`T1` com −x, −y), escalamos por (a, b) e voltamos (`T2` com +x, +y). A última linha fica `x − a·x = x(1−a)` e `y(1−b)`.

**Q1.4** Sobre $S_x$ e $S_y$ na matriz abaixo:

![[h5p-transf-matriz-sx-sy.png]]

- ✅ São os **fatores de escala** de um escalonamento 2D em coordenadas homogêneas.
- ❌ fatores de deslocamento de translação (as alternativas com $S(t)=S_0+Vt$ e "games de corrida" são pegadinha) · ❌ rotação 2D/3D · ❌ "escalonamento 3D com z unitário"

**Q1.5** A matriz abaixo é:

![[h5p-transf-matriz-rotacao.png]]

- ✅ **Rotação para um mundo 2D** em coordenadas homogêneas (3×3, cos/sen no bloco 2×2).
- ❌ translação 3D, escalonamento 3D, rotação 3D, escalonamento 2D, translação 2D

**Q1.6 (Quiz de treino)** A matriz abaixo é:

![[quiz-matriz-escala-2d.png]]

- ✅ **Escalonamento para um mundo 2D** em coordenadas homogêneas.

**Q1.7 (Quiz de treino)** Escalonamento **3D** pelo vetor S = [1 2 3] em coordenadas homogêneas:

![[quiz-matriz-escala-3d.png]]

- ✅ Matriz **4×4** com diagonal 1, 2, 3, **1**. Cuidado com as alternativas 3×3 ou com o 1 em outra posição.

**Q1.8 (Quiz de treino, POSCOMP 2016 Q57)** Sobre transformações 2D/3D:
- I. Coordenadas homogêneas são necessárias para representar translação como matriz → **V** (translação não é linear em 2D, só vira multiplicação em n+1 dimensões).
- II. Escala uniforme + rotação 2D: a ordem muda o resultado → **F** (escala uniforme comuta com rotação).
- III. Duas rotações 3D de 90° (em X e em Z): a ordem não afeta → **F** (rotações em eixos diferentes não comutam).
- ✅ **Apenas I.**

---

## 2. Window, viewport e clipping
Videoaula: [Aula 4.2 interativa](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20785) · [YouTube](https://youtu.be/rvDEhyDLcp8) · notas: [[04 - Clipping]], [[03 - Sistema de Coordenadas Normalizadas (SCN)]], [[01 - Conceitos Básicos]]

**Q2.1 Cohen-Sutherland.** Ordem dos RCs: RC[1] acima, RC[2] abaixo, RC[3] direita, RC[4] esquerda. Window de (10,11) a (16,20), reta de p1 = (7,12) a p2 = (13,12).

![[h5p-clip-reta-y12.png]]

- ✅ **p1 = [0 0 0 1] e p2 = [0 0 0 0]** (p1 está só à esquerda; p2 está dentro).

**Q2.2 Numérica, SCN com origem no centro da window, domínio [−1, 1].** Reta de p1 = (7,14) a p2 = (13,14), mesma window. Qual o X de p2 em coordenadas de window?

![[h5p-clip-reta-y14.png]]

- ✅ **0**. O centro da window é ((10+16)/2, (11+20)/2) = (13; 15,5), e p2 tem x = 13, o mesmo x do centro.
- Conta: $x_{scn} = 2\,\frac{x - x_{wmin}}{x_{wmax}-x_{wmin}} - 1 = 2\cdot\frac{3}{6} - 1 = 0$.

(Esta questão também caiu no quiz de treino:)

![[quiz-clip-wc.png]]

**Q2.3 Numérica, viewport.** Mesma window, reta (7,12)→(13,12). Viewport de **320×180** com origem em **(10,10)**. Lembre que o **y da viewport aponta para baixo**.
- X de p2 na viewport: $x_v = 10 + \frac{13-10}{16-10}\cdot 320 = 10 + 160 =$ ✅ **170**
- Y do novo p1' (clipado = (10,12)): $y_v = 10 + \left(1 - \frac{12-11}{20-11}\right)\cdot 180 = 10 + \frac{8}{9}\cdot 180 = 10 + 160 =$ ✅ **170**

**Q2.4** Algoritmo de recorte de retas baseado no cálculo e comparação dos parâmetros $p_k$ e $q_k$:

![[h5p-clip-liang-barsky-pq.png]]

- ✅ **Liang-Barsky**

**Q2.5** Algoritmo de recorte de retas baseado em comparar o **coeficiente angular** da reta com os coeficientes de retas de referência (de P1 até os cantos da window):

![[h5p-clip-nln-regioes.png]]

- ✅ **Nicholl-Lee-Nicholl**

**Q2.6** Exemplos de algoritmos de recorte de **polígonos**:
- ✅ **Sutherland-Hodgeman** e ✅ **Weiler-Atherton**
- ❌ Cohen-Sutherland, Liang-Barsky, Nicholl-Lee-Nicholl (esses três recortam **retas**) · ❌ Gauss-*, Runge-Kutta, Kruskal

**Q2.7 (Quiz de treino)** "É um exemplo de algoritmo de recorte de polígonos": ✅ **Weiler-Atherton** (nessa versão Sutherland-Hodgeman não estava entre as opções).

**Q2.8 (Quiz de treino, POSCOMP 2004)** Window (0,0)–(60,60), viewport (0,0)–(100,80). Instanciamento, nesta ordem: escala (1, 2), rotação 0°, translação (10, 0). Triângulo (10,0)–(10,30)–(40,0). Qual desenho?

![[quiz-poscomp2004-viewport.png]]

- ✅ **Opção c**
- Conta: escala → (10,0),(10,60),(40,0); translação → (20,0),(20,60),(50,0). Na window de 0..60, o lado vertical fica em x = 20/60 = **1/3** da largura e vai do fundo (y=0) ao topo (y=60); o terceiro vértice fica em 50/60 = **5/6** da largura, embaixo. É o desenho (c).

---

## 3. 3D (projeções e estrutura de arame)
Videoaulas: [Aula 7.3 Projeções Paralelas](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20786) · [Aula 8.1 Perspectiva](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20787) · notas: [[07 - 3D - Transformações e Projeção Paralela]], [[08 - Projeção em Perspectiva e Clipping 3D]]

> [!warning] Classificação do professor
> No gabarito do professor, **axonométricas (isométrica, dimétrica, trimétrica) aparecem sob "Oblíquas ou Pictóricas"**. O Foley classifica de outro jeito (axonométricas como ortográficas). **Na prova, vale a do professor.**

**Q3.1** Sobre projeção paralela, marque as verdadeiras:

![[h5p-proj-paralela.png]]

- ✅ A projeção paralela comumente usada em CG é a **Ortogonal**.
- ✅ Na paralela, os raios de projeção são **paralelos** e a amplitude do campo de visão **não muda** com a distância, por isso o tamanho aparente **não varia**.
- ✅ A **isométrica** é exemplo de *Projeção Paralela **Oblíqua** do tipo **Axonométrica*** (mantém as dimensões sobre os eixos), por isso é muito usada em desenho técnico e engenharia.
- ✅ Para fazer uma **Paralela Ortogonal**, depois de normalizar para o sistema de coordenadas da window, **basta ignorar Z**.
- ✅ Na paralela o tamanho aparente não varia com a distância, **por isso os objetos às vezes parecem distorcidos**.
- ❌ "Para uma **Perspectiva** basta ignorar Z" · ❌ "na paralela o tamanho aparente é ajustado fielmente à distância" · ❌ "raios formando pirâmide truncada" (isso é perspectiva)

**Q3.2** Sobre as técnicas de projeção, marque as verdadeiras:
- ✅ Paralela **Ortogonal**: depois de normalizar, basta ignorar Z.
- ✅ A isométrica é exemplo de **Projeções Paralelas** do tipo **Axonométrico**.
- ✅ A projeção paralela comum em CG é a Ortogonal.
- ✅ **Cavaleira** e **Cabinet** são **Paralelas Oblíquas ou Pictóricas**.
- ✅ Existem basicamente **dois tipos de projeção paralela**: (a) **Ortogonais ou Ortográficas** e (b) **Oblíquas ou Pictóricas**.
- ❌ "Perspectiva: basta ignorar Z" · ❌ "isométrica é exemplo de projeção **em perspectiva**" · ❌ "dois tipos de projeção: Ortogonais e Perspectiva" (o certo seria **Paralela** × Perspectiva)

**Q3.3 (Quiz de treino, POSCOMP 2014 Q57)** Sobre a estrutura de arame:
- I. É preciso obter o conjunto dos vértices de todos os pontos do objeto → **V**
- II. É preciso obter o conjunto dos pontos de cada face → **V**
- III. A normal de uma face é calculada com 3 pontos e **produto vetorial** → **V**
- IV. A normal é calculada com 3 pontos e **produto interno** → **F**
- ✅ **Somente I, II e III.**

---

## 4. Visualização realista (raytracing, raycasting, radiosidade)
Videoaula: [Aula 10 interativa](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20788) · [YouTube](https://youtu.be/Q1JN5jO8Ee0) · nota: [[10 - Visualização Realista - Raytracing, Raycasting e Radiosidade]]

**Q4.1** Programa que renderiza imagens 3D simulando o trajeto dos raios de luz **de trás para frente**: projeta, a partir do observador, um raio **para cada pixel da viewport**, que intercepta os objetos da cena.

![[h5p-raytracer.png]]

- ✅ **Ray Tracer**
- ❌ Ray Caster, Iluminador Global/Radiosidade, Modelo de Phong, Pixel Shader, Anti-Aliasing

**Q4.2** Em CG, **Radiância** e **Radiosidade** dizem respeito a:
- ✅ **Métodos de iluminação global** que modelam a **inter-reflexão difusa** entre os objetos da cena (interações luminosas e reflexos entre objetos).
- ❌ luz própria/corpo negro/2600–6000 K · ❌ dispersão de Rayleigh · ❌ raios crepusculares · ❌ raios umbrais · ❌ scattering/efeito Tyndall/névoa

**Q4.3** Programa que dispara raios **para dentro de um volume de dados 3D denso** e colore com a combinação das cores dos **voxels** atravessados (radar, tomografia, ressonância):

![[h5p-raycaster.png]]

- ✅ **Ray Caster Volumétrico**
- ❌ Ray Tracer Volumétrico, Ray Shader Volumétrico, Radiosidade Densa, "Phong Denso"

---

## 5. Iluminação, Phong e shading
Videoaula: [Aula 11.3 interativa](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20789) · [YouTube](https://youtu.be/xGaYix3TUac) · notas: [[12 - Iluminação - Modelo de Phong e Shading]], [[11 - Rasterização e Z-Buffer]]

**Q5.1** Por que calcular as **normais** das facetas é importante para a aparência?

![[h5p-phong-normais.png]]

- ✅ Permite calcular a intensidade do **reflexo especular** naquele ponto (o quão brilhante/espelhado ele fica).
- ✅ Permite calcular a intensidade da **iluminação difusa direta** naquele ponto.
- ❌ calcular **transparência** ou **translucência** · ❌ intensidade da luz **ambiente** (ela é constante e não depende da normal) · ❌ saber se o ponto está **na sombra** de outro objeto · ❌ curvatura do mesh · ❌ octrees/colisões

**Q5.2** Sobre o Modelo de Phong:
- ✅ Trabalha com **3 componentes aditivas**.
- ✅ Componentes: **Luz Direta (ou Difusa)**, **Luz Especular** e **Luz Ambiente (ou Indireta)**.
- ❌ 3 ou 4 componentes **multiplicativas** · ❌ 4 componentes aditivas · ❌ qualquer lista com "Transparente" ou com 4 itens

**Q5.3** Programa/módulo que produz níveis de cor e iluminação para os **pixels** de uma imagem (ou efeitos de reflexo/transparência), tipicamente codificado e executado na **GPU**:
- ✅ **Pixel Shader ou Ray Shader**

**Q5.4 (Quiz de treino, POSCOMP 2012 Q55)** Duas esferas no volume de visualização, uma totalmente encoberta pela outra, com projeção paralela:
- ✅ Com **Z-Buffer**, a imagem final é a mesma **independentemente da ordem** de rasterização das esferas.
- ❌ "algoritmos de superfície oculta não são úteis porque as duas estão no volume" · ❌ "a encoberta pode ser maior, basta estarem longe" (na **paralela** o tamanho não diminui com a distância, então uma esfera maior não fica totalmente coberta) · ❌ "**Gouraud** descreve a sombra de uma esfera na outra" (Gouraud é interpolação de intensidade e não calcula sombra) · ❌ "no **Phong**, a iluminação de uma esfera depende da cor da outra" (Phong é modelo **local**)

---

## 6. APIs, engines e ferramentas
Nota: [[01 - Conceitos Básicos]]

**Q6.1 (Quiz de treino)** Exemplos de **APIs gráficas** atuais:
- ✅ **OpenGL, WebGL e Direct3D**
- ❌ "OpenGL, Direct3D e **DirectX**" e "OpenGL, WebGL e **DirectX**". DirectX é uma **coleção** de APIs multimídia (som, input...); a API gráfica dentro dela é o Direct3D.
- ❌ Blender, Unity (Blender é modelador, Unity é engine) · ❌ Moray, POV-Ray (modelador e raytracer)

**Q6.2 (Quiz de treino)** Pacote com motor gráfico 2D/3D, motor de física/colisão, animação, som, IA, networking, memória, arquivos, threads, grafo de cena e linguagem de script:
- ✅ **Game Engine (Motor de Jogo)**
- ❌ Pacote de Modelagem 3D · ❌ "APK do WebGL/OpenGL" · ❌ "API gráfica de última geração"
