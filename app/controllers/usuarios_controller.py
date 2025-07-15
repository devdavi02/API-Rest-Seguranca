from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.usuarios_model import UsuarioCreate, UsuarioLogin
from app.services import usuario_service
from app.models.usuarios_model import Usuario
from app.utils.crypto import Crypto
from fastapi.encoders import jsonable_encoder

router = APIRouter()
crypto = Crypto()

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

@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    usuarios = crypto.descriptografar_lista(usuarios, ["cpf", "telefone"])
    return jsonable_encoder(usuarios)
