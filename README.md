# SLA de Cadastro

Projeto em Python para cálculo e organização de indicadores de SLA (Service Level Agreement) a partir de uma base tratada de dados.

## Objetivo

Automatizar o cálculo do tempo entre a emissão e a finalização de cada registro, validar inconsistências de datas, classificar o atendimento conforme uma meta de SLA e gerar uma nova base pronta para análise em ferramentas de Business Intelligence.

## O que o projeto faz

O script:

- lê uma base tratada em Excel;
- valida se as colunas obrigatórias estão presentes;
- converte as datas de emissão e finalização;
- calcula o tempo total entre os eventos;
- identifica registros com datas ausentes;
- identifica casos em que a finalização ocorre antes da emissão;
- classifica os registros conforme a meta de SLA;
- gera o tempo decorrido em dias, horas e minutos;
- calcula o SLA em dias para análises e médias;
- gera uma nova planilha pronta para uso em BI.

## Regra de SLA

Neste projeto, a meta utilizada é de:

**48 horas corridas**

Os registros são classificados como:

- `DENTRO DA META` — duração entre 0 e 48 horas;
- `ATRASADO` — duração acima de 48 horas;
- `SEM DATA` — emissão ou finalização ausente/inválida;
- `DATA INCONSISTENTE` — finalização anterior à emissão.

Valores negativos não são considerados no indicador `SLA Dias`, evitando que erros de origem contaminem médias e demais análises.

## Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL

## Estrutura do projeto

```text
sla_cadastro.py/
├── src/
│   └── sla_cadastro.py
├── data/
│   ├── input/
│   └── output/
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Coloque a base tratada em:

```text
data/input/crm_limpeza_final.xlsx
```

3. Execute:

```bash
python src/sla_cadastro.py
```

4. A saída será gerada em:

```text
data/output/base_geral_cadastro.xlsx
```

## Observação

O projeto representa uma rotina operacional de tratamento de dados e foi estruturado para portfólio sem incluir bases reais ou informações sensíveis.