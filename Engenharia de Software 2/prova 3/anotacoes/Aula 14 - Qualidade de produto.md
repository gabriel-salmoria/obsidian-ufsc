## Slide 5: Abordagem Conceitual para Qualidade

Este slide ilustra a cadeia de influências da qualidade, conforme a Figura 11.1 do livro. A ideia é que a **Qualidade do Processo** (as práticas de desenvolvimento) impacta as **Propriedades Internas** do software (características visíveis aos desenvolvedores, como a complexidade do código). Essas, por sua vez, influenciam as **Propriedades Externas** (características percebidas pelo usuário, como a confiabilidade). Finalmente, as propriedades externas determinam a **Qualidade em Uso**, que é o sucesso do software em ajudar o usuário a atingir seus objetivos no ambiente real.

---

## Slide 6: Tabela 11-2: Modelo de qualidade da ISO 25010:2011

Este slide apresenta a tabela completa do modelo de qualidade da ISO 25010. O modelo é uma ferramenta abrangente que detalha as oito características de qualidade do produto (como adequação funcional e usabilidade) e as cinco características de qualidade em uso (como efetividade e satisfação), subdividindo-as em características mais específicas. Ele serve como um guia para a especificação e avaliação da qualidade de um produto de software de forma sistemática.

---

## Slide 7: Adequação Funcional

A adequação funcional mede o grau em que o software fornece as funções que satisfazem as necessidades do usuário. Suas subcaracterísticas são:

* **Completude Funcional**: O software efetivamente possibilita executar todas as funções necessárias para que o usuário atinja seus objetivos? 
* **Corretude Funcional**: O software gera dados e consultas corretos e precisos, de acordo com sua definição? 
* **Funcionalidade Apropriada**: As funções do sistema realmente facilitam a realização das tarefas para as quais ele foi especificado? 

---

## Slide 8: Confiabilidade

A confiabilidade é a capacidade do software de manter um desempenho consistente ao longo do tempo, minimizando defeitos e operando adequadamente em situações anormais. As subcaracterísticas são:

* **Maturidade**: É a medida da frequência com que um software apresenta defeitos.
* **Disponibilidade**: Avalia o quanto o software está operacional e acessível para uso quando necessário.
* **Tolerância a Falhas**: Mede a capacidade do software de reagir e continuar funcionando em situações anormais, como falhas de hardware.
* **Recuperabilidade**: Refere-se à capacidade do software de recuperar dados e voltar a operar após um desastre.

---

## Slide 9: Usabilidade

A usabilidade avalia o grau em que um produto pode ser entendido, aprendido, usado e ser atraente para o usuário em condições específicas de uso. Suas subcaracterísticas incluem:

* **Apropriação Reconhecível**: Mede se os usuários conseguem reconhecer que o produto é apropriado para suas necessidades.
* **Inteligibilidade**: Refere-se à facilidade que o usuário tem para entender os conceitos do software e se tornar competente em seu uso.
* **Operabilidade**: Avalia o quão fácil é usar e controlar o produto.
* **Proteção contra Erro de Usuário**: Mede se o produto foi projetado para evitar que o usuário cometa erros.
* **Estética da Interface com Usuário**: Avalia se a interface proporciona uma interação satisfatória.
* **Acessibilidade**: Mede o grau em que o produto foi projetado para atender usuários com necessidades especiais.

---

## Slide 10: Eficiência de Desempenho

Esta característica trata da otimização do uso de recursos de tempo e espaço pelo software para realizar suas funções.

* **Comportamento em Relação ao Tempo**: Mede o tempo que o software leva para processar suas funções.
* **Utilização de Recursos**: Avalia o uso de recursos como armazenamento, memória e banda de transmissão de rede.
* **Capacidade**: Mede o grau em que os limites máximos do produto, como o número de transações simultâneas, atendem aos requisitos.

---

## Slide 11: Segurança

A segurança (*security*) avalia o grau em que as funções e os dados são protegidos contra acesso não autorizado. As subcaracterísticas são:

* **Confidencialidade**: Garante que as informações e funções sejam acessíveis apenas por quem tem a devida autorização.
* **Integridade**: Garante que os dados e o código do sistema sejam protegidos contra acesso e modificação por pessoas ou sistemas não autorizados.
* **Não Repúdio**: Permite constatar que ações ou acessos foram efetivamente feitos, de forma que não possam ser negados posteriormente.
* **Rastreabilidade de Uso**: Avalia se as ações realizadas podem ser rastreadas para comprovar quem as realizou.
* **Autenticidade**: Garante que a identidade de uma pessoa ou recurso é efetivamente aquela que se diz ser.

---

## Slide 12: Compatibilidade

A compatibilidade avalia o grau em que dois ou mais sistemas podem trocar informações e realizar suas funções enquanto compartilham o mesmo ambiente.

* **Coexistência**: Avalia a capacidade do produto de desempenhar suas funções eficientemente enquanto compartilha ambiente e recursos com outros produtos, sem causar impacto negativo.
* **Interoperabilidade**: Avalia a capacidade do software de interagir com outros sistemas com os quais se espera que ele interaja.

---

## Slide 13: Manutenibilidade

A manutenibilidade é uma característica interna que mede a facilidade de realizar alterações no software para evolução, correção de erros ou adaptação.

* **Modularidade**: Avalia se o sistema é subdividido em partes lógicas coesas, de forma que mudanças em uma parte tenham impacto mínimo nas outras.
* **Reusabilidade**: Avalia o grau em que partes do sistema podem ser usadas para construir outros sistemas.
* **Analisabilidade**: Um sistema é analisável quando permite encontrar defeitos (depurar) facilmente.
* **Modificabilidade**: Tem relação com a facilidade que o sistema oferece para que defeitos sejam corrigidos sem introduzir novos defeitos.
* **Testabilidade**: Mede a facilidade de realizar testes de regressão no software.

---

## Slide 14: Portabilidade

A portabilidade avalia o grau em que o software pode ser transferido de um ambiente (hardware ou software) para outro de forma eficaz e eficiente.

* **Adaptabilidade**: Mede o quão fácil é adaptar o software a outros ambientes sem que seja necessário aplicar ações além daquelas fornecidas com o próprio software.
* **Instalabilidade**: Avalia a facilidade de instalar o software.
* **Substituibilidade**: Avalia se o sistema pode substituir outro com os mesmos objetivos no mesmo ambiente.

---

## Slide 15: Qualidades do Software em Uso

Este slide introduz as características de qualidade do software em uso. Diferente das características de produto, estes são fatores externos que só podem ser plenamente avaliados quando o software está em seu ambiente de uso final, ou seja, em operação real. A avaliação em um ambiente de desenvolvimento é difícil ou impossível.

---

## Slide 16: Efetividade

A efetividade é uma qualidade de software em uso. Ela representa a capacidade que o produto de software tem para fazer com que o cliente atinja seus objetivos de negócio de forma correta e completa no ambiente real de uso. Em outras palavras, o software cumpre sua finalidade no contexto para o qual foi criado?

---

## Slide 17: Eficiência

A eficiência, como qualidade em uso, avalia o retorno que o produto dá ao cliente em relação ao que foi investido (seja em dinheiro, tempo ou outros recursos). Essa medida nem sempre é puramente financeira e busca responder se o investimento no sistema valeu a pena em termos de resultados obtidos.

---

## Slide 18: Satisfação

A satisfação é a capacidade do produto de satisfazer os usuários durante seu uso no ambiente final. Suas subcaracterísticas são:

* **Utilidade**: Avalia o grau em que o usuário fica satisfeito com a obtenção de metas pragmáticas, incluindo os resultados e consequências do uso.
* **Prazer**: Avalia o grau em que o usuário sente prazer em usar o sistema para satisfazer seus objetivos.
* **Conforto**: Avalia o conforto físico e mental do usuário ao usar o sistema.
* **Confiança**: Mede o grau em que o usuário ou outros interessados confiam que o sistema fará o que é esperado dele.

---

## Slide 19: Uso Sem Riscos

Esta característica de qualidade em uso representa a capacidade do produto de estar dentro de níveis aceitáveis de segurança relativa a riscos envolvendo pessoas, negócios e meio ambiente. Suas subcaracterísticas focam na mitigação de riscos específicos:

* **Mitigação de Risco Econômico**: Minimiza riscos financeiros potenciais, como danos à propriedade e à reputação.
* **Mitigação de Risco à Saúde e Segurança**: Minimiza riscos físicos às pessoas em seu contexto de uso.
* **Mitigação de Risco Ambiental**: Minimiza riscos ambientais ou à propriedade no seu contexto de uso.

---

## Slide 20: Cobertura de Contexto

A cobertura de contexto avalia o grau em que um produto ou sistema pode ser usado com efetividade, eficiência, sem riscos e com satisfação em diversos contextos.

* **Completude de Contexto**: Avalia se o sistema pode ser usado com qualidade em *todos* os contextos de uso especificados inicialmente.
* **Flexibilidade**: Avalia se o sistema pode ser usado com qualidade em contextos *diferentes* daqueles especificados inicialmente.

---

## Slide 21: Instalação de um Programa de Melhoria de Qualidade

Para que a gestão da qualidade seja eficaz, a organização deve ter um programa de melhoria de qualidade bem definido. Para que o programa funcione, é necessário:
* Que ele seja acordado e conhecido por todos, tornando-se parte da cultura da empresa.
* Que os planos sejam consistentes, factíveis e levados a sério, em vez de serem apenas documentos que são abandonados na primeira dificuldade.
* Que se estabeleça uma "anistia geral" no início, focando na melhoria conjunta sem buscar culpados por problemas passados.

---

## Slide 22: Gestão da Qualidade (Estágios)

Crosby (1979) define um modelo de maturidade organizacional em relação à qualidade com cinco estágios:

* **Desconhecimento**: A organização nem sabe que tem problemas com qualidade.
* **Despertar**: A organização reconhece os problemas, mas ainda vê a qualidade como um mal necessário e não como fonte de lucro.
* **Alinhamento**: A gestão da qualidade se torna uma ferramenta institucional e os problemas são resolvidos à medida que surgem.
* **Sabedoria**: A prevenção de problemas se torna rotina, e eles são identificados antes de surgirem.
* **Certeza**: A qualidade é uma constante e parte essencial do funcionamento da organização; quase todos os problemas são prevenidos.

---

## Slide 23: Papéis em uma Reunião Walkthrough

O **walkthrough** é uma forma de avaliação de produto que utiliza uma equipe de especialistas para analisar um artefato. Os papéis comuns na reunião são:
* **Apresentador**: Geralmente o autor do artefato, que o descreve e justifica suas decisões.
* **Coordenador**: O moderador da reunião, que mantém todos focados na tarefa.
* **Secretário**: Responsável por tomar nota das discussões e decisões.
* **Oráculo de Manutenção**: Garante que o código produzido seja compreensível e manutenível.
* **Guardião dos Padrões**: Verifica se o código está de acordo com os padrões da equipe.
* **Representante do Usuário**: Garante que o cliente receberá o produto que espera.
* **Outros Desenvolvedores**: Participam para contribuir com outros pontos de vista.

---

## Slide 24: Perfis Psicológicos em uma Reunião Walkthrough

Em uma reunião de walkthrough, o coordenador deve estar atento a diferentes perfis psicológicos para manter a produtividade:

* **Programadores Gênios**: São ótimos para detectar defeitos, mas podem ser arrogantes. Devem ser valorizados, mas o coordenador precisa controlar a discussão.
* **Pessoas Defensivas e Inseguras**: Podem se sentir pessoalmente atingidas pelas críticas. A discussão deve ser mantida sobre o produto, não sobre o desenvolvedor.
* **Conservadores**: Apegados a tradições, podem iniciar discussões improdutivas sobre modismos. Suas opiniões devem ser ouvidas, mas com moderação.
* **Alienados**: Interessam-se mais pelo processo do que pelo produto em si, podendo se tornar um incômodo.

---

## Slide 25: Papéis em uma Inspeção Fagan

A **Inspeção Fagan** é um processo mais estruturado e formal para encontrar defeitos. Os papéis típicos são:

* **Autor**: A pessoa (programador, designer, analista) que produziu o artefato a ser inspecionado.
* **Narrador**: Aquele que analisa, interpreta e sumariza o artefato e seus critérios de aceitação durante a reunião.
* **Revisores**: Aqueles que revisam o artefato com o objetivo de detectar eventuais defeitos.
* **Moderador**: O responsável pela sessão de inspeção e pelo andamento de todo o processo.

---

## Slide 26: Atividades de uma Inspeção Fagan

O processo de Inspeção Fagan é composto por um conjunto de atividades estruturadas:

* **Planejamento**: Inclui a preparação dos materiais (artefatos) e o convite aos participantes.
* **Visão Geral**: Uma instrução prévia aos participantes sobre os materiais a serem inspecionados.
* **Preparação**: Os participantes analisam os artefatos individualmente, anotando possíveis defeitos antes da reunião.
* **Reunião de Inspeção**: Momento em que os defeitos encontrados são discutidos em grupo e se decide o que fazer com eles.
* **Retrabalho**: Atividade em que o autor do artefato corrige os defeitos apontados na reunião.
* **Prosseguimento (Follow-up)**: O moderador verifica se todos os defeitos foram corrigidos para aprovar o produto para a próxima fase.

---

## Slide 27: Medição da Qualidade

A medição da qualidade busca quantificar características que são, por natureza, abstratas. A ideia é decompor uma característica de qualidade em partes menores até que seja possível definir um **procedimento operacional objetivo** para medi-la. Do ponto de vista da satisfação do usuário, a qualidade de um produto é o resultado de três fatores principais:

* **Funcionalidade**: Se as funções necessárias estão presentes ou ausentes.
* **Comportamento**: As qualidades não funcionais, que são normalmente mensuráveis (ex: tempo de resposta).
* **Restrições**: As regras que determinam como o usuário pode usar o produto.

---

## Slide 28: Requisitos de Qualidade

Os requisitos de qualidade devem fazer parte da especificação do produto, geralmente como requisitos suplementares ou não funcionais. É fundamental que esses requisitos sejam definidos de forma objetiva e, idealmente, acompanhados de uma métrica que permita verificar se foram atendidos.
* Um requisito subjetivo como "o software deve ser fácil de usar" é difícil de avaliar.
* Um requisito objetivo como "todas as janelas devem ter acesso a uma tela de ajuda pela tecla F1" pode ser inspecionado e validado.

---

## Slide 29: Escala MoSCoW

A escala **MoSCoW** é um padrão usado para classificar requisitos de qualidade (e outros) em diferentes graus de obrigatoriedade, já que qualidade também tem custo. Isso ajuda a priorizar o que é mais importante. As categorias são:

* **Must-have**: Requisitos essenciais para o produto.
* **Should-have**: Requisitos importantes, mas não vitais.
* **Could-have**: Requisitos desejáveis, que podem ser incluídos se houver tempo e recursos.
* **Won't-have / Would-have**: Requisitos que serão deixados de fora da versão atual, mas podem ser considerados no futuro.

---

## Slide 30: Custo da Qualidade

Este slide ilustra a relação entre o investimento em qualidade e a economia relacionada a falhas. O custo total da qualidade é a soma de dois componentes:
* **Custos de Prevenção e Detecção**: O investimento feito para evitar e encontrar defeitos (ex: inspeções, testes).
* **Custos de Falhas**: Os custos gerados por defeitos que não foram prevenidos ou detectados (ex: retrabalho, suporte ao cliente).

Existe um ponto ótimo de investimento em qualidade que minimiza o custo total, equilibrando os dois tipos de custo.

---

## Slide 31: GQM (Goal/Question/Metric) e Avaliação da Qualidade

O **GQM (Goal/Question/Metric)** é uma abordagem para avaliação da qualidade de software que define um modelo de mensuração em três níveis:

* **Nível Conceitual (Goal/Objetivo)**: Define um objetivo para um objeto (produto, processo) com respeito a um modelo de qualidade e um ponto de vista.
* **Nível Operacional (Question/Questão)**: Um conjunto de questões é usado para definir e focar no objeto de estudo.
* **Nível Quantitativo (Metric/Métrica)**: Um conjunto de dados é associado a cada questão para respondê-la de forma quantitativa.

A definição do processo é feita de forma *top-down* (do objetivo para as métricas), e a interpretação é *bottom-up* (das métricas para os objetivos).

---

## Slide 32: Associação de Riscos e Características de Qualidade (Exemplo GQM)

Este slide ilustra a primeira etapa de uma aplicação prática do GQM. Neste estudo de caso, os autores primeiro identificam os riscos importantes do sistema (como "Indisponibilidade do sistema" ou "Interceptação de informações"). Em seguida, associam cada risco a uma ou mais características e subcaracterísticas de qualidade do modelo de referência, que no exemplo era a norma ISO/IEC 9126 (predecessora da 25010).

---

## Slide 33: Detalhamento do GQM (Exemplo GQM)

Este slide demonstra a aplicação completa do modelo GQM para um risco específico: "R001 - Indisponibilidade do sistema para o usuário".
* **O Objetivo (Goal)** é estabelecido: "Avaliar a disponibilidade do sistema do ponto de vista do usuário".
* **As Questões (Questions)** são definidas para detalhar o objetivo: "Quão disponível é o sistema para uso durante um período específico?" ou "Qual é o tempo médio que o sistema leva para completar a recuperação?".
* **As Métricas (Metrics)** são propostas para responder quantitativamente a cada questão, como "Tempo de operação / (Tempo de operação + Tempo de reparo)" ou "Soma de todos os tempos de recuperação / número total de casos".
Isso mostra como o GQM transforma um conceito abstrato (risco de indisponibilidade) em medições concretas.