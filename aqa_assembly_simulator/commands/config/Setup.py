import re as regular_expression
import json
import sys

from ascii_table import Table

from aqa_assembly_simulator.helpers.Constants import REGISTERS_REGEX, MEMORY_CAPACITY_REGEX, VM_CONFIG
from aqa_assembly_simulator.helpers.Exceptions import AssemblySimulatorVMConfigException
from aqa_assembly_simulator.helpers.Util import write_file, SortedDictionary
from aqa_assembly_simulator.commands.Command import Command


class Setup(Command):

    def run(self):
        """
        Run method for config setup

        :return: (None)
        """

        registers = input("Enter number of registers in the virtual machine: ")

        if not regular_expression.match(REGISTERS_REGEX, registers):
            print(AssemblySimulatorVMConfigException({
                "message": "invalid number of registers",
                "format": "[0-9]{1,2}",
                "registers": registers
            }), file=sys.stderr)
            return

        memory_capacity = input("Enter number of addressable memory units in the virtual machine: ")

        if not regular_expression.match(MEMORY_CAPACITY_REGEX, memory_capacity):
            print(AssemblySimulatorVMConfigException({
                "message": "invalid number of addressable memory units",
                "format": "[0-9]{1,3}",
                "memory capacity": memory_capacity
            }), file=sys.stderr)
            return

        config = {
            "memory capacity": int(memory_capacity),
            "registers": int(registers)
        }
        write_file(VM_CONFIG, json.dumps(config))

        config = SortedDictionary(config)
        print("\nVirtual Machine Config")
        print(Table([config.names(), config.values()]))
