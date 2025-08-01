from parser.context import Context
from parser.instructions.base import Instruction


class PrintTable(Instruction):
    def __init__(self, column_separator: str = " | ", row_separator: str = "-"):
        self.__column_separator = column_separator
        self.__row_separator = row_separator

    def __print_row(self, cells: list[str]):
        stroke = ""
        for cell in cells:
            stroke += cell + self.__column_separator
        print(stroke)
        print(self.__row_separator * len(stroke))

    def perform(self, context: Context) -> Context:
        columns = context.last_response.find_all("th", {"data-column": True})
        data = context.last_response.find_all("td", {"data-type": True})
        columns = list(map(lambda x: x.get("data-column"), columns))
        data = list(map(lambda x: x.text, data))
        self.__print_row(columns)
        count_columns = len(columns)
        for i in range(0, len(data), count_columns):
            self.__print_row(data[i:i + count_columns])
        return context
