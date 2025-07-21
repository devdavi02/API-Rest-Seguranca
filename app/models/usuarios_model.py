from sqlalchemy import Column, Integer, String
from app.database.db import Base
from pydantic import BaseModel, EmailStr, constr

CPFStr = constr(min_length=11, max_length=11)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    telefone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)

class UsuarioCreate(BaseModel):
    nome: str
    idade: int
    cpf: CPFStr # type: ignore
    telefone: str
    email: EmailStr
    senha: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str
