# ========================
# Primeiro query
# ========================

CREATE TABLE pessoa (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER,
    email VARCHAR(100)
);

CREATE TABLE profissao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE pessoa_profissao (
    id SERIAL PRIMARY KEY,
    pessoa_id INTEGER NOT NULL,
    profissao_id INTEGER NOT NULL,

    FOREIGN KEY (pessoa_id) REFERENCES pessoa(id),
    FOREIGN KEY (profissao_id) REFERENCES profissao(id)
);

# ========================
# Segundo query
# ========================

INSERT INTO profissao (nome) VALUES
('Professor'),
('Programador'),
('Advogado'),
('Médico'),
('Designer'),
('Engenheiro'),
('Enfermeiro');