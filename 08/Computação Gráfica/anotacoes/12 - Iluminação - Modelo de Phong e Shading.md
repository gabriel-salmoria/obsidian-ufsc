---
tags: [cg, modulo-2]
---
# 12 · Iluminação: Modelo de Phong e Shading

[[Computação Gráfica|↑ Índice]] · anterior: [[11 - Rasterização e Z-Buffer]] · próximo: [[13 - Modelos Hierárquicos e Animação]]
Página do professor: [Modelando a Iluminação de um Objeto](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/iluminacao.html)
Videoaula interativa (vem do banco): [Aula 11.3 Phong e Pixel Shading](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20789) · questões em [[Banco de Questões#5. Iluminação, Phong e shading]]

## Modelo de Phong (Bui-Tuong Phong, CACM 1975)
- O modelo de iluminação provavelmente **mais usado** em CG.
- **3 componentes, ADITIVAS**: **Difusa (Direta)** + **Especular** + **Ambiente (Indireta)**.

> [!danger] Pegadinhas do gabarito
> - ❌ "multiplicativas" · ❌ "4 componentes" · ❌ qualquer lista com **"Luz Transparente"** ou com Direta **e** Difusa como componentes separadas.
> - ✅ "Luz Direta (ou Difusa), Luz Especular e Luz Ambiente (ou Indireta)".

$$
I = \underbrace{I_a\,k_a}_{\text{ambiente}} \;+\; \underbrace{I_l\,k_d\,(\hat N\cdot\hat L)}_{\text{difusa}} \;+\; \underbrace{I_l\,k_s\,(\hat R\cdot\hat V)^n}_{\text{especular}}
$$

### Difusa
- Reflexões **não direcionais**: reflete **igual em todas as direções**, então **não depende de onde o observador está**.
- Depende só do **cosseno do ângulo entre a normal N e a direção da luz L** (Lambert).
- **Coeficiente de reflectância difusa** $k_d$, que carrega a **cor do objeto**.

### Especular
- Reflexos **extremamente direcionais**, como num espelho. Diz o quão **brilhante** o objeto é.
- **Não é afetada pela cor da superfície**: o reflexo tem a **cor da luz** (bule vermelho só com especular aparece preto com reflexo branco). Simula metal e esmalte.
- Proporcional a $\cos^n$ do ângulo entre a **direção de visada V** e a **direção de reflexão R** (R é L espelhado em torno de N, mesmo ângulo e lado oposto).
- **Coeficiente de reflectividade especular** $k_s$ e **expoente especular n**: n grande = brilho **pequeno e concentrado** (decai rápido).

### Ambiente
- Aproxima a **luz das interações entre objetos** e da difusão na atmosfera. Na Lua (sem atmosfera) as sombras são quase pretas; numa floresta úmida, não.
- Calcular isso de verdade é o **método da radiância/radiosidade** ([[10 - Visualização Realista - Raytracing, Raycasting e Radiosidade#Radiosidade|radiosidade]]). Phong simplifica com um **termo constante** × **coeficiente de reflectividade ambiente** $k_a$, como se o objeto **emitisse** essa luz igual em todas as direções.

### Por que calcular normais? (caiu)
- ✅ Para a intensidade **difusa** direta (precisa de N·L).
- ✅ Para o **reflexo especular** (R depende de N).
- ❌ **Não** serve para transparência ou translucência, **nem** para a luz ambiente (constante), **nem** para saber se o ponto está **na sombra** de outro objeto (isso exige **raios umbrais**/shadow rays).
- A normal reduz o cálculo de inclinação da superfície a ângulos entre vetores, o que é **rápido** em tempo real.

## Shading (como aplicar a iluminação aos polígonos)
| Técnica | Calcula a iluminação | Resultado |
|---|---|---|
| **Flat** (constante) | **1 vez por face** (normal da face) | facetado |
| **Gouraud** | nos **vértices** e **interpola as intensidades** ao longo da face | suave, mas perde/borra brilhos especulares no meio da face |
| **Phong shading** | **interpola as normais** e calcula a iluminação **por pixel** | brilho especular correto, mais caro |

- **Modelo de Phong** (equação de iluminação) ≠ **Phong shading** (interpolar normais). Não confundir.
- Phong e Gouraud são **modelos locais**: **não calculam sombras** nem dependem da cor de outros objetos (POSCOMP 2012, alternativas d e e são falsas).

## Pixel shader
Programa que calcula **cor e iluminação por pixel** (ou reflexo/transparência), **tipicamente na GPU**. No trabalho 3: rasterização + z-buffer + Phong por pixel.
