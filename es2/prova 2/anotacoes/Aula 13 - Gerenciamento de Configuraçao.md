### Slide 1: Gerenciamento de Configuração e Mudança
Este capítulo aborda o gerenciamento de configuração e mudança, iniciando com os conceitos básicos, como itens de configuração, versões, *baselines* e *releases*. A disciplina de gerenciamento de configuração de *software* (GCS) ou gerenciamento de configuração e mudança (GCM) é crucial na indústria de *software*, pois os componentes e produtos são frequentemente desenvolvidos e modificados ao longo do tempo, exigindo a disponibilidade de diferentes versões. O objetivo do gerenciamento de configuração é indicar como as diferentes versões dos artefatos devem ser modificadas e identificadas.

---

### Slide 2: Conteúdo
Este slide apresenta o conteúdo que será abordado na aula sobre Gerenciamento de Configuração e Mudança. Os principais tópicos incluem:
* **Conceitos Básicos**: Introdução aos termos e fundamentos da área.
* **Controle de Versão**: Discussão sobre como as diferentes versões dos artefatos de *software* são gerenciadas.
* **Controle de Mudança**: Explicação dos processos para gerenciar as alterações nos itens de configuração.
* **Auditoria**: Detalhamento das atividades de verificação e conformidade das configurações.
* **Ferramenta**: Apresentação de ferramentas que auxiliam no gerenciamento de configuração e mudança.
O conteúdo é baseado na obra "Engenharia de Software: Conceitos e Práticas, 2ª edição", de Wazlawick, R. S., publicada pela Elsevier em 2019.

---

### Slide 3: Gerenciamento de Configuração de Software (GCS) ou Gerenciamento de Configuração e Mudança (GCM)
O Gerenciamento de Configuração de *Software* (GCS) ou Gerenciamento de Configuração e Mudança (GCM) é uma disciplina fundamental dentro do gerenciamento de projetos. Sua importância é acentuada na indústria de *software*, onde componentes e produtos são frequentemente alterados durante e após o projeto. Isso demanda que diferentes versões de um mesmo componente ou produto estejam disponíveis em momentos distintos. O GCS/GCM, portanto, estabelece como as múltiplas versões dos artefatos de desenvolvimento de *software* devem ser modificadas e identificadas. A imagem ilustra a ideia de organização e rastreamento de diferentes documentos ou versões, remetendo à natureza do gerenciamento de configuração. Este conteúdo também é referenciado na obra "Engenharia de Software: Conceitos e Práticas, 2ª edição", de Wazlawick, R. S., Elsevier, 2019.

---

### Slide 4: Item de Configuração de Software
Um Item de Configuração de *Software* (ICS) é a unidade básica para controle de versão, ou um conjunto de elementos tratados como uma entidade única no sistema de gerenciamento de configuração. Não apenas o código de programação é um ICS, mas também a documentação, diagramas, planos, ferramentas, casos de teste e outros artefatos relacionados ao desenvolvimento do *software*. Cada ICS geralmente recebe um número, que pode ser composto por várias partes (ex: 1.2.4 para Disco de instalação do sistema, versão 1.2.4).

A granularidade dos ICS é um desafio: muitos itens podem dificultar o controle, resultando em listas extensas de configurações. Poucos itens, por outro lado, levam a um grande número de versões para cada um. Em sistemas orientados a objetos, um ICS geralmente corresponde a um pacote ou componente de classes afins, com dezenas de classes no máximo, embora isso possa variar com o tamanho do projeto.

---

### Slide 5: Elementos Definidores de um ICS
Todo Item de Configuração de *Software* (ICS) é definido por quatro elementos essenciais:
* **Nome**: Uma sequência curta de caracteres que identifica de forma única o item, seja ele básico ou composto.
* **Descrição**: Detalha o tipo do item (documento, diagrama, dados, código fonte, etc.) e fornece informações adicionais sobre ele.
* **Lista de Recursos**: Inclui outros itens de configuração que são requeridos pelo ICS em questão. No caso de itens compostos, essa lista pode ser a união das listas de seus itens básicos.
* **Realização**: Para um item básico, é um ponteiro ou endereço para o artefato que de fato implementa o item. Para itens compostos, a realização é o conjunto das realizações de seus itens básicos.

Os ICS podem ser classificados como básicos (individuais e indivisíveis para controle de versão) ou compostos (formados por outros itens básicos e/ou compostos). A imagem no slide visualmente representa esses elementos, com cada um como um ponto de interrogação a ser preenchido para definir um ICS.

---

### Slide 6: Relacionamentos entre ICS
Itens de Configuração de *Software* (ICS) podem ter diversos tipos de relacionamentos entre si, muitos dos quais são gerenciados por ferramentas CASE e representados em diagramas UML. Alguns exemplos importantes de relacionamentos incluem:
* **Dependência**: Indica que um componente utiliza funções implementadas em outro. Associações na UML podem representar essa dependência, onde uma classe usa funções de outra.
* **Agregação e Composição**: Mostram que um componente é formado por outros componentes.
* **Realização**: Aponta que um componente concreto é a implementação de um componente mais abstrato.
* **Especialização**: Indica que um componente é uma variante mais específica de outro. Geralmente, o componente especializado depende do genérico. A dependência mútua ocorre se o genérico tem métodos abstratos que devem ser implementados no especializado.
A relação de dependência é especialmente crítica, pois determina quais testes de integração são necessários ao atualizar os ICS. O slide visualiza esses relacionamentos com setas e caixas, representando diferentes tipos de conexão entre os itens.

---

### Slide 7: Rastreabilidade
Rastreabilidade, ou controle de rastros, é um princípio da Engenharia de *Software* que ainda apresenta desafios significativos em sua implementação. Embora o controle de rastros entre módulos de código seja mais simples, devido às indicações sintáticas das linguagens de programação (ex: `import` ou `uses`), mantê-lo entre artefatos de análise e *design* é mais complexo.

A rastreabilidade é vital para manter a consistência entre artefatos (análise, *design*, código) quando alterações são feitas, evitando que a documentação se torne rapidamente desatualizada e inútil. A técnica mais comum em ferramentas CASE é a matriz de rastreabilidade, que associa elementos como casos de uso a diagramas de sequência, ou classes a módulos de programa. No entanto, essa visualização matricial se torna impraticável com o aumento de elementos, especialmente se o controle for manual.

Pesquisas buscam automatizar a recuperação de relações de rastreabilidade a partir de evidências sintáticas, mas a arbitrariedade na nomeação dos artefatos frequentemente resulta em muitos falsos positivos, o que inviabiliza seu uso prático. Uma abordagem experimental propõe que, ao criar elementos em editores de diagramas, com exceção dos requisitos externos, todos os outros elementos sejam criados como derivação de algo já existente. Dessa forma, um rastro é automaticamente criado entre o item novo e sua origem. Apenas requisitos, que vêm do cliente, podem ser adicionados sem essa derivação. No geral, porém, cabe à equipe de desenvolvimento definir e executar uma política de registro de artefatos no sistema de gerenciamento de versões para manter as dependências documentadas e atualizadas. O slide apresenta uma imagem que remete à ideia de seguir um rastro ou conexão entre elementos.

---

### Slide 8: Versões de ICS
A versão de um Item de Configuração de *Software* (ICS) representa um estado específico desse item ao longo do desenvolvimento de um sistema. Geralmente, uma versão é identificada por um número, que pode ter uma, duas ou três partes.

Existem basicamente dois tipos de sucessores para uma versão:
* **Revisão**: Uma nova versão de um item criada para substituir uma versão anterior.
* **Variante**: Uma nova versão do item adicionada à configuração sem a intenção de substituir a versão antiga.

Também podem existir versões experimentais, onde uma revisão é feita, mas ainda não há decisão sobre sua manutenção definitiva. Nesse caso, a revisão pode ser vista como uma variante, já que a versão anterior não é automaticamente obsoleta.

---

### Slide 9: Configuração de Software
Uma configuração de *software* refere-se ao estado do *software* em um determinado momento. Embora possa incluir todos os elementos físicos ou abstratos relacionados ao produto, normalmente se limita aos artefatos mantidos em formato eletrônico, como programas, documentos eletrônicos, ferramentas CASE, sistema operacional e bibliotecas de suporte.

A configuração de *software* é definida como uma lista dos Itens de Configuração de *Software* (ICS) que compõem o *software* e suas respectivas versões. É fundamental que cada uma dessas versões seja armazenada de forma que possa ser recuperada sempre que for necessário reproduzir uma determinada configuração do *software*. A imagem no slide ilustra uma lista numerada, que pode representar os diversos ICS e suas versões que compõem uma configuração de *software*.

---

### Slide 10: Baseline
Uma *baseline* é uma configuração de *software* criada especificamente para uma situação particular. Ela é formalmente aprovada em um ponto específico do ciclo de vida do *software* e serve como referência para desenvolvimentos futuros.

Uma *baseline* só pode ser modificada por meio de um processo formal de mudança. Juntamente com todas as alterações aprovadas para ela, a *baseline* representa a configuração aprovada atualmente. Exemplos de *baselines* incluem:
* Um projeto aprovado para execução e formalizado por um contrato.
* Um conjunto de requisitos e interfaces aprovados pelo cliente para desenvolvimento.
* Uma versão do sistema entregue ao cliente e aprovada nos testes de aceitação.

A ideia central da *baseline* é que ela é uma versão acordada e aprovada pelas partes interessadas. Novas versões geradas a partir dela não têm automaticamente o mesmo *status* de versão acordada. Contudo, é comum que, durante o desenvolvimento, sucessivas versões sejam geradas até que um processo formal de homologação transforme uma delas em uma nova *baseline*. A imagem no slide, com o início da constituição dos EUA, simboliza um documento fundamental e aprovado, representando a ideia de uma *baseline* como um ponto de referência formal e inalterável sem um processo específico.

---

### Slide 11: Release
Uma *release*, ou entrega, é a distribuição de uma versão do *software* (ou de um Item de Configuração de *Software* - ICS) para fora do ambiente de desenvolvimento. A principal vantagem de utilizar sistemas de controle de versão é a capacidade de gerar *releases* atuais ou anteriores a qualquer momento, utilizando as *baselines* e as mudanças que foram armazenadas. A imagem de uma pomba branca alçando voo pode simbolizar a "liberação" ou "entrega" do *software*, que é o significado de *release*.

---

### Slide 12: Controle de Versão
A ausência de controle de versão pode gerar problemas significativos em projetos de *software*. As questões apresentadas no slide indicam a necessidade desse controle:
* Perda de versões anteriores de arquivos de projeto.
* Dificuldade em manter duas versões diferentes do sistema operando simultaneamente.
* Modificações indevidas em código-fonte, com perda do original.
* Dificuldade em identificar quem fez o quê em um projeto.

O controle de versão é essencial para rastrear todos os artefatos do projeto (itens de configuração) e gerenciar o trabalho paralelo de vários desenvolvedores, oferecendo as seguintes funcionalidades:
* Manter e disponibilizar todas as versões produzidas de cada Item de Configuração de *Software* (ICS).
* Permitir o desenvolvimento paralelo de diferentes variantes de um mesmo item (ramificações).
* Estabelecer uma política de sincronização de mudanças para evitar retrabalho e perda de trabalho.
* Fornecer um histórico detalhado das mudanças para cada item de configuração.

Com o controle de versão, é possível desfazer alterações ("*undo*") e retornar a uma versão anterior de um artefato, seja código, diagrama ou texto. Isso é fundamental em projetos de desenvolvimento de *software*. Cada versão gravada no sistema de gerenciamento de versões é *read-only* (somente leitura), ou seja, não pode ser alterada diretamente, mas uma nova versão pode ser criada a partir de uma cópia modificada. Além dos itens de configuração, os relacionamentos entre eles também devem ser controlados.

---

### Slide 13: Compatibilidade entre ICS
A compatibilidade entre Itens de Configuração de *Software* (ICS) é um aspecto crucial no gerenciamento de versões, especialmente quando há atualizações. Se uma classe X na versão 1.0 depende de métodos da classe Y na versão 1.5, uma atualização da classe Y para a versão 1.6 pode resultar em incompatibilidade com a classe X na versão 1.0.

Apenas após a integração entre Y 1.6 e X 1.0 ser testada e aprovada é que a nova dependência poderá ser validada. Até que isso ocorra, a classe X 1.0 continuará a depender de Y 1.5, e o sistema de versões deve indicar que Y 1.5 está desatualizada e que uma nova integração é necessária. A imagem no slide ilustra essa situação de dependência e a possível quebra de compatibilidade com uma nova versão.

---

### Slide 14: Repositório
Todos os arquivos que correspondem às realizações dos itens de configuração são armazenados em um local centralizado conhecido como repositório, sob a gestão do sistema de controle de versão. O repositório funciona como um banco de dados que mantém e identifica automaticamente as diversas versões de cada item.

Um sistema de controle de versões eficiente deve otimizar o espaço de armazenamento no repositório. Geralmente, ele armazena apenas o artefato original e, a partir daí, registra somente as modificações, evitando a necessidade de armazenar cópias completas de cada nova versão. Dessa forma, qualquer versão pode ser reproduzida aplicando-se sequencialmente as modificações sobre a versão original. Para agilizar o acesso, a última versão, por ser a mais utilizada, pode ser mantida em *cache* como uma cópia completa. Quando essa versão deixa de ser a mais recente, a cópia em *cache* é descartada, restando no repositório apenas as modificações necessárias para gerá-la e a cópia da nova versão atual. A imagem no slide representa um local de armazenamento organizado, que pode ser associado à ideia de um repositório.

---

### Slide 15: Políticas de Compartilhamento de Itens
Os desenvolvedores não trabalham diretamente nos itens armazenados no repositório, mas sim em cópias desses itens. Ao finalizar as alterações, eles salvam uma nova versão do item no repositório. Quando múltiplos desenvolvedores trabalham no mesmo item, o sistema deve adotar uma política para gerenciar a concorrência. Existem duas políticas usuais para o compartilhamento de itens:

* **Trava-modifica-destrava (*exclusive lock*)**: Um desenvolvedor que copia um item para modificação o trava no repositório, impedindo que outros desenvolvedores o alterem até que a nova versão seja salva. A vantagem é evitar colisões, onde as alterações de um desenvolvedor são perdidas ao serem sobrescritas por outro. No entanto, a desvantagem é que desenvolvedores podem ter que esperar, mesmo se pudessem trabalhar em partes distintas do item, especialmente quando os ICS são grandes.
* **Copia-modifica-resolve (*optimistic merges*)**: Múltiplos desenvolvedores podem trabalhar simultaneamente no mesmo ICS. Ao salvar a nova versão, possíveis interferências são resolvidas. Conflitos são raros e geralmente resolvidos automaticamente pelo sistema de controle de versões, ou exigem que os desenvolvedores decidam como tratar as alterações na mesma parte do artefato.

No modelo *copia-modifica-resolve*, se o desenvolvedor A salva uma nova versão (ex: 1.2) enquanto o desenvolvedor B também está trabalhando em uma cópia da versão anterior (1.1), o sistema avisa a B que sua versão está desatualizada. O desenvolvedor B deve então mesclar (merge) sua cópia com a versão 1.2, avaliando as alterações de A e resolvendo conflitos se ocorrerem nas mesmas linhas. Ao final, o desenvolvedor B salva a versão 1.3.

---

### Slide 16: Envio de Versões (Commit)
O envio de versões, também conhecido como *commit*, é geralmente realizado a critério do desenvolvedor. No entanto, é fundamental que uma nova versão de qualquer artefato seja enviada ao repositório somente se estiver minimamente estável, ou seja, razoavelmente livre de defeitos e revisada conforme os padrões de escrita.

Para artefatos de código, essa estabilidade pode ser garantida pela execução de testes de unidade, que devem inclusive acompanhar o código como parte do Item de Configuração de *Software* (ICS). Esses mesmos testes de unidade podem ser utilizados para compor os testes de integração quando aplicados a uma *build* do sistema, em vez de um item isolado. A imagem no slide de um caminhão transportando uma caixa pode representar a ideia de "enviar" ou "comprometer" as mudanças para o repositório.

---

### Slide 17: Controle de Mudança
O controle de mudança, ou gerência de solicitações de mudança, é um componente vital do gerenciamento de configuração. Ele permite compreender a razão pela qual uma versão de um Item de Configuração de *Software* (ICS) foi sucedida por outra. Enquanto um sistema de controle de versões pode identificar quais linhas foram alteradas em um artefato, ele não informa o motivo dessas alterações. O controle de mudança, portanto, mantém um histórico dos motivos que levaram a cada alteração nos artefatos, como a correção de um defeito no código.

Um sistema de controle de mudança de *software* tipicamente registra:
* **Mudanças de uma versão para outra**: Detalha quais funcionalidades foram adicionadas, removidas ou modificadas, e quais defeitos foram corrigidos. Por exemplo, de uma versão 2.2 para 2.3, podem ter ocorrido correções de defeitos (D345, D346), adição de funcionalidades (requisito R43) e melhorias de usabilidade (interface I12).
* **Pendências para versões futuras**: Lista os itens que ainda precisam ser resolvidos ou implementados. Exemplos incluem defeito D347 e melhoria de usabilidade da interface I13.

As modificações podem ser tanto aquelas planejadas no desenvolvimento (adição de funcionalidades de requisitos ou casos de uso) quanto mudanças solicitadas pelo usuário, ou características não incorporadas por falta de tempo. Na fase de produção (*evolução e manutenção*), o gerenciamento de mudança controla as atividades de manutenção corretiva, adaptativa e perfectiva.

Embora o sistema gerenciador de versões possa comparar artefatos e indicar as alterações sintáticas, a descrição da motivação da mudança precisa ser adicionada. Se a ferramenta de gerenciamento de mudança estiver integrada à ferramenta de distribuição de tarefas, essas descrições podem ser obtidas quase automaticamente da descrição da tarefa.

---

### Slide 18: Auditoria
A auditoria de configuração é uma atividade cujo propósito é verificar se os itens de configuração presentes em uma versão ou *baseline* estão corretos e se todos os itens necessários estão de fato no repositório. Além disso, a auditoria pode ser utilizada para garantir a consistência entre a documentação fornecida ao usuário e a configuração de sistema entregue.

Os passos para executar uma auditoria de configuração incluem:
* Preparar um relatório listando cada item a ser verificado na *baseline* e o procedimento de teste correspondente.
* Executar os testes e registrar os itens que foram aprovados.
* Se algum item não passar no teste, documentar a falha no relatório de descobertas da auditoria e encaminhá-lo ao setor responsável para as devidas providências.

Auditorias de versões antigas de um produto também podem ser necessárias, por exemplo, se um usuário alegar problemas e demandar indenização. A capacidade de gerar essa versão anterior para análise permite identificar ou refutar a causa real do problema. A imagem no slide de uma pessoa olhando através de uma lupa simboliza o processo de exame detalhado e verificação inerente à auditoria.

---

### Slide 19: Ferramenta para Controle de Versão
Atualmente, o controle de versões em projetos de *software* não é mais realizado manualmente, utilizando diretórios e padrões de nomeação de arquivos. Essa abordagem manual é ineficaz para obter relatórios de versões ou para o desenvolvimento de variantes, além de consumir muito espaço de armazenamento, pois cada versão é guardada integralmente.

O mais recomendado para empresas de desenvolvimento de *software* é o uso de um sistema automatizado de controle de versões. Atualmente (2018), a ferramenta mais amplamente utilizada para esse fim é o Git. O Git é um projeto de código aberto, originalmente desenvolvido por Linus Torvalds a partir de 2005.

O Git é considerado uma ferramenta de controle de versões distribuída. Diferente de outros sistemas que possuem apenas um repositório centralizado, o Git garante que cada desenvolvedor trabalhando em um repositório tenha uma cópia completa dele. A ferramenta permite o trabalho simultâneo em várias ramificações (*branch*) de um projeto. Por exemplo, um analista pode estar desenvolvendo a versão 2.0 de um item e, ao mesmo tempo, voltar para a versão 1.3 já presente em uma *release* para corrigir um defeito, gerando a versão 1.3.1, e então retornar ao trabalho na versão 2.0. O slide exibe o logotipo do Git, representando a ferramenta mencionada.