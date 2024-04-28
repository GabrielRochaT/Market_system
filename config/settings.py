from dotenv import load_dotenv
import os

try:
    load_dotenv()
    USER = os.environ["USER"]
    PASSWORD = os.environ["PASSWORD"]
    HOST = os.environ["HOST"]

except Exception as err:
    raise Exception(f"Erro ao carregar variáveis de ambiente! {err}")