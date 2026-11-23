"""Conexao e funcoes utilitarias do PostgreSQL."""
import uuid
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
#import os
#from dotenv import load_dotenv
import config

def conectar():
    """Abre conexão com o PostgreSQL."""
    return psycopg2.connect(**config.DB_CONFIG)

def get_engine():
    """
    Retorna engine do PostgreSQL.
    Engine SQL Alchemy é uma ferramenta de ORM (Object Relational Mapper)
      que permite mapear classes Python para tabelas do banco de dados 
      e realizar operações de forma mais intuitiva.
    """
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL

    cfg = config.DB_CONFIG
    #print(f"Configurações do banco: {cfg}")
    url = URL.create(
        "postgresql+psycopg2",
        username=cfg["user"],
        password=cfg["password"],
        host=cfg["host"],
        port=int(cfg["port"]),
        database=cfg["database"],
    )
    return create_engine(url)