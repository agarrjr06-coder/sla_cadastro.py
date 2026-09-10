# SLA de Cadastro

Projeto em Python para cálculo e organização de indicadores de SLA (Service Level Agreement) a partir de uma base tratada de dados.

## Objetivo

Automatizar o cálculo do tempo entre a emissão e a finalização de cada registro, classificando o atendimento conforme uma meta de SLA e gerando uma nova base pronta para análise em ferramentas de Business Intelligence.

## O que o projeto faz

O script:

- lê uma base tratada em Excel;
- converte as datas de emissão e finalização;
- calcula o tempo total entre os eventos;
- classifica os registros conforme a meta de SLA;
- gera o tempo decorrido em formato de dias e horas;
- calcula o SLA em dias para análises e médias;
- gera uma nova planilha pronta para uso em BI.

## Regra de SLA

Neste projeto, a meta utilizada é de:

**48 horas corridas**

Os registros são classificados como:

- `DENTRO DA META`
- `ATRASADO`
- `SEM DATA`

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
