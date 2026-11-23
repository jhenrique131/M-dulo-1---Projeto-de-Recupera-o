import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ZIP_PATH = DATA_DIR / "viagens_2025_6meses.zip"

# ID do arquivo .zip no Google Drive
DRIVER_FILE_ID = "1pQjKacyHdIsyteknQbwKGM5_4hL5V4RV"
# https://drive.google.com/file/d/1pQjKacyHdIsyteknQbwKGM5_4hL5V4RV/view?usp=drive_link
CHUNK_SIZE = 50_000
CSV_SEP = ";"
CSV_ENCODING = "latin-1"

DB_CONFIG = {
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "123456"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "viagens_servico"),
}
# tabela Raw - Arquivo CSV original, sem tratamento
ARQUIVOS_RAW = {
    "raw_viagem": "2025_Viagem.csv",
    "raw_pagamento": "2025_Pagamento.csv",
    "raw_passagem": "2025_Passagem.csv",
    "raw_trecho": "2025_Trecho.csv",
}
