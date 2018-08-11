import sys

from aqa_assembly_simulator.virtual_machine.config.VirtualMachineConfig import VirtualMachineConfig
from aqa_assembly_simulator.virtual_machine.VirtualMachine import VirtualMachine
from aqa_assembly_simulator.commands.Command import Command
from aqa_assembly_simulator.helpers.Util import read_file
from aqa_assembly_simulator.parser.Parser import Parser
from aqa_assembly_simulator.lexer.Lexer import Lexer


class Execute(Command):

    def __init__(self, arguments):
        super().__init__(arguments)
        self._file_location = self._arguments["<file>"]
        self._trace = self._arguments["--trace"]

    def run(self):
        errors, virtual_machine_errors = self._run(read_file(self._file_location))

        if errors:
            sys.exit(65)

        if virtual_machine_errors:
            sys.exit(70)

    def _run(self, source):
        lexer_errors, parser_errors, virtual_machine_errors = [], [], []

        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        parser = Parser(tokens)
        statements = parser.parse()

        lexer_errors, parser_errors = lexer.get_errors(), parser.get_errors()
        self._print_errors(lexer_errors + parser_errors)

        if len(lexer_errors + parser_errors) > 0:
            return lexer_errors + parser_errors, virtual_machine_errors

        virtual_machine = VirtualMachine(
            statements, VirtualMachineConfig.get_registers(),
            VirtualMachineConfig.get_memory_capacity(), self._trace
        )

        virtual_machine.execute()
        virtual_machine_errors = virtual_machine.get_errors()

        self._print_errors(virtual_machine_errors)

        return lexer_errors + parser_errors, virtual_machine_errors

    def _print_errors(self, errors):
        for error in errors:
            print(error)
            if hasattr(error, "report"):
                print(error.report())
            else:
                print("Python error: {0}".format(error))
