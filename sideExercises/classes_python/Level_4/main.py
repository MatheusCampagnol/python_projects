import requests


#get call to api:
def call_open_trivia_api():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print("Failed to retrieve data from the API.")
        return []


def main():
    call_open_trivia_api()    


if __name__ == "__main__":
    main()