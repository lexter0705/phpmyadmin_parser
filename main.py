from requests import Session

from parser import Context
from parser.instructions import Instructions, Login, ScrapDatabase, PrintTable

PHP_ADMIN_LINK = "http://185.244.219.162/phpmyadmin"
LOGIN = "test"
PASSWORD = "JHFBdsyf2eg8*"

instruction = Instructions([Login(PHP_ADMIN_LINK, LOGIN, PASSWORD),
                            ScrapDatabase(PHP_ADMIN_LINK),
                            PrintTable()])

if __name__ == '__main__':
    context = Context(Session())
    instruction.perform(context)
