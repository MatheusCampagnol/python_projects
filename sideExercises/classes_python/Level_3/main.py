from dados_api import data
from usuario_api import UsuarioAPI



def main():
#Criando lista vazia de objetos.
    lista_de_objetos = []
#Loop for para percorrer a APi:
    for item in data:
#Instanciando a classe UsuarioAPi()
        usuario = UsuarioAPI(
                    id_usuario=item["id"],
                    nome=item["nome"],
                    email=item["email"]
                    )
#Adicionando meu usuário à lista de objetos.        
        lista_de_objetos.append(usuario)
#Loop secundário para percorrer a lista e chamar o exibir perfil.
    for usuario in lista_de_objetos:
        usuario.exibir_perfil()


if __name__ == "__main__":
    main()