from bs4 import BeautifulSoup

from parser.context import Context
from parser.instructions.base import Instruction


class ScrapDatabase(Instruction):
    def __init__(self,
                 site_url: str,
                 table_url: str = "index.php?route=/sql&db=testDB&table=users&sql_query=SELECT+%2A+FROM+%60users"):
        self.__site_url = site_url + "/" + table_url

    def __set_to_view_all_rows(self, context: Context):
        data = {
            "db": "testDB",
            "table": "users",
            "server": "1",
            "sql_query": "SELECT * FROM `users` ORDER BY `id` ASC",
            "is_browse_distinct": "",
            "goto": "",
            "session_max_rows": "25",
            "pos": "0",
            "navig": "all"
        }
        context.session.post(self.__site_url, data)

    def perform(self, context: Context) -> Context:
        self.__set_to_view_all_rows(context)
        data = context.session.get(self.__site_url).text
        html = BeautifulSoup(data, "html.parser")
        rows = html.find("table", {"class": "table_results"})
        return Context(context.session, rows)
