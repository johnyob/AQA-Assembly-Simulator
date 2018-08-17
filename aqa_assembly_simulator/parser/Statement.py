from abc import ABC as Abstract, abstractmethod


class StatementVisitor(Abstract):
    """
    Abstract class.
    Used to traverse the abstract syntax tree produced by the parser.
    """

    @abstractmethod
    def visit_load_statement(self, statement):
        pass

    @abstractmethod
    def visit_store_statement(self, statement):
        pass

    @abstractmethod
    def visit_add_statement(self, statement):
        pass

    @abstractmethod
    def visit_subtract_statement(self, statement):
        pass

    @abstractmethod
    def visit_move_statement(self, statement):
        pass

    @abstractmethod
    def visit_compare_statement(self, statement):
        pass

    @abstractmethod
    def visit_branch_statement(self, statement):
        pass

    @abstractmethod
    def visit_branch_equal_statement(self, statement):
        pass

    @abstractmethod
    def visit_branch_not_equal_statement(self, statement):
        pass

    @abstractmethod
    def visit_branch_greater_than_statement(self, statement):
        pass

    @abstractmethod
    def visit_branch_less_than_statement(self, statement):
        pass

    @abstractmethod
    def visit_and_statement(self, statement):
        pass

    @abstractmethod
    def visit_or_statement(self, statement):
        pass

    @abstractmethod
    def visit_eor_statement(self, statement):
        pass

    @abstractmethod
    def visit_not_statement(self, statement):
        pass

    @abstractmethod
    def visit_left_shift_statement(self, statement):
        pass

    @abstractmethod
    def visit_right_shift_statement(self, statement):
        pass

    @abstractmethod
    def visit_halt_statement(self):
        pass

    @abstractmethod
    def visit_label_statement(self, statement):
        pass


class Statement(Abstract):
    """
    Parent class of the Statement class.
    Inherited by all statement objects.
    """

    @abstractmethod
    def accept(self, visitor):
        pass


class Load(Statement):

    def __init__(self, tokens):
        """
        Load statement constructor

        :param tokens: (|tokens| = 2) (list)
        """

        self._register, self._direct_address = tokens

    def get_register(self):
        """
        Returns register operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register

    def get_direct_address(self):
        """
        Returns direct address (memory reference) operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._direct_address

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_load_statement(self)

    def __repr__(self):
        """
        Returns string representation of load statement

        :return: (string)
        """

        return "LDR {0}, {1}".format(self._register, self._direct_address)


class Store(Statement):

    def __init__(self, tokens):
        """
        Store statement constructor

        :param tokens: (|tokens| = 2) (list)
        """

        self._register, self._direct_address = tokens

    def get_register(self):
        """
        Returns register operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register

    def get_direct_address(self):
        """
        Returns direct address (memory reference) operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._direct_address

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_store_statement(self)

    def __repr__(self):
        """
        Returns string representation of store statement

        :return: (string)
        """

        return "STR {0}, {1}".format(self._register, self._direct_address)


class Add(Statement):

    def __init__(self, tokens):
        """
        Add statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_add_statement(self)

    def __repr__(self):
        """
        Returns string representation of add statement

        :return: (string)
        """

        return "ADD {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class Subtract(Statement):

    def __init__(self, tokens):
        """
        Subtract statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_subtract_statement(self)

    def __repr__(self):
        """
        Returns string representation of subtract statement

        :return: (string)
        """

        return "SUB {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class Move(Statement):

    def __init__(self, tokens):
        """
        Move statement constructor

        :param tokens: (|tokens| = 2) (list)
        """

        self._register_d, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_move_statement(self)

    def __repr__(self):
        """
        Returns string representation of move statement

        :return: (string)
        """

        return "MOV {0}, {1}".format(self._register_d, self._operand)


class Compare(Statement):

    def __init__(self, tokens):
        """
        Compare statement constructor

        :param tokens: (|tokens| = 2) (list)
        """

        self._register_d, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_compare_statement(self)

    def __repr__(self):
        """
        Returns string representation of compare statement

        :return: (string)
        """

        return "CMP {0}, {1}".format(self._register_d, self._operand)


class Branch(Statement):

    def __init__(self, tokens):
        """
        Branch statement constructor

        :param tokens: (|tokens| = 1) (list)
        """

        self._label = tokens[0]

    def get_label(self):
        """
        Returns label operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._label

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_branch_statement(self)

    def __repr__(self):
        """
        Returns string representation of branch statement

        :return: (string)
        """

        return "B {0}".format(self._label)


class BranchEqual(Statement):

    def __init__(self, tokens):
        """
        Branch equal statement constructor

        :param tokens: (|tokens| = 1) (list)
        """

        self._label = tokens[0]

    def get_label(self):
        """
        Returns label operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._label

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_branch_equal_statement(self)

    def __repr__(self):
        """
        Returns string representation of branch equal statement

        :return: (string)
        """

        return "BEQ {0}".format(self._label)


class BranchNotEqual(Statement):

    def __init__(self, tokens):
        """
        Branch not equal statement constructor

        :param tokens: (|tokens| = 1) (list)
        """

        self._label = tokens[0]

    def get_label(self):
        """
        Returns label operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._label

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_branch_not_equal_statement(self)

    def __repr__(self):
        """
        Returns string representation of branch not equal statement

        :return: (string)
        """

        return "BNE {0}".format(self._label)


class BranchGreaterThan(Statement):

    def __init__(self, tokens):
        """
        Branch greater than statement constructor

        :param tokens: (|tokens| = 1) (list)
        """

        self._label = tokens[0]

    def get_label(self):
        """
        Returns label operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._label

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_branch_greater_than_statement(self)

    def __repr__(self):
        """
        Returns string representation of branch greater than statement

        :return: (string)
        """

        return "BGT {0}".format(self._label)


class BranchLessThan(Statement):

    def __init__(self, tokens):
        """
        Branch less than statement constructor

        :param tokens: (|tokens| = 1) (list)
        """

        self._label = tokens[0]

    def get_label(self):
        """
        Returns label operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._label

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_branch_less_than_statement(self)

    def __repr__(self):
        """
        Returns string representation of branch less than statement

        :return: (string)
        """

        return "BLT {0}".format(self._label)


class And(Statement):

    def __init__(self, tokens):
        """
        And statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_and_statement(self)

    def __repr__(self):
        """
        Returns string representation of and statement

        :return: (string)
        """

        return "AND {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class Or(Statement):

    def __init__(self, tokens):
        """
        Or statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_or_statement(self)

    def __repr__(self):
        """
        Returns string representation of or statement

        :return: (string)
        """

        return "ORR {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class Eor(Statement):

    def __init__(self, tokens):
        """
        Xor statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_eor_statement(self)

    def __repr__(self):
        """
        Returns string representation of xor statement

        :return: (string)
        """

        return "EOR {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class Not(Statement):

    def __init__(self, tokens):
        """
        Not statement constructor

        :param tokens: (|tokens| = 2) (list)
        """

        self._register_d, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_not_statement(self)

    def __repr__(self):
        """
        Returns string representation of not statement

        :return: (string)
        """

        return "MVN {0}, {1}".format(
            self._register_d, self._operand
        )


class LeftShift(Statement):

    def __init__(self, tokens):
        """
        Logical left shift statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_left_shift_statement(self)

    def __repr__(self):
        """
        Returns string representation of logical left shift statement

        :return: (string)
        """

        return "LSL {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class RightShift(Statement):

    def __init__(self, tokens):
        """
        Logical right shift statement constructor

        :param tokens: (|tokens| = 3) (list)
        """

        self._register_d, self._register_n, self._operand = tokens

    def get_register_d(self):
        """
        Returns register_d operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_d

    def get_register_n(self):
        """
        Returns register_n operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._register_n

    def get_operand(self):
        """
        Returns <operand 2> operand

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._operand

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_right_shift_statement(self)

    def __repr__(self):
        """
        Returns string representation of logical right shift statement

        :return: (string)
        """

        return "LSR {0}, {1}, {2}".format(
            self._register_d, self._register_n, self._operand
        )


class Halt(Statement):

    def __init__(self, tokens):
        """
        Halt statement constructor

        :param tokens: (|tokens| = 0) (list)
        """

        pass

    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_halt_statement()

    def __repr__(self):
        """
        Returns string representation of halt statement

        :return: (string)
        """

        return "HALT"


class Label(Statement):

    def __init__(self, identifier):
        """
        Label statement constructor

        :param identifier: label identifier (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        self._identifier = identifier

    def get_identifier(self):
        """
        Returns the identifier of the label

        :return: (aqa_assembly_simulator.lexer.TokenType.TokenType)
        """

        return self._identifier


    def accept(self, visitor):
        """
        Traversal method.
        Used to process of the node of abstract syntax tree.

        :param visitor: visitor class (sub-class of the StatementVisitor class)
        :return:
        """

        return visitor.visit_label_statement(self)

    def __repr__(self):
        """
        Returns string representation of the label statement

        :return: (string)
        """

        return "{0}:".format(self._identifier)
