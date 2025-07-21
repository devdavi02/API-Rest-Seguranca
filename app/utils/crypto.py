from cryptography.fernet import Fernet
import base64
import os
from typing import Union


class Crypto():

    def __init__(self):
        # Carrega ou gera chave secreta (em produção, armazene em local seguro como variáveis de ambiente ou arquivo separado)
        self.key = os.environ.get("FERNET_KEY") or self._generate_and_show_key()
        self.fernet = Fernet(self.key)

    def _generate_and_show_key(self):
        key = Fernet.generate_key()
        print(f"🔐 Salve essa chave em segurança e defina no ambiente como FERNET_KEY:\n{key.decode()}")
        return key
    
    def criptografar(self, texto: str) -> str:
        return self.fernet.encrypt(texto.encode()).decode()

    def criptografar_dict(self, data: dict, ignorar: list = None) -> str:
        ignorar = ignorar or []
        resultado = {}

        for chave, valor in data.items():
            if chave in ignorar or not isinstance(valor, str):
                resultado[chave] = valor
            else:
                resultado[chave] = self.criptografar(valor)
        return resultado

    def descriptografar(self, texto_criptografado: str) -> str:
        return self.fernet.decrypt(texto_criptografado.encode()).decode()
    
    def descriptografar_campos(self, obj: Union[dict, object], campos: list):
        for campo in campos:
            valor = getattr(obj, campo, None) if hasattr(obj, campo) else obj.get(campo)
            if valor is not None:
                try:
                    valor_descriptografado = self.descriptografar(valor)
                    if hasattr(obj, campo):
                        setattr(obj, campo, valor_descriptografado)
                    else:
                        obj[campo] = valor_descriptografado
                except Exception:
                    pass
        return obj

    
    def descriptografar_lista(self, lista_objetos: list, campos: list):
        for obj in lista_objetos:
            self.descriptografar_campos(obj, campos)
        return lista_objetos
    




        
