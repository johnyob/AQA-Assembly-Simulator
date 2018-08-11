from ascii_table import Table

from aqa_assembly_simulator.virtual_machine.config.VirtualMachineConfig import VirtualMachineConfig
from aqa_assembly_simulator.helpers.Util import SortedDictionary
from aqa_assembly_simulator.commands.Command import Command


class Show(Command):

    def run(self):
        """
        Return method for config show command

        :return: (None)
        """

        config = SortedDictionary(VirtualMachineConfig.get_config())

        print("\nVirtual Machine Config")
        print(Table([config.names(), config.values()]))