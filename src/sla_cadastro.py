"""Cálculo de indicadores de SLA a partir de uma base tratada.

O script lê uma planilha com datas de emissão e finalização,
calcula o tempo decorrido entre os eventos e gera uma nova
planilha pronta para análise em BI.
"""

from pathlib import Path

import pandas as pd


INPUT_FILE = Path("data/input/crm_limpeza_final.xlsx")
OUTPUT_FILE = Path("data/output/base_geral_cadastro.xlsx")

SLA_LIMIT_HOURS = 48


def calculate_sla_hours(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula a diferença em horas entre emissão e finalização."""

    df = df.copy()

    df["dt_emissao"] = pd.to_datetime(
        df["Data Emissão"],
        dayfirst=True,
        errors="coerce",
    )

    df["dt_finaliza"] = pd.to_datetime(
        df["Data finalização"],
        dayfirst=True,
        errors="coerce",
    )

    df["diff_horas"] = (
        df["dt_finaliza"] - df["dt_emissao"]
    ).dt.total_seconds() / 3600

    return df


def define_status(hours: float) -> str:
    """Classifica o registro conforme a meta definida de SLA."""

    if pd.isna(hours):
        return "SEM DATA"

    if hours <= SLA_LIMIT_HOURS:
        return "DENTRO DA META"

    return "ATRASADO"


def format_time(hours: float) -> str:
    """Converte horas decimais para o formato dias e horas."""

    if pd.isna(hours):
        return "N/A"

    days = int(hours // 24)
    remaining_hours = int(hours % 24)

    return f"{days}d {remaining_hours}h"


def process_sla(
    input_file: Path = INPUT_FILE,
    output_file: Path = OUTPUT_FILE,
) -> None:
    """Executa o processamento completo do SLA."""

    if not input_file.exists():
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado: {input_file}"
        )

    print("1. Lendo a base tratada...")

    df = pd.read_excel(input_file)

    df = calculate_sla_hours(df)

    df["Status SLA"] = df["diff_horas"].apply(define_status)
    df["Tempo Total"] = df["diff_horas"].apply(format_time)
    df["SLA Dias"] = (df["diff_horas"] / 24).round(2)

    final_columns = [
        "Data Emissão",
        "Marca",
        "N° NF",
        "Volume",
        "Valor NF",
        "Tipo NF",
        "Responsável",
        "Data finalização",
        "Tempo Total",
        "Status SLA",
        "SLA Dias",
    ]

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("2. Gerando base final...")

    df[final_columns].to_excel(
        output_file,
        index=False,
    )

    print("✅ SUCESSO! Base de SLA gerada.")
    print(f"📁 Destino: {output_file}")


if __name__ == "__main__":
    process_sla()
