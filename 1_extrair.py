"""Fase 1 - Extracao e carga da camada Raw.

Baixa o .zip do Google Drive, le os 4 CSVs em blocos e carrega nas tabelas
Raw sem alterar o conteudo. Idempotente (TRUNCATE) e resiliente (try/except).
"""

import logging
import sys
import zipfile
from pathlib import Path
import gdown
import pandas as pd
import config
from banco import conectar, executar, inserir_em_lote
import psycopg2

try:
    #Abre a conexão utilizando as configurações do banco.py
    conn = conectar()
    conn.autocommit = True
    cursor = conn.cursor()

    # Abrir e ler o arquivo SQL original 
    with open('0_criar_banco.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()

 
    #Divide o script por ponto e vírgula para executar comando por comando
    sql_comandos = [cmd.strip() for cmd in sql_script.split(";") if cmd.strip()]

    for comando in sql_comandos:
        # CREATE DATABASE para gerenciar a conexão nativamente.
        if "CREATE DATABASE" in comando or "viagens_servico" in comando or comando.startswith("\\"):
            continue
        cursor.execute(comando)
        
    #Fecha os cursores de forma segura
    cursor.close()
    conn.close()
    print("Estrutura de tabelas (RAW e SILVER) recriada com sucesso!")

except Exception as e:
    print(f"Erro ao inicializar o banco de dados: {e}")
    print("Verifique se o banco 'viagens_servico' já foi criado no seu PostgreSQL.")
####################################################################################
####################################################################################
####################################################################################

#Início do Script 1_extrair.py

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("extrair")

def baixar_zip():
    """Baixa o .zip da fonte oficial (Google Drive)."""
    if config.DRIVER_FILE_ID.startswith("https://drive.google.com"):
        raise ValueError("Defina DRIVE_FILE_ID em config.py como o ID do arquivo, não a URL completa.")
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    url = f"https://drive.google.com/uc?id={config.DRIVER_FILE_ID}"
    log.info(f"Baixando arquivo .zip do Google Drive: {url}")
    caminho = gdown.download(url, str(config.ZIP_PATH), quiet=False)
    if not caminho:
        raise RuntimeError("Falha ao baixar o arquivo .zip do Google Drive.")
    return Path(caminho)