## Processo Unificado (UP)

O Processo Unificado (UP) é um framework de desenvolvimento de software que combina abordagens prescritivas e ágeis, centrado na orientação a objetos e fortemente integrado ao uso da UML. Ele é iterativo, incremental, centrado na arquitetura e dirigido por casos de uso.

---

## 5.1 Características do Processo Unificado

### Dirigido por Casos de Uso
- Casos de uso são a base para:
  - Definição da arquitetura
  - Criação de testes
  - Planejamento de iterações
  - Documentação do usuário
- São fundamentais para organizar os requisitos funcionais.

### Centrado na Arquitetura
- A arquitetura é incrementada a cada iteração com as funcionalidades definidas pelos casos de uso.
- É entendida como um modelo que organiza componentes, operações e camadas.

### Iterativo e Incremental
- Cada iteração gera valor através de entregas parciais.
- Todas as disciplinas (análise, design, teste, etc.) ocorrem em cada iteração com intensidade variável.

### Focado em Riscos
- Os casos de uso mais críticos são tratados primeiro.
- Ajuda a mitigar riscos cedo, com custo e impacto menores.

---

## 5.2 Fases do Processo Unificado

### Concepção
- Estabelece visão do sistema, principais requisitos e plano preliminar.
- Produz um conjunto inicial de casos de uso e verifica viabilidade do projeto.
- Marco: **LCO (Lifecycle Objective Milestone)**

### Elaboração
- Refina requisitos e desenvolve a arquitetura executável.
- Elimina riscos principais.
- Marco: **LCA (Lifecycle Architecture Milestone)**

### Construção
- Produz código funcional e testado.
- Incorpora todos os casos de uso detalhados.
- Marco: **IOC (Initial Operational Capability Milestone)**

### Transição
- Coloca o sistema em produção.
- Inclui testes de aceitação, treinamento e migração de dados.
- Marco: **PR (Product Release Milestone)**

---

## 5.3 RUP – Rational Unified Process

O RUP é a implementação mais completa do UP, criada pela Rational (IBM). É fortemente orientado a ferramentas e práticas formais.

### Princípios do RUP
- Iteratividade orientada a riscos
- Gerência de requisitos
- Arquitetura baseada em componentes
- Modelagem visual com UML
- Verificação contínua da qualidade
- Controle de mudanças

### Blocos do RUP
- **Papéis:** atividades atribuídas a perfis (analista, desenvolvedor, testador etc.)
- **Atividades:** trabalhos atribuídos a papéis com entregáveis concretos
- **Artefatos:** documentos, diagramas, código, etc.
- **Workflows:** grafos que relacionam atividades e dependências

### Disciplinas
- **Projeto:** Modelagem de negócio, Requisitos, Análise/Design, Implementação, Teste, Implantação
- **Suporte:** Gerência de configuração, Projeto, Ambiente

---

## 5.4 EUP – Enterprise Unified Process

Extensão do RUP para o ciclo de vida organizacional completo.

### Novas fases:
- **Produção:** manutenção e evolução do sistema em uso.
- **Desativação:** retirada planejada do sistema.

### Novas disciplinas:
- Operação e suporte
- Modelagem de negócio da empresa
- Gerência de portfólio
- Arquitetura da empresa
- Reuso estratégico
- Gerência de pessoas
- Administração
- Melhoria de processo de software

---

## 5.5 RUP-SE – RUP para Engenharia de Sistemas

Voltado a sistemas complexos com software, hardware e processos humanos.

### Ponto de vista da arquitetura:
- Empresa, Computação, Engenharia, Informação, Processo

---

## 5.6 OUM – Oracle Unified Method

Implementação do UP voltada ao ecossistema Oracle.

### Fases:
- Inception, Elaboration, Construction, Transition, Production

### Disciplinas adicionais:
- Gerência de performance, Arquitetura técnica, Conversão de dados, Documentação, Adoção e aprendizado, etc.

---

## 5.7 DAD – Disciplined Agile Delivery

Framework ágil híbrido, orientado a pessoas, aprendizado e entrega de valor.

### Características:
- Baseado em Scrum, XP, UP, Lean, Kanban
- Mais papéis (primários e secundários)
- Centrado em objetivos e escalável

---

## 5.8 OpenUP – Open Unified Process

Versão leve e aberta do UP mantida pela Eclipse Foundation.

### Características:
- Baixa cerimônia
- Independente de ferramenta
- Adota incrementalmente práticas do UP
- Princípios: colaboração, evolução, balanceamento de prioridades, foco em arquitetura

---