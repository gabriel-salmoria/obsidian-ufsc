---
tags: [cg, modulo-2]
---
# 11 · Rasterização (Conversão por Varredura) e Z-Buffer

[[Computação Gráfica|↑ Índice]] · anterior: [[10 - Visualização Realista - Raytracing, Raycasting e Radiosidade]] · próximo: [[12 - Iluminação - Modelo de Phong e Shading]]
Slides: [[11.1 - Rasterização (Shader I).pdf]] · [[11.2 - Z-Buffer (Shader II).pdf]]
Páginas do professor: [z-Buffering](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/zbuffering/index.html) · [Conversão de Varredura](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/varredura/index.html)

## Pipeline do "raytracing/pixel shading" no SGI (trabalho 3)
1. Criação da Window com orientação arbitrária
2. Transformação do mundo para **SCN**
3. **Clipping**
4. **Conversão por Varredura** (rasterização)
5. **Z-Buffering**, junto com a varredura (oclusão)
6. **Raytracing por pixel** (Pixel Shading)
7. Cópia do Z-Buffer (matriz de cor) para a **Viewport**

## Conversão por varredura (Scan Conversion / Rasterização)
- Dado um polígono em **coordenadas do plano de projeção** (espaço de imagem), determina **quais pixels** da viewport o interceptam.
- Junto com o Z-Buffer, decide **qual objeto preenche cada pixel** da imagem final.
- Método do professor: **dividir o polígono em trapézios** com topo e base **horizontais** (paralelos às linhas de varredura). Triângulos são trapézios degenerados.
  1. Ache os vértices de **maior e menor y**.
  2. Ordene os demais em **y decrescente** e trace uma horizontal por cada vértice.
  3. Converta cada trapézio; a união dos pixels é o polígono.
- **Rastreador de bordas** (*edge tracker*): segue as interseções da linha de varredura com cada borda lateral.
  - Ponto inicial: $(x_2 + x_d,\; \lfloor y_2\rfloor,\; z_2 + z_d)$ (discretização-piso de y; $x_d$ por semelhança de triângulos) [EQ 10.1]
  - Próxima linha: $P' = (x + x_{inc},\; y - 1,\; z + z_{inc})$, com $x_{inc} = \Delta x/\Delta y$, $z_{inc} = \Delta z/\Delta y$ [EQ 10.2]
  - Estrutura: `(x, y, z), xinc, zinc, ymin` (ymin diz quando parar)
- Em cada linha de varredura, preenche os pixels entre as bordas esquerda e direita, **incrementando z** de pixel a pixel [EQ 10.3/10.4], e manda cada pixel para o Z-Buffer.

## Z-Buffer (Buffer de Profundidade)
- Resolve o **problema da superfície visível** (*visible-surface*: o que se vê) ou, visto do outro lado, da **superfície oculta** (*hidden-surface*: o que não se vê).
- Para **cada pixel** guarda a **profundidade z** do objeto mais próximo e a **cor** desse ponto.
- Inicialização: z-buffer = **+∞** (um valor positivo enorme); matriz de cor = **fundo** (preto).

```
para cada polígono P:
    para cada pixel (x, y) que intercepta P:
        z = profundidade de P em (x, y)
        se z < zbuffer[x][y]:
            cor[x][y] = intensidade de P em (x, y)
            zbuffer[x][y] = z
desenhe cor
```
- É como "achar o menor valor num array", pixel a pixel.
- **A ordem de processamento dos polígonos não muda o resultado** (POSCOMP 2012). Duas esferas, uma cobrindo a outra: a imagem é a mesma qualquer que seja a ordem.
- Encaixa naturalmente na varredura: o z de cada pixel já sai das equações incrementais.
- Custos: **memória** de um z por pixel; precisão finita de z (z-fighting).

> [!note] Sentido do z
> Nos slides, "mais perto" = **menor z** (buffer começa em +∞). A página web antiga usa z do mundo apontando para o observador, e aí troca se o z for **maior**. O conceito é o mesmo: fica com o mais próximo.
