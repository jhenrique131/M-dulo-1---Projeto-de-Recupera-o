import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ZIP_PATH = DATA_DIR / "viagens_2025_6meses.zip"

#ID do arquivo .zip no Google Drive
DRIVER_FILE_ID = "1pQjKacyHdIsyteknQbwKGM5_4hL5V4RV"
#https://drive.google.com/file/d/1pQjKacyHdIsyteknQbwKGM5_4hL5V4RV/view?usp=drive_link
CHUNK_SIZE = 50_000
CSV_SEP = ";"
CSV_ENCODING = "latin-1"