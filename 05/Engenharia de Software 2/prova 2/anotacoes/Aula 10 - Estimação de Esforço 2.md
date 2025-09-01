## Estimação de Esforço II: COCOMO II (Slide 1)

Este slide apresenta o título da aula: "ESTIMAÇÃO DE ESFORÇO II", com foco em "COCOMO II". Indica o nome do professor, Raul Sidnei Wazlawick, e a instituição, UFSC-CTC-INE[cite: 905].

---

## Conteúdo da Aula (Slide 2)

Este slide delineia os tópicos a serem abordados na apresentação[cite: 906]:
* SLOC (Source Lines of Code) e KSLOC (Kilo Source Lines of Code) [cite: 906]
* COCOMO 81 [cite: 906]
* COCOMO II [cite: 906]

---

## SLOC e KSLOC: Estimativa (Slide 3)

Este slide introduz o tema SLOC e KSLOC com a pergunta: "Como se faz a estimação?"[cite: 907], sugerindo que os métodos de estimativa baseados em linhas de código serão discutidos.

---

## KSLOC Usado nas Estimativas (Slide 4)

Este slide apresenta uma abordagem para consolidar estimativas de KSLOC quando não há consenso na equipe[cite: 908]. A fórmula sugerida para calcular o KSLOC esperado é uma média ponderada:

$KSLOC = (4 \times KSLOC_{esperado} + KSLOC_{otimista} + KSLOC_{pessimista}) / 6$ [cite: 908]

O slide é ilustrado com uma imagem de uma equipe em reunião[cite: 908].

---

## Padrão para Contagem de SLOC em Java, C, C++ e C# (Slide 5)

Este slide exibe uma tabela que estabelece um padrão para a contagem de Linhas de Código Fonte (SLOC) em linguagens como Java, C, C++ e C#[cite: 909, 910]. A tabela é organizada por precedência e detalha, para cada estrutura da linguagem (comandos de seleção, iteração, desvio, expressões, delimitadores de bloco, diretivas de compilação e declaração de dados), a regra de contagem específica a ser aplicada[cite: 910]. Por exemplo, comandos de seleção como `if` e `switch` contam uma vez por ocorrência, enquanto para comandos de iteração como `for`, a inicialização, condição e incremento não são contabilizados separadamente[cite: 910].

---

## Como Contar SLOCs? Exemplo (Slide 6)

Este slide demonstra a aplicação das regras de contagem de SLOC apresentadas anteriormente através de um exemplo de código em Java[cite: 912, 913]. O código calcula termos da sequência de Fibonacci. Para cada linha ou bloco de código relevante, é indicada a contagem de SLOC e a regra de precedência aplicada (conforme a tabela do slide 5)[cite: 913]. No exemplo, o total de SLOC contabilizado para a classe Fibonacci é 8[cite: 913].

---

## Backfire Table (Slide 7)

Este slide apresenta uma "Backfire Table", que relaciona Pontos de Função (uma métrica de tamanho funcional) com Linhas de Código Fonte (SLOC) para diversas linguagens de programação[cite: 915, 916]. A tabela mostra, para linguagens como Assembly, C, C++, C#, Java, Perl, SQL e Visual Basic, os valores médios, medianos, de melhor caso e de pior caso de SLOC por Ponto de Função[cite: 916]. Por exemplo, para Java, a média é de 53 SLOC por Ponto de Função, com um melhor caso de 14 e um pior caso de 134[cite: 916].

---

## COCOMO (Slide 8)

Este slide introduz o COCOMO (Constructive Cost Model), especificamente a versão COCOMO 81, desenvolvida por Barry Boehm em 1981[cite: 918]. O slide também apresenta uma foto de Barry Boehm[cite: 918].

---

## Tipos de Projeto no COCOMO 81 (Slide 9)

Este slide lista os três modos ou tipos de projeto definidos no modelo COCOMO 81, que são utilizados para categorizar o software a ser desenvolvido e aplicar as fórmulas de estimativa correspondentes[cite: 919]:
* MODO ORGÂNICO [cite: 919]
* MODO SEMIDESTACADO [cite: 919]
* MODO EMBUTIDO [cite: 919]

Esses modos refletem diferentes níveis de complexidade, tamanho, rigidez de restrições e familiaridade da equipe com o projeto[cite: 549, 550, 551].

---

## Informações Básicas Estimadas pelo COCOMO (Slide 10)

Este slide destaca as três informações básicas de projeto que podem ser determinadas utilizando as implementações do modelo COCOMO[cite: 920]:
* **E – ESFORÇO TOTAL:** O trabalho total necessário, geralmente em pessoas-mês[cite: 920].
* **T - TEMPO LINEAR IDEAL:** A duração ótima para o desenvolvimento do projeto, em meses[cite: 920].
* **P - TAMANHO MÉDIO DA EQUIPE:** O número médio de pessoas necessárias para o projeto[cite: 920].

---

## Fórmulas de Esforço, Tempo Linear e Tamanho de Equipe no COCOMO 81 (Slide 11)

Este slide apresenta as equações fundamentais do COCOMO 81 para calcular o esforço, o tempo de desenvolvimento e o tamanho da equipe[cite: 921]:
* Esforço (E): $E = a_b \times KSLOC^{b_b}$ [cite: 921]
* Tempo Linear Ideal (T): $T = c_b \times E^{d_b}$ [cite: 921]
* Tamanho Médio da Equipe (P): $P = E/T$ [cite: 921]

As constantes $a_b, b_b, c_b, d_b$ variam conforme o tipo de projeto (orgânico, semidestacado ou embutido)[cite: 559, 560].

---

## COCOMO II - CII (Slide 12)

Este slide simplesmente introduz o COCOMO II, também referido como CII, indicando a transição para a versão mais recente do modelo de estimativa de custo construtivo[cite: 922].

---

## Equação Geral do Esforço no COCOMO II (Slide 13)

Este slide apresenta a equação geral para o cálculo do esforço (E) no modelo COCOMO II[cite: 923, 581]:

$E = A \times KSLOC^S \times \prod M_i$ [cite: 923, 581]

Onde:
* `A` é uma constante de calibração (valor base ~2.94)[cite: 573, 574].
* `KSLOC` representa o tamanho do software em milhares de linhas de código[cite: 574]. (O texto cap7.pdf [cite: 572] menciona que "Tamanho" pode ser KSLOC ou Pontos de Função).
* `S` é o coeficiente de escala, que leva em consideração fatores de economia ou deseconomia de escala[cite: 572, 575].
* $\prod M_i$ é o produto dos multiplicadores de esforço (Cost Drivers), que ajustam a estimativa com base em diversos atributos do projeto, produto, plataforma e pessoal[cite: 572, 576].

---

## Coeficiente de Escala (S) no COCOMO II (Slide 14)

Este slide exibe a fórmula para calcular o Coeficiente de Escala (S) no COCOMO II[cite: 924]:

$S = B + 0,001 \times \sum F_j$ [cite: 924]

Onde:
* `B` é uma constante de calibração (valor base no COCOMO II é 0,91 [cite: 601, 602]).
* $\sum F_j$ é o somatório dos valores numéricos de cinco Fatores de Escala (SFj)[cite: 602].
*(Nota: O `cap7.pdf` [cite: 600] apresenta esta fórmula como $S = B + 0,01 \times \sum F_j$. Este resumo reporta o que está no slide.)*

---

## Fatores de Escala (SFj) e Aplicação do CII (Slide 15)

Este slide ilustra os cinco Fatores de Escala (SFj) que compõem o Coeficiente de Escala S no COCOMO II: PREC (Precedentes), FLEX (Flexibilidade), RESL (Resolução de Riscos e Arquitetura), TEAM (Coesão da Equipe) e PMAT (Maturidade do Processo)[cite: 925, 609]. A imagem também mostra que o COCOMO II é aplicado para estimar o esforço nas fases de Elaboração e Construção do Processo Unificado[cite: 925, 569].

---

## Relação entre Tamanho de Equipe, Esforço e Tempo Linear (Slide 16)

Este slide apresenta um gráfico que ilustra as interdependências entre o tamanho da equipe, o esforço total do projeto e o tempo linear de desenvolvimento[cite: 926, 583]. O gráfico superior mostra que, até um certo limite, aumentar a equipe pode reduzir o tempo linear, mas com um aumento no esforço total; após esse limite, aumentar a equipe pode até aumentar o tempo linear[cite: 580, 583]. O gráfico inferior mostra que existe um tamanho ideal de equipe para um tempo linear ótimo, e que reduzir o tempo abaixo do ideal implica um aumento não linear no esforço[cite: 583, 589].

---

## Cálculo do Tempo Linear Ideal (T) no COCOMO II (Slide 17)

Este slide apresenta a fórmula para calcular o Tempo Linear Ideal de Desenvolvimento (T) em meses no modelo COCOMO II, uma vez que o esforço (E) já foi estimado[cite: 927, 584]:

$T = C \times E^{D+0,2 \times (S-B)}$ [cite: 927]

Onde:
* `C` é uma constante de calibração (valor base ~3.67)[cite: 585, 597].
* `E` é o esforço total estimado em pessoas-mês[cite: 586].
* `D` é uma constante de calibração (valor base ~0.28)[cite: 585, 597].
* `S` é o Coeficiente de Escala[cite: 587].
* `B` é uma constante de calibração do expoente de escala (valor base ~0.91)[cite: 585, 597].

---

## Características dos Fatores de Escala (Slide 18)

Este slide descreve as características gerais dos Fatores de Escala no COCOMO II[cite: 928, 929]:
* A avaliação de cada fator varia de "muito baixo" a "extremamente alto"[cite: 928, 603].
* Esses fatores têm um impacto exponencial no cálculo do esforço de desenvolvimento[cite: 929, 604].

---

## Lista dos Fatores de Escala (Slide 19)

Este slide reitera os cinco Fatores de Escala utilizados no cálculo do Coeficiente de Escala S no COCOMO II[cite: 930, 609]:
* **PRECEDENTES (PREC):** Similaridade do produto com projetos desenvolvidos anteriormente[cite: 930, 609].
* **FLEXIBILIDADE NO DESENVOLVIMENTO (FLEX):** Grau de aderência estrita aos requisitos e interfaces predefinidas[cite: 930, 610].
* **ARQUITETURA/RESOLUÇÃO DE RISCOS (RESL):** Qualidade do suporte para resolução de riscos e definição da arquitetura[cite: 930, 611].
* **COESÃO DA EQUIPE (TEAM):** Nível de formação e coesão da equipe de desenvolvimento[cite: 930, 612].
* **MATURIDADE DE PROCESSO (PMAT):** Nível de maturidade dos processos de software da organização (e.g., CMMI)[cite: 930, 613].

---

## Fator de Escala: Precedentes (PREC) (Slide 20)

Este slide apresenta a tabela de avaliação para o Fator de Escala "Precedentes (PREC)"[cite: 931, 623]. A tabela guia a atribuição de um valor numérico (de 0,00 para "Totalmente familiar" a 6,20 para "Totalmente sem precedentes") com base em características como[cite: 623]:
* Compreensão organizacional dos objetivos do produto.
* Experiência em sistemas relacionados.
* Desenvolvimento concorrente de novo hardware/procedimentos.
* Necessidade de arquiteturas/algoritmos inovadores.

A nota média dessas características leva a uma interpretação e ao fator numérico correspondente[cite: 618, 623].

---

## Fator de Escala: Flexibilidade no Desenvolvimento (FLEX) (Slide 21)

Este slide detalha a tabela de avaliação para o Fator de Escala "Flexibilidade no Desenvolvimento (FLEX)"[cite: 932, 634]. O valor numérico (de 0,00 para "Metas gerais" a 5,07 para "Rigoroso") é determinado com base em[cite: 634]:
* Necessidade de conformação a requisitos preestabelecidos.
* Necessidade de conformação a especificações de interfaces externas.
* Combinação de inflexibilidades com prêmio por término antecipado.

Uma maior rigidez (menor flexibilidade) resulta em um fator numérico maior, indicando mais esforço[cite: 633, 635].

---

## Fator de Escala: Arquitetura/Resolução de Riscos (RESL) - Parte 1 (Slide 22)

Este slide inicia a apresentação da tabela de avaliação para o Fator de Escala "Arquitetura/Resolução de Riscos (RESL)"[cite: 933, 637]. São listadas as primeiras características para determinar o fator numérico, que varia de 0,00 (Totalmente - 100% de resolução) a 7,07 (Pouco - 20% de resolução)[cite: 637]. As características incluem[cite: 637]:
* Existência de plano de gerenciamento de risco e marcos para resolução.
* Compatibilidade de cronograma, orçamento e marcos internos com o plano de risco.
* Percentual do cronograma dedicado a estabelecer a arquitetura.
* Percentual de arquitetos experientes disponíveis.
* Suporte de ferramentas para resolver riscos e verificar a arquitetura.

---

## Fator de Escala: Arquitetura/Resolução de Riscos (RESL) - Parte 2 (Slide 23)

Este slide continua a tabela de avaliação para o Fator de Escala "Arquitetura/Resolução de Riscos (RESL)", apresentando as características finais[cite: 934, 639]:
* Nível de incerteza nos determinantes-chave da arquitetura (missão, interface, COTS, hardware, tecnologia, desempenho)[cite: 639].
* Número de itens de risco e sua importância (críticos ou não críticos)[cite: 639, 640].

A combinação da avaliação dessas características (incluindo as do slide anterior) leva à interpretação (e.g., "Pouco", "Algum", "Totalmente") e ao fator numérico correspondente[cite: 637].

---

## Fator de Escala: Coesão da Equipe de Desenvolvimento (TEAM) (Slide 24)

Este slide apresenta a tabela para avaliar o Fator de Escala "Coesão da Equipe de Desenvolvimento (TEAM)"[cite: 935, 646]. O fator numérico (de 0,00 para "Interações perfeitas" a 5,48 para "Interações muito difíceis") é baseado em[cite: 646]:
* Consistência dos objetivos e cultura dos interessados.
* Habilidade e vontade dos interessados em acomodar objetivos de outros.
* Experiência dos interessados em trabalhar como uma equipe.
* Construção de equipes para obter visão compartilhada e compromissos.

---

## Fator de Escala: Maturidade do Processo (PMAT) (Slide 25)

Este slide detalha a avaliação do Fator de Escala "Maturidade do Processo (PMAT)"[cite: 936, 651]. O fator numérico varia de 0,00 (Processo em otimização constante - Nível CMMI 5) a 7,80 (Sem processo definido - Nível CMMI 0)[cite: 651, 653]. A avaliação é baseada principalmente no nível CMMI, SPICE ou EPML (Estimated Process Maturity Level) da organização[cite: 615, 653].

---

## Multiplicadores de Esforço no COCOMO II (Slide 26)

Este slide ilustra quando os diferentes conjuntos de Multiplicadores de Esforço do COCOMO II são aplicados em relação às fases do Processo Unificado[cite: 937, 656]:
* **Early Design Model:** Usado durante a fase de Concepção e início da Elaboração, quando há menos informações detalhadas sobre o projeto[cite: 656].
* **Post-Architecture Model:** Usado a partir de um ponto mais avançado da fase de Elaboração (quando a arquitetura está mais estável) e durante a Construção[cite: 656].

O modelo aplicado estima o esforço total para as fases de Elaboração e Construção combinadas[cite: 657].

---

## Grupos de Multiplicadores de Esforço do Post-Architecture Model (Slide 27)

Este slide lista os quatro grupos nos quais os 17 Multiplicadores de Esforço (Cost Drivers) do Post-Architecture Model do COCOMO II são categorizados[cite: 938, 939]:
* Fatores do Produto [cite: 938, 659]
* Fatores da Plataforma [cite: 939]
* Fatores Humanos [cite: 939, 659]
* Fatores de Projeto [cite: 939, 659]

---

## Multiplicadores de Esforço: Fatores do Produto (Slide 28)

Este slide detalha os cinco Multiplicadores de Esforço que pertencem ao grupo "Fatores do Produto" no Post-Architecture Model do COCOMO II[cite: 940, 941, 660, 661]:
* **RELY (Software com Confiabilidade Requerida):** Avalia as consequências de falhas no software[cite: 940, 660].
* **DATA (Tamanho da Base de Dados):** Considera o tamanho relativo da base de dados de teste[cite: 940, 660].
* **CPLX (Complexidade do Produto):** Avalia a complexidade em áreas como operações de controle, computacionais, dependentes de dispositivos, gerenciamento de dados e interface[cite: 940, 661].
* **RUSE (Desenvolvimento Visando Reusabilidade):** Mede o esforço adicional para desenvolver componentes reusáveis[cite: 941, 661].
* **DOCU (Documentação Necessária para o Ciclo de Desenvolvimento):** Avalia a adequação da documentação produzida às necessidades do ciclo de vida[cite: 941, 661].

---

## Multiplicador de Esforço: Confiabilidade Requerida (RELY) (Slide 29)

Este slide apresenta a tabela de avaliação para o Multiplicador de Esforço "Software com Confiabilidade Requerida (RELY)"[cite: 942, 666]. O valor numérico é atribuído com base no impacto de uma falha do software, variando de 0,82 (Pequena inconveniência) a 1,26 (Risco à vida humana)[cite: 665, 666]. A avaliação "Extra alto" não é aplicável para RELY[cite: 666, 667].

---

## Multiplicador de Esforço: Tamanho da Base de Dados (DATA) (Slide 30)

Este slide exibe a tabela de avaliação para o Multiplicador de Esforço "Tamanho da Base de Dados (DATA)"[cite: 943, 671]. A avaliação e o valor numérico correspondente (de 0,90 a 1,28) são determinados pela razão D/P, onde D é o tamanho da base de dados de teste em Kbytes e P é o tamanho estimado do programa em KSLOC[cite: 669, 671]. Por exemplo, se D/P estiver entre 10 e 100, a avaliação é "Baixo" e o fator é 0,90[cite: 671]. As avaliações "Muito baixo" e "Extra alto" não são aplicáveis[cite: 671].

---

## Multiplicador de Esforço: Complexidade do Produto (CPLX) - Parte 1 (Slide 31)

Este slide inicia a apresentação da extensa tabela de avaliação para o Multiplicador de Esforço "Complexidade do Produto (CPLX)"[cite: 944, 679]. Este fator é avaliado em cinco áreas distintas. O slide foca nas primeiras áreas[cite: 679]:
* **Operações de controle:** Avalia estruturas de controle, aninhamento, predicados, controle intermódulos, processamento distribuído, tempo real, reentrância, sincronização, etc.[cite: 680, 681, 682, 683, 684, 685].
* **Operações computacionais:** Considera a complexidade de expressões matemáticas, uso de rotinas padrão, análise numérica (interpolação, equações diferenciais), paralelização, etc.[cite: 686, 687, 688, 689, 690].
* **Operações dependentes de dispositivo:** Avalia a complexidade da entrada/saída, formatação, conhecimento de características de hardware, processamento de E/S em nível físico, gerenciamento de comunicação, sistemas embarcados, etc.[cite: 691, 692, 693, 694, 695, 696].

A complexidade geral do produto é uma média ponderada subjetiva dessas áreas, resultando em um valor numérico de 0,73 (Muito baixo) a 1,74 (Extra alto)[cite: 678, 679].

---

## Multiplicador de Esforço: Complexidade do Produto (CPLX) - Parte 2 (Slide 32)

Este slide continua e conclui a tabela de avaliação para o Multiplicador de Esforço "Complexidade do Produto (CPLX)", detalhando as últimas áreas e as avaliações finais[cite: 945, 698]:
* **Operações de gerenciamento de dados:** Avalia a complexidade de manipulação de dados, desde arrays simples em memória, consultas e atualizações em bancos de dados (COTS), até estruturas relacionais e de objetos dinâmicas e gerenciamento de dados em linguagem natural[cite: 697, 699, 700, 701, 702, 703].
* **Operações de gerenciamento de interface com usuário:** Considera desde formulários simples e geradores de relatórios, uso de construtores de GUI, widgets, até multimídia complexa, realidade virtual e interface em linguagem natural[cite: 704, 705, 706, 707].

A avaliação final (Muito baixo, Baixo, Nominal, Alto, Muito alto, Extra alto) e o respectivo equivalente numérico (0,73 a 1,74) são obtidos pela média subjetivamente ponderada das cinco áreas de complexidade[cite: 678, 679].

---

## Multiplicador de Esforço: Desenvolvimento Visando Reusabilidade (RUSE) (Slide 33)

Este slide apresenta a tabela de avaliação para o Multiplicador de Esforço "Desenvolvimento Visando Reusabilidade (RUSE)"[cite: 946, 710]. O fator numérico, que varia de 0,95 (Reuso dentro do projeto) a 1,24 (Reuso entre múltiplas Linhas de Produto de Software - SPLs), reflete o esforço adicional investido para tornar os componentes de software reusáveis em diferentes contextos[cite: 708, 710]. "Nenhum reuso" não possui um valor numérico direto na tabela, mas o esforço aumenta conforme o escopo da reusabilidade planejada se expande[cite: 710].

---

## Multiplicador de Esforço: Documentação Necessária para o Ciclo de Desenvolvimento (DOCU) (Slide 34)

Este slide detalha a avaliação do Multiplicador de Esforço "Documentação Necessária para o Ciclo de Desenvolvimento (DOCU)"[cite: 947, 717]. O valor numérico é atribuído com base na adequação da documentação às necessidades do ciclo de vida do projeto, variando de 0,81 (Muitas necessidades não cobertas) a 1,23 (Muito excessiva para as necessidades)[cite: 712, 717]. O valor nominal (1,00) corresponde a uma documentação exatamente dimensionada[cite: 717]. A avaliação "Extra alto" não é aplicável[cite: 717].

---

## Multiplicadores de Esforço: Fatores da Plataforma (Slide 35)

Este slide lista os três Multiplicadores de Esforço que compõem o grupo "Fatores da Plataforma" no Post-Architecture Model do COCOMO II[cite: 948, 949, 721, 722]:
* **TIME (Restrição de Tempo de Execução):** Avalia a porcentagem de uso dos processadores disponíveis pela aplicação[cite: 948, 722].
* **STOR (Restrição de Memória Principal):** Considera a porcentagem de uso da memória principal pela aplicação[cite: 949, 722].
* **PVOL (Volatilidade da Plataforma):** Mede a frequência de mudanças no hardware e software básicos da plataforma de desenvolvimento[cite: 949, 722].

---

## Multiplicador de Esforço: Restrição de Tempo de Execução (TIME) (Slide 36)

Este slide apresenta a tabela de avaliação para o Multiplicador de Esforço "Restrição de Tempo de Execução (TIME)"[cite: 950, 723]. O fator numérico é determinado pela porcentagem esperada de utilização do tempo de execução disponível pelos processadores, variando de 1,00 (até 85% de uso - Nominal) a 1,63 (95% de uso - Extra alto)[cite: 722, 723]. Avaliações para menos de 50% e 70% de uso não possuem valores numéricos diretos ("n/a") nesta tabela, indicando que abaixo de um certo limiar, o impacto pode ser considerado nominal ou não significativo para aumentar o esforço[cite: 723].

---

## Multiplicador de Esforço: Restrição de Memória Principal (STOR) (Slide 37)

Este slide detalha a avaliação do Multiplicador de Esforço "Restrição de Memória Principal (STOR)"[cite: 951, 726]. Similar ao TIME, o valor numérico é baseado na porcentagem esperada de uso da memória principal pela aplicação, indo de 1,00 (até 85% de uso - Nominal) a 1,46 (95% de uso - Extra alto)[cite: 724, 726]. Avaliações para menos de 50% e 70% de uso da memória também são indicadas como "n/a"[cite: 726].

---

## Multiplicador de Esforço: Volatilidade da Plataforma (PVOL) (Slide 38)

Este slide apresenta a tabela para o Multiplicador de Esforço "Volatilidade da Plataforma (PVOL)"[cite: 952, 731]. Este fator avalia a estabilidade da plataforma de desenvolvimento (hardware e software básico)[cite: 728]. O valor numérico varia de 0,87 (Mudanças grandes a cada 12 meses, pequenas a cada mês - Baixo) a 1,30 (Mudanças grandes a cada 2 semanas, pequenas a cada 2 dias - Muito alto)[cite: 729, 731]. O valor nominal (1,00) corresponde a mudanças grandes a cada 6 meses e pequenas a cada 2 semanas[cite: 731]. As avaliações "Muito baixo" e "Extra alto" são "n/a"[cite: 731].

---

## Multiplicadores de Esforço: Fatores Humanos (Slide 39)

Este slide lista os seis Multiplicadores de Esforço que compõem o grupo "Fatores Humanos" no Post-Architecture Model do COCOMO II[cite: 953, 954, 955, 732, 733]:
* **ACAP (Capacidade dos Analistas)** [cite: 953, 732]
* **PCAP (Capacidade dos Programadores)** [cite: 954, 732]
* **PCON (Continuidade de Pessoal)** [cite: 954, 732]
* **APEX (Experiência em Aplicações Semelhantes)** [cite: 954, 732]
* **PLEX (Experiência na Plataforma)** [cite: 954, 733]
* **LTEX (Experiência na Linguagem e Ferramentas)** [cite: 955, 733]

---

## Multiplicador de Esforço: Capacidade dos Analistas (ACAP) (Slide 40)

Este slide apresenta a tabela de avaliação para o Multiplicador de Esforço "Capacidade dos Analistas (ACAP)"[cite: 956, 737]. O fator numérico é determinado pelo percentil em que os analistas do projeto se encontram em termos de capacidade (análise, modelagem, eficiência, cooperação, comunicação)[cite: 734, 735]. Os valores variam de 0,71 (percentil 90 - Muito alto) a 1,42 (percentil 15 - Muito baixo)[cite: 736, 737]. A avaliação "Extra alto" não é aplicável[cite: 737].

---

## Multiplicador de Esforço: Capacidade dos Programadores (PCAP) (Slide 41)

Este slide detalha a avaliação do Multiplicador de Esforço "Capacidade dos Programadores (PCAP)"[cite: 957, 740]. Similarmente ao ACAP, este fator é baseado no percentil da capacidade dos programadores[cite: 739]. Os valores numéricos variam de 0,76 (percentil 90 - Muito alto) a 1,34 (percentil 15 - Muito baixo)[cite: 740]. A avaliação "Extra alto" não é aplicável[cite: 740].

---

## Multiplicador de Esforço: Continuidade de Pessoal (PCON) (Slide 42)

Este slide apresenta a tabela para o Multiplicador de Esforço "Continuidade de Pessoal (PCON)"[cite: 958, 742]. Este fator avalia o impacto da rotatividade de pessoal no projeto, medido pela porcentagem de trocas de desenvolvedores ao ano[cite: 741]. Os valores numéricos vão de 0,81 (3% de troca/ano - Muito alto) a 1,29 (48% de troca/ano - Muito baixo)[cite: 741, 742]. Uma menor rotatividade resulta em um menor fator de multiplicação do esforço[cite: 741]. A avaliação "Extra alto" não é aplicável[cite: 742].

---

## Multiplicador de Esforço: Experiência em Aplicações Semelhantes (APEX) (Slide 43)

Este slide exibe a tabela de avaliação para o Multiplicador de Esforço "Experiência em Aplicações Semelhantes (APEX)"[cite: 959, 744]. O fator é determinado pelo tempo médio de experiência da equipe em projetos com características similares ao que está sendo desenvolvido[cite: 743]. Os valores numéricos variam de 0,81 (6 anos de experiência - Muito alto) a 1,22 (Menos de 2 meses de experiência - Muito baixo)[cite: 743, 744]. A avaliação "Extra alto" não é aplicável[cite: 744].

---

## Multiplicador de Esforço: Experiência na Plataforma (PLEX) (Slide 44)

Este slide detalha a avaliação do Multiplicador de Esforço "Experiência na Plataforma (PLEX)"[cite: 960, 746]. Este fator considera a experiência da equipe com a plataforma de desenvolvimento (hardware, SO, bibliotecas, banco de dados, middleware)[cite: 745]. Os valores numéricos vão de 0,85 (6 anos de experiência - Muito alto) a 1,19 (Menos de 2 meses de experiência - Muito baixo)[cite: 746]. A avaliação "Extra alto" não é aplicável[cite: 746].

---

## Multiplicador de Esforço: Experiência na Linguagem e Ferramentas (LTEX) (Slide 45)

Este slide apresenta a tabela para o Multiplicador de Esforço "Experiência na Linguagem e Ferramentas (LTEX)"[cite: 961, 749]. Avalia-se o tempo médio de experiência da equipe com as linguagens de programação e ferramentas CASE utilizadas no projeto[cite: 748]. Os valores numéricos variam de 0,84 (6 anos de experiência - Muito alto) a 1,20 (Menos de 2 meses de experiência - Muito baixo)[cite: 749]. A avaliação "Extra alto" não é aplicável[cite: 749].

---

## Multiplicadores de Esforço: Fatores de Projeto (Slide 46)

Este slide lista os três Multiplicadores de Esforço que pertencem ao grupo "Fatores de Projeto" no Post-Architecture Model do COCOMO II[cite: 962, 963, 750, 751]:
* **TOOL (Uso de Ferramentas de Software):** Avalia a qualidade e integração do suporte computacional ao ambiente de desenvolvimento[cite: 962, 750].
* **SITE (Equipe de Desenvolvimento Distribuída):** Considera o impacto da distribuição geográfica e organizacional da equipe[cite: 963, 750].
* **SCED (Cronograma de Desenvolvimento Requerido):** Reflete a aceleração ou relaxamento do cronograma em relação ao tempo nominal ideal[cite: 963, 751].

---

## Multiplicador de Esforço: Uso de Ferramentas de Software (TOOL) (Slide 47)

Este slide apresenta a tabela de avaliação para o Multiplicador de Esforço "Uso de Ferramentas de Software (TOOL)"[cite: 964, 754]. O fator numérico é determinado pela sofisticação e integração das ferramentas de desenvolvimento utilizadas, variando de 0,78 (Ferramentas de ciclo de vida fortes, maduras e bem integradas com processos, métodos e reuso - Muito alto) a 1,17 (Editar, codificar, debugar - Muito baixo)[cite: 752, 753, 754, 755, 756]. A avaliação "Extra alto" não é aplicável[cite: 757].

---

## Multiplicador de Esforço: Equipe de Desenvolvimento Distribuída (SITE) (Slide 48)

Este slide detalha a avaliação do Multiplicador de Esforço "Equipe de Desenvolvimento Distribuída (SITE)"[cite: 965, 764]. Este fator é único por considerar dois descritores para determinar a avaliação: co-locação da equipe (desde internacional até totalmente co-locada) e o nível de comunicação (desde alguns telefones até multimídia interativa)[cite: 761, 762, 764]. A nota final é uma média subjetiva desses dois descritores[cite: 762]. Os valores numéricos variam de 0,80 (Totalmente co-locada com multimídia interativa - Extra alto) a 1,22 (Internacional com comunicação limitada - Muito baixo)[cite: 764].

---

## Multiplicador de Esforço: Cronograma de Desenvolvimento Requerido (SCED) (Slide 49)

Este slide apresenta a tabela para o Multiplicador de Esforço "Cronograma de Desenvolvimento Requerido (SCED)"[cite: 966, 767]. Este fator reflete o impacto de acelerar ou relaxar o cronograma do projeto em relação ao tempo nominal ideal[cite: 765]. Se o cronograma é comprimido para 75% do nominal, o fator é 1,43 (Muito baixo, indicando maior esforço); se for 100% do nominal, o fator é 1,00 (Nominal)[cite: 766, 767]. Cronogramas estendidos (130% ou 160% do nominal) também resultam em um fator de 1,00 (Alto e Muito alto, respectivamente), sugerindo que não há redução de esforço por estender o prazo além do ideal nestes níveis[cite: 767]. A avaliação "Extra alto" não é aplicável[cite: 767].

---

## Multiplicadores de Esforço do Early Design Model (Slide 50)

Este slide lista os sete Multiplicadores de Esforço utilizados no Early Design Model do COCOMO II, que é aplicado nas fases iniciais do projeto quando as informações ainda são menos detalhadas[cite: 967, 968, 969, 768, 771]. Estes fatores são geralmente combinações ou simplificações dos fatores do Post-Architecture Model[cite: 768, 770]. Os fatores são[cite: 968, 969, 771]:
* PERS (Capacidade de Pessoal) [cite: 967, 771]
* RCPX (Confiabilidade e Complexidade do Produto) [cite: 968, 772]
* RUSE (Desenvolvimento para Reuso) [cite: 968, 772] (Este é o mesmo do Post-Architecture Model [cite: 785])
* PDIF (Dificuldade com a Plataforma) [cite: 968, 773]
* PREX (Experiência do Pessoal) [cite: 968, 774]
* FCIL (Instalações) [cite: 968, 774]
* SCED (Cronograma de Desenvolvimento Requerido) [cite: 969, 774] (Este é o mesmo do Post-Architecture Model [cite: 795])

---

## Distribuição de Esforço e Tempo por Fase do Processo Unificado (RUP) (Slide 51)

Este slide apresenta uma tabela que mostra a distribuição nominal e os intervalos de variação do esforço (E) e do tempo linear (T) pelas quatro fases do Processo Unificado (RUP), conforme estimado pelo COCOMO II[cite: 970, 800].
* **Concepção:** Nominalmente 6% do Esforço Total (E_RUP) e 12,5% do Tempo Total (T_RUP)[cite: 799, 800].
* **Elaboração:** Nominalmente 24% de E_RUP e 37,5% de T_RUP[cite: 799, 800]. (O esforço E calculado pelo CII principal cobre Elaboração e Construção [cite: 796, 797]).
* **Construção:** Nominalmente 76% de E_RUP e 62,5% de T_RUP[cite: 799, 802].
* **Transição:** Nominalmente 12% de E_RUP e 12,5% de T_RUP[cite: 799, 802].
Os totais nominais somam 118% do esforço (E) e 125% do tempo (T) originalmente calculados para as fases de elaboração e construção, devido à adição das fases de concepção e transição[cite: 798, 802].

---

## Exemplo de Distribuição de Esforço e Tempo por Fase (Slide 52)

Este slide fornece um exemplo prático da aplicação da distribuição de esforço e tempo pelas fases do RUP, utilizando um projeto hipotético com Esforço (E, para Elaboração + Construção) = 56 pessoas-mês e Tempo (T, para Elaboração + Construção) = 11,5 meses[cite: 971, 804].
A tabela mostra os valores nominais e os intervalos para cada fase[cite: 804]:
* **Concepção:** Esforço 3,4 (intervalo 1,12-8,4); Tempo 1,4 (intervalo 0,23-3,45)[cite: 804].
* **Elaboração:** Esforço 13,4 (intervalo 11,2-15,68); Tempo 4,3 (intervalo 3,795-4,83)[cite: 804].
* **Construção:** Esforço 42,6 (intervalo 40,32-44,8); Tempo 7,2 (intervalo 6,67-7,705)[cite: 804].
* **Transição:** Esforço 6,7 (intervalo 0,0-11,2); Tempo 1,4 (intervalo 0,0-2,3)[cite: 804].
Os totais para as quatro fases são 66,1 pessoas-mês de esforço e 14,3 meses de tempo[cite: 804].

---

## Distribuição de Esforço por Disciplina do RUP em Cada Fase (Slide 53)

Este slide apresenta uma tabela que resume a distribuição percentual do esforço relativo às disciplinas do Processo Unificado (RUP) dentro de cada uma das quatro fases (Concepção, Elaboração, Construção, Transição)[cite: 972, 814]. As disciplinas listadas são: Gerenciamento, Ambiente/Configuração, Requisitos, Design, Implementação, Avaliação/Teste e Implantação[cite: 816]. Por exemplo, na fase de Concepção, a disciplina de Requisitos consome nominalmente 38% do esforço da fase, enquanto na Construção, a Implementação consome 34%[cite: 816]. Cada coluna de fase soma 100% do esforço daquela fase específica[cite: 816].

---

## Calibragem do Modelo COCOMO II (Slide 54)

Este slide enfatiza a importância da calibragem do modelo COCOMO II para obter estimativas mais precisas[cite: 973]. O texto sugere que as constantes do modelo, que foram definidas a partir de um conjunto de projetos-base, devem ser ajustadas para os parâmetros específicos da organização que está utilizando a técnica[cite: 817]. Essa calibragem pode ser necessária ao longo do tempo devido a mudanças na empresa[cite: 818].

---

## Exemplo de Calibragem da Constante A (Slide 55)

Este slide ilustra o processo de calibragem da constante `A` da equação geral de esforço do COCOMO II, utilizando dados históricos de pelo menos cinco projetos[cite: 974, 820, 821]. É apresentada uma tabela adaptada de Boehm (2000) com dados de oito projetos[cite: 820, 821]. Para cada projeto, são listados o esforço real e o valor da estimativa não ajustada ($KSLOC^S \times \prod M_i$)[cite: 821, 824]. Calcula-se o logaritmo natural (ln) desses valores e a diferença entre eles[cite: 825, 826]. A média (X) dessas diferenças é então utilizada para calcular a nova constante A como $A = e^X$[cite: 827, 828]. No exemplo, o valor calibrado de A foi 2,62, diferindo do valor padrão de 2,94[cite: 821, 829].