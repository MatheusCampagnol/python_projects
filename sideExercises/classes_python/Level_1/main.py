from usuario_api import UsuarioAPI


def main():
    id_number = 0
    should_continue = True

    while should_continue == True:
        id_number += 1
        usuario = UsuarioAPI(
            id_usuario=id_number, 
            nome=input("Nome: "), 
            email=input("Email: ")
        )
        usuario.exibir_perfil()
        should_continue = usuario.still_want_to_continue(input("Deseja continuar? Responda somente sim ou não: "))                

if __name__ == "__main__":
    main()
