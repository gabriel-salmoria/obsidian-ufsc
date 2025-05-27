##  Modelos de Processo Prescritivos

O capítulo explora diferentes abordagens prescritivas de desenvolvimento de software. Estes modelos são estruturados e orientados por fases, documentos e critérios claros de transição. Os modelos variam conforme o grau de formalidade, foco em testes, tratamento de riscos ou flexibilidade. São também chamados de "ciclos de vida" do software.

## 1. Codificar e Consertar (Code and Fix)
Modelo informal e ad-hoc, onde:
- Começa com uma ideia vaga do sistema.
- Parte-se diretamente para a implementação.
- As correções são feitas à medida que o cliente aponta erros.
- Testes são superficiais e não sistemáticos.

**Problemas:**
- Baixa previsibilidade.
- Código difícil de manter.
- Altos riscos e difícil controle de qualidade.

**Vantagens limitadas:**
- Agilidade inicial.
- Simples de entender.
- Útil apenas para sistemas muito pequenos ou descartáveis.

---

## 2. Modelo Cascata (Waterfall)
Modelo clássico e sequencial com fases distintas:
1. Requisitos
2. Projeto (arquitetural e detalhado)
3. Implementação
4. Testes
5. Entrega
6. Manutenção

**Características:**
- Documentação extensiva.
- Revisões entre fases.
- Progressão rígida entre etapas.

**Críticas:**
- Dificuldade de adaptação a mudanças.
- Descobertas tardias geram muito retrabalho.
- Apenas desenvolvedores experientes entendem a documentação técnica.

---

## 3. Modelo Sashimi (Cascata Entrelaçado)
- Introduz sobreposição entre fases.
- A análise continua durante o design, e o design continua durante a codificação.

**Vantagens:**
- Reduz a rigidez do Modelo Cascata.
- Possibilita identificação precoce de erros.

**Problemas:**
- Dificuldade de gestão.
- Marcos pouco definidos.

---

## 4. Modelo V
- Extensão do Modelo Cascata com ênfase em testes.
- Cada fase de desenvolvimento tem uma fase de teste correspondente.

**Destaques:**
- Testes unitários, de integração e de sistema.
- Verificação e validação contínuas.

**Desvantagens:**
- Compartilha limitações do Modelo Cascata.
- Dificuldade com mudanças de requisitos.

---

## 5. Modelo W
- Aperfeiçoamento do Modelo V.
- Planejamento de testes começa nas fases iniciais.
- Inclui depuração e replanejamento.

**Benefícios:**
- Antecipação de problemas de testabilidade.
- Design mais coeso e simples.

---

## 6. Cascata com Subprojetos
- Divide o sistema em subsistemas que podem ser desenvolvidos paralelamente.
- Favorece modularidade.

**Desafios:**
- Integração final complexa.
- Exige bom planejamento arquitetural.

---

## 7. Cascata com Redução de Risco
- Acrescenta fase inicial focada na redução de incertezas.
- Utiliza técnicas como protótipos, entrevistas e storyboards.

**Uso ideal:**
- Projetos com requisitos vagos ou muito riscos técnicos.

---

## 8. Modelo Espiral
- Iterativo e orientado à redução de risco.
- Cada ciclo aborda um risco significativo, seguido por planejamento e prototipação.

**Etapas de cada ciclo:**
1. Determinação de objetivos.
2. Análise e mitigação de riscos.
3. Desenvolvimento e verificação.
4. Planejamento da próxima iteração.

**Indicado para:**
- Projetos complexos e de P&D.

---

## 9. Prototipação Evolucionária
- Protótipos são gradualmente refinados até se tornarem o sistema final.
- Requisitos são descobertos durante o processo.

**Perigos:**
- Pode regredir ao modelo "Codificar e Consertar" se mal gerenciado.

---

## 10. Entrega em Estágios
- O sistema é entregue em partes funcionais já finalizadas.
- Baseia-se em planejamento técnico e gerencial rigoroso.

**Vantagens:**
- Entregas contínuas.
- Feedback e evolução mais ágeis.

---

## 11. Modelo Orientado a Cronograma
- Iterações têm duração fixa.
- Funcionalidades mais importantes são priorizadas.

**Objetivo:**
- Garantir entregas mínimas até o prazo final, mesmo que parciais.

---

## 12. Entrega Evolucionária
- Combinação entre prototipação e entrega em estágios.
- Pode acomodar mudanças de escopo conforme feedback do cliente.

**Flexível:**
- Pode priorizar mudanças ou seguir plano original conforme decisão de gestão.

---

## 13. Modelos Orientados a Ferramentas
- Modelos que dependem fortemente de CASE tools ou geradores de código.
- Alta produtividade, mas limitados às capacidades das ferramentas.

**Exemplos:**
- jCompany, WebRatio.

---

## 14. Linhas de Produto de Software (SPL)
- Baseadas em reuso sistemático de um núcleo comum de componentes.
- Ideal para famílias de produtos similares.

**Requisitos:**
- Boa arquitetura.
- Investimento inicial elevado.
- Três atividades principais:
  - Desenvolvimento do núcleo de ativos.
  - Desenvolvimento dos produtos.
  - Gerência da linha de produtos.

**Quando aplicar:**
- Três ou mais produtos semelhantes.
- Necessidade de personalizações planejadas.

---

## Reflexões Finais do Capítulo
- Nenhum modelo é universalmente melhor.
- Muitas vezes, combinar modelos é o mais adequado.
- A escolha deve considerar:
  - Estabilidade dos requisitos
  - Conhecimento da arquitetura
  - Cronograma
  - Nível de risco
  - Tamanho da equipe e do projeto

**Recomendação:**
> "É mais útil escolher um modelo simples e bem executado do que um sofisticado mal gerenciado."

