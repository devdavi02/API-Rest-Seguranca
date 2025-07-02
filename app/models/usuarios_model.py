from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    idade = Column(Integer)
    CPF = Column(String(50))
    telefone = Column(String(50))
    email = Column(String(100))
    senha = Column(String(100))

class UsuariosBase(BaseModel):
    nome: str
    idade: int
    CPF: str
    telefone: str
    email: str
    senha: str

class UsuariosCreate(UsuariosBase):
    pass