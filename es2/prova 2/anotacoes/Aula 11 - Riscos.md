## Gerenciamento de Riscos (Slide 1)

Este slide apresenta o título da aula: "MANAGE YOUR RISK - GERENCIAMENTO DE RISCOS". Indica o nome do professor, Raul Sidnei Wazlawick, e a instituição, UFSC-CTC-INE.

---

## Conteúdo da Aula (Slide 2)

Este slide delineia os tópicos que serão abordados na apresentação sobre gerenciamento de riscos:
* Plano de Gerência de Riscos
* Identificação de Riscos
* Checklist de Riscos
* Análise de Riscos
* Planos de Mitigação de Riscos
* Plano de Contingência
* Monitoramento de Riscos
* Controle de Risco
* Comunicação de Riscos

---

## Risco: Incertezas, Problemas, Planos (Slide 3)

Este slide apresenta uma imagem conceitual relacionada a risco e destaca três palavras-chave fundamentais para o entendimento do tema:
* **Incertezas:** Riscos estão associados a eventos futuros e incertos.
* **Problemas:** Riscos, se concretizados, tornam-se problemas para o projeto.
* **Planos:** É necessário planejar para lidar com os riscos.

---

## Modelo de Gerenciamento de Riscos (SEI) (Slide 4)

Este slide apresenta o modelo de gerenciamento de riscos proposto pelo Software Engineering Institute (SEI) do Carnegie Mellon. As etapas do modelo são:
* **Identificação:** Descobrir e documentar os riscos potenciais.
* **Análise:** Avaliar a probabilidade e o impacto de cada risco.
* **Planejamento:** Definir ações para tratar os riscos (mitigação, contingência).
* **Rastreamento ou monitoramento:** Acompanhar os riscos e os planos de ação.
* **Controle:** Executar os planos de resposta e ajustar conforme necessário.
* **Comunicação:** Manter as partes interessadas informadas sobre os riscos.

---

## Plano de Gerência de Riscos (Slide 5)

Este slide detalha o conteúdo essencial de um Plano de Gerência de Riscos. Ele deve incluir:
* **IN:** Quais são os riscos identificados.
* Uma análise qualitativa ou quantitativa de cada risco, indicando a probabilidade de sua ocorrência e seu provável impacto sobre o projeto.
* **X:** Planos de mitigação e de contingência para os riscos.
* Responsáveis por cada plano.
* Cronogramas para a execução dos planos.
* Recursos necessários.
* Indicadores para acompanhar a evolução dos riscos.
* Orçamentos para os planos de mitigação e contingência.

---

## Identificação de Riscos (Slide 6)

Este slide lista diversas técnicas que podem ser utilizadas para identificar riscos em um projeto:
* **Brainstorming:** Reunião de equipe para levantar ideias sobre possíveis riscos.
* **Entrevistas:** Conversas com especialistas, stakeholders e membros da equipe.
* **Análise de Causa-Raiz:** Investigar as causas fundamentais de problemas passados para prever riscos futuros.
* **Estudo de projetos anteriores (lições aprendidas):** Analisar a documentação e experiência de projetos similares.
* **Checklists:** Utilizar listas predefinidas de riscos comuns.

---

## Categorias de Risco (SEI) (Slide 7)

Este slide apresenta as categorias de risco definidas pelo SEI, que ajudam a organizar e identificar potenciais ameaças:
* **Riscos de Projeto:** Relacionados ao planejamento e execução do projeto.
    * Orçamento e cronograma
    * Organização e gerenciamento
    * Clientes e usuários
    * Subcontratados
* **Riscos Técnicos:** Associados à tecnologia e aos processos de desenvolvimento.
    * Requisitos
    * Tecnologia
    * Engenharia de software (projeto, implementação, testes, manutenção)
    * Qualidade
* **Riscos de Negócio:** Relacionados ao ambiente de negócios da empresa.
    * Mercado
    * Estratégia
    * Financeiro
    * Legal

---

## Checklist - O que pode dar errado? (Slide 8)

Este slide propõe um checklist com perguntas direcionadas para auxiliar na identificação de riscos em diversas áreas do projeto:
* **Requisitos:** Instáveis, incompletos, complexos, ambíguos?
* **Estimativas:** Imprecisas, otimistas demais?
* **Equipe:** Inexperiente, desmotivada, com alta rotatividade, conflitos?
* **Tecnologia:** Nova, obsoleta, instável, incompatível?
* **Ferramentas:** Inadequadas, com problemas de integração, falta de treinamento?
* **Clientes/Usuários:** Indecisos, com expectativas irrealistas, falta de envolvimento?
* **Gerenciamento:** Falta de planejamento, comunicação deficiente, liderança inadequada?
* **Restrições:** Cronograma apertado, orçamento limitado, recursos escassos?

---

## Identificação de Riscos - Estrutura (Slide 9)

Este slide sugere uma estrutura para descrever os riscos identificados, utilizando uma relação de causa e efeito (condição -> consequência):
* **Formato:** "SE [condição do risco existe], ENTÃO [consequência indesejada ocorre]."
* **Exemplo:** "Se o novo sistema operacional não for estável, ENTÃO alguns recursos importantes do sistema podem não funcionar como deveriam."

---

## Análise de Riscos - Qualitativa (Probabilidade) (Slide 10)

Este slide introduz a análise qualitativa de riscos, focando na avaliação da probabilidade de ocorrência. É apresentada uma tabela de exemplo com escalas para classificar a probabilidade:
* **Muito Alta:** > 80%
* **Alta:** 61 – 80%
* **Média:** 41 – 60%
* **Baixa:** 21 – 40%
* **Muito Baixa:** < 20%

---

## Análise de Riscos - Qualitativa (Impacto) (Slide 11)

Este slide continua a discussão sobre a análise qualitativa de riscos, agora focando na avaliação do impacto caso o risco se concretize. É apresentada uma tabela de exemplo com escalas para classificar o impacto em diferentes dimensões (Custo, Cronograma, Escopo, Qualidade):
* **Muito Alto:** Aumento de custo > 20%, Atraso > 20%, Escopo muito reduzido, Qualidade inaceitável.
* **Alto:** Aumento de custo 10-20%, Atraso 10-20%, Escopo reduzido, Qualidade ruim.
* **Médio:** Aumento de custo 5-10%, Atraso 5-10%, Escopo pouco reduzido, Qualidade regular.
* **Baixo:** Aumento de custo 1-5%, Atraso 1-5%, Escopo pouco afetado, Qualidade boa.
* **Muito Baixo:** Aumento de custo < 1%, Atraso < 1%, Escopo não afetado, Qualidade ótima.

---

## Análise de Riscos - Matriz de Probabilidade e Impacto (Slide 12)

Este slide apresenta uma Matriz de Probabilidade e Impacto (geralmente 5x5), uma ferramenta visual para classificar a severidade dos riscos. A combinação dos níveis de probabilidade e impacto determina se um risco é considerado de severidade Baixa, Moderada ou Alta, ajudando na priorização das ações de resposta. Riscos na zona "Alta" (vermelha) exigem atenção imediata.

---

## Análise de Riscos - Quantitativa (Slide 13)

Este slide introduz a análise quantitativa de riscos, que busca atribuir valores numéricos aos riscos. O foco é no cálculo do **Valor Monetário Esperado (VME)**, também conhecido como Exposição ao Risco:

$VME = Probabilidade \times Impacto Monetário$

O impacto monetário representa a perda financeira caso o risco ocorra.

---

## Análise de Riscos - Exemplo de Cálculo (Slide 14)

Este slide demonstra um exemplo prático de análise quantitativa. É apresentada uma tabela com uma lista de riscos, suas respectivas probabilidades de ocorrência (P), a perda financeira estimada caso ocorram (L), e a Exposição ao Risco (ER) calculada como $ER = P \times L$.
Por exemplo:
* Risco: Falta de pessoal qualificado; P=30%; L=R$10.000; ER=R$3.000.
* Risco: Atraso na entrega do hardware; P=10%; L=R$20.000; ER=R$2.000.

---

## Análise de Riscos - Exemplo (Gráfico de Pareto) (Slide 15)

Este slide mostra um Gráfico de Pareto aplicado à análise de riscos. Os riscos (do exemplo anterior) são ordenados da maior para a menor exposição. O gráfico de barras representa a exposição individual de cada risco, e uma linha representa a exposição acumulada. Isso ajuda a identificar os poucos riscos vitais que contribuem para a maior parte da exposição total (Princípio de Pareto 80/20), permitindo focar os esforços de mitigação nos riscos mais significativos.

---

## Planejamento de Respostas a Riscos (Slide 16)

Este slide apresenta as principais estratégias para o planejamento de respostas a riscos:
* **Prevenir/Evitar (Avoid):** Eliminar a ameaça ou proteger o projeto de seu impacto, alterando o plano do projeto.
* **Transferir (Transfer):** Passar o impacto negativo (e a responsabilidade pela resposta) para um terceiro (e.g., seguro, subcontratação).
* **Mitigar (Mitigate):** Reduzir a probabilidade de ocorrência do risco e/ou seu impacto para um limiar aceitável.
    * Reduzir Probabilidade
    * Reduzir Impacto
* **Aceitar (Accept):** Nenhuma ação é tomada para alterar o plano do projeto, ou nenhuma estratégia de resposta é viável. Pode ser passiva (aceitar as consequências) ou ativa (estabelecer um plano de contingência).

---

## Planos de Mitigação de Riscos (ANTES) (Slide 17)

Este slide foca nos Planos de Mitigação, que são ações proativas realizadas *antes* que o risco se concretize, com o objetivo de reduzir sua probabilidade ou impacto.
* Devem ser planejados para os riscos mais importantes.
* Custos de mitigação devem ser considerados.
* **Exemplo:** "Fazer protótipos para diminuir o risco de requisitos mal interpretados pelo cliente."

---

## Exemplo de Ações de Mitigação (Continuação) (Slide 18)

Este slide continua o exemplo da análise de riscos, apresentando uma tabela com possíveis ações de mitigação para os riscos identificados anteriormente. Para cada ação, são listados:
* Custo da mitigação.
* Redução da probabilidade (P) e/ou da perda (L).
* A nova exposição ao risco (ER) após a mitigação.
Isso permite avaliar a eficácia e o custo-benefício das ações de mitigação. Por exemplo, uma ação de mitigação para "Falta de pessoal qualificado" poderia ser "Treinamento intensivo", com um custo, e resultando em uma nova probabilidade e/ou perda menor.

---

## Plano de Redução de Probabilidade de Risco (Exemplo) (Slide 19)

Este slide apresenta um exemplo de formulário para um Plano de Redução de Probabilidade de Risco. O exemplo detalha um plano para o risco "Atraso na entrega de componentes de hardware essenciais":
* **Risco:** Atraso na entrega de componentes de hardware.
* **Responsável:** Gerente de Compras.
* **Estratégia de Redução de Probabilidade:** Negociar prazos mais curtos com fornecedores alternativos; realizar pedidos com antecedência; monitorar de perto o progresso da entrega.
* **Recursos Necessários:** Tempo para pesquisa e negociação.
* **Indicador:** Confirmação de datas de entrega dos fornecedores.
* **Prazo:** Data limite para confirmação.

---

## Plano de Redução de Impacto de Risco (Exemplo) (Slide 20)

Este slide mostra um exemplo de formulário para um Plano de Redução de Impacto de Risco, usando o mesmo risco do slide anterior ("Atraso na entrega de componentes de hardware essenciais"):
* **Risco:** Atraso na entrega de componentes de hardware.
* **Responsável:** Gerente de Projeto.
* **Estratégia de Redução de Impacto:** Identificar componentes substitutos compatíveis; preparar equipe para integrar componentes alternativos; realocar tarefas do cronograma para minimizar ociosidade.
* **Recursos Necessários:** Tempo para pesquisa de substitutos; possível custo adicional de componentes.
* **Indicador:** Plano de integração para componentes alternativos pronto.
* **Prazo:** Data limite para ter o plano de substituição.

---

## Plano de Contingência (DEPOIS) (Slide 21)

Este slide explica o Plano de Contingência, que é a resposta ao risco *após* sua ocorrência efetiva.
* Deve ser preparado com antecedência para os riscos que não puderam ser evitados ou totalmente mitigados.
* Define as ações a serem tomadas quando o risco se torna um problema.
* **Exemplo:** "Se o gerente de projetos sair inesperadamente da empresa durante o projeto, contratar um gerente de projetos substituto temporário de uma consultoria especializada."
O slide apresenta uma imagem ilustrativa de um plano de emergência.

---

## Documento (Sistema) de Monitoramento de Risco (Slide 22)

Este slide descreve os campos essenciais que um documento ou sistema de monitoramento de riscos deve conter para um acompanhamento eficaz:
* **ID:** Identificador único do risco.
* **Descrição:** Detalhes do risco.
* **Probabilidade:** Nível de probabilidade atual.
* **Impacto:** Nível de impacto atual.
* **Importância:** Prioridade do risco (e.g., calculada pela exposição).
* **Primeiro indicador:** Sinal de alerta de que o risco pode estar se concretizando.
* **Planos de mitigação e contingência:** Referência ou resumo dos planos.
* **Responsável:** Pessoa encarregada de monitorar e gerenciar o risco.
* **Prazo:** Datas relevantes para o monitoramento e ações.
* **Status:** Situação atual do risco (potencial, atual, em tratamento, resolvido).

---

## Top Ten Risk List (Boehm) (Slide 23)

Este slide apresenta a "Top Ten Risk List" de Barry Boehm, uma lista clássica dos dez principais riscos que frequentemente afetam projetos de software:
1.  Deficiências de pessoal.
2.  Cronogramas e orçamentos não realistas.
3.  Desenvolvimento de funcionalidades erradas.
4.  Desenvolvimento de interface de usuário errada.
5.  Gold plating (funcionalidades desnecessárias).
6.  Mudanças contínuas de requisitos.
7.  Deficiências em componentes externos.
8.  Deficiências em tarefas realizadas externamente.
9.  Problemas de desempenho em tempo real.
10. Estar abaixo das capacidades da tecnologia.

---

## Controle de Riscos (Slide 24)

Este slide detalha as atividades envolvidas no Controle de Riscos, que é o processo de implementar os planos de resposta e monitorar os resultados:
* Implementar planos de mitigação e de contingência.
* Corrigir desvios em relação aos planos.
* Identificar novos riscos que surgem durante o projeto.
* Reavaliar os riscos existentes (probabilidade, impacto).
* Comunicar o status dos riscos e das ações de controle.
* Garantir que os procedimentos de gerenciamento de riscos estão sendo seguidos.

---

## Comunicação de Riscos (Slide 25)

Este slide enfatiza a importância da Comunicação de Riscos:
* O gerenciamento de riscos não é responsabilidade apenas do gerente de projeto, mas de toda a equipe.
* É crucial comunicar os riscos identificados, suas análises e os planos de resposta a todas as partes interessadas relevantes.
* O slide faz a pergunta: "Quem é o principal responsável pela gestão de riscos em um projeto?" A resposta implícita e geralmente aceita é o Gerente de Projeto, embora a responsabilidade seja compartilhada.

---

## Referências (Slide 26)

Este slide lista as referências bibliográficas utilizadas como base para a aula de gerenciamento de riscos:
* Boehm, B. (Software Risk Management)
* Heldman, K. (Gerência de Projetos)
* Kerzner, H. (Gestão de Projetos – As Melhores Práticas)
* SEI - Software Engineering Institute
* Thomsett, R. (Radical Project Management)
* Wazlawick, R. S. (Engenharia de Software: Conceitos e Práticas)