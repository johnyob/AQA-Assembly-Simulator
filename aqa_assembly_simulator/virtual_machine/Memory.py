from ascii_table import Table

from aqa_assembly_simulator.error.VirtualMachineError import VirtualMachineError


class Memory:

    def __init__(self, capacity):
        """
        Memory constructor.
        Constructs _memory using a list comprehension.

        :param capacity: number of addressable memory units (integer)
        """

        self._capacity = capacity

        self._memory = [
            0 for address in range(capacity)
        ]

    def __getitem__(self, address):
        """
        Returns data stored at memory address :param address.
        If :param address out of index range -> virtual machine error is raised.

        :param address: address index (0 <= a < n) (integer)
        :return: (integer)
        """

        if not 0 <= address.get_literal() < self._capacity:
            raise VirtualMachineError(address, "Address index out of range")

        return self._memory[address.get_literal()]

    def __setitem__(self, address, value):
        """
        Sets the value stored in address :param address to :param value.
        If :param address out of index range -> virtual machine error raised.

        :param address: address index (0 <= a < n) (integer)
        :param value: (integer)
        :return: (None)
        """

        if not 0 <= address.get_literal() < self._capacity:
            raise VirtualMachineError(address, "Address index out of range")

        self._memory[address.get_literal()] = int(value)

    def __repr__(self):
        """
        Returns string representation of the memory unit using an ascii_table.Table object

        :return: (string)
        """

        return str(Table([
            {
                "Header": "Addresses",
                "Contents": list(map(str, range(self._capacity)))
            },
            {
                "Header": "Values",
                "Contents": list(map(str, self._memory))
            }
        ]))
