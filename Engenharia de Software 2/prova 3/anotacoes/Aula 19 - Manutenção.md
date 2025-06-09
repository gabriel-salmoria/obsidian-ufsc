## Slide 1: Manutenção de Software

Este slide introduz o tema da aula: Manutenção de Software. A manutenção de software é o processo de adaptação, otimização e correção de defeitos em um software já desenvolvido para preservar sua qualidade ao longo do tempo. Sem a manutenção, o valor percebido do software e, consequentemente, sua qualidade, se deterioram.

---

## Slide 2: Manutenção X Evolução de Software

Este slide aborda a distinção entre manutenção e evolução de software. Modernamente, o termo "manutenção de software" tem sido substituído ou usado em conjunto com "evolução de software". "Evolução" é considerado um termo mais adequado, pois as atividades de modificação do software não visam apenas mantê-lo como está, mas sim adaptá-lo a novos requisitos e corrigir defeitos. A evolução pode ser vista como uma sequência de manutenções ao longo do tempo, onde a manutenção representa as tarefas individuais de modificação.

---

## Slide 3: Leis de Lehman

Este slide introduz as Leis de Lehman, que explicam a necessidade e a inevitabilidade da evolução do software. Atualmente, existem oito leis baseadas nas observações do autor sobre os processos de evolução de sistemas.

---

## Slide 4: Tipos de Sistema

Este slide apresenta os três tipos de sistemas identificados por Lehman: Tipo-S, Tipo-P e Tipo-E.
* **Tipo-S (especificado):** Sistemas formalmente especificados e entendidos como objetos matemáticos, cuja correção pode ser provada. Um exemplo é uma biblioteca de funções matemáticas.
* **Tipo-P (resolução de problemas):** Sistemas desenvolvidos para executar um conjunto de procedimentos que definem o que o programa pode fazer, como um sistema de xadrez.
* **Tipo-E (evolucionário):** Sistemas desenvolvidos para uso em um ambiente real, como sistemas de informação, que não são gerados por métodos formais. Um exemplo é um sistema de folha de pagamento. As Leis de Lehman se aplicam principalmente aos sistemas do Tipo-E, que são propensos a defeitos e precisam evoluir para atender a requisitos em mudança.

---

## Slide 5: 1. Lei da Mudança Contínua

Este slide descreve a primeira Lei de Lehman, a Lei da Mudança Contínua. Esta lei, de 1974, afirma que um sistema efetivamente usado deve ser continuamente melhorado. Caso contrário, ele se torna cada vez menos útil à medida que seu contexto de uso evolui. Isso expressa o fato de que programas grandes nunca são finalizados; eles continuam a evoluir para evitar a obsolescência.

---

## Slide 6: 2. Lei da Complexidade Crescente

Este slide detalha a segunda Lei de Lehman, a Lei da Complexidade Crescente. Datada de 1974, esta lei postula que, à medida que um programa evolui, sua complexidade inerente aumenta. Isso ocorre porque as correções e mudanças podem deteriorar a organização interna do software, tornando a estrutura cada vez mais desestruturada. Para combater isso, medidas específicas como a refatoração do sistema se tornam necessárias e, eventualmente, obrigatórias.

---

## Slide 7: 3. Lei Fundamental da Evolução de Programas: Auto Regulação

Este slide apresenta a terceira Lei de Lehman, a Lei da Autorregulação. Proposta em 1974, esta lei estabelece que a evolução de programas é sujeita a uma dinâmica de autorregulação controlada por feedback. Isso torna as medidas globais de esforço e outros atributos do processo estatisticamente previsíveis, seguindo uma distribuição normal. A organização onde o software é desenvolvido e mantido possui seus próprios processos e objetivos, que acabam regulando o esforço aplicado ao sistema.

---

## Slide 8: 4. Lei da Conservação da Estabilidade Organizacional: Taxa de Trabalho Invariante

Este slide explica a quarta Lei de Lehman, a Lei da Conservação da Estabilidade Organizacional. De 1980, esta lei afirma que a taxa média efetiva de trabalho global em um sistema em evolução é invariante no tempo, ou seja, não aumenta nem diminui. Embora se possa pensar que a carga de trabalho depende apenas das decisões da gerência, na prática, as demandas dos usuários também influenciam, mantendo a taxa de trabalho praticamente constante.

---

## Slide 9: 5. Lei da Conservação da Familiaridade: Complexidade Percebida

Este slide aborda a quinta Lei de Lehman, a Lei da Conservação da Familiaridade. Também de 1980, esta lei expressa que a taxa de crescimento de um sistema é limitada pela necessidade de manter a familiaridade. Para que um sistema evolua de forma saudável, todos os envolvidos devem manter-se familiarizados com suas características. Se o sistema crescer muito rápido, essa familiaridade se perde e é preciso tempo para recuperá-la.

---

## Slide 10: 6. Lei do Crescimento Contínuo

Este slide apresenta a sexta Lei de Lehman, a Lei do Crescimento Contínuo. Formulada em 1980, esta lei estabelece que o conteúdo funcional de um sistema deve crescer continuamente para manter a satisfação do usuário. A mudança no software será sempre necessária, seja para correção de erros (manutenção corretiva), aperfeiçoamento de funções (manutenção perfectiva) ou adaptação a novos contextos (manutenção adaptativa).

---

## Slide 11: 7. Lei da Qualidade Decrescente

Este slide detalha a sétima Lei de Lehman, a Lei da Qualidade Decrescente. De 1996, esta lei afirma que a qualidade de um sistema parecerá diminuir com o tempo, a menos que medidas rigorosas sejam tomadas para mantê-lo e adaptá-lo. Mesmo que um software funcione perfeitamente, com o tempo, os usuários se tornam mais exigentes e, consequentemente, mais insatisfeitos com ele.

---

## Slide 12: 8. Lei do Sistema Realimentado

Este slide explica a oitava Lei de Lehman, a Lei do Sistema Realimentado. Proposta em 1996, esta lei estabelece que a evolução de sistemas é um processo de realimentação multinível, multiloop e multiagente. A evolução do software é um sistema complexo que recebe feedback constante dos vários interessados. A longo prazo, a taxa de evolução é determinada por retornos positivos e negativos dos usuários, verba disponível e novas solicitações de funções.

---

## Slide 13: Classificação das Atividades de Manutenção

Este slide classifica as atividades de manutenção em quatro tipos, conforme a norma ISO/IEC 14764:2006:
* **Corretiva:** Visa corrigir erros ou defeitos do software.
* **Adaptativa:** Visa adaptar as características do software a requisitos que mudaram, como novas funções ou questões tecnológicas.
* **Perfectiva:** Visa melhorar o desempenho ou outras qualidades do software sem alterar sua funcionalidade.
* **Preventiva:** Visa melhorar as qualidades do software para que erros potenciais sejam descobertos e resolvidos mais facilmente.

---

## Slide 14: Manutenção Corretiva

Este slide detalha a manutenção corretiva, que visa corrigir possíveis defeitos que causam erros. Suas atividades podem ser subdivididas em:
* **Manutenção para correção de erros conhecidos:** Erros já identificados, mas que não foram corrigidos porque o processo de depuração ainda não localizou a causa, ou porque a correção seria muito longa e complexa.
* **Manutenção para detecção e correção de novos erros:** Erros detectados pelos usuários durante o uso do software.

---

## Slide 15: Manutenção Adaptativa

Este slide explora a manutenção adaptativa. Esta forma de manutenção é inevitável em sistemas que evoluem. Ela ocorre porque:
* Requisitos de cliente e usuário mudam com o tempo.
* Novos requisitos surgem.
* Leis e normas mudam.
* Novas tecnologias entram em uso.

---

## Slide 16: Requisitos Permanentes e Transitórios

Este slide introduz a diferenciação entre requisitos permanentes e transitórios. Cabe ao analista, junto aos interessados, identificar quais requisitos serão permanentes e quais serão transitórios.
* **Requisitos Transitórios:** Podem ser adaptados por um simples processo de configuração pelo usuário. Implementá-los tem um custo maior no desenvolvimento, mas são mais baratos e rápidos de mudar depois.
* **Requisitos Permanentes:** Só podem ser alterados através de um processo de manutenção. São mais baratos de incorporar inicialmente, mas mais caros e demorados para alterar no futuro.

---

## Slide 17: Manutenção Perfectiva

Este slide define a manutenção perfectiva, que consiste em mudanças que afetam mais as características de desempenho do que a funcionalidade do software. Geralmente, essas melhorias são impulsionadas pela pressão do mercado, que prefere produtos mais eficientes e com melhor usabilidade, especialmente em áreas como jogos e sistemas de controle em tempo real.

---

## Slide 18: Manutenção Preventiva

Este slide explica a manutenção preventiva, que pode ser realizada através de atividades de reengenharia para resolver problemas potenciais. Um exemplo é refatorar a arquitetura de um sistema que está se aproximando de seu limite de acessos simultâneos para suportar uma carga maior e evitar um colapso. Outro uso é aplicar técnicas de engenharia reversa para melhorar a manutenibilidade do software.

---

## Slide 19: Processo de Manutenção

Este slide ilustra o processo de manutenção, que é definido pela Norma ISO/IEC 14764:2006 e compreende seis atividades:
* **Implementação do processo:** O responsável pela manutenção estabelece os planos e procedimentos.
* **Análise do problema e modificação:** O analista analisa a solicitação, replica o problema, desenvolve opções e obtém aprovação.
* **Implementação da modificação:** O responsável desenvolve e testa a modificação no software.
* **Revisão da manutenção/aceitação:** Assegura que as modificações estão corretas e de acordo com os padrões.
* **Migração:** Se necessário, planeja e executa a migração do sistema para um novo ambiente.
* **Desativação:** Quando o software chega ao fim de sua vida útil, é desativado, com atenção especial ao acesso e conversão de dados legados.

---

## Slide 20: Tipos de Atividades de Manutenção

Este slide introduz os diferentes tipos de atividades de manutenção, que variam muito e podem ser classificadas em várias categorias, conforme será detalhado nos próximos slides.

---

## Slide 21: Reparação de Defeitos

Este slide foca na reparação de defeitos, a atividade mais urgente e importante na manutenção, pois visa eliminar problemas que não deveriam existir. O custo dessas atividades é normalmente absorvido pela empresa desenvolvedora. Uma métrica comum é o número de defeitos que uma organização consegue reparar por mês, sendo um valor aceitável em torno de 8, e empresas com bons processos chegando a 20.

---

## Slide 22: Tabela 14-1: Tempo de Resposta ao Erro em Função de sua Severidade

Este slide apresenta uma tabela que relaciona a severidade de um erro com o tempo de resposta esperado e o percentual de defeitos relatados.
* **Severidade 1 (Aplicação não funciona):** Tempo de resposta de 1 dia, correspondendo a 1% dos defeitos.
* **Severidade 2 (Funcionalidade principal não funciona):** Tempo de resposta de 2 dias, correspondendo a 12% dos defeitos.
* **Severidade 3 (Funcionalidade secundária não funciona):** Tempo de resposta de 30 dias, correspondendo a 52% dos defeitos.
* **Severidade 4 (Erro cosmético):** Tempo de resposta de 120 dias, correspondendo a 35% dos defeitos.

---

## Slide 23: Fatores que Podem Influenciar a Estimação de Esforço...

Este slide lista fatores que influenciam a estimativa de esforço para reparação de defeitos:
* **Defeitos suspensos (abeyant):** Cerca de 10% das vezes, a falha relatada pelo cliente não é reproduzida no ambiente de manutenção ("na minha máquina funciona"). São difíceis de detectar e caros de corrigir.
* **Defeitos inválidos:** Cerca de 15% dos relatos não são defeitos do software, mas sim erros dos usuários ou de sistemas relacionados. Mesmo assim, demandam tempo e esforço para serem analisados.
* **Consertos ruins (bad fix injection):** Cerca de 7% das correções introduzem novos erros, podendo variar de 1 a 20%.
* **Defeitos duplicados:** É comum que o mesmo defeito seja relatado por vários usuários, exigindo tempo para identificar a duplicação. Em grandes empresas, pode chegar a 10% dos relatos.

---

## Slide 24: Remoção de Módulos Sujeitos a Erros

Este slide discute a concentração de defeitos em módulos específicos. Uma pesquisa da IBM nos anos 1960 mostrou que os defeitos não se distribuem aleatoriamente; eles tendem a se concentrar em determinados módulos. Em um grande sistema, observou-se que 31 dos 425 módulos concentravam mais de 60% do total de erros. Módulos muito problemáticos podem nunca estabilizar, pois a taxa de introdução de novos defeitos durante a correção pode ser alta.

---

## Slide 25: Suporte a Usuários

Este slide aborda o suporte a usuários, que serve como interface entre o cliente e a empresa de manutenção. A equipe de suporte recebe reclamações, faz uma triagem, oferece soluções conhecidas ou encaminha o problema para o setor de manutenção. O tamanho da equipe depende da quantidade esperada de defeitos e de clientes. Um atendente pode tratar cerca de 150 chamadas por telefone por mês, número que pode subir para mil se o contato for por e-mail ou chat.

---

## Slide 26: Migração entre Plataformas

Este slide trata da migração de um produto para outra plataforma. Quando o software é personalizado, a migração ocorre por demanda do cliente. No caso de software de prateleira, a intenção é aumentar o mercado. A taxa de migração pode ser de cinquenta pontos de função por desenvolvedor-mês para sistemas bem documentados, mas pode cair para apenas cinco em sistemas mal documentados e com organização obscura.

---

## Slide 27: Conversão de Arquitetura

Este slide discute a conversão de arquitetura, que geralmente é motivada por pressão tecnológica, como mudar de arquivos simples para bancos de dados. Também pode ser uma estratégia para melhorar a manutenção, transformando um sistema monolítico em um mais bem estruturado. A produtividade dessa conversão depende da qualidade das especificações do sistema; quanto mais obscuras, mais difícil será a conversão.

---

## Slide 28: Adaptações Obrigatórias

Este slide foca nas adaptações obrigatórias, consideradas os piores tipos de manutenção. Elas decorrem de mudanças em normas, leis, cálculo de impostos, etc. O problema é que essas mudanças não podem ser previstas, têm prazos curtos e estritos para serem aplicadas, e as penalidades por não adaptação costumam ser altas.

---

## Slide 29: Otimização de Performance

Este slide aborda a otimização de performance, que implica em analisar e resolver gargalos da aplicação, geralmente relacionados a acesso a dados, processamento e número de usuários simultâneos. Como essas atividades variam muito, é difícil estabelecer um padrão para estimar custos. Uma técnica que pode ser usada é a otimização estilo *anytime*, com *timeboxing*, para se obter a melhor otimização possível dentro do tempo e com os recursos disponíveis.

---

## Slide 30: Melhorias

Este slide discute as melhorias, que são um tipo de manutenção adaptativa e perfectiva, geralmente iniciadas pelos clientes. Existem dois tipos:
* **Pequenas melhorias:** Consistem em aproximadamente cinco pontos de função, como a introdução de um novo relatório, consulta ou tela.
* **Grandes melhorias:** Consistem em um número significativamente maior de pontos de função, geralmente mais de 20, e devem ser tratadas como pequenos projetos de desenvolvimento. Estima-se que sistemas em operação aumentem seus pontos de função em cerca de 7% anualmente devido a melhorias.

---

## Slide 31: Modelos de Estimação de Esforço de Manutenção

Este slide apresenta três modelos para estimar o esforço de manutenção: ACT, COCOMO II-Manutenção e FP e SMPEEM. Assim como nos modelos para desenvolvimento, esses modelos podem usar como base o número de pontos de função ou de linhas de código.

---

## Slide 32: Modelo ACT

Este slide explica o Modelo ACT (Annual Change Traffic ou Tráfego de Mudança Anual).
* Este modelo se baseia em uma estimativa da porcentagem de linhas de código que sofrerão manutenção em um ano.
* São consideradas tanto as novas linhas de código criadas quanto as linhas alteradas durante a manutenção.
* O valor da variável ACT é o número de linhas que sofrem manutenção dividido pelo número total de linhas de código em um ano típico.

---

## Slide 33: ACT (Fórmula)

Este slide apresenta a fórmula do modelo ACT para estimar o esforço de manutenção durante um ano:
$E = ACT * SDT$
* **E:** Esforço estimado, medido em desenvolvedor-mês.
* **ACT:** Porcentagem de linhas que sofrerão manutenção.
* **SDT:** Software Development Time (Tempo de Desenvolvimento do Software), também em desenvolvedor-mês.

---

## Slide 34: Exemplo (ACT)

Este slide fornece um exemplo de aplicação do modelo ACT.
* Um software desenvolvido com um esforço de 80 desenvolvedores-mês tem um $SDT = 80$.
* Se a taxa anual esperada de linhas em manutenção (ACT) for de 2%, o esforço anual esperado de manutenção será:
    $E = 0,02 * 80 = 1,6$
* Isso significa um esforço anual de 1,6 desenvolvedor-mês em atividades de manutenção.

---

## Slide 35: Variação de Schaefer

Este slide apresenta a variação de Schaefer para o modelo ACT, proposta em 1985. A fórmula é:
$E = ACT * 2,4 * KSLOC^{1,05}$
Nesta variação, Schaefer substitui o tempo de desenvolvimento do produto (SDT) por uma fórmula baseada no número total de milhares de linhas de código do produto (KSLOC).

---

## Slide 36: Exemplo (Variação de Schaefer)

Este slide mostra um exemplo da variação de Schaefer.
* Para um software com 20 mil linhas de código (KSLOC = 20) e um ACT de 2%, o esforço anual de manutenção em desenvolvedor-mês seria:
    $E = 0,02 * 2,4 * 20^{1,05} = 1,115$

---

## Slide 37: Modelo de Manutenção de CII

Este slide introduz o modelo de manutenção do COCOMO II (CII), que é semelhante ao modelo *post-architecture*. A equação é:
$E = A * KSLOC_m^S * \prod_{i=1}^{n} M_i$
Onde:
* **E:** Esforço de manutenção em desenvolvedor-mês.
* **A:** Constante calibrada pelo método (inicialmente 2,94).
* **$KSLOC_m$:** Número de linhas de código a serem adicionadas ou alteradas, ajustado pelo fator de manutenção (MAF). Linhas excluídas não são contadas.
* **S:** Coeficiente de esforço determinado por fatores de escala.
* **M:** Multiplicadores de esforço.

---

## Slide 38: Mudanças em Relação ao Modelo Post-Architecture...

Este slide detalha as mudanças do modelo de manutenção do CII em relação ao modelo *post-architecture*:
* **SCED (Cronograma de Desenvolvimento Requerido):** Não é usado, pois se espera que os ciclos de manutenção tenham duração fixa predeterminada.
* **RUSE (Desenvolvimento para Reuso):** Não é usado, pois se considera que o esforço para manter a reusabilidade é balanceado pela redução do esforço de manutenção devido ao projeto, documentação e testes cuidadosos.
* **RELY (Software com Confiabilidade Requerida):** Tem uma tabela de aplicação diferenciada, pois o esforço para consertar o software dependerá da confiabilidade com que ele foi desenvolvido.

---

## Slide 39: Tabela 14-2: Forma de obtenção do equivalente numérico para RELY...

Este slide apresenta a tabela para o multiplicador RELY na fase de manutenção. A confiabilidade original do sistema (avaliada como muito baixa, baixa, nominal, alta, muito alta ou extra alta) determina um valor numérico a ser aplicado. Os valores são inversamente proporcionais aos usados na fase de desenvolvimento; um sistema desenvolvido com baixa confiabilidade (ex: "Muito baixo", com valor 1,23) terá maior esforço de manutenção, enquanto um com alta confiabilidade (ex: "Alto", com valor 0,99) terá menor esforço, exceto em casos de risco à vida humana.

---

## Slide 40: Fator de Ajuste de Manutenção (MAF)

Este slide explica o Fator de Ajuste de Manutenção (MAF), usado para ajustar o KSLOC na fase de manutenção.
A fórmula para o KSLOC ajustado é:
$KSLOC_m = (KSLOC_{adicionadas} + KSLOC_{modificadas}) * MAF$
E o MAF é calculado como:
$MAF = 1 + (\frac{SU}{100} * UNFM)$
Onde:
* **SU (Software Understanding):** Fator de ajuste relacionado à compreensão do software.
* **UNFM (Unfamiliarity):** Fator de não familiaridade com o software.

---

## Slide 41: Tabelas 14-3 (SU) e 14-4 (UNFM)

Este slide mostra as tabelas para calcular os valores de SU e UNFM.
* **Tabela 14-3 (Valor de SU):** O valor de SU varia de 10 (muito alto) a 50 (muito baixo) e é determinado pela avaliação de três critérios: Estrutura (coesão, acoplamento), Clareza da aplicação e Autodescrição (documentação, código).
* **Tabela 14-4 (Valor de UNFM):** O valor de UNFM mede o nível de não familiaridade da equipe com o software, variando de 0,0 (Completamente familiar) a 1,0 (Completamente não familiar).

---

## Slide 42: Modelos FP e SMPEEM

Este slide introduz os modelos baseados em Pontos de Função (FP) e o modelo SMPEEM. O modelo FP para manutenção calcula os pontos de função não ajustados (UFP) de quatro tipos de funções:
* **ADD:** UFP de funções que serão adicionadas.
* **CHG:** UFP de funções que serão alteradas.
* **DEL:** UFP de funções que serão removidas.
* **CFP:** UFP de funções que serão adicionadas por conversão.

---

## Slide 43: Equação do Modelo FP

Este slide apresenta a equação do modelo de manutenção baseado em Pontos de Função. A técnica propõe que o Fator de Ajuste Técnico (VAF) seja calculado em dois momentos: antes da manutenção ($VAF_A$) e depois da manutenção ($VAF_D$). A equação de esforço (E) é:
$E = (ADD + CHG + CPF) * VAF_D + DEL * VAF_A$
Isso ocorre porque a atividade de manutenção pode alterar fatores que afetam o VAF, como a segurança ou a facilidade de uso do sistema.

---

## Slide 44: Evolução SMPEEM

Este slide descreve o modelo SMPEEM (Software Maintenance Project Effort Estimation Model), uma evolução do modelo FP. Ele inclui dez fatores de ajuste específicos para as atividades de manutenção:
* Conhecimento do domínio da aplicação.
* Familiaridade com a linguagem de programação.
* Experiência com o software básico.
* Estruturação e independência dos módulos.
* Legibilidade e modificabilidade da linguagem.
* Reusabilidade de módulos legados.
* Atualização da documentação, conformidade com padrões e testabilidade.
Os três primeiros fatores referem-se às habilidades da equipe, os quatro seguintes às características técnicas e os três últimos ao ambiente de manutenção.

---

## Slide 45: Engenharia Reversa e Reengenharia

Este slide introduz os conceitos de Engenharia Reversa e Reengenharia, que são técnicas usadas em processos de manutenção de software, especialmente em situações mais drásticas. Sistemas antigos, mal documentados e mal mantidos podem exigir um processo completo de reengenharia para voltarem a evoluir de forma saudável.

---

## Slide 46: Taxionomia de Chikofsky e Cross II

Este slide apresenta a taxonomia de Chikofsky e Cross (1990) que relaciona os termos da reengenharia de software.
* **Engenharia Reversa:** Analisa um sistema para produzir especificações de nível mais alto. Vai da implementação para o projeto e para os requisitos.
* **Reengenharia:** Exame e alteração de um sistema para reconstruí-lo de forma diferente. Geralmente, envolve engenharia reversa seguida de engenharia direta.
* **Reestruturação/Redocumentação:** Formas de refatoração. A redocumentação é uma subárea da engenharia reversa que obtém formas alternativas de especificação no mesmo nível.
* **Recuperação de Projeto:** Subárea da engenharia reversa que realiza abstrações para produzir artefatos em níveis mais altos.

---

## Slide 47: Engenharia Reversa (Tipos)

Este slide classifica a engenharia reversa em dois tipos, com base em seu objeto:
* **De código (Fonte, Objeto):** Usada para melhorar a compreensão de sistemas legados (código-fonte) ou para clonagem de produtos (código-objeto).
* **De dados:** Focada na localização, organização e reinterpretação do significado dos dados de um sistema.

---

## Slide 48: Técnicas de Engenharia Reversa de Código

Este slide lista as técnicas para realizar a engenharia reversa de código:
* **Análise de fluxo de dados:** Verifica o comportamento do sistema como uma caixa-preta, sem conhecimento da estrutura interna, para desenvolver um novo sistema com o mesmo comportamento.
* **Dessassemblagem (Disassembly):** Usa um desassemblador para converter código executável em mnemônicos de linguagem Assembly.
* **Descompilação:** Usa um descompilador para obter uma aproximação do código original usado para produzir o executável.

---

## Slide 49: Componentes de um Descompilador

Este slide detalha os componentes de um descompilador, que são mais complexos que os de um desassemblador.
* **Carregador:** Carrega o programa e identifica informações básicas como tipo de processador e ponto de entrada.
* **Desassemblador:** Transforma os códigos de máquina em uma representação mnemônica.
* **Identificador de Expressões Idiomáticas:** Cataloga e reconhece sequências de instruções comuns para operações simples (ex: `xor eax, eax` para `eax = 0`).
* **Análise de Programa:** Agrupa sequências de operações em comandos de alto nível.
* **Análise de Fluxo de Dados:** Detecta variáveis e seu escopo.
* **Análise de Tipos:** Infere o tipo das variáveis observando as operações executadas sobre elas.
* **Estruturação:** Transforma estruturas de máquina em estruturas de alto nível (ex: `if`, `while`).
* **Geração de Código:** Gera o código final na linguagem-alvo.

---

## Slide 50: Engenharia Reversa de Dados

Este slide foca na engenharia reversa de dados, um caso especial cujo foco é a localização, organização e reinterpretação do significado dos dados de um sistema. Uma de suas atividades centrais é a análise de dados, que consiste em recuperar um modelo de dados atualizado, completo e semanticamente anotado a partir de um sistema em operação. Esta atividade é particularmente difícil de ser automatizada, pois informações semânticas e estruturais importantes acabam diluídas no código executável e na documentação.