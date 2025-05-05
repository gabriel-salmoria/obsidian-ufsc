## Aula 9 - Estimação de Esforço I: APF e PH

---

### Slide 1: Título
Esta aula trata da Estimação de Esforço no contexto da Engenharia de Software, apresentando duas metodologias proeminentes: a Análise de Pontos de Função (APF) e os Pontos de História (PH). A estimação precisa do esforço de desenvolvimento é crucial para o planejamento de projetos, influenciando diretamente o cronograma, o custo e a alocação de recursos. É uma atividade fundamental para garantir a viabilidade e o sucesso de um projeto de software.

---

### Slide 2: Conteúdo
Nosso foco principal nesta sessão será aprofundar a compreensão de duas técnicas de estimação. Primeiramente, exploraremos a Análise de Pontos de Função, uma técnica amplamente utilizada e padronizada. Em seguida, abordaremos a técnica de Pontos de História, que ganhou popularidade, especialmente em ambientes de desenvolvimento ágil. Ambas as técnicas oferecem abordagens distintas para quantificar o trabalho, e entender seus fundamentos e aplicações é essencial para estimativas mais acuradas.

---

### Slide 3: Tipos de Estimação de Esforço
Existem diversas abordagens para estimar o esforço em projetos de software. Podemos classificá-las, de forma geral, em Técnicas Paramétricas e Técnicas Não Paramétricas.
* **Técnicas Paramétricas:** Baseiam a estimação em um ou mais parâmetros mensuráveis do software ou do projeto, como tamanho (linhas de código, pontos de função), complexidade, ou características da equipe. APF e modelos baseados em linhas de código (como COCOMO) são exemplos.
* **Técnicas Não Paramétricas:** Dependem mais do julgamento, da experiência e da intuição de especialistas ou da equipe, sem a necessidade de parâmetros objetivos rigorosos. A estimação por especialista é um exemplo puro, enquanto Pontos de História combina elementos de comparação relativa com o julgamento da equipe.

---

### Slide 4: Análise de Pontos de Função
A Análise de Pontos de Função (APF) é uma técnica paramétrica consolidada, utilizada para medir o tamanho funcional de um sistema de software. Essa medida de tamanho é independente da tecnologia de implementação e é usada como base para estimar o esforço, custo e cronograma.
* **Propósitos da Contagem de APF:**
    * **Contagem para desenvolvimento de projeto:** Estimar o esforço para criar um novo sistema.
    * **Contagem para melhoria de projeto:** Estimar o esforço para atividades de manutenção evolutiva (adição, alteração, exclusão de funcionalidades).
    * **Contagem de aplicação:** Medir o tamanho funcional de um sistema existente, útil para benchmarking ou comparação.

---

### Slide 5: Natureza de Funções (APF)
A APF classifica as funcionalidades visíveis para o usuário em dois tipos principais: Funções de Dados e Funções Transacionais. A correta identificação e classificação dessas funções a partir dos requisitos é o primeiro passo para a contagem.
* **Funções de Dados:** Representam a informação que o sistema gerencia ou utiliza.
    * **Arquivos Lógicos Internos (ALI):** Grupos de dados mantidos pela aplicação.
    * **Arquivos de Interface Externas (AIE):** Grupos de dados utilizados pela aplicação, mas mantidos por outros sistemas.
* **Funções Transacionais:** Representam processos elementares que interagem com as Funções de Dados.
    * **Entradas Externas (EE):** Processam informações que entram no sistema e alteram o estado dos dados.
    * **Consultas Externas (CE):** Recuperam e apresentam informações ao usuário sem realizar cálculos significativos.
    * **Saídas Externas (SE):** Recuperam e apresentam informações ao usuário, incluindo pelo menos um dado derivado ou calculado.

---

### Slide 6: Complexidade de Funções Transacionais (APF)
A complexidade de cada Função Transacional (EE, CE, SE) é determinada por dois fatores: o número de Arquivos Lógicos (AL) que ela acessa e o número de Tipos de Dados Elementares (TDE) que ela processa.
* **Arquivos Lógicos (AL):** Refere-se aos arquivos lógicos (ALI ou AIE) envolvidos na transação.
* **Tipos de Dados Elementares (TDE):** São os campos ou atributos individuais que são inseridos, atualizados, excluídos, consultados ou apresentados pela transação.

---

### Slide 7: Complexidade Funcional de Entradas Externas (EE) (APF)
A complexidade (Baixa, Média, Alta) de uma Entrada Externa é determinada consultando uma tabela que cruza o número de Tipos de Dados Elementares (#TDE) com o número de Arquivos Lógicos (#AL) acessados. Por exemplo:
* Baixa Complexidade: Poucos TDEs e poucos ALs.
* Alta Complexidade: Muitos TDEs ou muitos ALs (ou ambos).

---

### Slide 8: Complexidade Funcional de Saídas Externas (SE) e Consultas Externas (CE) (APF)
Similarmente, a complexidade (Baixa, Média, Alta) de uma Saída Externa ou Consulta Externa é determinada por uma tabela específica que cruza o número de Tipos de Dados Elementares (#TDE) apresentados com o número de Arquivos Lógicos (#AL) consultados. As faixas de valores para #TDE e #AL nesta tabela são ajustadas para o perfil dessas funções.

---

### Slide 9: Complexidade de Funções de Dados (APF)
A complexidade dos Arquivos Lógicos Internos (ALI) e Arquivos de Interface Externas (AIE) é avaliada com base em dois parâmetros internos a eles: o número de Registros Lógicos (RL) e o número de Tipos de Dados Elementares (TDE).
* **Registros Lógicos (RL):** Representam subconjuntos de dados reconhecíveis pelo usuário dentro de um ALI ou AIE.
* **Tipos de Dados Elementares (TDE):** São os campos ou atributos contidos nesses Registros Lógicos.

---

### Slide 10: Complexidade Funcional de Arquivos Lógicos Internos (ALI) e Arquivos de Interface Externa (AIE) (APF)
A complexidade (Baixa, Média, Alta) de um ALI ou AIE é definida pela interseção do número de Tipos de Dados Elementares (#TDE) e o número de Registros Lógicos (#RL) contidos nesse arquivo, utilizando uma tabela específica para Funções de Dados.

---

### Slide 11: Pontos de Função Não Ajustados por Tipo e Complexidade de Função (APF)
Após determinar a complexidade de cada função individual (dados ou transacional), uma tabela padrão da APF atribui um valor numérico de pontos de função não ajustados (UFP) a cada uma, com base no seu tipo e nível de complexidade (Baixa, Média, Alta). A soma desses pontos de todas as funções do sistema fornece o UFP total do projeto.

---

### Slide 12: Exemplo (APF)
A aplicação prática da APF envolve analisar os requisitos para identificar as Funções de Dados e Transacionais. Por exemplo, um requisito para "gerenciar clientes" geralmente implica um Arquivo Lógico Interno (Clientes) e várias Entradas Externas (incluir, alterar, excluir cliente), Consultas Externas (consultar cliente) e Saídas Externas (relatório de clientes). O exemplo fornecido ilustra como analisar requisitos específicos, como gerenciamento de livros e usuários, registro de empréstimos e impressão de recibo, para identificar e classificar as funções correspondentes, quebrando requisitos complexos em funções elementares contáveis.

---

### Slide 13: (Imagem/Transição)
Este slide serve como um divisor visual na apresentação, possivelmente indicando uma transição para a próxima etapa ou tópico relacionado à estimação de esforço.

---

### Slide 14: Tipos de Contagem (APF)
A APF permite diferentes níveis de profundidade na contagem, adequados a diferentes estágios do projeto ou disponibilidade de informação:
* **Contagem Detalhada:** A mais precisa, requer identificação e classificação completa de todas as funções e suas complexidades.
* **Contagem Indicativa:** Realizada em fases iniciais com menos informação, baseada no modelo conceitual e pressupondo um número médio de transações por arquivo lógico. Oferece uma ordem de magnitude.
* **Contagem Estimada:** Utilizada quando se conhece a lista de funções, mas não a complexidade detalhada. Assume complexidade média para funções transacionais e baixa para funções de dados.

---

### Slide 15: Pontos de Função Ajustados (APF)
Para obter uma estimativa mais refinada, o UFP (Pontos de Função Não Ajustados) é ajustado por 14 fatores técnicos, conhecidos como General Systems Characteristics (GSC). Esses fatores avaliam a influência de aspectos técnicos e operacionais do projeto (como performance, reusabilidade, complexidade do processamento, etc.). Cada GSC é pontuado de 0 a 5, e a soma dessas pontuações determina o Grau Total de Influência (TDI). O AFP (Pontos de Função Ajustados) é calculado multiplicando o UFP pelo TDI (AFP = UPF × TDI). Este ajuste visa refletir o esforço adicional ou reduzido que as características do ambiente e do projeto podem impor.

---

### Slide 16: Esforço Total (APF)
O Esforço Total do projeto é estimado multiplicando-se os Pontos de Função Ajustados (AFP) pelo Índice de Produtividade (IP) da equipe ou organização (Esforço = AFP × IP). O IP é uma medida empírica da capacidade da equipe de entregar pontos de função por unidade de tempo (por exemplo, horas por ponto de função). Ele varia significativamente entre diferentes equipes, tecnologias e domínios de aplicação, e deve ser calibrado com dados históricos da própria organização para maior precisão.

---

### Slide 17: Custo (APF)
A estimativa de Custo do projeto é obtida multiplicando o Esforço Total (expresso em unidades de tempo, como horas ou meses) pelo custo médio da unidade de tempo (Custo = Esforço × Custo Unitário de Tempo). O custo unitário deve incluir todos os gastos associados ao trabalho, como salários, encargos, infraestrutura e ferramentas.

---

### Slide 18: Duração Ideal e Mínima (APF)
A partir do esforço total estimado, é possível calcular a Duração Ideal do projeto, que representa o tempo ótimo para sua conclusão considerando uma equipe de tamanho apropriado. Modelos de estimação frequentemente fornecem fórmulas empíricas para relacionar esforço e duração. Além da duração ideal, pode-se estimar uma Duração Mínima, o prazo mais curto possível, embora prazos muito apertados geralmente resultem em aumento do esforço total e dos riscos.

---

### Slide 19: Tamanho Médio da Equipe (APF)
O Tamanho Médio da Equipe necessário para o projeto pode ser estimado dividindo-se o Esforço Total pela Duração estimada (ideal ou mínima) (Tamanho da Equipe = Esforço Total / Duração). Este cálculo fornece uma média da quantidade de pessoas que seriam necessárias para concluir o projeto no prazo estimado, assumindo dedicação integral.

---

### Slide 20: Pontos de Histórias (PH)
Pontos de História (Story Points) são uma técnica de estimação de esforço amplamente utilizada em metodologias ágeis, como Scrum. Diferentemente da APF, que busca uma medida de tamanho funcional objetiva, Pontos de História representam uma medida de esforço *relativa* e consensual da equipe para completar uma História de Usuário. O valor atribuído reflete a percepção da equipe sobre a Complexidade, o Esforço e o Risco da história em comparação com outras histórias já estimadas.

---

### Slide 21: Escala Camiseta (PH)
Uma maneira de simplificar a atribuição de Pontos de História é usar escalas não numéricas, como a "Escala Camiseta" (Pequeno, Médio, Grande, Extra Grande). Essa abordagem evita discussões excessivas sobre valores numéricos precisos e foca na comparação relativa entre as histórias, facilitando o processo de estimação inicial, especialmente para equipes menos experientes. Outras escalas comuns incluem a sequência de Fibonacci (1, 2, 3, 5, 8, ...).

---

### Slide 22: Critérios Subjetivos (PH)
A estimação em Pontos de História é inerentemente subjetiva e baseada na discussão e consenso da equipe. Os critérios que influenciam a atribuição de pontos geralmente incluem:
* **Complexidade:** A dificuldade intrínseca da história, que pode envolver algoritmos complexos, novas tecnologias, etc.
* **Esforço:** A quantidade total de trabalho necessária, incluindo desenvolvimento, testes, documentação, coordenação, etc.
* **Risco:** Incidência de incertezas, dependências externas, ou áreas desconhecidas que podem impactar o trabalho.

---

### Slide 23: Medição de Velocidade (PH)
Pontos de História são fundamentais para a medição da Velocidade da equipe em metodologias ágeis. A velocidade é a soma dos Pontos de História das histórias de usuário concluídas por uma equipe em uma iteração (sprint). O acompanhamento da velocidade ao longo do tempo permite que a equipe:
* Planeje as próximas iterações com mais precisão, sabendo quanto trabalho (em PH) é capaz de realizar.
* Monitore o progresso do projeto em relação ao escopo total.
* Identifique variações na produtividade, o que pode indicar problemas a serem investigados ou sucesso na implementação de melhorias de processo.