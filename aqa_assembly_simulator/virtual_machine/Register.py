from ascii_table import Table

from aqa_assembly_simulator.error.VirtualMachineError import VirtualMachineError


class Register:

    def __init__(self, registers):
        """
        Register constructor.
        Constructs _register using dictionary comprehension.

        :param registers: number of registers (integer)
        """

        self._registers = registers
        self._register = {
            register: 0 for register in range(1, registers + 1)
        }

    def __getitem__(self, register):
        """
        Returns the data stored in :param register.
        If :param register out of index range -> virtual machine error raised.

        :param register: register index (1 <= r <= n) (integer)
        :return: (integer)
        """

        if not 1 <= register.get_literal() <= self._registers:
            raise VirtualMachineError(register, "Register index out of range.")

        return self._register[register.get_literal()]

    def __setitem__(self, register, value):
        """
        Sets the value stored in register :param register to :param value.
        If :param register out of index range -> virtual machine error raised.

        :param register: register index (1 <= r <= n) (integer)
        :param value: (integer)
        :return: (None)
        """

        if not 1 <= register.get_literal() <= self._registers:
            raise VirtualMachineError(register, "Register index out of range.")

        self._register[register.get_literal()] = int(value)

    def __repr__(self):
        """
        Returns string representation of the register using an ascii_table.Table object

        :return: (string)
        """

        return str(Table([
            {
                "Header": str(register),
                "Contents": [str(value)]
            } for register, value in self._register.items()
        ]))