from pydantic import BaseModel

class UsuarioAPI(BaseModel):
    id_usuario: int
    nome: str
    email: str

    def exibir_perfil(self):
        print(f"Usuário #{self.id_usuario}: {self.nome}, ({self.email})")

