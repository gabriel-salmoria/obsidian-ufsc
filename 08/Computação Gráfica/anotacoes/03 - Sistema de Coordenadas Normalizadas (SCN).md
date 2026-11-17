---
tags: [cg, modulo-1]
---
# 03 · Sistema de Coordenadas Normalizadas (SCN) e rotação da window

[[Computação Gráfica|↑ Índice]] · anterior: [[02 - Transformações 2D e Coordenadas Homogêneas]] · próximo: [[04 - Clipping]]
Material: [[Biezuner - Transformações de Sistemas de Coordenadas.pdf]] · [[04 - Clipping.pdf]] (o início do PPT trata de coordenadas normalizadas)

## Por que normalizar
- Se a window pode **rodar**, deixa de ser um retângulo alinhado aos eixos do mundo. Fazer zoom, pan e clipping direto em coordenadas de mundo fica difícil.
- Solução: representar tudo num **sistema de coordenadas da window**. As duas opções vistas em aula são:
  - **SCN**: Sistema de Coordenadas Normalizado;
  - **PPC**: Sistema de Coordenadas do **Plano de Projeção** (os slides de rasterização chamam de "Coordenadas do Plano de Projeção / espaço de imagem"). No slide de clipping: *"sempre realizamos recorte em coordenadas da Clip Window, no nosso caso em PPC"*. O algoritmo se chama **"Gerar Descrição em PPC"**.
- Domínio usual: **[−1, 1]** com origem no **centro da window** (Window Center, WC). Os cantos da window viram (−1,−1) e (1,1).
- Vantagens: o clipping fica sempre contra o mesmo retângulo fixo (−1..1), e a transformada de viewport fica simples:
  $x_{vp} = \frac{x_{scn}+1}{2}\,(x_{vpmax}-x_{vpmin})$, $\;y_{vp} = \left(1-\frac{y_{scn}+1}{2}\right)(y_{vpmax}-y_{vpmin})$

## Gerando a descrição em SCN (algoritmo do professor)
1. Cria uma window no mundo com centro $(W_{cx}, W_{cy})$, altura e largura.
2. **Translada** o mundo por $(-W_{cx}, -W_{cy})$.
3. Determina o **vetor up** (view-up vector, VUP) da window e o **ângulo θ** entre ele e o eixo Y.
4. **Rotaciona** o mundo por **−θ** (alinha VUP com Y).
5. **Normaliza** (escala) pelo inverso do tamanho da window, $(\frac{2}{largura}, \frac{2}{altura})$, para o domínio [−1, 1].
6. Guarda essas coordenadas normalizadas em cada objeto (sem perder as coordenadas de mundo!).
7. Clipping é feito em SCN, depois a transformada de viewport.

Tudo isso é **uma matriz só**: $M_{SCN} = T(-W_c)\cdot R(-\theta)\cdot S\!\left(\tfrac{2}{w},\tfrac{2}{h}\right)$.

Com o SCN:
- **zoom** muda o tamanho da window → só muda o S;
- **pan** move o centro → só muda o T. Se a window está rodada, o pan "para cima" segue o VUP da window, não o Y do mundo;
- **rotação da window** muda o θ → só muda o R.

## Exemplo numérico (caiu)
Window de (10,11) a (16,20) → centro (13; 15,5), largura 6, altura 9.
Ponto (13, 14): $x_{scn} = 2\cdot\frac{13-10}{6}-1 = 0$, $\;y_{scn} = 2\cdot\frac{14-11}{9}-1 = -\tfrac{1}{3}$.
→ o X em coordenadas de window é **0** ([[Banco de Questões#2. Window, viewport e clipping|Q2.2]]).
