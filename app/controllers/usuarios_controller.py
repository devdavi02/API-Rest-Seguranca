from fastapi import APIRouter, Depends
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

@router.post("/cadastro")
def cadastrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.cadastrar_usuario(usuario, db)

@router.post("/login")
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    return usuario_service.login_usuario(usuario, db)
