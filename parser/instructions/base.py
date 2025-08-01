import abc

from parser.context import Context


class Instruction(abc.ABC):
    @abc.abstractmethod
    def perform(self, session: Context) -> Context:
        pass
