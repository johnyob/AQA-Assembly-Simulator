from aqa_assembly_simulator.parser.Statement import StatementVisitor
import aqa_assembly_simulator.parser.Statement as Statement
from aqa_assembly_simulator.virtual_machine.Register import Register
from aqa_assembly_simulator.virtual_machine.ComparisonRegister import ComparisonRegister
from aqa_assembly_simulator.virtual_machine.Memory import Memory
from aqa_assembly_simulator.lexer.TokenType import TokenType
from aqa_assembly_simulator.error.VirtualMachineError import VirtualMachineError


class VirtualMachine(StatementVisitor):

    def __init__(self, statements, registers, memory_capacity, trace=False):
        """
        Virtual Machine constructor.
        Interpreter for aqa_assembly_simulator.parser.Statement.Statement objects.
        Constructs label pointer references.
        Constructs memory, registers and comparison registers.

        :param statements: list of statements produced by the parser (list)
        :param registers: number of registers in the virtual machine (integer)
        :param memory_capacity: number of addressable memory units in the virtual machine (integer)
        :param trace: indicates whether registers and memory units should be printed after each statement (boolean)
        """

        self._statements = statements
        self._labels = {
            statement.get_identifier().get_lexeme(): pointer - 1
            for pointer, statement in enumerate(statements)
            if isinstance(statement, Statement.Label)
        }

        self._trace = trace

        self._memory = Memory(memory_capacity)
        self._register = Register(registers)
        self._comparison_register = ComparisonRegister()

        self._program_counter = 0
        self._branched = False
        self._halted = False

        self._errors = []

    def _operand(self, operand):
        """
        Returns the literal value for the <operand 2> operand

        :param operand: <operand 2> operand (aqa_assembly_simulator.lexer.Token.Token)
        :return: (integer)
        """

        if operand.get_type() == TokenType.IMMEDIATE_ADDRESS:
            return operand.get_literal()

        return self._register[operand]

    def visit_load_statement(self, statement):
        """
        Handles :param statement according to the operation of a Load Statement.
        Loads value stored in memory into a register.

        :param statement: (aqa_assembly_simulator.parser.Statement.Load)
        :return: (None)
        """

        self._register[statement.get_register()] = self._memory[statement.get_direct_address()]

    def visit_store_statement(self, statement):
        """
        Handles :param statement according to the operation of a Store Statement.
        Stores value stored in register into memory

        :param statement: (aa_assembly_simulator.parser.Statement.Store)
        :return: (None)
        """

        self._memory[statement.get_direct_address()] = self._register[statement.get_register()]

    def visit_add_statement(self, statement):
        """
        Handles :param statement according to the operation of a Add Statement.
        Stores sum of r_n and <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.Add)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] + self._operand(
            statement.get_operand()
        )

    def visit_subtract_statement(self, statement):
        """
        Handles :param statement according to the operation of a Subtract statement.
        Stores difference of r_n and <operand 2> in register r_d

        :param statement: (aqa_assembly_simulator.parser.Statement.Subtract)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] - self._operand(
            statement.get_operand()
        )

    def visit_move_statement(self, statement):
        """
        Handles :param statement according to the operation of a Move Statement.
        Stores value of <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.Move)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._operand(statement.get_operand())

    def visit_compare_statement(self, statement):
        """
        Handles :param statement according to the operation of a Compare Statement.
        Compares value of r_d and <operand 2> and stores results in comparison register

        :param statement: (aqa_assembly_simulator.parser.Statement.Compare)
        :return: (None)
        """

        register_d = self._register[statement.get_register_d()]
        operand = self._operand(statement.get_operand())

        self._comparison_register.set_register({
            "EQ": register_d == operand,
            "NE": register_d != operand,
            "GT": register_d > operand,
            "LT": register_d < operand
        })

    def visit_branch_statement(self, statement):
        """
        Handles :param statement according to the operation of a Branch Statement.
        Jumps to label.

        :param statement: (aqa_assembly_simulator.parser.Statement.Branch)
        :return: (None)
        """

        if statement.get_label().get_lexeme() not in self._labels:
            raise VirtualMachineError(statement.get_label(), "Invalid label identifier")

        self._program_counter = self._labels[statement.get_label().get_lexeme()]
        self._branched = True

    def visit_branch_equal_statement(self, statement):
        """
        Handles :param statement according to the operation of a Branch Equal Statement.
        Jumps to label if a result of a comparison returns equal.

        :param statement: (aqa_assembly_simulator.parser.Statement.BranchEqual)
        :return: (None)
        """

        if self._comparison_register["EQ"]:
            self.visit_branch_statement(statement)

    def visit_branch_not_equal_statement(self, statement):
        """
        Handles :param statement according to the operation of a Branch Not Equal Statement.
        Jumps to label if a result of a comparison returns not equal.

        :param statement: (aqa_assembly_simulator.parser.Statement.BranchNotEqual)
        :return: (None)
        """

        if self._comparison_register["NE"]:
            self.visit_branch_statement(statement)

    def visit_branch_greater_than_statement(self, statement):
        """
        Handles :param statement according to the operation of a Branch Greater Than Statement.
        Jumps to label if a result of a comparison returns greater than

        :param statement: (aqa_assembly_simulator.parser.Statement.BranchGreaterThan)
        :return: (None)
        """

        if self._comparison_register["GT"]:
            self.visit_branch_statement(statement)

    def visit_branch_less_than_statement(self, statement):
        """
        Handles :param statement according to the operation of a Branch Less Than Statement.
        Jumps to label if a result of a comparison returns less than

        :param statement: (aqa_assembly_simulator.parser.Statement.BranchLessThan)
        :return: (None)
        """

        if self._comparison_register["LT"]:
            self.visit_branch_statement(statement)

    def visit_and_statement(self, statement):
        """
        Handles :param statement according to the operation of a And Statement.
        Stores value of logical AND operation on register r_n and <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.And)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] & self._operand(
            statement.get_operand()
        )

    def visit_or_statement(self, statement):
        """
        Handles :param statement according to the operation of a Or Statement.
        Stores value of logical OR operation on register r_n and <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.Or)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] | self._operand(
            statement.get_operand()
        )

    def visit_eor_statement(self, statement):
        """
        Handles :param statement according to the operation of a Eor Statement.
        Stores value of logical XOR operation on register r_n and <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.Eor)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] ^ self._operand(
            statement.get_operand()
        )

    def visit_not_statement(self, statement):
        """
        Handles :param statement according to the operation of a Not Statement.
        Stores value of logical NOT operation on <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.Not)
        :return: (None)
        """

        self._register[statement.get_register_d()] = ~ self._operand(statement.get_operand())

    def visit_left_shift_statement(self, statement):
        """
        Handles :param statement according to the operation of a Left Shift Statement.
        Stores value of logical Left Shift operation on register r_n and <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.LeftShift)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] << self._operand(
            statement.get_operand()
        )

    def visit_right_shift_statement(self, statement):
        """
        Handles :param statement according to the operation of a Right Shift Statement.
        Stores value of logical Right Shift operation on register r_n and <operand 2> in register r_d.

        :param statement: (aqa_assembly_simulator.parser.Statement.RightShift)
        :return: (None)
        """

        self._register[statement.get_register_d()] = self._register[
            statement.get_register_n()
        ] >> self._operand(
            statement.get_operand()
        )

    def visit_halt_statement(self):
        """
        Handles halt statement according to the operation of a Halt Statement
        Sets _halted true -> Virtual Machine has Halted.

        :return: (None)
        """

        self._halted = True

    def visit_label_statement(self, statement):
        """
        Handles Label Statement.

        :param statement: (aqa_assembly_simulator.parser.Statement.Label)
        :return: (None)
        """
        if self._trace:
            print("\nEntering {0} Label".format(statement.get_identifier().get_lexeme()))


    def execute(self):
        """
        Executes statements stored in _statements.
        Handles the incrementation of the program counter.
        If a virtual machine error occurs during the execution of statements, then the
        error is appended to the internal errors list and the program is halted.

        :return: (None)
        """

        try:
            while not self._halted and self._program_counter < len(self._statements):
                CIR = self._statements[self._program_counter]
                self._execute_statement(CIR)
                self._print_trace(CIR)

                self._program_counter += 1
                self._branched = False

            print("\nResults of program being executed:")
            self._print_registers()

        except (VirtualMachineError, Exception) as error:
            self._error(error)
            self._halted = True

    def _print_trace(self, CIR):
        """
        Prints program counter, registers and memory contents if tracing is enabled.

        :param CIR: Current statement has just been executed (aqa_assembly_simulator.parser.Statement.Statement)
        :return: (None)
        """

        if self._trace:
            print("\nCurrent Instruction Register: {0}".format(CIR))

            print("\nResult of CIR being executed:")
            print("\nProgram Counter: {0}".format(self._program_counter + self._branched))
            self._print_registers()

    def _print_registers(self):
        """
        Prints registers and memory contents

        :return: (None)
        """

        print("\nRegister")
        print(self._register)
        print("\nComparison Register")
        print(self._comparison_register)
        print("\nMemory")
        print(self._memory)

    def _execute_statement(self, statement):
        """
        Executes :param statement using public AST (Abstract Syntax Tree) traversal method.

        :param statement: (aqa_assembly_simulator.parser.Statement.Statement)
        :return: (None)
        """

        statement.accept(self)

    def _error(self, error):
        """
        Appends virtual machine error :param error to internal errors list

        :param error: (aqa_assembly_simulator.error.VirtualMachineError)
        :return: (None)
        """

        self._errors.append(error)

    def get_errors(self):
        """
        Returns internal virtual machine errors

        :return: (list)
        """

        return self._errors
