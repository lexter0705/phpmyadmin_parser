class IncorrectLoginOrPassword(Exception):
    def __init__(self, username: str, password: str):
        super().__init__(f"Incorrect username: {username}, or password: {password}")
