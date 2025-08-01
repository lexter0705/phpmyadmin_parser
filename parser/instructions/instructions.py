from parser.context import Context
from parser.instructions.base import Instruction


class Instructions(Instruction):
    def __init__(self, instructions: list[Instruction]):
        self.__instructions = instructions

    def perform(self, context: Context) -> Context:
        for instruction in self.__instructions:
            context = instruction.perform(context)
        return context
