import os

from aqa_assembly_simulator import ROOT, OS

separator = "\\" if OS == "nt" else "/"

SYNTAX_JSON = os.path.join(ROOT, "parser{0}syntax.json".format(separator))
COMMANDS_JSON = os.path.join(ROOT, "commands.json")
VM_CONFIG = os.path.join(ROOT, "virtual_machine{0}config{0}config.json".format(separator))

REGISTERS_REGEX = r"^(\d{1,2})$"
MEMORY_CAPACITY_REGEX = r"^(\d{1,3})$"
