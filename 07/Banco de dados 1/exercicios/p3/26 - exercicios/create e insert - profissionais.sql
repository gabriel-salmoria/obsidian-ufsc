-- Criação da tabela pessoa
CREATE TABLE pessoa (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_de_nascimento DATE
);

-- Criação da tabela profissao
CREATE TABLE profissao (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    area VARCHAR(50)
);

-- Criação da tabela profissao_pessoa
CREATE TABLE profissao_pessoa (
    codigo_pessoa INT,
    codigo_profissao INT,
    data_inicio DATE NOT NULL,
    data_fim DATE NULL, -- Pode ser nulo caso a pessoa ainda esteja atuando
    salario DECIMAL(10, 2),
    PRIMARY KEY (codigo_pessoa, codigo_profissao, data_inicio),
    FOREIGN KEY (codigo_pessoa) REFERENCES pessoa(codigo),
    FOREIGN KEY (codigo_profissao) REFERENCES profissao(codigo)
);

-- Inserindo 30 Pessoas
INSERT INTO pessoa (codigo, nome, email, telefone, data_de_nascimento) VALUES
(1, 'Ana Clara Silva', 'ana.clara@email.com', '(11) 99999-1111', '1985-04-12'),
(2, 'Bruno Souza', 'bruno.souza@email.com', '(21) 98888-2222', '1990-07-23'),
(3, 'Carlos Eduardo Costa', 'carlos.costa@email.com', '(31) 97777-3333', '1982-11-05'),
(4, 'Daniela Almeida', 'daniela.almeida@email.com', '(41) 96666-4444', '1995-02-18'),
(5, 'Eduardo Lima', 'eduardo.lima@email.com', '(51) 95555-5555', '1979-09-30'),
(6, 'Fernanda Gomes', 'fernanda.gomes@email.com', '(61) 94444-6666', '1988-12-14'),
(7, 'Gabriel Martins', 'gabriel.martins@email.com', '(71) 93333-7777', '1992-05-21'),
(8, 'Helena Rodrigues', 'helena.rodrigues@email.com', '(81) 92222-8888', '1980-03-08'),
(9, 'Igor Pereira', 'igor.pereira@email.com', '(91) 91111-9999', '1998-10-10'),
(10, 'Julia Carvalho', 'julia.carvalho@email.com', '(11) 90000-0000', '1986-06-25'),
(11, 'Kleber Santos', 'kleber.santos@email.com', '(21) 99999-2222', '1975-01-15'),
(12, 'Larissa Mendes', 'larissa.mendes@email.com', '(31) 98888-3333', '1993-08-09'),
(13, 'Marcelo Rocha', 'marcelo.rocha@email.com', '(41) 97777-4444', '1981-04-03'),
(14, 'Natália Ferreira', 'natalia.ferreira@email.com', '(51) 96666-5555', '1989-11-28'),
(15, 'Otávio Ribeiro', 'otavio.ribeiro@email.com', '(61) 95555-6666', '1996-07-17'),
(16, 'Patrícia Castro', 'patricia.castro@email.com', '(71) 94444-7777', '1983-02-02'),
(17, 'Quintino Moraes', 'quintino.moraes@email.com', '(81) 93333-8888', '1978-09-22'),
(18, 'Renata Nunes', 'renata.nunes@email.com', '(91) 92222-9999', '1991-12-05'),
(19, 'Sérgio Barbosa', 'sergio.barbosa@email.com', '(11) 91111-1111', '1984-05-19'),
(20, 'Tatiane Araújo', 'tatiane.araujo@email.com', '(21) 90000-2222', '1994-10-31'),
(21, 'Umberto Teixeira', 'umberto.teixeira@email.com', '(31) 99999-3333', '1976-03-27'),
(22, 'Vitória Cardoso', 'vitoria.cardoso@email.com', '(41) 98888-4444', '1987-08-14'),
(23, 'Wagner Pires', 'wagner.pires@email.com', '(51) 97777-5555', '1997-01-08'),
(24, 'Xuxa Meneghel', 'xuxa.m@email.com', '(61) 96666-6666', '1963-03-27'),
(25, 'Yuri Machado', 'yuri.machado@email.com', '(71) 95555-7777', '1999-06-11'),
(26, 'Zélia Duncan', 'zelia.d@email.com', '(81) 94444-8888', '1964-10-28'),
(27, 'Alberto Diniz', 'alberto.diniz@email.com', '(91) 93333-9999', '1982-12-30'),
(28, 'Beatriz Viana', 'beatriz.viana@email.com', '(11) 92222-0000', '2001-02-15'), -- Sem profissão
(29, 'Caio Borges', 'caio.borges@email.com', '(21) 91111-1234', '2000-09-04'), -- Sem profissão
(30, 'Diana Silva', 'diana.silva@email.com', '(31) 90000-5678', '2002-11-20'); -- Sem profissão

-- Inserindo 30 Profissões
INSERT INTO profissao (codigo, nome, area) VALUES
(1, 'Engenheiro de Software', 'TI'),
(2, 'Analista de Dados', 'TI'),
(3, 'Cientista de Dados', 'TI'),
(4, 'Administrador de Banco de Dados', 'TI'),
(5, 'Especialista em Segurança', 'TI'),
(6, 'Médico Clínico', 'Saúde'),
(7, 'Enfermeiro', 'Saúde'),
(8, 'Fisioterapeuta', 'Saúde'),
(9, 'Psicólogo', 'Saúde'),
(10, 'Nutricionista', 'Saúde'),
(11, 'Professor de Matemática', 'Educação'),
(12, 'Professor de História', 'Educação'),
(13, 'Pedagogo', 'Educação'),
(14, 'Coordenador Pedagógico', 'Educação'),
(15, 'Diretor Escolar', 'Educação'),
(16, 'Advogado Civil', 'Direito'),
(17, 'Advogado Trabalhista', 'Direito'),
(18, 'Juiz de Direito', 'Direito'),
(19, 'Promotor de Justiça', 'Direito'),
(20, 'Defensor Público', 'Direito'),
(21, 'Contador', 'Negócios'),
(22, 'Administrador de Empresas', 'Negócios'),
(23, 'Economista', 'Negócios'),
(24, 'Analista Financeiro', 'Negócios'),
(25, 'Consultor de Vendas', 'Negócios'),
(26, 'Engenheiro Civil', 'Engenharia'),
(27, 'Arquiteto', 'Engenharia'),
(28, 'Jornalista', 'Comunicação'), -- Sem pessoas vinculadas
(29, 'Publicitário', 'Comunicação'), -- Sem pessoas vinculadas
(30, 'Designer Gráfico', 'Comunicação'); -- Sem pessoas vinculadas

-- Inserindo 50 Ocorrências de Profissões e Pessoas
INSERT INTO profissao_pessoa (codigo_pessoa, codigo_profissao, data_inicio, data_fim, salario) VALUES
(1, 1, '2015-02-01', NULL, 12000.50),
(1, 2, '2010-01-15', '2015-01-31', 8500.00),
(2, 3, '2018-05-10', NULL, 14000.00),
(3, 4, '2012-03-20', '2020-12-31', 9500.00),
(3, 5, '2021-01-01', NULL, 15500.75),
(4, 6, '2019-08-01', NULL, 18000.00),
(5, 7, '2011-04-10', NULL, 6500.00),
(6, 8, '2016-11-22', '2022-05-15', 5500.00),
(6, 9, '2022-06-01', NULL, 7200.00),
(7, 10, '2014-09-05', NULL, 6800.00),
(8, 11, '2005-02-15', '2015-12-20', 4500.00),
(8, 14, '2016-01-10', NULL, 8000.00),
(9, 12, '2020-03-01', NULL, 5000.00),
(10, 13, '2013-07-15', NULL, 5200.00),
(11, 15, '2010-02-01', NULL, 11000.00),
(12, 16, '2017-08-10', NULL, 9500.00),
(13, 17, '2008-05-20', '2018-04-30', 8500.00),
(13, 16, '2018-05-01', NULL, 12000.00),
(14, 18, '2021-01-15', NULL, 32000.00),
(15, 19, '2019-10-01', NULL, 28000.00),
(16, 20, '2015-06-01', NULL, 24000.00),
(17, 21, '2005-03-10', NULL, 7800.00),
(18, 22, '2016-02-15', '2021-09-30', 9000.00),
(18, 23, '2021-10-01', NULL, 13500.00),
(19, 24, '2012-11-01', NULL, 10500.00),
(20, 25, '2018-04-10', NULL, 6000.00),
(21, 26, '2009-08-25', NULL, 14500.00),
(22, 27, '2014-05-15', '2020-12-10', 8000.00),
(22, 26, '2021-01-05', NULL, 12500.00),
(23, 1, '2022-03-01', NULL, 9500.00),
(24, 2, '2011-06-15', '2016-12-31', 7000.00),
(24, 3, '2017-01-01', NULL, 15000.00),
(25, 4, '2020-09-10', NULL, 8500.00),
(26, 5, '2013-02-20', '2019-11-30', 11000.00),
(26, 1, '2019-12-01', NULL, 16000.00),
(27, 6, '2010-01-10', NULL, 21000.00),
(1, 11, '2008-02-01', '2009-12-31', 3000.00), -- Pessoa 1 teve uma profissão antiga na educação
(2, 21, '2015-01-10', '2018-04-30', 5500.00),
(4, 8, '2014-03-01', '2019-07-31', 4500.00),
(5, 13, '2005-02-10', '2011-03-31', 3500.00),
(7, 24, '2010-08-01', '2014-08-31', 6000.00),
(9, 25, '2018-01-15', '2020-02-28', 4000.00),
(10, 22, '2009-05-10', '2013-06-30', 6500.00),
(11, 12, '2000-02-01', '2010-01-31', 4000.00),
(12, 17, '2014-01-15', '2017-07-31', 6000.00),
(14, 16, '2015-05-01', '2020-12-31', 11000.00),
(15, 20, '2016-03-10', '2019-09-30', 14000.00),
(17, 23, '2000-08-01', '2005-02-28', 5000.00),
(19, 21, '2008-01-15', '2012-10-31', 4500.00),
(21, 27, '2005-06-10', '2009-07-31', 7500.00);