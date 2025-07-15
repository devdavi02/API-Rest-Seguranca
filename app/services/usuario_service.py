from sqlalchemy.orm import Session
from app.models.usuarios_model import Usuario, UsuarioCreate, UsuarioLogin
from app.repositories.usuarios_repository import buscar_por_email, salvar_usuario
from app.utils.auth import gerar_hash_senha, verificar_senha
from app.utils.crypto import Crypto

crypto = Crypto()
IGNORAR_CRIPTO = ["nome", "senha", "email"]

def cadastrar_usuario(dados: UsuarioCreate, db: Session):
    if buscar_por_email(db, dados.email):
        return {"erro": "Email já cadastrado"}
    
    usuario_dict = dados.dict()
    usuario_dict["senha"] = gerar_hash_senha(usuario_dict["senha"])

     # Criptografa todos os campos exceto os ignorados
    usuario_dict = crypto.criptografar_dict(usuario_dict, ignorar=IGNORAR_CRIPTO)

    novo_usuario = Usuario(**usuario_dict)

    salvar_usuario(db, novo_usuario)

    return {
        "mensagem": "Usuário cadastrado com sucesso",
        "usuario": {
            "nome": dados.nome,
            "email": dados.email
        }
    }

   # novo_usuario = Usuario(
       # nome=dados.nome,
        #idade=dados.idade,
        #cpf=dados.cpf,
        #telefone=dados.telefone,
        #email=dados.email,
        #senha=gerar_hash_senha(dados.senha)
   # )

   # return {"mensagem": "Usuário cadastrado com sucesso", "usuario": salvar_usuario(db, novo_usuario)}

def login_usuario(dados: UsuarioLogin, db: Session):
    usuario = buscar_por_email(db, dados.email)
    if not usuario or not verificar_senha(dados.senha, usuario.senha):
        return {"erro": "Credenciais inválidas"}
    return {"mensagem": "Login autorizado", "nome": usuario.nome}
