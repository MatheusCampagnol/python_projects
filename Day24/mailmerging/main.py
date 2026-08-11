#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pathlib import Path

SAMPLE_LETTER_PATH = 'Input/Letters'
INVITED_NAMES_LIST_PATH = 'Input/Names'
OUTPUT_LETTER_PATH = 'Output/ReadyToSend'


def main():
    # 1. Encontra a pasta exata onde este script está salvo no Linux
    pasta_script = Path(__file__).parent

    # 2. Constrói os caminhos resolvendo os '..' de forma nativa do sistema
    # O método .resolve() transforma o caminho relativo em um caminho absoluto real
    caminho_carta = (pasta_script / SAMPLE_LETTER_PATH / 'starting_letter.txt').resolve()
    caminho_nomes = (pasta_script / INVITED_NAMES_LIST_PATH / 'invited_names.txt').resolve()

    # Um print temporário para você ver no terminal o caminho exato que o Linux está procurando
    print(f"[DEBUG] Procurando carta em: {caminho_carta}")
    print(f"[DEBUG] Procurando nomes em: {caminho_nomes}\n")

    # 3. Abre os arquivos usando o gerenciador de contexto (with), que evita erros de travamento
    with open(caminho_carta, 'r', encoding='utf-8') as sample_letter:
        conteudo_carta = sample_letter.read() # Guarda o modelo da carta na memória

    with open(caminho_nomes, 'r', encoding='utf-8') as invited_names:
        # Lê as linhas diretamente no loop
        for name in invited_names:
            nome_limpo = name.strip()
            if nome_limpo: # Ignora linhas em branco
                print(f"Nome lido com sucesso: {nome_limpo}")

        # [Código anterior onde você lê o modelo da carta]
    with open(caminho_carta, 'r', encoding='utf-8') as sample_letter:
        conteudo_original = sample_letter.read()

    # Define a pasta de saída de forma correta (sem o '..')
    caminho_saida_pasta = (pasta_script / 'Output' / 'ReadyToSend').resolve()

    with open(caminho_nomes, 'r', encoding='utf-8') as invited_names:
        for name in invited_names:
            nome_limpo = name.strip()
            
            if nome_limpo:
                # 1. PESQUISA E SUBSTITUIÇÃO:
                # Digamos que na sua carta tenha o texto "[name]", trocamos pelo nome da pessoa
                carta_personalizada = conteudo_original.replace("[name]", nome_limpo)
                
                # 2. DEFINIR NOME DO NOVO ARQUIVO:
                # Cria um arquivo ex: 'carta_para_Matheus.txt'
                nome_arquivo_saida = f"carta_para_{nome_limpo}.txt"
                caminho_final_arquivo = caminho_saida_pasta / nome_arquivo_saida
                
                # 3. SALVAR O ARQUIVO NOVO:
                # Usamos o modo 'w' (write) para escrever o novo texto no Linux
                with open(caminho_final_arquivo, 'w', encoding='utf-8') as nova_carta:
                    nova_carta.write(carta_personalizada)
                    
                print(f"Carta gerada com sucesso para: {nome_limpo}")


if __name__ == "__main__":
    main()