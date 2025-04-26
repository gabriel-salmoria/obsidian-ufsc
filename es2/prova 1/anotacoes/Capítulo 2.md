## Processo de Desenvolvimento de Software

Este capítulo aborda os fundamentos do processo de desenvolvimento de software, com foco em sua estrutura, componentes e importância dentro da Engenharia de Software.

---

## 📌 1. Conceito de Processo

Um **processo** de software é um conjunto estruturado de atividades interdependentes, com entradas e saídas bem definidas, executadas por responsáveis com papéis específicos e com uso de recursos adequados.

### Diferenças importantes:
- **Processo**: Regras gerais adotadas por uma organização para guiar o desenvolvimento de projetos.
- **Projeto**: Execução concreta de atividades com início e fim definidos.
- **Modelo de Processo**: Representa uma filosofia ou abordagem genérica (ex: cascata, ágil), usada para derivar processos específicos.

> Um projeto é uma **instância** de um processo.

---

## 🧩 2. Vantagens do Uso de Processos

- **Treinamento facilitado**: Novos membros da equipe podem ser integrados com mais facilidade.
- **Uniformidade**: Produtos tendem a ser mais consistentes.
- **Capitalização de experiências**: Melhoria contínua do processo com base em feedback e descobertas dos desenvolvedores.

---

## 🌀 3. Estrutura de Processos

### 3.1 Fases (conforme ISO/IEC TS 24748-1:2016)
Divisões macro do processo, cada uma com objetivos específicos:

1. **Concepção**: Levantamento inicial das necessidades e ideias.
2. **Desenvolvimento**: Modelagem do produto com base nas necessidades.
3. **Produção**: Implementação e construção do software.
4. **Utilização**: Uso do produto pelo cliente final.
5. **Suporte**: Manutenção, correções e melhorias.
6. **Desativação**: Retirada de operação do sistema.

> Alguns modelos fundem ou omitem fases dependendo de sua natureza (prescritivo, iterativo, ágil).

---

### 3.2 Disciplinas

Conjunto de atividades correlacionadas que compõem o processo. Exemplos:
- Produção: Análise de requisitos, modelagem, codificação, testes.
- Apoio: Gerência de projeto, ambiente, configuração, portfólio.

> No UP, disciplinas são ortogonais às fases. No modelo cascata, fases e disciplinas são coincidentes.

---

### 3.3 Atividades

Toda atividade possui:
- **Objetivo principal**
- **Entradas e saídas (artefatos)**
- **Responsáveis e participantes**
- **Recursos necessários**
- **Passos, procedimentos e regras**

> Atividades são descritas por documentos detalhados, podendo incluir fluxogramas, UML ou BPMN.

---

## 📄 4. Documentação de Atividades

As atividades são documentadas com um **template** padrão contendo:

- Identificação da fase, disciplina e atividade
- Responsável e participantes
- Artefatos de entrada e saída
- Recursos (humanos e físicos)
- Passos (com pré-condições, regras e procedimentos específicos)

### Exemplo de atividade:
> Atividade 1.2.5 - Captura de Requisitos a partir de Entrevistas

Com passos como:
1. Listar requisitos funcionais
2. Listar requisitos não funcionais
3. Agrupar requisitos em pacotes
4. Gerar o documento de requisitos

---

## 👥 5. Equipe de Processo

- Responsável por manter, avaliar e otimizar o processo.
- Deve ser composta por **1 a 3%** dos profissionais envolvidos no desenvolvimento de software.
- Pode ser um único funcionário em empresas pequenas.

---

## 🏭 6. Processos da Indústria de Software (ISO/IEC/IEEE 12207:2017)

A norma define categorias de processos:

### 🔹 Processos de Acordo
- **Aquisição e fornecimento** entre cliente e fornecedor.

### 🔹 Processos Organizacionais
- Suporte e viabilização, como:
  - Garantia da qualidade
  - Gerenciamento de RH, conhecimento, infraestrutura

### 🔹 Processos de Gerenciamento Técnico
- Ligados diretamente ao produto:
  - Planejamento
  - Controle e avaliação
  - Gerência de riscos, decisões, configuração

### 🔹 Processos Técnicos
- Relacionados à produção direta do software:
  - Requisitos, arquitetura, design, codificação
  - Verificação, validação, integração, manutenção

> A organização deve declarar quais processos, atividades e tarefas da norma serão seguidos, não sendo obrigatório usar todos.

---

## 📚 Considerações Finais

- O processo deve ser **adaptável e evolutivo**.
- A documentação deve ser clara, sem ser excessivamente detalhada.
- Modelos mais maduros (como RUP e DAD) já apresentam documentação em **formato de hipertexto**.

---
