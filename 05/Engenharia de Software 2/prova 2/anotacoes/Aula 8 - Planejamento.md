## Seleção de Projetos

A seleção de projetos é uma decisão crítica tanto para a empresa desenvolvedora quanto para a cliente. Para a desenvolvedora, é essencial avaliar se ela possui competência técnica, capacidade operacional disponível e se o projeto trará retorno financeiro. Já do lado do cliente, os fatores mais considerados são retorno sobre investimento, aumento de participação no mercado, melhoria da imagem, aproveitamento de capacidade ociosa e aquisição de novas tecnologias. Quando o desenvolvimento é para o mercado (COTS), a própria desenvolvedora assume os riscos.

---

## Termo de Abertura (Project Charter)

O termo de abertura oficializa o início do projeto. Segundo o PMBOK, ele deve conter informações como: objetivo e justificativa do projeto, descrição de alto nível do produto, requisitos de alto nível, nomeação do gerente de projeto, cronograma de marcos, definição de papéis e responsabilidades, premissas, restrições, estudo de viabilidade e orçamento preliminar. Sua aprovação por um gerente sênior confere autoridade ao gerente de projeto para iniciar os trabalhos.

---

## Business Model Canvas

O Business Model Canvas é uma ferramenta visual que organiza ideias de negócio em áreas específicas, facilitando a concepção de um projeto. No lado direito, são abordados clientes, proposta de valor e canais de entrega. No lado esquerdo, recursos, atividades e parcerias necessárias para viabilizar a proposta. Segmentos de clientes e a proposta de valor devem ser claramente definidos, priorizando necessidades e tipos de relacionamento. Fontes de receita, estrutura de custos e canais de comunicação também são estruturados no Canvas.

---

## Declaração de Escopo

A declaração de escopo é o documento que define os objetivos claros do projeto. Diferente do termo de abertura, ela detalha o produto final esperado e lista as entregas principais. Os objetivos devem ser quantificáveis, com métricas claras de prazo, custo e qualidade. Critérios de aceitação são definidos aqui. Não pode haver novos requisitos além dos previstos no termo de abertura; qualquer mudança exige renegociação.

---

## Atividades do Planejamento Geral

O planejamento geral engloba a estimativa do esforço total, cálculo da duração linear e tamanho médio da equipe, além da duração e esforço de cada fase. Também se estima a duração e número de iterações. Essas atividades são fundamentais para criar um cronograma viável e ajustar expectativas de prazo e custo do projeto.

---

## Estimação da Duração e Esforço nas Diferentes Fases

Utilizando como exemplo o Processo Unificado (UP), a distribuição típica é: concepção (10% tempo, 5% esforço), elaboração (30% tempo, 20% esforço), construção (50% tempo, 65% esforço) e transição (10% tempo, 10% esforço). Essas porcentagens guiam a divisão de tempo e recursos ao longo do projeto, mas podem ser ajustadas conforme o contexto.

---

## Exemplo de Estimativas

Num projeto com 40 desenvolvedor-mês de esforço estimado e duração ideal de 8,5 meses:
- Concepção: 0,85 meses, 2,35 devs.
- Elaboração: 2,55 meses, 3,13 devs.
- Construção: 4,25 meses, 6,11 devs.
- Transição: 0,85 meses, 4,7 devs.
Os cálculos consideram a equação $T = 2.5 \times \sqrt[3]{E}$, onde E é o esforço total.

---

## Alterações do Perfil Típico

Certos fatores podem alterar o perfil típico de esforço e duração. Se o projeto precisa de pesquisa de mercado ou envolve riscos altos, a concepção e a elaboração podem demandar mais tempo. Se o projeto for uma evolução de um produto já existente, essas fases podem ser encurtadas. A necessidade de atender mercados rapidamente ou realizar uma migração crítica também impactam as fases.

---

## Estimação da Duração das Iterações

A duração típica de uma iteração varia:
- Pequenas equipes (até 5 pessoas): 1 semana.
- Médias (6-20 pessoas): 2 a 4 semanas.
- Grandes (>20 pessoas): 4 a 8 semanas.
Equipes maiores, processos mais burocráticos ou maior criticidade do projeto tendem a aumentar a duração das iterações.

---

## Outros Fatores que Afetam a Duração

Automatização de processos, experiência da equipe e criticidade de qualidade influenciam o tempo das iterações. Idealmente, as iterações devem ser as mais curtas possíveis para manter a agilidade e o feedback rápido.

---

## Retomando o Exemplo

Num projeto de 8,5 meses, considerando iterações de duas semanas, temos cerca de 17 iterações. A proporção de iterações entre elaboração e construção deve respeitar a divisão de 30% e 50% do tempo total respectivamente.

---

## Planejamento de Iteração

O planejamento de cada iteração é detalhado apenas quando a anterior está em andamento. Os objetivos podem envolver:
- Desenvolvimento de casos de uso críticos.
- Mitigação de riscos de alta exposição.
- Implementação de modificações necessárias.
É fundamental que o objetivo da iteração seja palpável e mensurável.

---

## Priorização no Planejamento de Iterações

Prioriza-se casos de uso críticos para o negócio, riscos de alta exposição e modificações arquiteturais urgentes. A equipe pode incluir tarefas complementares para aproveitar afinidades, desde que respeitem o limite de esforço disponível.

---

## WBS – Estrutura Analítica da Iteração

A Work Breakdown Structure (WBS) é a decomposição hierárquica do trabalho que precisa ser executado para alcançar os objetivos da iteração ou do projeto. Cada atividade definida deve resultar em um artefato palpável ou numa alteração consistente de artefato existente. A ideia central é transformar grandes entregas em partes gerenciáveis.

Durante a criação da WBS, é recomendável que se aproveite experiências anteriores, utilizando templates ou exemplos de projetos similares. A WBS pode ser estruturada como uma árvore, onde o trabalho vai sendo quebrado em níveis sucessivos de maior detalhe, até chegar em pacotes de trabalho suficientemente pequenos para serem atribuídos a indivíduos ou pequenos grupos.

Cada atividade deve ser clara, concreta e evitar nomes vagos. Sempre que possível, usa-se substantivos que representem o que será entregue ("documento de requisitos validado", "protótipo da interface", etc.), e não ações ("fazer requisitos", "testar módulo").

A WBS é essencial tanto em métodos tradicionais quanto em métodos ágeis — embora em ágeis ela seja mais informal e dinâmica.

---

## Regra 8-80

A regra 8-80 estabelece que nenhuma atividade terminal da WBS deve ter duração estimada menor que 8 horas nem maior que 80 horas.

Se a atividade for muito grande (mais de 80 horas), ela precisa ser subdividida em atividades menores. Se for muito pequena (menos de 8 horas), é melhor agregá-la a outra para formar uma unidade de trabalho mais robusta.

O motivo dessa regra é evitar microgerenciamento desnecessário no caso de tarefas muito curtas, e perda de controle no caso de tarefas muito longas.

Métodos como XP (Extreme Programming) vão além e preferem tarefas com duração entre 1 e 3 dias de trabalho (8 a 24 horas), para manter ciclos curtos de feedback.

---

## Regra dos Níveis

A WBS deve ser estruturada com, no máximo, 3 ou 4 níveis de decomposição. Cada nível representa uma subdivisão maior de detalhamento.

Mais níveis aumentam a complexidade do gerenciamento, tornando o controle e a comunicação internos confusos. Cada nível deve contribuir com clareza e agilidade, não com burocracia.

A decomposição deve ser feita até o ponto em que o trabalho possa ser planejado, monitorado e controlado de maneira adequada.

---

## Regra do Número de Atividades

O número total de pacotes de trabalho (as atividades finais na WBS) deve ser limitado a cerca de 100 a 200 atividades.

Se houver mais de 200 atividades, o projeto ou iteração deve ser subdividido em partes menores. Projetos com mais de 100 atividades já demandam bastante esforço de coordenação.

Essa limitação evita que o projeto se torne excessivamente detalhado, dificultando a gestão, e ao mesmo tempo assegura que todos os itens importantes estejam incluídos.

---

## Regra dos 100%

A WBS deve cobrir 100% do trabalho necessário para atingir os objetivos definidos, sem lacunas ou itens fora da estrutura.

Isso significa que:
- Todo trabalho do projeto deve estar representado.
- Toda atividade deve gerar um artefato de saída definido.
- Nenhuma atividade pode ser executada fora do que está previsto na WBS.

A regra dos 100% também vale para os níveis internos de decomposição: a soma das atividades de um nível deve cobrir totalmente a atividade do nível superior.

Essa disciplina garante que não se perca o controle sobre o que está sendo desenvolvido e que não ocorram esforços não planejados.

---

## Identificação dos Responsáveis

Cada atividade terminal da WBS deve ser atribuída a uma pessoa específica, com responsabilidade clara pela execução e entrega do artefato.

Além do responsável principal, podem ser associados participantes para apoio, mas o controle e cobrança de resultados recaem sobre o responsável.

Essa atribuição tem impacto no cronograma: atividades simultâneas só podem ser planejadas se os responsáveis forem distintos.

---

## Identificação dos Recursos e Custo

Além das pessoas, é necessário prever recursos físicos (máquinas, licenças, ambientes de teste, materiais) e financeiros necessários para cada atividade.

O custo de uma atividade é a soma:
- Do custo de trabalho das pessoas alocadas.
- Do custo dos recursos consumidos.

Antecipar esses custos no planejamento reduz riscos financeiros e evita atrasos por falta de recursos no meio da execução.

---

## Identificação das Dependências

Dependências ocorrem quando uma atividade precisa de um artefato ou de uma saída de outra atividade para ser iniciada.

Elas precisam ser explicitadas na estrutura de planejamento para que o sequenciamento correto das tarefas possa ser respeitado.

Dependências mal mapeadas podem gerar gargalos e paradas de equipe, portanto, devem ser levantadas e analisadas logo no planejamento.

---

## Exemplo de WBS

Um exemplo de WBS para a fase de concepção de um sistema poderia ser:

- Modelo preliminar de casos de uso.
- Elicitação inicial de requisitos.
- Protótipo de interfaces críticas.
- Documento de visão do sistema.

Cada um desses elementos pode ser decomposto em subatividades, sempre respeitando a regra 8-80.

---

## Rede PERT

A Rede PERT é o grafo das atividades planejadas, com suas durações e dependências explícitas.

Permite calcular:
- Sequência de atividades.
- Tempo mínimo para concluir o projeto.
- Identificação do caminho crítico (as tarefas que, se atrasarem, atrasam o projeto).

Ferramentas como Redmine e OpenProject permitem construir redes PERT de forma visual e automática, a partir dos dados da WBS.

---

## Como Recuperar um Atraso no Caminho Crítico

Se atividades do caminho crítico atrasarem, as principais opções são:

- **Aumentar jornada de trabalho** (não recomendado como prática contínua).
- **Adicionar pessoas** (mas novos membros exigem treinamento e integração, podendo inicialmente piorar o problema).
- **Remover funcionalidades** da iteração atual (opção mais segura e controlada, transferindo objetivos para ciclos futuros).

Manter o moral da equipe e a qualidade do produto é essencial ao decidir como agir sobre atrasos.

---

## Cronograma (Diagrama de Gantt)

O cronograma é a visualização do projeto no tempo, indicando o início e fim previsto de cada atividade.

O Diagrama de Gantt exibe claramente:
- Atividades simultâneas.
- Atividades críticas (em destaque).
- Datas de entrega intermediárias e finais.

Ferramentas modernas geram Gantt a partir da WBS e da Rede PERT, automatizando boa parte do ajuste de prazos conforme mudanças ocorrem no projeto.

---
