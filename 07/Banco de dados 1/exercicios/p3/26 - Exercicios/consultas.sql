-- 1
SELECT p.nome AS nomepessoa, pr.nome AS profissao
FROM pessoa p
JOIN profissao_pessoa pp ON p.codigo = pp.codigo_pessoa
JOIN profissao pr ON pp.codigo_profissao = pr.codigo
WHERE pr.nome LIKE '%Advogado%';

-- 2
SELECT p.nome AS nomepessoa, pr.nome AS profissao, pr.area, pp.salario,
       CASE WHEN pp.salario <= 10000 THEN 'Promove' ELSE 'Permanece' END AS status
FROM pessoa p
JOIN profissao_pessoa pp ON p.codigo = pp.codigo_pessoa
JOIN profissao pr ON pp.codigo_profissao = pr.codigo
WHERE pr.area = 'TI'
ORDER BY status;

-- 3
SELECT p.nome AS nome_pessoa, pr.nome AS nome_profissao
FROM pessoa p
FULL OUTER JOIN profissao_pessoa pp ON p.codigo = pp.codigo_pessoa
FULL OUTER JOIN profissao pr ON pp.codigo_profissao = pr.codigo;

-- 4
SELECT pr.area AS area_prof, COUNT(*) AS qtd_prof, AVG(pp.salario) AS media_salarial
FROM profissao pr
JOIN profissao_pessoa pp ON pr.codigo = pp.codigo_profissao
WHERE pp.data_inicio >= '2010-01-01' AND pp.data_fim IS NOT NULL
GROUP BY pr.area
HAVING AVG(pp.salario) > 8000
ORDER BY media_salarial DESC;

-- 5
SELECT p.nome, p.data_de_nascimento
FROM pessoa p
JOIN profissao_pessoa pp ON p.codigo = pp.codigo_pessoa
JOIN profissao pr ON pp.codigo_profissao = pr.codigo
GROUP BY p.codigo, p.nome, p.data_de_nascimento
HAVING COUNT(DISTINCT pp.codigo_profissao) > 1
   AND SUM(CASE WHEN pr.area IN ('Direito', 'Educação') THEN 1 ELSE 0 END) = 0
ORDER BY p.data_de_nascimento ASC;
