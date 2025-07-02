from passlib.context import CryptContext

# Define o contexto de criptografia usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para gerar hash da senha
def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

# Função para verificar se a senha digitada confere com a do banco
def verificar_senha(senha_plain: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_plain, senha_hash)
