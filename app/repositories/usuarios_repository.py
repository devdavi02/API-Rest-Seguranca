from app.models.usuarios_model import Usuario
from sqlalchemy.orm import Session

def buscar_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def salvar_usuario(db: Session, usuario: Usuario):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def buscar_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def deletar_usuario(db: Session, usuario: Usuario):
    db.delete(usuario)
    db.commit()