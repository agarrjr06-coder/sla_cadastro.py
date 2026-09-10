# sla_cadastro.py
Este script em Python automatiza o processamento de indicadores de performance (SLA - Service Level Agreement) a partir de dados extraídos de um sistema CRM. Ele foi desenvolvido para facilitar a análise de eficiência no processo de faturamento e cadastro de notas fiscais

import pandas as pd
import numpy as np
import os

# --- CONFIGURAÇÕES DE CAMINHO ---
ARQUIVO_BASE = r"data\input\crm_limpeza_final.xlsx"
ARQUIVO_FINAL = r"data\output\Base_geral_cadastro.xlsx"

def calcular_sla_geral():
    try:
        if not os.path.exists(ARQUIVO_BASE):
            print(f"❌ ERRO: A base 'crm_limpeza_final' não foi encontrada.")
            return

        print("1. Lendo a base limpa...")
        df = pd.read_excel(ARQUIVO_BASE)

        # --- CONVERSÃO DE DATAS ---
        # Como as datas já estão no formato DD/MM/AAAA HH:MM:SS, vamos converter para cálculo
        df['dt_emissao'] = pd.to_datetime(df['Data Emissão'], dayfirst=True, errors='coerce')
        df['dt_finaliza'] = pd.to_datetime(df['Data finalização'], dayfirst=True, errors='coerce')

        # --- CÁLCULO DO SLA ---
        # Diferença em horas totais
        df['diff_horas'] = (df['dt_finaliza'] - df['dt_emissao']).dt.total_seconds() / 3600

        # 1. Status Meta (48 Horas Corridas)
        def definir_status(h):
            if pd.isna(h): return "SEM DATA"
            return "DENTRO DA META" if h <= 48 else "ATRASADO"
        
        df['Status SLA'] = df['diff_horas'].apply(definir_status)

        # 2. Tempo Formatado (Ex: 1d 4h)
        def formatar_tempo(h):
            if pd.isna(h): return "N/A"
            dias = int(h // 24)
            horas_restantes = int(h % 24)
            return f"{dias}d {horas_restantes}h"

        df['Tempo Total'] = df['diff_horas'].apply(formatar_tempo)

        # 3. SLA em Dias (Decimal para o BI fazer média)
        df['SLA Dias'] = (df['diff_horas'] / 24).round(2)

        # --- ORGANIZAÇÃO FINAL ---
        # Mantemos as colunas originais e adicionamos as de performance
        colunas_bi = [
            'Data Emissão', 'Marca', 'N° NF', 'Volume', 'Valor NF', 
            'Tipo NF', 'Responsável', 'Data finalização', 
            'Tempo Total', 'Status SLA', 'SLA Dias'
        ]

        print("2. Gerando Base Geral de Cadastro...")
        df[colunas_bi].to_excel(ARQUIVO_FINAL, index=False)
        
        print(f"✅ SUCESSO! Planilha 'Base_geral_cadastro' criada.")
        os.startfile(os.path.dirname(ARQUIVO_FINAL))

    except Exception as e:
        print(f"❌ Erro ao calcular SLA: {e}")

if __name__ == "__main__":
    calcular_sla_geral()
