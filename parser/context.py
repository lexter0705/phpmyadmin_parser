from dataclasses import dataclass

from bs4 import BeautifulSoup
from requests import Session


@dataclass(frozen=True)
class Context:
    session: Session = Session()
    last_response: BeautifulSoup = BeautifulSoup()



