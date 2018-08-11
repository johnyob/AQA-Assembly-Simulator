import os

from aqa_assembly_simulator import ROOT

SYNTAX_JSON = os.path.join(ROOT, "parser\\syntax.json")
COMMANDS_JSON = os.path.join(ROOT, "commands.json")
VM_CONFIG = os.path.join(ROOT, "virtual_machine\\config\\config.json")

REGISTERS_REGEX = r"^(\d{1,2})$"
MEMORY_CAPACITY_REGEX = r"^(\d{1,3})$"
