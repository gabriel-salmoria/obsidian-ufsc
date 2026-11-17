---
tags: [cg, modulo-3]
---
# 13 · Modelos Hierárquicos e Animação

[[Computação Gráfica|↑ Índice]] · anterior: [[12 - Iluminação - Modelo de Phong e Shading]] · próximo: [[14 - Percepção de Cor]]
Livro: [[Angel & Shreiner - Cap. 8 - Modelos Hierárquicos (trechos).pdf]]
Páginas do professor: [Modelos Hierárquicos em CG](http://www.inf.ufsc.br/~awangenh/grafica/modelosHierarquicos/index.html) · [Movimentação de humanos e animais](http://www.inf.ufsc.br/~awangenh/grafica/modelosHierarquicos/caminhar/index.html) · [Material adicional](https://www.inf.ufsc.br/~awangenh/grafica/apostilas/modelos-hierarquicos/)

> [!info] Este é o tópico da aula de 17/11, a mais recente antes da prova. Ainda não tem videoaula interativa nem questão no quiz de treino. Vale saber os conceitos abaixo.

## Símbolos e instâncias (Angel 8.1)
- **Símbolo**: um objeto modelado uma vez, no **seu próprio sistema de coordenadas** (ex.: cilindro unitário).
- **Instância**: o símbolo colocado na cena com uma **transformação de instância** $M = T\cdot R\cdot S$ (escala, orienta e posiciona). Com vetor-linha: $S\cdot R\cdot T$.
- Uma tabela de instâncias (símbolo + transformação) é "plana": **não guarda relações** entre as partes.

## Modelos hierárquicos (8.2–8.4)
- Partes de um objeto **dependem** umas das outras: mover o braço move o antebraço e a mão. A estrutura é uma **árvore** (ou **DAG**, quando partes iguais são compartilhadas, ex. as 4 rodas de um carro).
- Cada **nó** guarda: a geometria da parte, a **transformação relativa ao pai** e ponteiros para os filhos.
- A transformação de uma parte no mundo é o **produto das transformações de todos os ancestrais** até ela.
- **Braço robótico** (base → braço inferior → braço superior):
  - base gira θ em torno de y: $R_y(\theta)$
  - braço inferior: $R_y(\theta)\,T(0,h_1,0)\,R_z(\phi)$
  - braço superior: $R_y(\theta)\,T(0,h_1,0)\,R_z(\phi)\,T(0,h_2,0)\,R_z(\psi)$
  - Cada rotação é **relativa à junta**: girar a base leva tudo junto.
- **Percurso da árvore** (pré-ordem/DFS) com **pilha de matrizes**: **push** antes de descer para um filho e **pop** ao voltar, para que os irmãos (ex.: a outra perna) partam da mesma matriz do pai. Em OpenGL clássico: `glPushMatrix`/`glPopMatrix`.
- Representação comum: **filho-esquerdo, irmão-direito** (*left-child right-sibling*).

## Animação (8.6)
- Animar = mudar os **parâmetros das juntas** (ângulos) ao longo do tempo. A hierarquia propaga o movimento.
- **Cinemática direta** (*forward kinematics*): dados os ângulos das juntas, onde fica o efetuador (mão, pé).
- **Cinemática inversa**: dada a posição desejada do efetuador, quais ângulos usar. É mais difícil, pode ter várias ou nenhuma solução.
- **Key-frames + interpolação** dos parâmetros. **Motion capture** (MoCap, aula prática no TECMÍDIA) captura o movimento real para aplicar no esqueleto.
- **Rigging** (Blender/Unity): criar o **esqueleto** (ossos = hierarquia) e associá-lo à malha (*skinning*).

## Simulando a locomoção (página do professor, base do trabalho 4)
Temas do trabalho com modelo hierárquico:
- **sem deslocamento**: braço mecânico pegando objetos numa esteira;
- **bípede**: humanoide/robô que anda e gesticula;
- **quadrúpede I**: réptil (lagarto);
- **quadrúpede II**: mamífero (cachorro, cavalo): caminhada simétrica, corrida simétrica e **assimétrica** (galope);
- **hexápode**: inseto de 6 patas (bicho-pau, barata).

Usa resultados de **biomecânica/cinesiologia** e robótica bioinspirada. Cada perna é uma cadeia hierárquica, e a **sequência de passadas** (ordem em que as patas se movem) define o tipo de marcha.

## Grafos de cena (8.8–8.9)
- Generalizam a árvore: nós de **geometria**, **transformação**, **material/luz**, **câmera**, **grupo**.
- Exemplos: **Open Scene Graph**, os sistemas internos das **game engines** (Unity, Unreal). "Suporte a grafos de cena" é uma das características de game engine no [[Banco de Questões#6. APIs, engines e ferramentas|quiz]].
