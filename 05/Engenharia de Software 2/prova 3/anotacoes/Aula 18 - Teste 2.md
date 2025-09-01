## Teste Funcional (Slide 1)

Este slide introduz o tema da apresentação: **Teste Funcional**. Esta é uma técnica de teste de software do tipo "caixa-preta", o que significa que o teste é realizado sem conhecimento da estrutura interna ou do código do programa. O foco é verificar a funcionalidade de um programa, comparando suas entradas e saídas com o que foi especificado nos requisitos. O objetivo é garantir que o software se comporta conforme o esperado do ponto de vista do usuário.

---

## Conteúdo (Slide 2)

Este slide apresenta um roteiro dos tópicos que serão abordados. A apresentação se aprofundará em:
* **Teste Funcional**, detalhando duas técnicas principais:
    * **Particionamento de Equivalência:** Uma forma de otimizar a seleção de dados de teste.
    * **Análise de Valor Limítrofe:** Uma técnica complementar que foca nos valores de fronteira das entradas.
    * **Execução em Nível de Sistema:** Como aplicar o teste funcional a fluxos completos do sistema, baseados em casos de uso.
* **TDD (Desenvolvimento Orientado por Testes):** Uma filosofia de desenvolvimento onde os testes são escritos antes do código.
* **Medição em Teste:** A importância de usar métricas para acompanhar o processo de teste e a qualidade do produto.
* **Depuração:** O processo de encontrar e corrigir os defeitos identificados pelos testes.

---

## Particionamento de Equivalência (Slide 3)

Este slide introduz o conceito de **Particionamento de Equivalência**. A ideia central é dividir todos os dados de entrada possíveis em um número finito de "classes de equivalência". A técnica parte do pressuposto de que se um valor de uma classe funciona, todos os outros valores da mesma classe também funcionarão. Da mesma forma, se um valor falha, todos os outros daquela classe também falharão. Isso permite reduzir drasticamente o número de casos de teste necessários, selecionando apenas um ou alguns representantes de cada classe para testar, tornando o processo de teste mais eficiente e gerenciável.

---

## Exemplo: adicionarItem (Slide 4)

Este slide apresenta um exemplo prático para aplicar as técnicas de teste: a operação `adicionarItem(idCompra, isbn, quantidade)`.
* As **Precondições** definem o que deve ser verdadeiro para que a operação funcione corretamente:
    * O `idCompra` deve se referir a uma compra existente e que não esteja fechada.
    * O `isbn` deve pertencer a um livro cadastrado no sistema.
    * A `quantidade` deve ser um número inteiro positivo.
    * A `quantidade` solicitada não pode ser maior que o estoque disponível do livro.
* As **Pós-condições** descrevem o que acontece após a execução:
    * Se o livro já está na compra, sua quantidade é incrementada.
    * Se o livro não está na compra, ele é adicionado como um novo item.
    * Em ambos os casos, o estoque do livro é decrementado.

---

## Classes de Equivalência (Slide 5)

Este slide detalha as classes de equivalência, válidas e inválidas, para cada parâmetro da função `adicionarItem`:
* **idCompra:**
    * **Válida (v1.1):** Um ID de uma compra existente e aberta.
    * **Inválidas (i1.1, i1.2):** Um ID que não corresponde a nenhuma compra ou que corresponde a uma compra já fechada.
* **isbn:**
    * **Válidas (v2.1, v2.2):** Um ISBN de um livro que já consta na compra (para testar a atualização) e um ISBN de um livro que não consta na compra (para testar a adição). Ambas são classes válidas, pois levam a comportamentos diferentes, mas corretos.
    * **Inválida (i2.1):** Um ISBN que não corresponde a nenhum livro cadastrado.
* **quantidade:**
    * **Válida (v3.1):** Um valor maior que zero e menor ou igual ao estoque.
    * **Inválidas (i3.1, i3.2):** Um valor menor ou igual a zero, ou um valor maior que o estoque disponível.

---

## Casos de Teste (Slides 6 e 7)

Estes slides demonstram como as classes de equivalência são combinadas para criar **casos de teste** concretos.
* **Testes de Sucesso:** Combinam apenas classes válidas para verificar se a funcionalidade principal está correta.
    * **s1:** Testa a atualização de um item existente na compra (v1.1, v2.1, v3.1).
    * **s2:** Testa a adição de um novo item à compra (v1.1, v2.2, v3.1).
* **Testes de Falha:** Geralmente, combinam uma classe inválida com as demais classes válidas para garantir que o sistema lida corretamente com os erros.
    * **f1 a f8:** Cada um desses casos testa uma condição de erro específica, como usar uma compra inexistente (f1), uma compra fechada (f2, f3), um ISBN não cadastrado (f4), ou uma quantidade inválida (não positiva em f5/f6, ou acima do estoque em f7/f8). O objetivo é garantir que o sistema rejeita a operação e informa o erro adequado.

---

## Tipos Primitivos Estáticos (Slide 8)

Este slide aborda uma forma de reduzir a necessidade de testes para certas classes inválidas: o uso de **tipos primitivos estáticos e fortes**. Em linguagens de programação que permitem isso, é possível definir tipos de dados que já restringem os valores possíveis em tempo de compilação.
* **Exemplos:**
    * **Números naturais:** Impediria a entrada de valores negativos.
    * **Valor de ISBN:** Poderia validar o formato do código.
    * **Intervalo:** Poderia garantir que uma data está dentro de um período válido.
* Ao usar esses tipos, o próprio compilador impediria a criação de um valor inválido, eliminando a necessidade de um caso de teste para essa condição, pois ela nunca ocorreria em tempo de execução.

---

## Conjuntos Dinâmicos (Slide 9)

Em contrapartida ao slide anterior, este destaca situações em que a validação não pode ser feita de forma estática, pois depende de **conjuntos de dados dinâmicos**, que mudam durante a execução do sistema.
* **Exemplos:**
    * Verificar se o número de uma compra já foi efetuado.
    * Verificar se o CPF de uma pessoa já está cadastrado.
    * Verificar se uma data corresponde ao aniversário de um cliente cadastrado.
* Nesses casos, a validação só pode ocorrer em tempo de execução, consultando uma base de dados. Portanto, é essencial criar classes de equivalência e casos de teste para essas condições, pois não podem ser prevenidas pela tipagem estática.

---

## Análise de Valor Limítrofe (Slide 10)

Este slide introduz a **Análise de Valor Limítrofe (AVL)**. A experiência mostra que muitos bugs se escondem "nas frestas", ou seja, nas fronteiras entre as classes de equivalência. Por exemplo, se um campo aceita valores de 18 a 64, os erros são mais prováveis de ocorrer com os valores 17, 18, 64 e 65 do que com valores como 30 ou 50. A AVL é uma técnica que complementa o particionamento de equivalência, focando os testes exatamente nesses valores limítrofes para aumentar a chance de encontrar defeitos.

---

## Exemplo: Análise de Valor Limítrofe (Slide 11)

Este slide aplica a AVL a um exemplo de classificação por **idade**.
* As classes de equivalência são:
    * Inválido: < 0
    * Válido (menor de idade): 0 a 17
    * Válido (adulto): 18 a 64
    * Válido (idoso): 65 a 120
    * Inválido (idoso improvável): > 120
* Os **valores a serem testados** com AVL seriam as fronteiras de cada intervalo: **-1, 0, 17, 18, 64, 65, 120, 121**. Para maior robustez, o slide também inclui valores aleatórios dentro de cada partição (-10, 8, 30, 80, 156), combinando as duas técnicas.

---

## Teste Funcional em Nível de Sistema (Slide 12)

O teste funcional não se aplica apenas a unidades de código, mas também ao **sistema como um todo**. Nesse nível, o objetivo é verificar se os fluxos de trabalho completos, do ponto de vista do usuário, funcionam corretamente. A abordagem mais comum para documentar e testar esses fluxos é através de **casos de uso**. O sistema é tratado como uma caixa-preta, e os testes simulam a interação de um usuário para executar um processo de negócio do início ao fim, validando se o resultado final atende aos requisitos.

---

## Exemplo: Caso de Uso - Comprar livros (Slide 13)

Este slide detalha um caso de uso para "Comprar Livros", que servirá de base para os testes de sistema.
* **Fluxo Principal (Caminho Feliz):** Descreve a sequência ideal de passos:
    1.  Usuário busca por um livro.
    2.  Sistema lista os resultados.
    3.  Usuário seleciona um livro e a quantidade.
    4.  Sistema mostra o resumo do pedido.
    5.  Usuário finaliza a compra.
    6.  Sistema confirma a compra.
* **Fluxos de Exceção:** Tratam de erros, como `E3a` (usuário indica quantidade acima do estoque) e `E5a` (usuário tenta finalizar a compra sem estar logado).
* **Fluxos de Variantes:** Descrevem comportamentos alternativos, mas válidos, como `V5a` (usuário decide selecionar mais livros) ou `V5b` (usuário decide fazer uma nova pesquisa).

---

## Casos de Teste de Sistema (Slide 14)

Este slide traduz os fluxos do caso de uso em **casos de teste de sistema**. Cada caso de teste representa um cenário completo.
* **Caso 1:** Testa o fluxo principal (caminho feliz). O objetivo é garantir que uma compra pode ser realizada com sucesso.
* **Caso 2:** Testa a exceção `E3a`, verificando se o sistema impede a compra de um item sem estoque e permite que o usuário corrija a quantidade e continue.
* **Caso 3:** Testa a exceção `E5a`, garantindo que um usuário não logado seja solicitado a fazer login antes de finalizar a compra.
* **Caso 4 e 5:** Testam as variantes `V5a` e `V5b`, verificando se o usuário pode navegar de volta para adicionar mais itens ou iniciar uma nova busca, e depois concluir a compra com sucesso.

---

## TDD - Desenvolvimento Orientado por Testes (Slide 15)

Este slide ilustra o ciclo do **TDD (Test-Driven Development)**. É uma filosofia de desenvolvimento que inverte a ordem tradicional:
1.  **Escrever o Teste (vermelho):** Primeiro, o desenvolvedor escreve um teste automatizado para uma nova funcionalidade que ainda não existe. Naturalmente, esse teste falhará.
2.  **Escrever o Código Mínimo (verde):** Em seguida, ele escreve a quantidade mínima de código necessária apenas para fazer o teste passar.
3.  **Refatorar:** Com a segurança dos testes, o desenvolvedor pode então limpar e melhorar o código (refatorar) sem alterar seu comportamento.
O ciclo se repete para cada pequena funcionalidade, garantindo que o software tenha uma suíte de testes completa e que o design evolua de forma incremental e segura.

---

## Exemplo TDD: Requisitos (Slide 16)

Aqui começa um exemplo prático de TDD. A tarefa é criar uma função `categoria(idade)`.
* Os **requisitos iniciais** são:
    * **Menor:** Para idades de 0 a 17 anos (classe válida).
    * **Adulto:** Para idades a partir de 18 anos (classe válida).
    * **Não nascido:** Para idades negativas (classe inválida), o programa deve gerar um erro.

---

## Código Inicial (Slide 17)

Este slide mostra o primeiro passo do TDD na prática: **escrever os testes primeiro**. Antes mesmo de implementar a lógica da função `categoria`, o desenvolvedor cria um conjunto de testes automatizados (`asserts`) que definem o comportamento esperado.
* São criados testes para os valores limítrofes (0, 17, 18) e valores intermediários (8, 45).
* Um teste específico é criado para a classe inválida (idades -20 e -1), verificando se a função lança uma exceção, conforme o requisito.
Neste ponto, a função `categoria` é apenas um esqueleto vazio (`return`), e, ao executar o programa, os testes irão falhar.

---

## Código Minimalista para Passar no Teste (Slides 18 e 19)

Estes slides ilustram o segundo passo do TDD: escrever o **código mínimo** para fazer os testes passarem.
* **Slide 18:** Mostra uma primeira tentativa de código: `if idade <= 18`. Ao rodar os testes, o desenvolvedor perceberá que o teste para `idade 18` falha, pois o código retorna "menor" quando deveria retornar "adulto". O inseto no slide simboliza esse bug.
* **Slide 19:** O desenvolvedor corrige o erro, alterando a condição para `if idade < 18`. Agora, todo o conjunto de testes passa. O código está funcional, embora ainda não necessariamente elegante ou otimizado. O importante é que ele atende aos requisitos definidos pelos testes.

---

## Mudança no Requisito (Slide 20)

Este slide introduz uma **mudança nos requisitos**, uma situação comum em projetos de software. A função `categoria` agora precisa ser mais detalhada:
* **Adulto:** A classe agora vai de 18 a 64 anos.
* **Idoso:** Uma nova classe válida é adicionada, para idades de 65 a 120 anos.
* **Improvável:** A classe inválida para idades muito altas é formalizada, considerando valores a partir de 121.

---

## Novos Testes são Escritos (Slide 21)

Seguindo a filosofia TDD, antes de alterar o código da função, o desenvolvedor primeiro **atualiza a suíte de testes** para refletir os novos requisitos.
* Novos testes são adicionados para a categoria "Idoso", cobrindo seus limites (65, 120) e um valor intermediário (80).
* O teste da classe "Adulto" é ajustado para seu novo limite superior (64).
* O teste de classe inválida é atualizado para incluir valores como 121 e 200.
Ao rodar a função antiga com estes novos testes, ela irá falhar (por exemplo, ao testar a idade 65), sinalizando que o código precisa ser modificado.

---

## Programa Final (Slide 22)

Este slide mostra o **programa final**, após o código ser ajustado para passar na nova e expandida suíte de testes.
* A lógica foi alterada para incluir as novas regras de negócio, com um `assert` para o limite superior de 120 e uma cláusula `elif` para diferenciar "adulto" de "idoso".
* Este processo demonstra como o TDD facilita a manutenção e a evolução do software. A suíte de testes existente serve como uma rede de segurança, garantindo que as alterações não quebrem funcionalidades antigas, e guia o desenvolvedor na implementação correta dos novos requisitos.

---

## Medição em Teste (Slide 23)

Este slide aborda a importância da **medição** para gerenciar a atividade de teste de forma objetiva. As métricas são divididas em duas categorias principais:
* **Métricas do Processo de Teste:** Focam no esforço e no andamento da atividade de teste.
    * *Exemplos:* Número de testes previstos, planejados e executados. Isso ajuda a entender se o planejamento está sendo seguido.
* **Métricas de Teste do Produto:** Focam na qualidade do software que está sendo testado.
    * *Exemplos:* Número de defeitos descobertos e corrigidos, e sua distribuição por gravidade ou por módulo. Isso ajuda a identificar as áreas mais problemáticas do sistema e a medir a eficácia da equipe em resolver os problemas.

---

## Evolução Esperada das Medições de Teste (Slide 24)

Este gráfico ilustra a **evolução esperada das métricas de produto** ao longo do tempo em um projeto.
* **Curva de Defeitos Descobertos:** A linha superior mostra o total acumulado de defeitos encontrados. Espera-se que ela cresça rapidamente no início e depois se estabilize (achate), indicando que menos defeitos novos estão sendo encontrados e o produto está amadurecendo.
* **Curva de Defeitos Corrigidos:** A linha inferior mostra o total de defeitos que foram consertados. Ela deve seguir a curva de descobertos.
* O **espaço entre as duas curvas** representa o backlog de defeitos — bugs conhecidos mas ainda não resolvidos. O objetivo é que, ao final do projeto, essas duas curvas estejam o mais próximo possível, indicando um produto estável e com alta qualidade.

---

## Depuração (Slide 25)

Finalmente, o slide aborda a **Depuração (Debugging)**. Enquanto o teste se preocupa em encontrar *falhas* (comportamentos incorretos), a depuração é a atividade de investigar essas falhas para encontrar sua **causa-raiz**, o *defeito* (o erro no código), e então corrigi-lo. É um processo que se inicia após um teste falhar ou um usuário reportar um problema. A imagem do "Flit" (um antigo inseticida) é uma brincadeira com o termo "bug" (inseto), que se popularizou na computação para designar defeitos de software. Ferramentas modernas, como *debuggers*, são essenciais para auxiliar nesse processo investigativo.