from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.usuarios_model import UsuarioCreate, UsuarioLogin
from app.services import usuario_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cadastro", summary="Cadastrar usuário", description="Cria um novo usuário com nome, email, telefone, CPF e senha. Os dados sensíveis são criptografados.")
def cadastrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.cadastrar_usuario(usuario, db)

@router.post("/login", summary="Login do usuário", description="Verifica se o email e senha correspondem a um usuário existente.")
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    return usuario_service.login_usuario(usuario, db)

@router.delete("/usuarios", summary="Excluir usuário por login", description="Exclui o usuário a partir do e-mail e senha informados.")
def deletar_usuario_login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    return usuario_service.excluir_usuario_por_login(usuario, db)

@router.put("/usuarios/anonimizar", summary="Anonimizar dados do usuário", description="Substitui os dados sensíveis do usuário por informações genéricas (anonimizadas).")
def anonimizar_usuario(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    return usuario_service.anonimizar_usuario_por_login(usuario, db)