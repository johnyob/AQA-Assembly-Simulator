from ascii_table import Table

from aqa_assembly_simulator.virtual_machine.Register import Register


class ComparisonRegister(Register):

    def __init__(self):
        """
        Comparison Register constructor, subclass of Register.
        Constructs mappings between Comparison codes and registers.
        """

        super().__init__(4)
        self._mapping = {
            "EQ": 1,
            "NE": 2,
            "GT": 3,
            "LT": 4
        }

    def __getitem__(self, condition):
        """
        Returns boolean value stored in register :param condition

        :param condition: condition mnemonic -> condition in ["EQ", "NE", "GT", "LT"] (string)
        :return: (boolean)
        """

        return bool(self._register[self._mapping[condition]])

    def set_register(self, register):
        """
        Sets _register to :param register

        :param register: (dict)
        :return: (None)
        """

        for key, value in register.items():
            self._register[self._mapping[key]] = int(value)

    def __repr__(self):
        """
        Returns string representation of the comparison register using an ascii_table.Table object

        :return: (string)
        """

        return str(Table([
            {
                "Header": condition,
                "Contents": [str(int(self.__getitem__(condition)))]
            } for condition in ["EQ", "NE", "GT", "LT"]
        ]))


