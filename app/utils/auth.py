from passlib.context import CryptContext
from cryptography.fernet import Fernet
import os

# ==== Criptografia de senha com bcrypt ====
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha_plain: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_plain, senha_hash)

# ==== Criptografia de dados sensíveis (AES via Fernet) ====

# Você deve armazenar esta chave com segurança (ex: variável de ambiente ou cofre)
CHAVE_CRIPTO = os.environ.get("CHAVE_CRIPTO")
if not CHAVE_CRIPTO:
    # Gera uma nova chave se não existir
    CHAVE_CRIPTO = Fernet.generate_key()
    print("Chave gerada (salve com segurança):", CHAVE_CRIPTO.decode())

fernet = Fernet(CHAVE_CRIPTO)

def criptografar_dado(dado: str) -> str:
    return fernet.encrypt(dado.encode()).decode()

def descriptografar_dado(dado_cripto: str) -> str:
    return fernet.decrypt(dado_cripto.encode()).decode()
