from bs4 import BeautifulSoup

from parser.context import Context
from parser.exceptions import IncorrectLoginOrPassword
from parser.instructions.base import Instruction


class Login(Instruction):
    def __init__(self, site_url: str, login: str, password: str, file_to_request: str = "index.php?route=/"):
        self.__site_url = site_url + "/" + file_to_request
        self.__data = {
            "pma_username": login,
            "pma_password": password,
            "server": "1",
            "route": "/",
            "lang": "ru",
        }

    def perform(self, context: Context) -> Context:
        login_page = context.session.get(self.__site_url)
        soup = BeautifulSoup(login_page.text, 'html.parser')
        token = soup.find('input', {'name': 'token'}).get('value')
        set_session = soup.find('input', {'name': 'set_session'}).get('value')
        self.__data["token"] = token
        self.__data["set_session"] = set_session
        response = context.session.post(self.__site_url, data=self.__data).status_code
        if response != 200:
            raise IncorrectLoginOrPassword(self.__data["password"], self.__data["token"])
        return Context(context.session, soup)
