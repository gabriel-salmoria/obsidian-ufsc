## Teste de Software I - Teste Estrutural (Slide 1)

Este slide introduz o tema da aula: Teste Estrutural, também conhecido como "White Box Testing" ou "Teste Caixa Branca". A imagem ilustra o conceito: um "inspetor" analisando o interior de uma caixa, que representa o código-fonte de um programa. O pequeno trecho de código em Java exemplifica o tipo de estrutura interna que será analisada. A disciplina de teste de software é crucial porque, por melhores que sejam as técnicas de desenvolvimento, o erro humano é um fator sempre presente. É um mito acreditar que bons desenvolvedores, mesmo com ótimas ferramentas, são capazes de criar software sem erros.

---

## Conteúdo (Slide 2)

Este slide apresenta os tópicos que serão abordados na aula. Iniciaremos com os **Fundamentos** do teste de software, definindo termos essenciais. Em seguida, exploraremos os **Níveis de teste de funcionalidade**, que categorizam os testes com base em seus objetivos, desde a verificação de pequenas partes do código até a validação do sistema completo. Depois, discutiremos os **Testes suplementares**, que avaliam características não-funcionais como performance e segurança. Por fim, o foco principal, o **Teste estrutural**, que é uma técnica de teste que analisa a estrutura interna do código.

---

## Erro Humano (Slide 3)

Este slide, com a imagem de um acidente rodoviário, serve como uma analogia para o **erro humano** no desenvolvimento de software. Assim como um erro de sinalização ou de condução pode causar um acidente, um engano por parte de um programador pode introduzir um defeito no software. A Lei de Murphy é frequentemente citada na indústria de software, com máximas como "Se alguma coisa pode sair errado, sairá" e "Se tudo parece estar indo bem é porque você não olhou direito", ressaltando a inevitabilidade de problemas. Antigamente, testar era visto como uma tarefa ingrata que expunha as falhas dos desenvolvedores, mas hoje é uma disciplina essencial e integrada ao processo de desenvolvimento.

---

## Fundamentos (Slide 4)

Este slide introduz quatro termos fundamentais com significados precisos na área de teste. É importante distingui-los:
* **Engano (mistake):** É a ação humana que resulta em um defeito. Por exemplo, um programador digita um operador errado.
* **Defeito (fault):** Também chamado de *bug*, é o resultado do engano. É uma linha de código, um bloco ou um conjunto de dados incorretos que podem provocar um erro.
* **Erro (error):** É uma diferença observada entre o resultado esperado e o resultado real de uma computação, causada por um defeito.
* **Falha (failure):** É o não funcionamento do software como um todo, a observação de que o sistema não está funcionando adequadamente. Uma falha pode ser provocada por um defeito, mas também por outras causas, como problemas de infraestrutura ou dados incorretos. A área de teste foca principalmente em encontrar falhas provocadas por defeitos para que possam ser corrigidos.

---

## Verificação, Validação e Teste (Slide 5)

Este slide aborda três conceitos inter-relacionados:
* **Verificação:** Consiste em analisar o software para garantir que ele está sendo construído "do jeito certo", ou seja, de acordo com as especificações. O objetivo é saber se o produto atende aos requisitos especificados, estando livre de defeitos. Isso normalmente é o foco dos testes de unidade, integração e sistema.
* **Validação:** Consiste em analisar o software para ver se ele atende às reais necessidades dos interessados (clientes, usuários). A pergunta-chave aqui é: "Estamos fazendo a coisa certa?". Esse é o objetivo principal dos testes de aceitação.
* **Teste:** É a atividade que permite realizar tanto a verificação quanto a validação do software.

---

## Depuração (Slide 6)

Este slide ilustra o conceito de **Depuração (Debugging)**. Enquanto o teste se concentra em encontrar erros desconhecidos, a depuração é a atividade de buscar a causa raiz do erro, ou seja, o defeito oculto que o está causando. Saber que o software não funciona não significa saber qual linha de código está errada. A depuração pode ser um processo caro e demorado, por isso as práticas modernas recomendam a integração incremental de pequenas partes de código. Se o sistema funcionava antes e para de funcionar após uma nova integração, o defeito provavelmente está no componente recém-adicionado.

---

## Teste de Partes de Software (Slide 7)

Este slide destaca que, frequentemente, partes do software, como componentes individuais, precisam ser testadas de forma isolada. No entanto, essas partes normalmente não existem sozinhas; elas se comunicam e dependem de outras partes do sistema. Isso introduz a necessidade de simular os componentes ausentes durante o teste, o que nos leva aos conceitos de Stubs e Drivers.

---

## Stub (Slide 8)

Este slide explica o que é um **Stub**. Um stub é usado quando o componente que estamos testando (Componente A) depende de outro componente (Componente B) que ainda não foi implementado. O stub é uma implementação simplificada do Componente B. Ele não realiza o cálculo real, mas retorna valores predeterminados que são suficientes para permitir o teste do Componente A. O exemplo em Python mostra um stub para uma função `primo` que, em vez de calcular números primos, simplesmente retorna valores fixos para as primeiras cinco chamadas, permitindo que a classe que a utiliza seja testada.

---

## Driver (Slide 9)

Este slide apresenta o conceito de **Driver**. Um driver é o inverso de um stub. Ele é utilizado quando o componente que queremos testar (Componente B) já está implementado, mas o componente que o utiliza (Componente A) ainda não existe. O driver é uma simulação do Componente A, responsável por chamar as funções do componente testado (B) e executar os casos de teste necessários para validá-lo. Enquanto stubs são geralmente descartáveis ("throw-away"), os drivers são considerados patrimônio de teste e devem ser guardados para testes futuros, como os testes de regressão.

---

## Fixture (Slide 10)

Este slide define **Fixtures**, que são variáveis ou objetos criados especificamente para serem usados em testes automatizados. A execução de um teste com fixtures geralmente segue três etapas:
1.  **Preparar o cenário:** É o momento em que as fixtures são criadas e o ambiente de teste é configurado.
2.  **Executar o teste:** As funções a serem testadas são chamadas, utilizando as fixtures como entrada, e o resultado é verificado.
3.  **Limpar o ambiente:** Após a execução do teste, todas as fixtures e recursos alocados são liberados ou destruídos.

---

## Níveis de Teste de Funcionalidade (Slide 11)

Este slide lista os principais **níveis de teste de funcionalidade**, que têm como objetivo verificar e validar se as funções implementadas estão corretas em suas diversas granularidades. Os níveis são:
* **Unidade:** Testa componentes individuais de forma isolada (métodos, classes).
* **Integração:** Testa a comunicação e a interação entre unidades que já foram testadas.
* **Sistema:** Testa o sistema completo, do ponto de vista do usuário, executando casos de uso de ponta a ponta.
* **Aceitação:** Realizado pelo cliente ou usuário final para validar se o sistema atende às suas necessidades e pode ser aprovado.
* **Ciclo de Negócio:** Testa uma sequência de casos de uso que representam um processo de negócio completo.
* **Regressão:** Executado após uma modificação para garantir que as funcionalidades existentes não foram quebradas.
* **Operação:** Realizado no ambiente final de produção para verificar compatibilidade e convivência com outros sistemas.

---

## Testes Suplementares (Slide 12)

Além dos testes de funcionalidade, existem os **testes suplementares**, que verificam características não-funcionais do sistema. Este slide lista os mais comuns:
* **Interface com Usuário:** Avalia a usabilidade, eficiência e conformidade ergonômica da interface.
* **Performance (Carga, Estresse e Resistência):** Mede o comportamento do sistema sob diferentes cargas de trabalho. O teste de carga avalia o desempenho em condições normais. O teste de estresse leva o sistema a seus limites para verificar sua robustez. O teste de resistência avalia a estabilidade do sistema ao longo do tempo.
* **Segurança:** Testa a proteção do sistema contra ameaças, avaliando aspectos como integridade, autenticação, autorização, confidencialidade, disponibilidade e não repúdio.
* **Recuperação de Falha:** Verifica a capacidade do sistema de se restabelecer após uma falha (ex: queda de energia).
* **Instalação:** Garante que o software pode ser instalado corretamente em diferentes ambientes e que não entra em conflito com outros sistemas.

---

## Teste Estrutural (Slide 13)

Este slide reitera o foco da aula: o **Teste Estrutural**. Como o nome e a imagem sugerem, esta família de técnicas de teste foca na **estrutura interna** do código implementado. O objetivo não é apenas verificar as entradas e saídas (como no teste funcional), mas analisar os caminhos de execução, os laços de repetição, as estruturas condicionais e os comandos que compõem o programa. O teste estrutural é fundamental para garantir que todas as partes do código sejam exercitadas ao menos uma vez durante o teste.

---

## Complexidade Ciclomática (Slide 14)

Este slide introduz uma métrica fundamental para o teste estrutural: a **Complexidade Ciclomática**, desenvolvida por McCabe. Ela mede a complexidade de um programa e ajuda a determinar o número de testes necessários.
* **Definição Simplificada:** A complexidade é calculada como `n + 1`, onde `n` é o número de estruturas de decisão (como `if`, `for`, `while`) no programa.
* **Código de Exemplo:** O código `maior_sequencia` é apresentado. Ele possui três estruturas de decisão: um `for` (linha 5), um `if` (linha 6) e outro `if` (linha 8). Portanto, sua complexidade ciclomática é `3 + 1 = 4`.
* **Significado:** Um valor de complexidade 4 indica que são necessários, no máximo, 4 casos de teste independentes para cobrir todos os caminhos possíveis de execução do código. Programas com complexidade até 10 são considerados simples de testar, enquanto valores acima de 50 são geralmente considerados não testáveis.

---
## Grafo de Fluxo (Slide 15)

Este slide mostra o **Grafo de Fluxo** para a função `maior_sequencia`. O grafo de fluxo é uma representação visual da estrutura de controle de um programa.
* **Nós:** Representam os comandos ou sequências de comandos. Comandos sequenciais podem ser agrupados em um único nó (ex: nó 1-4).
* **Arestas:** Representam o fluxo de controle entre os nós.
* **Estruturas de Decisão:** Nós como o `5` (laço `for`) e `6` (primeiro `if`) têm múltiplas arestas de saída, representando os diferentes caminhos que a execução pode tomar.
* **Cálculo da Complexidade:** A complexidade ciclomática também pode ser calculada a partir do grafo usando a fórmula: `arestas - nós + 2`. Neste grafo, temos 12 arestas e 10 nós (incluindo os nós de início e fim), resultando em `12 - 10 + 2 = 4`, o que confirma o cálculo anterior. Outra forma é contar as regiões fechadas no grafo, que neste caso são 4.

---
## Programa com "Break" (Slide 16)

Este slide apresenta um programa que utiliza o comando `break` dentro de laços, e o seu respectivo grafo de fluxo. O uso de `break` (e `GOTO`, em linguagens mais antigas) pode criar grafos de fluxo mais complexos.
* **Código:** O programa cria uma lista ordenada de números aleatórios, simulando um sorteio. Ele usa dois `break` (linhas 6 e 9) para interromper o laço `for` prematuramente. A estrutura `for-else` do Python faz com que o bloco `else` (linha 11) só seja executado se o `for` terminar todas as suas repetições sem um `break`.
* **Grafo de Fluxo:** O grafo correspondente mostra os saltos causados pelos `break`. Os nós 6 e 8-9, se executados, interrompem o laço interno (nó 3) e fazem o fluxo retornar ao laço externo (nó 1). A complexidade ciclomática deste programa é 5, correspondendo a 4 comandos de decisão (`while`, `for-else`, dois `if`) mais 1.

---
## Caminhos Independentes (Slide 17)

Este slide aplica o conceito de **caminhos independentes** ao primeiro exemplo (`maior_sequencia`). Um caminho independente é uma rota do início ao fim do grafo que introduz pelo menos uma nova aresta que não foi coberta por outros caminhos.
* **Complexidade e Caminhos:** O valor da complexidade ciclomática (que calculamos como 4) determina o número máximo de caminhos independentes necessários para garantir a cobertura de todas as arestas.
* **Caminhos Identificados:**
    * $c_1$: `<1-4, 5, 13>` - O laço `for` não executa nenhuma vez (lista vazia).
    * $c_2$: `<1-4, 5, 6, 10-11, 12, 5, 13>` - O laço executa uma vez, a condição em 6 é falsa.
    * $c_3$: `<1-4, 5, 6, 7-8, 12, 5, 13>` - A condição em 6 é verdadeira, mas a em 8 é falsa.
    * $c_4$: `<1-4, 5, 6, 7-8, 9, 12, 5, 13>` - As condições em 6 e 8 são verdadeiras.
* **Cobertura:** Juntos, esses quatro caminhos exercitam todos os comandos e todas as condições (verdadeiras e falsas) do programa.

---
## Caminhos Independentes (Slide 18)

Este slide mostra os caminhos independentes para o segundo exemplo, o programa com `break`. A complexidade ciclomática é 5, portanto, precisamos de no máximo cinco caminhos independentes.
* **Caminhos Identificados:**
    * $c_1$: `<1, 12>` - O laço `while` não executa.
    * $c_2$: `<1, 2, 3, 10-11, 1, 12>` - O laço `while` executa, o `for` termina sem `break`.
    * $c_3$: `<1, 2, 3, 4-5, 6, 1, 12>` - O `break` da linha 6 é executado.
    * $c_4$: `<1, 2, 3, 4-5, 7, 8-9, 1, 12>` - O `break` da linha 9 é executado.
    * $c_5$: `<1, 2, 3, 4-5, 7, 3, 10-11, 1, 12>` - Este caminho cobre a aresta de 7 para 3, que não havia sido coberta, representando o caso em que o `if` da linha 7 é falso.
* **Objetivo:** O objetivo de identificar esses caminhos é garantir que os casos de teste subsequentes forcem o programa a percorrer cada um deles.

---
## Casos de Teste (Slide 19)

Após identificar os caminhos independentes, o próximo passo é definir **casos de teste** — ou seja, os dados de entrada — que forçarão a execução de cada caminho e qual a saída esperada.
* **Tabela de Casos de Teste:** A tabela relaciona cada caminho a uma entrada (`lista`) e à `saida_esperada` (`maior_contador`).
    * $c_1$: Para não entrar no laço `for`, a entrada deve ser uma lista vazia `[]`. A saída esperada é `0`.
    * $c_2$: Para o `if` da linha 6 ser falso, a lista precisa ter um elemento, como `[5]`. A saída esperada é `1`.
    * $c_3$: Para o `if` da linha 8 ser falso em uma sequência, deve haver uma sequência maior antes. Entrada: `[5, 5, 5, 7, 7]`. Saída esperada: `3`.
    * $c_4$: Para o `if` da linha 8 ser verdadeiro, basta uma lista com dois elementos iguais, como `[5, 5]`. Saída esperada: `2`.

---
## Execução do Teste (Slide 20)

Este slide mostra a execução dos casos de teste definidos anteriormente. Um `assert` é usado para verificar se a saída real da função corresponde à saída esperada. Se não corresponder, o `assert` falha.
* **Falha no Teste:** O slide indica uma "FALHA!". Ao executar `maior_sequencia([5])`, o programa original não atualiza a variável `maior_contador`. Ela permanece com seu valor inicial `0`, mas a saída esperada era `1`. Portanto, `assert maior_sequencia([5]) == 1` falha.
* **Causa do Defeito:** O defeito ocorre porque a atualização do `maior_contador` está dentro de uma estrutura condicional que não é ativada para uma lista de um único elemento.

---
## Depuração (Slide 21)

Este slide apresenta a versão corrigida do código, resultado do processo de **depuração**.
* **A Correção:** O problema foi que a atualização da variável `maior_contador` estava aninhada incorretamente. A correção envolve mover as linhas que atualizam o contador (`if contador > maior_contador: maior_contador = contador`) para fora do `else`.
* **Novo Processo:** A má notícia é que, como a estrutura do programa mudou, o grafo de fluxo também muda. Isso significa que, para sermos rigorosos, precisaríamos refazer o grafo, reidentificar os caminhos independentes e redefinir os casos de teste para o novo código.

---
## Múltiplas Condições e Caminhos Impossíveis (Slide 22)

Este slide introduz dois novos conceitos usando um programa que verifica se um ano é bissexto.
* **Múltiplas Condições:** A linha 4 contém uma condição `if` complexa, com múltiplos operadores lógicos (`and`, `or`). O critério de cobertura de teste deve garantir que todas as combinações de verdadeiro/falso dessas sub-condições sejam testadas.
* **Caminhos Impossíveis:** Às vezes, a lógica do programa torna certos caminhos no grafo de fluxo impossíveis de serem executados. O slide aponta o caminho $c_2: <1-4, 4b, 5>$ como impossível. Um ano não pode ser "não divisível por 4" (o que levaria ao nó `4b`) e ao mesmo tempo ser "divisível por 400" (condição para chegar ao nó 5 a partir de `4b`), pois 400 é múltiplo de 4.

---
## Refazendo os Caminhos Independentes (Slide 23)

Este slide mostra como lidar com um caminho impossível.
* **Reconstrução:** O conjunto original de caminhos independentes precisa ser refeito para evitar o caminho impossível. Os novos caminhos são logicamente possíveis.
* **Novos Caminhos:**
    * $c_1: <1-4, 4a, 5>$: Ano é divisível por 4, mas não por 100. (Ex: 2004)
    * $c_2: <1-4, 4b, 6-7>$: Ano não é divisível por 4. (Ex: 1999)
    * $c_3: <1-4, 4a, 4b, 5>$: Ano é divisível por 4, por 100 e por 400. (Ex: 2000)
    * $c_4: <1-4, 4a, 4b, 6-7>$: Ano é divisível por 4 e por 100, mas não por 400. (Ex: 1800)
* **Casos de Teste:** A tabela fornece exemplos de entradas (`ano`) para cada caminho e a saída esperada (`bissexto?`).

---
## Caminho Impossível (FOR Constante) (Slide 24)

Este slide dá um exemplo muito simples de caminho impossível.
* **Código:** O programa calcula o número de grãos de arroz em um tabuleiro de xadrez, usando um laço `for i in range(64)`.
* **Caminho Impossível:** Em um laço `for` com limites variáveis (ex: `for i in range(n)`), existem dois caminhos possíveis: o laço executa pelo menos uma vez, e o laço não executa nenhuma vez (se `n <= 0`). No entanto, quando o limite é uma constante, como `range(64)`, o laço SEMPRE executará 64 vezes. O caminho que corresponde a "não executar o laço" é, portanto, impossível.

---
## Caminho Impossível (WHILE TRUE) (Slide 25)

Este slide ilustra outro tipo de caminho impossível, desta vez com um laço `while True`.
* **Código:** O programa simula a evolução de uma população, com um laço `while True:` que, teoricamente, seria infinito.
* **Ponto de Decisão Real:** A verdadeira condição de parada não está no `while`, mas sim no `if` da linha 12, que contém um `break`.
* **Caminho Impossível no Grafo:** A aresta que sairia do nó do `while` para o fim do programa (representando a condição do `while` sendo falsa) nunca será percorrida. Na prática, a complexidade do programa é menor do que a análise puramente estrutural do `while` sugeriria, pois a decisão foi transferida para o `if`.

---
## Caminho Impossível (IF) (Slide 26)

Este slide mostra o exemplo mais trivial de um caminho impossível.
* **Código:** `if 1 == 2: print(...)`.
* **Lógica:** Qualquer programador pode ver que a condição `1 == 2` será sempre falsa. Portanto, a linha `print(...)` está em um caminho impossível e nunca será executada. Embora simples de identificar aqui, nem sempre é o caso.

---
## Situação em que é difícil determinar se um caminho é impossível (Slide 27)

Este slide apresenta um caso extremo de um caminho de difícil determinação, usando o Último Teorema de Fermat.
* **Código:** A função `fermat` testa a conjectura $a^x + b^x = c^x$.
* **O Desafio:** Para saber se a linha `print` (linha 3) é um caminho impossível para inteiros com $x > 2$, seria necessário provar o Último Teorema de Fermat.
* **Contexto Histórico:** Esse teorema levou 359 anos para ser provado matematicamente, e a conclusão é que, para $x > 2$, não existem inteiros positivos $a, b, c$ que satisfaçam a equação. Portanto, a linha 3 de fato representa um caminho impossível para $x > 2$, mas determiná-lo estava longe de ser trivial.

---
## Limitações do Teste Estrutural (Slide 28)

O teste estrutural é poderoso, mas tem limitações. A principal delas é que ele **não testa código que deveria existir, mas não existe**.
* **Exemplo `é_primo`:** A função `é_primo` apresentada funciona para os casos de teste derivados de seus caminhos (números como 2, 4, 5, 6).
* **O Defeito Oculto:** A função não verifica corretamente números menores que 2 (como 0, 1 ou negativos). Para qualquer entrada menor que 2, o laço `for` não executa, e a função retorna `True` incorretamente.
* **A Limitação:** Como não há código para tratar esses casos, o teste estrutural (que só testa o código existente) não detecta essa omissão. Seria necessário adicionar um `if numero < 2: return False` para corrigir o defeito.

---
## Mas é bom para identificar código malicioso (Slide 29)

Apesar de suas limitações, o teste estrutural é excelente para uma tarefa específica: **identificar código malicioso ou sabotagens**.
* **Cenário:** O teste funcional testa um programa com base em sua especificação. Para uma função `fatorial`, o analista de teste escolheria valores como 0, 1, 2, 5, 8, 12.
* **O Código Malicioso:** O slide mostra um código `fatorial` que foi adulterado. Ele contém uma linha `if n == 31: return 0`. Essa linha faz a função falhar para uma entrada específica e arbitrária (31) que provavelmente não seria escolhida em um teste funcional.
* **A Vantagem do Teste Estrutural:** O teste estrutural, por sua natureza, precisa testar todas as linhas e condições do programa. Ele seria obrigado a criar um caso de teste para a condição `n == 31`, forçando a execução da linha maliciosa e revelando a sabotagem que o teste funcional provavelmente não encontraria.