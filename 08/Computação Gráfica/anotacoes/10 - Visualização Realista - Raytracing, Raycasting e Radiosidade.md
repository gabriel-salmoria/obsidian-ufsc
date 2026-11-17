---
tags: [cg, modulo-2]
---
# 10 · Visualização Realista: Raytracing, Raycasting e Radiosidade

[[Computação Gráfica|↑ Índice]] · anterior: [[09 - Superfícies Bicúbicas]] · próximo: [[11 - Rasterização e Z-Buffer]]
Slides: [[10 - Módulo II - Raytracing e Raycasting.pdf]] (versão comprimida; o PPTX original tem 122 MB e está [no Moodle](https://presencial.moodle.ufsc.br/mod/resource/view.php?id=1710537))
Páginas do professor: [O que é Raytracing](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/index.html) · [Principais raytracers](http://www.inf.ufsc.br/~awangenh/grafica/raytracing/raytracers.html) · [Radiosidade](http://www.lapix.ufsc.br/ensino/computacao-grafica/computacao-graficao-metodo-da-radiosidade-modelando-radiancia-e-interacao-luminosa-entre-objetos)
Videoaula interativa (vem do banco): [Aula 10](https://presencial.moodle.ufsc.br/mod/hvp/view.php?id=20788) · questões em [[Banco de Questões#4. Visualização realista (raytracing, raycasting, radiosidade)]]

## Definições que caem quase literalmente
| Termo | Definição (a do gabarito) |
|---|---|
| **Ray Tracer** | Renderiza imagens 3D **simulando o trajeto dos raios de luz, mas de trás para frente**: do **observador**, um raio **para cada pixel da viewport**, que intercepta os objetos da cena. |
| **Ray Caster** | Dispara raios do observador e pega **só a 1ª interseção**, sem raios secundários recursivos (sem reflexo/refração). |
| **Ray Caster Volumétrico** | Dispara raios **para dentro de um volume de dados 3D denso** e colore com a **combinação das cores dos voxels** atravessados. Usado para radar, **tomografia**, **ressonância** (exemplo do LAPIX: visualização volumétrica realista de estruturas anatômicas). |
| **Pixel Shader / Ray Shader** | Produz os **níveis de cor e iluminação de cada pixel** (ou efeitos de reflexo/transparência). **Tipicamente codificado para a GPU e executado nela.** |
| **Radiância / Radiosidade** | **Métodos de iluminação global** que modelam a **inter-reflexão difusa** entre os objetos (interações luminosas entre objetos). |
| **Modelo de Phong** | Modelo de **iluminação local** com 3 componentes aditivas, ver [[12 - Iluminação - Modelo de Phong e Shading]]. |

## Raytracing
- No mundo real a luz sai das fontes, reflete e refrata nos objetos e chega ao olho. Mas **a esmagadora maioria dos raios nunca chega ao observador**, então simular "para frente" é impraticável.
- Por isso o raytracing **opera de trás para frente**: começa na "**área de captura**" da câmera (o recorte do plano de projeção dado pela **Window**) e traça os raios **de volta para dentro da cena**.
- O usuário especifica o plano de projeção, as fontes de luz, os objetos e as **propriedades de superfície** (modelo de Phong), o interior (se transparente) e meios atmosféricos (névoa, turbidez, fogo).
- Para **cada pixel**, um ou mais **raios de visada** saem do observador e passam pela Window:
  - a **interseção** usa um algoritmo da família **zBuffering** (buffer de profundidade);
  - a **resolução da viewport** diz quantos pontos de incidência existem na window e parametriza a **conversão por varredura**.
- Quando um raio atinge um objeto:
  - disparam-se **raios umbrais** (*shadow rays*) até **cada fonte de luz**, para saber se o ponto está **na sombra**;
  - se a superfície for **refletiva, espelhada, transparente ou translúcida**, disparam-se **novos raios** (refletido/refratado), recursivamente.
- Componentes:
  - **Direta**: da fonte, ou via superfícies perfeitamente especulares. Fontes extensas usam amostragem de **Monte Carlo** para penumbra.
  - **Especular indireta**: luz de outras superfícies refletida de forma **direcional** (redireciona o raio).
  - **Difusa indireta**: luz refletida **sem direção preferencial**. Exige centenas de direções (Monte Carlo); como varia pouco ao longo da superfície, amostra-se esparsamente e interpola-se. **Essa é a premissa da radiosidade.**
- Efeitos extras (inter-reflexão difusa, atmosfera, luzes de área) exigem **muitos raios adicionais por pixel**.

### Raytracers
- Programas de simulação de iluminação que sintetizam imagens a partir de modelos 3D.
- Características: **estáticos** (lentos, mas qualidade altíssima: reflexões, sombras, perspectiva realistas) e **orientados a linguagem de descrição de cena** (o mundo é a entrada).
- Exemplos: **POV-Ray**, **Radiance**, Blender (Cycles), Mental Ray, V-Ray, YafRay, Indigo, Kerkythea, BRL-CAD, Sunflow, Bryce. Modelador para POV-Ray: **Moray**.

## Radiosidade
- Toda superfície recebe **luz direta** (da fonte, atenuada só pelo meio) + **luz refletida** por outras superfícies.
- Superfície **difusa** reflete igualmente em todas as direções, dependendo só do ângulo entre a normal e a luz incidente (**Lei de Lambert**).
- **Color bleeding** ("sangramento"): uma parede vermelha "despeja" vermelho na parede branca ao lado.
- Origem: **transferência de calor** (radiação térmica). Supõe superfícies **difusas** que emitem e refletem uniformemente, e um **equilíbrio** de energia.
- **Independente do ponto de vista**: a solução vale para qualquer câmera. (O raytracing **depende** do ponto de vista.)
- **Radiosidade de uma superfície** = taxa com que a energia **deixa** a superfície (energia/tempo/área): emitida + refletida.
- **Fator de forma** $F_{ij}$: fração da energia que sai de *j* e chega em *i*. É **puramente geométrico** (distância e orientação das normais), sem dimensão, independente do ponto de vista e dos atributos.
- **Analogia de Nusselt**: projeta a superfície num **hemisfério** unitário e depois na base. O fator de forma é a área projetada sobre a área da base.
- **Semicubo** (*hemicube*): meio cubo sobre o ponto, com faces divididas em células de fator de forma **pré-calculado**. Projeta as superfícies nele e soma as células cobertas.
- **Radiosidade progressiva**: em vez de resolver a "matriz total", **dispara** a energia da superfície mais brilhante a cada passo. A imagem melhora iterativamente.
- Comparação: ray tracing "típico" tem **reflexo espelhado** e **sombras de contorno duro**, sem luz ambiente real. Com iluminação global/radiosidade, as **sombras ficam suaves** e há luz ambiente verdadeira.
