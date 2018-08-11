"""
AQA Assembly Simulator

Usage:
  aqa-assembly-simulator config setup
  aqa-assembly-simulator config show
  aqa-assembly-simulator execute <file> [--trace]

Options:
  -h --help                 Show this screen.
  --version                 Show version.
  --trace                   Shows program counter, registers and memory during VM execution.

Help:
  For help, please see https://github.com/johnyob/AQA-Assembly-Simulator
"""

from importlib import import_module
from functools import reduce
from docopt import docopt
import json

from aqa_assembly_simulator.helpers.Constants import COMMANDS_JSON
from aqa_assembly_simulator.helpers.Util import read_file
from aqa_assembly_simulator import __version__


class Client:

    def __init__(self):
        """
        Client Class.
        Retrieves options from docopt. Options are then filtered using data stored in commands.json.
        Command is then imported and instantiated.
        """

        self._options = docopt(__doc__, version=__version__)
        self._arguments = {
            k: v for k, v in self._options.items()
            if not isinstance(v, bool) or k == "--trace"
        }

        commands_json = json.loads(read_file(COMMANDS_JSON))
        command = list(filter(lambda x: self._is_command(x["Conditions"]), commands_json))[0]

        getattr(
            import_module("aqa_assembly_simulator.commands.{0}".format(command["Module Identifier"])),
            command["Class Identifier"]
        )(self._arguments).run()

    def _is_command(self, conditions):
        return reduce(lambda x, y: x and y, map(lambda y: self._options[y], conditions))