import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("ERRO: A variável de ambiente GOOGLE_API_KEY não está configurada em .env.")
    exit()