from sqlalchemy.orm import Session
from app.models.usuarios_model import Usuario, UsuarioCreate, UsuarioLogin
from app.repositories.usuarios_repository import buscar_por_email, salvar_usuario
from app.utils.auth import gerar_hash_senha, verificar_senha
from app.utils.auth import gerar_hash_senha, criptografar_dado
from app.utils.auth import verificar_senha, criptografar_dado, descriptografar_dado
from app.repositories.usuarios_repository import buscar_por_id, deletar_usuario

def cadastrar_usuario(dados: UsuarioCreate, db: Session):
    if buscar_por_email(db, dados.email):  # <-- e-mail em texto simples
        return {"erro": "Email já cadastrado"}

    novo_usuario = Usuario(
        nome=criptografar_dado(dados.nome),
        idade=dados.idade,
        cpf=criptografar_dado(dados.cpf),
        telefone=criptografar_dado(dados.telefone),
        email=dados.email,  
        senha=gerar_hash_senha(dados.senha)
    )

    return {
        "mensagem": "Usuário cadastrado com sucesso",
        "usuario": salvar_usuario(db, novo_usuario)
    }

def login_usuario(dados: UsuarioLogin, db: Session):
    usuario = buscar_por_email(db, dados.email)  
    
    if not usuario or not verificar_senha(dados.senha, usuario.senha):
        return {"erro": "Credenciais inválidas"}
    
    return {
        "mensagem": "Login autorizado",
        "nome": descriptografar_dado(usuario.nome)  
    }

def excluir_usuario_por_login(dados_login, db: Session):
    usuario = buscar_por_email(db, dados_login.email)
    if not usuario or not verificar_senha(dados_login.senha, usuario.senha):
        return {"erro": "Credenciais inválidas"}

    deletar_usuario(db, usuario)
    return {"mensagem": "Usuário excluído com sucesso"}

def anonimizar_usuario_por_login(dados_login, db: Session):
    usuario = buscar_por_email(db, dados_login.email)
    if not usuario or not verificar_senha(dados_login.senha, usuario.senha):
        return {"erro": "Credenciais inválidas"}

    usuario.nome = criptografar_dado("anonimizado")
    usuario.cpf = criptografar_dado("anonimizado")
    usuario.telefone = criptografar_dado("anonimizado")
    usuario.email = f"anonimizado{usuario.id}@anonimo.com"  

    salvar_usuario(db, usuario)

    return {"mensagem": "Dados do usuário anonimizados com sucesso"}
