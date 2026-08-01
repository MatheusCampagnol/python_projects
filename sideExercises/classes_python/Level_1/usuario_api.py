class UsuarioAPI:

    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def exibir_perfil(self):
        print(f"Usuário #{self.id_usuario}: {self.nome} ({self.email})")

    def still_want_to_continue(self, answer):
        if answer.lower() == "sim":
            return True
        elif answer.lower() == "não":
            return False
        else:
            nova_resposta = input("Resposta inválida. Digite apenas 'sim' ou 'não': ")
            return self.still_want_to_continue(nova_resposta)