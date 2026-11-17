---
tags: [bd2, indice]
disciplina: INE5432 - Banco de Dados II (2026-2)
professor: Renato Fileto
---
# INE5432 · Banco de Dados II: Índice e Guia da P2

[Moodle](https://presencial.moodle.ufsc.br/course/view.php?id=50499) · [Informações da disciplina](https://presencial.moodle.ufsc.br/mod/page/view.php?id=1625418) · [Plano de ensino](https://programas-planos.inf.ufsc.br/disciplinas/INE5432/turmas/07208/plano/20262) · [Vídeos Lemahieu (Principles of DB Management)](https://www.youtube.com/watch?v=o36Z_OqC2ac&list=PLdQddgMBv5zHcEN9RrhADq3CBColhY2hl)

## 📅 Prova 2
| | |
|---|---|
| **Data** | **Quarta, 25/11/2026, 16:20–18:00** (aula no CTC203). Vem do planejamento de aulas do professor; ainda **não** há quiz da P2 criado no Moodle nem aviso no fórum. |
| **Revisão** | Segunda, **23/11**: revisão, dúvidas e exercícios para a P2 (ENS213) |
| **Depois** | 30/11 correção e vista · 02/12 e 07/12 recuperação · 09/12 prova de recuperação |
| **Consulta** | Pela regra da P1: **pode** consultar o conteúdo do Moodle, livros, manuais e páginas Web. **Não pode** se comunicar com outros alunos. |
| **Formato provável** (igual à P1) | **Parte 1**: quiz no Moodle (P1: classificar escalonamento + contas de B+-tree, 3 + 3 pts). **Parte 2**: tarefa com **upload de PDF** (P1: árvore de consulta otimizada, 4 pts, correção manual, 15 min de tolerância). O PDF também leva **resoluções e justificativas sucintas** das questões da Parte 1. **Provas diferentes** são sorteadas entre os alunos. |

## 🧭 O que cai na P2
No Moodle há o marcador **"FIM DA MATÉRIA DA PRIMEIRA PROVA!!!"** logo depois do Exercício 3.2. Tudo depois dele é P2:

| Tópico | Livro (E&N 7ª ed. / 6ª PT) | Nota | Exercícios no Moodle |
|---|---|---|---|
| Trancas e **2PL** (variantes), deadlock | cap. 21 / cap. 22 | [[01 - Controle de Concorrência - Trancas e 2PL]] | **Ex. 3.3** (não feito) · **E3** ✅ |
| Timestamps, multiversão, otimista, **níveis de isolamento** | cap. 21 / cap. 22 | [[02 - Outros Métodos de Concorrência e Níveis de Isolamento]] | página "Níveis de isolamento" |
| **Recuperação de falhas** (log, WAL, UNDO/REDO, adiada/imediata, shadowing, checkpoint) | cap. 22 / cap. 23 | [[03 - Recuperação de Falhas]] | **L2** ✅ |
| **BDD**: conceitos, Date & Codd, CAP, **fragmentação**, replicação, LAV/GAV | cap. 23 / cap. 25 | [[04 - BDD - Conceitos, Fragmentação e Replicação]] | Ex. 4.1, 4.2, 4.5 |
| **BDD**: processamento de consultas (semi-join, agregação parcial, tráfego) | cap. 23 / cap. 25 | [[05 - BDD - Processamento de Consultas]] | Ex. 4.2, 4.3, 4.5 · **E4** ✅ |
| **BDD**: **2PC**, locks distribuídos, deadlock distribuído | cap. 23 / cap. 25 | [[06 - BDD - Transações, 2PC e Deadlock]] | **Ex. 4.4** (não feito) · **E4** ✅ |
| Base da P1 que continua sendo cobrada (escalonamentos) | cap. 20 / cap. 21 | [[00 - Base - Caracterização de Escalonamentos]] | E3 |

**Incerto**: as aulas de 11, 16 e 18/11 foram "apresentações de trabalhos e **temas avançados**". O programa lista "Tópicos em BDs" (SQL embutida/cursores, integração de dados, BDs não convencionais, recuperação de informação), mas não há exercício disso. Pergunte na revisão de 23/11 se entra.

## ✅ O que faltava no vault (e o que ainda falta)
Antes não existia **nada** de BD2 no vault. Agora tem:
- [x] Slides das 2 unidades da P2 (+ os da P1), exportados do Google Slides do professor → `slides/p1`, `slides/p2`
- [x] Anotações de todos os tópicos da P2 (`anotacoes/`)
- [x] [[Banco de Questões P2]]: E3, L2 e E4 com respostas e explicação, mais o Ex. 3.2 corrigido
- [x] [[Exercícios 4.1 a 4.5 - BDD]]: enunciados + roteiro de resolução
- [ ] **Fazer no Moodle o Exercício 3.3 (2PL) e o Exercício 4.4 (2PC)**. Ainda não têm tentativa, e as perguntas só aparecem ao abrir o quiz.
- [ ] **Livro-texto** (Elmasri & Navathe 7ª ed. EN e 6ª ed. PT) e **Özsu & Valduriez**: o professor marcou como **"acesso emergencial e privado (não redistribuir)"**, então **não coloquei no vault** (ele vai para o GitHub público). Use pelo Moodle: [E&N 7ª](https://presencial.moodle.ufsc.br/mod/resource/view.php?id=1625421) · [E&N 6ª PT](https://presencial.moodle.ufsc.br/mod/resource/view.php?id=1625422) · [Özsu](https://presencial.moodle.ufsc.br/mod/resource/view.php?id=1625423)
- [ ] O deck "Integração de Dados" (tópicos avançados) não é público no Google Slides e não baixou.
- [ ] Os slides **não têm** a seção de técnicas de recuperação (o índice cita, mas o PDF acaba antes). Leia o **cap. 22 (7ª ed.)** do livro.

## 📚 Slides
| Unidade | Arquivo | Prova |
|---|---|---|
| 1. Organização e acesso a dados em disco | [[01 - Organização e acesso a dados em disco.pdf]] | P1 |
| 2. Processamento e otimização de consultas | [[02 - Processamento e otimização de consultas.pdf]] | P1 |
| 3. Transações, concorrência e recuperação | [[03 - Transações, concorrência e recuperação.pdf]] | P1 até o marcador, **P2 depois** (2PL em diante) |
| 4a. BDs descentralizados | [[04a - Sistemas de BDs descentralizados.pdf]] | P2 |
| 4b. BDs distribuídos | [[04b - Bancos de dados distribuídos.pdf]] | P2 |
