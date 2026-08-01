class RespostaAPI:

    def __init__(self, endpoint, status):
        self.endpoint = endpoint
        self.status = status

    def is_success(self):
        return self.status == 200