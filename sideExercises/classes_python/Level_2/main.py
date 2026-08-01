import requests
from RespostaAPI import RespostaAPI


def main():
    endpoint = "https://opentdb.com/api.php?amount=10&type=multiple"
    status = requests.get(endpoint).status_code
    resposta = RespostaAPI(endpoint, status)
    success = resposta.is_success()
    print(f"Response from API: {success}")

if __name__ == "__main__":
    main()