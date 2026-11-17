---
tags: [cg, modulo-2]
---
# 14 · Percepção de Cor e Uso de Cores em CG

[[Computação Gráfica|↑ Índice]] · anterior: [[13 - Modelos Hierárquicos e Animação]]
Slides: [[12 - Percepção de Cor e Uso de Cores.pdf]] · Moodle: [Teoria das Cores](https://presencial.moodle.ufsc.br/mod/page/view.php?id=1710623) · [Visão a cores (Wikipedia)](http://en.wikipedia.org/wiki/Color_vision)

> [!info] A aula é em **24/11**, dois dias antes da prova. Revise depois que ela acontecer, o professor pode acrescentar material no Moodle.

## Conceitos básicos
- **Cores** são faixas de frequência do espectro eletromagnético que o olho humano percebe como semelhantes.
- O olho vê aproximadamente **uma oitava**: de **~780 nm (vermelho)** a **~350–380 nm (violeta)**.
- **Cores reflexivas**: reflexão **seletiva** de frequências pela superfície. Podem ser **opacas** ou **especulares**.
- **Cores emissivas**: o objeto **emite** radiação visível.
- **Em CG todos os objetos são emissivos** (o vídeo emite luz). Simular cores reflexivas serve para dar realismo.

## Fisiologia
- A **retina** capta a luz e transforma em impulsos nervosos. É organizada em **campos receptivos hexagonais** (colmeia).
- **Bastonetes**: muito sensíveis, funcionam com **pouca luz** (**visão noturna**), **não diferenciam cor** e codificam só intensidade.
- **Cones**: precisam de **muita luz**. **Três tipos** de opsinas, sensíveis a ondas **curtas (azul), médias (verde) e longas (vermelho)**.
- **Células horizontais** interligam os campos e "calculam a **segunda derivada**" do sinal (realce de bordas). **Células ganglionares** levam o sinal ao cérebro.
- Córtex visual:
  - **primário** = a "**tela mental**", só **intensidade** (imagem P&B);
  - **terciário** = processa e integra **cor**, mas **não forma imagens**. A cor é "pintada" sobre a imagem P&B **a posteriori**;
  - **secundário** detecta linhas.
- Consequência: **qualquer cor** pode ser criada misturando **3 componentes** que dividam o espectro como o olho divide (tricromacia). Formalizado por **Maxwell** (séc. XIX). Princípio usado desde a **Lanterna Mágica** e a **Fantasmagoria** (séc. XVII).

## Modelos de cor
| Modelo | Tipo | Uso |
|---|---|---|
| **CIE 1931 (XYZ)** | representa **toda cor visível** como vetor 3D, levando em conta a sensibilidade do olho | referência; **pouco intuitivo** ("que cor é X=0,7, Y=0,3, Z=0,6?") |
| **RGB** | **aditivo**, mimetiza os cones | monitores; o mais intuitivo; **cubo de cores** |
| **HSV / HSI** | tom (hue), saturação, valor/intensidade | interessante matematicamente, intuitivo para escolher cor |
| **CMYK** | **subtrativo** (ciano, magenta, amarelo, preto) | **indústria gráfica**, impressão |
| Pantone etc. | tabelas proprietárias | indústria gráfica, otimizar tinta |

## Geração de cor
- **True color**: cada pixel guarda a cor diretamente (ex.: 24 bits RGB).
- **Indexed color**: cada pixel guarda um **índice** numa **tabela de cores** (paleta/LUT).
- **Gamut**: a capacidade do dispositivo de representar cores, expressa como um **polígono** dentro do diagrama CIE.
