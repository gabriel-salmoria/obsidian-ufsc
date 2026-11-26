---
tags: [cg, indice]
disciplina: INE5420 - Computação Gráfica (2026-2)
professor: Aldo von Wangenheim
---
# INE5420 · Computação Gráfica: Índice e Guia da Prova

[Moodle da disciplina](https://presencial.moodle.ufsc.br/course/view.php?id=49656) · [Site LAPIX](http://www.lapix.ufsc.br/ensino/computacao-grafica) · [Playlist de videoaulas](https://www.youtube.com/playlist?list=PLmDIGfkfgKy0EDQWQdkvQ4QmA-hWSkV1P) · [Curso público de videoaulas interativas](https://bit.ly/CGinterativa) · [Plano de ensino](https://programas-planos.inf.ufsc.br/planos/5297)

## 📅 Prova Teórica Semestral
| | |
|---|---|
| **Data** | **Quinta, 26/11/2026**, abre 08:20, fecha 10:00 |
| **Local** | Online **presencial**, no **3º andar do INE** (quiz no Moodle com **senha**, lista de presença em papel; sem assinar, a nota não conta) |
| **Duração** | **55 min**: 5 min de leitura prévia + **5 min por questão** → **~10 questões** |
| **Consulta** | **Toda a internet, menos redes sociais e chats** |
| **Tentativas** | 1 · aprovação a partir de 6,0 |
| **Peso** | **30% da nota semestral** (os trabalhos valem 70%) |
| **19/11** | Data alternativa **só com justificativa** (atestado, aceite de artigo...). É por isso que o quiz no Moodle mostra 19/11 nas configurações. O fórum confirma **26/11** para a turma. |

> [!tip] Estratégia
> 1. **O banco de questões é a melhor fonte.** O professor diz que as questões das videoaulas interativas (H5P) **saem do banco da prova**. Estão todas, com gabarito, em [[Banco de Questões]].
> 2. Faça mais tentativas do [Quiz de Treino](https://presencial.moodle.ufsc.br/mod/quiz/view.php?id=1710606) (aberto até 14/12, vale a maior nota). Cada tentativa sorteia questões diferentes.
> 3. Tenha o [[Formulário]] aberto durante a prova, para as contas de window/viewport/clipping.
> 4. Questões "marque todas" mudam **uma palavra** (oblíqua/ortogonal, aditiva/multiplicativa, 3/4 componentes). Leia devagar.

## 🗂️ Anotações (em ordem do curso)
**Módulo I: CG Básica (SGI)**
1. [[01 - Conceitos Básicos]]: display file, random × raster scan, window/viewport, APIs × engines
2. [[02 - Transformações 2D e Coordenadas Homogêneas]] ⭐ (tem H5P)
3. [[03 - Sistema de Coordenadas Normalizadas (SCN)]]
4. [[04 - Clipping]] ⭐ (tem H5P, questões numéricas)
5. [[05 - Curvas - Hermite e Bézier]]
6. [[06 - B-Splines e Forward Differences]]
7. [[07 - 3D - Transformações e Projeção Paralela]] ⭐ (tem H5P)
8. [[08 - Projeção em Perspectiva e Clipping 3D]] ⭐ (tem H5P)
9. [[09 - Superfícies Bicúbicas]]

**Módulo II: Visualização realista e iluminação**
10. [[10 - Visualização Realista - Raytracing, Raycasting e Radiosidade]] ⭐ (tem H5P)
11. [[11 - Rasterização e Z-Buffer]]
12. [[12 - Iluminação - Modelo de Phong e Shading]] ⭐ (tem H5P)
13. [[13 - Modelos Hierárquicos e Animação]]
14. [[14 - Percepção de Cor]]

**Consulta rápida**: [[Colinha v1]] (versão atual, com glossário e algoritmos; também em `provas/Colinha v1.html` e `.pdf`) · [[Colinha]] (v0, versão anterior, congelada) · [[Mapa do que cai]] (cada assunto que aparece nas questões → seção da Colinha) · processamento de imagens e a matemática de vetores estão na Colinha, seções [S18] e [S21] · [[Formulário]] · [[Banco de Questões]] · [[Quiz de treino - banco do professor]] (77 questões do quiz de 2021 com explicação; versão interativa em `provas/quiz-treino.html`) · [[POSCOMP - Computação Gráfica]] (105 questões do POSCOMP 2002–2026: CG, matemática usada em CG e processamento de imagens, gabarito oficial; interativa em `provas/poscomp-cg.html`)

⭐ = tópico com videoaula interativa, cujas questões vêm do banco da prova.

## 📚 Material (por tópico)
| Tópico | Slides | Apostila / extra | Videoaula interativa |
|---|---|---|---|
| Intro | [[01 - Introdução e Visão Geral da Disciplina.pdf]] | | |
| 1.1 Conceitos básicos | [[02 - Conceitos Básicos - Window, Viewport e Display File.pdf]] | [[Apostila 1.1 - Conceitos Básicos.pdf]] | |
| 1.2 Transformações 2D | [[03 - Transformações 2D e Coordenadas Homogêneas.pdf]] | [[Apostila 1.2 - Transformações 2D.pdf]] · [[Exercícios de Transformações.pdf]] | [Aula 3.0](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20784) |
| 1.3 SCN | (início do PPT de clipping) | [[Biezuner - Transformações de Sistemas de Coordenadas.pdf]] | |
| 1.3.2 Clipping | [[04 - Clipping.pdf]] | [[Apostila - Clipping.pdf]] · [[Revisão 1.3.3 - Exercícios de Clipping de Polígonos.pdf]] · [[Weiler & Atherton (1977) - Hidden Surface Removal Using Polygon Area Sorting.pdf]] | [Aula 4.2](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20785) |
| 1.4 Hermite/Bézier | [[05.1 - Curvas Paramétricas - Conceitos Básicos e Hermite.pdf]] · [[05.2 - Curvas Paramétricas - Bézier.pdf]] | [[Apostila antiga - Curvas Paramétricas (CG4).pdf]] · [[Exercício 1.4.1 - Plote uma curva com Hermite e Bézier.pdf]] | |
| 1.4.2 B-spline + FD | [[06.1 - Curvas Paramétricas - B-Splines.pdf]] · [[06.2 - Curvas Paramétricas - Forward Differences.pdf]] · [[06.3 - B-Splines e Forward Differences (corrigido).pdf]] · [[06.4 - B-Splines e Forward Differences (PDF novo).pdf]] · [[06.5 - Desempenho de Operações em Ponto Flutuante.pdf]] | [[Exemplo - Forward Differences com B-Splines 2D.pdf]] | |
| 1.5 3D + paralela | [[07.1 - Rotação 3D Passo a Passo.pdf]] · [[07.2 - Exemplo Numérico de Projeção Paralela.pdf]] | [[Livro - Rotações em 2D e 3D.pdf]] · [[Especificação OBJ v3.pdf]] | [Aula 7.3](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20786) |
| 1.5.2 Perspectiva | [[08 - Projeção em Perspectiva.pdf]] | | [Aula 8.1](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20787) |
| 1.6 Superfícies | [[09.1 - Superfícies Bicúbicas.pdf]] · [[09.2 - Forward Differences em Superfícies Bicúbicas.pdf]] | [[Foley - Cap. 11 - Curvas e Superfícies.pdf]] · [[Salomon - Forward Differences em Superfícies Bicúbicas.pdf]] | |
| 2.0 Raytracing | [[10 - Módulo II - Raytracing e Raycasting.pdf]] | [páginas do prof.](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/index.html) | [Aula 10](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20788) |
| 2.1 Rasterização/Z-buffer | [[11.1 - Rasterização (Shader I).pdf]] · [[11.2 - Z-Buffer (Shader II).pdf]] | | |
| 2.3 Phong | (H5P) | [iluminação](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/iluminacao.html) · [radiosidade](http://www.lapix.ufsc.br/ensino/computacao-grafica/computacao-graficao-metodo-da-radiosidade-modelando-radiancia-e-interacao-luminosa-entre-objetos) | [Aula 11.3](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20789) |
| 3 Modelos hierárquicos | | [[Angel & Shreiner - Cap. 8 - Modelos Hierárquicos (trechos).pdf]] | |
| 2.4 Cor | [[12 - Percepção de Cor e Uso de Cores.pdf]] | | |

Livros completos que ficaram **fora do vault** por tamanho (passam do limite de 100 MB do GitHub): [Foley 2ª ed. (179 MB)](https://presencial.moodle.ufsc.br/mod/resource/view.php?id=1710288) · [OpenGL SuperBible 6ª (92 MB)](https://presencial.moodle.ufsc.br/mod/resource/view.php?id=1710289). O [[Salomon - Curves and Surfaces for Computer Graphics.pdf|Salomon]] (12 MB) está em `livros/`.

## 🧭 Conteúdo programático (plano de ensino) → o que pode cair
1. Introdução, aplicações · 2. Conceitos básicos · 3. Coordenadas 2D: transformações, homogêneas, sistema da window, clipping 2D · 4. Curvas: blending functions, forward differences · 5. 3D: projeções, paralelas, transformações 3D · 6. Perspectiva e clipping 3D · 7. Superfícies bicúbicas (analíticos e iterativos) · 8. Teoria da iluminação: raytracing/raycasting/rayshading, z-buffer, varredura, iluminação · 9. Pixel shading (CPU/GPU) · 10. Ferramentas: POV-Ray, Moray, linguagens de cena · 11. Radiância · 12. APIs gráficas (OpenGL...) · 13. Modelos hierárquicos

IA gerativa **não está no programa** (o professor diz isso no Moodle; vale só ponto extra nos trabalhos).

## 🗓️ Cronograma final (fórum, 02/11)
| Data | Aula |
|---|---|
| 10/11 | 2.1 Rasterização, Z-Buffer + 2.3 Phong, raytracing × pixel shading |
| 12/11 | 2.2 Prática: Blender |
| 17/11 | 3. Modelos hierárquicos & animação |
| 19/11 | 3.1.1 Personagens + rigging & Unity (e data alternativa da prova) |
| 24/11 | 2.4 Percepção de cor |
| **26/11** | **Prova teórica** |
| 01/12 e 03/12 | Defesa dos trabalhos 2, 3 e 4 ([conferenciaweb](https://conferenciaweb.rnp.br/ufsc/lapix)) |
