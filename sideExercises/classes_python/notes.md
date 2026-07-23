# Exercícios de Python: Programação Orientada a Objetos (OOP) & APIs

---

## Nível 1: O Seu Primeiro Objeto de API (Básico)

### Contexto
Quando fazemos uma requisição para uma API, recebemos dados de um recurso (como um usuário). Vamos transformar esses dados brutos em um objeto para organizá-los.

### Requisitos
1. Crie uma classe chamada `UsuarioAPI`.
2. Crie o método construtor `__init__` que receba os parâmetros: `self`, `id_usuario`, `nome` e `email`.
3. Guarde essas três informações como atributos do objeto usando a sintaxe `self.atributo = valor`.
4. Crie um método chamado `exibir_perfil(self)` que imprima no console:
   ```text
   Usuário #1: Ana (ana@email.com)
   ```
5. **Fora da classe:** Crie uma instância dessa classe passando dados fictícios e execute o método `exibir_perfil()`.

---

## Nível 2: Adicionando Lógica e Métodos de Verificação (Intermediário)

### Contexto
Toda chamada de API retorna um **Status Code** (ex: `200` para sucesso, `404` para não encontrado). Agora vamos criar uma classe que representa a **resposta** de uma requisição e adicionaremos um método com lógica condicional (`if/else`).

### Requisitos
1. Crie uma classe chamada `RespostaAPI`.
2. No método `__init__`, receba: `self`, `endpoint` (ex: `"/api/v1/produtos"`) e `status_code` (ex: `200` ou `404`).
3. Crie um método chamado `eh_sucesso(self)` que:
   * Retorne `True` se o `status_code` for igual a `200`.
   * Retorne `False` para qualquer outro valor.
4. Crie um método chamado `exibir_status(self)` que:
   * Imprima o endpoint e o status.
   * Se `eh_sucesso()` for verdadeiro, imprima `"Requisição concluída com sucesso!"`.
   * Caso contrário, imprima `"Erro ao acessar a API!"`.

### Exemplo de uso esperado
```python
# Teste 1: Sucesso
resposta_ok = RespostaAPI("/api/v1/dados", 200)
resposta_ok.exibir_status()

# Teste 2: Erro
resposta_erro = RespostaAPI("/api/v1/dados", 404)
resposta_erro.exibir_status()
```

---

## Nível 3: Manipulando Listas de Objetos e JSON Fictício (Avançado)

### Contexto
Na vida real e no trabalho com dados, APIs devolvem uma lista de registros (formato JSON/Dicionários). O objetivo aqui é aprender a usar uma classe para processar uma lista contendo múltiplos dados.

### Requisitos
1. Utilize a mesma classe `UsuarioAPI` que você construiu no **Nível 1**.
2. Crie uma lista fora da classe simulando o retorno de uma API com 3 dicionários:
   ```python
   dados_api = [
       {"id": 1, "nome": "Ana", "email": "ana@email.com"},
       {"id": 2, "nome": "Bruno", "email": "bruno@email.com"},
       {"id": 3, "nome": "Carla", "email": "carla@email.com"}
   ]
   ```
3. Crie uma lista vazia chamada `lista_de_objetos = []`.
4. Faça um loop `for` para percorrer `dados_api`. A cada volta do loop:
   * Instancie um objeto `UsuarioAPI` com as informações do dicionário.
   * Adicione esse novo objeto dentro da `lista_de_objetos`.
5. Faça outro loop `for` para percorrer a `lista_de_objetos` e chame o método `exibir_perfil()` para cada usuário instanciado.

---

## Nível 4: Conectando em uma API Real (Open Trivia DB)

### Contexto
Agora vamos integrar o aprendizado com uma requisição HTTP real utilizando a biblioteca `requests` para alimentar a nossa classe com dados dinâmicos da internet.

### Requisitos
1. Importe a biblioteca `requests` no topo do seu script (`import requests`).
2. Crie uma classe chamada `PerguntaTrivia`:
   * No `__init__`, receba: `self`, `categoria`, `pergunta` e `resposta_correta`.
   * Crie um método `exibir_desafio(self)` que imprima no console:
     ```text
     [Categoria: History]
     Pergunta: Who was the first President of the United States?
     ```
   * Crie um método `checar_resposta(self, chute_do_usuario)` que compare o chute com a resposta correta (use `.lower()` para ignorar maiúsculas/minúsculas) e retorne `True` ou `False`.
3. Faça uma chamada GET para a URL: `[https://opentdb.com/api.php?amount=1&type=multiple](https://opentdb.com/api.php?amount=1&type=multiple)`.
4. Extraia a primeira pergunta do JSON retornado e instancie um objeto da classe `PerguntaTrivia`.
5. Execute os métodos `exibir_desafio()` e `checar_resposta()` para testar o funcionamento.

### Esqueleto de código base
```python
import requests

url = "https://opentdb.com/api.php?amount=1&type=multiple"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    item = dados["results"][0]

    categoria_real = item["category"]
    pergunta_real = item["question"]
    resposta_real = item["correct_answer"]

    # TODO: Instanciar a classe PerguntaTrivia com os dados reais acima
else:
    print("Erro ao conectar na API!")
```