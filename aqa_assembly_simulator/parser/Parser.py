import json

from aqa_assembly_simulator.lexer.TokenType import TokenType, STATEMENTS
from aqa_assembly_simulator.helpers.Constants import SYNTAX_JSON
from aqa_assembly_simulator.error.ParseError import ParseError
from aqa_assembly_simulator.parser.Statement import Label
from aqa_assembly_simulator.helpers.Util import read_file


class Parser:

    def __init__(self, tokens):
        """
        Parser (syntactic analyser) constructor

        :param tokens: list containing tokens produced from lexical analysis (list)
        """

        self._current = 0
        self._tokens = tokens

        self._syntax = self._read_syntax()
        self._errors = []

    def get_errors(self):
        """
        Returns internal parser errors

        :return: (list)
        """

        return self._errors

    def _read_syntax(self):
        """
        Returns syntax conditions stored in syntax.json.
        Converts keys from string to integer.

        :return: (dict)
        """

        return {
            int(key): value for key, value
            in json.loads(read_file(SYNTAX_JSON)).items()
        }

    def parse(self):
        """
        Performs syntactic analysis on the tokens to produce a list of statements.

        :return: (list)
        """

        statements = []

        while not self._is_at_end():
            statements.append(self._declaration())

        return statements

    def _declaration(self):
        """
        Checks for a label declaration, if not then parse token to statement.
        If a parser error occurs then synchronise tokens until next valid token.

        :return: (aqa_assembly_simulator.parser.Statement.Statement)
        """

        try:
            if self._match(TokenType.IDENTIFIER):
                return self._label_declaration()

            return self._statement()
        except ParseError:
            self._synchronise()
            return None

    def _label_declaration(self):
        """
        Parses label declaration.
        If invalid syntax then raises parser error.

        :return: (aqa_assembly_simulator.parser.Statement.Label)
        """

        identifier = self._previous()
        self._consume(TokenType.COLON, "Expect colon after label identifier")

        return Label(identifier)

    def _statement(self):
        """
        Parses tokens to statement.
        Uses syntax conditions stored in syntax.json to parse tokens to valid statements.
        If an unexpected token is discovered then a parser error is raised.

        :return: (aqa_assembly_simulator.parser.Statement.Statement)
        """

        for type in self._syntax.keys():
            if self._match(TokenType(type)):
                return self._instruction(type)

        raise self._error(self._peek(), "Unexpected token")

    def _instruction(self, type):
        """
        Uses syntax conditions for :param type to parse current tokens to statement.
        If unexpected token is discovered then a parser error is raised.
        If an <operand 2> condition is discovered then it is validated and appended to the tokens list.

        :param type: token type (integer)
        :return: (aqa_assembly_simulator.parser.Statement.Statement)
        """

        tokens = []

        for token in self._syntax[type]:
            if TokenType(token["Type"]) == TokenType.COMMA:
                self._consume(TokenType.COMMA, token["Error"])
            elif TokenType(token["Type"]) == TokenType.OPERAND:
                tokens.append(self._operand(token))
            else:
                tokens.append(self._consume(TokenType(token["Type"]), token["Error"]))

        return STATEMENTS[type](tokens)

    def _operand(self, token):
        """
        Validates token based on <operand 2> conditions.

        :param token: token condition object (dict)
        :return: (aqa_assembly_simulator.lexer.Token.Token)
        """

        if self._check(TokenType.IMMEDIATE_ADDRESS) or self._check(TokenType.REGISTER):
            return self._move()

        raise self._error(self._peek(), token["Error"])

    def _consume(self, type, message):
        """
        Consumes current token if expected token is found, otherwise raise parser error

        :param type: expected token type (aqa_assembly_simulator.lexer.TokenType.TokenType)
        :param message: error message (string)
        :return: (aqa_assembly_simulator.parser.Statement.Statement)
        """

        if self._check(type):
            return self._move()

        raise self._error(self._peek(), message)

    def _match(self, type):
        """
        Matches current token to expected token type. If expected token type found, then move one token along and
        return true, otherwise return false.

        :param type: expected token type (aqa_assembly_simulator.lexer.TokenType.TokenType
        :return: (boolean)
        """

        if self._check(type):
            self._move()
            return True

        return False

    def _check(self, type):
        """
        Checks current token against expected token type. If at end of token list then return false.
        Otherwise return whether current token type equals expected token type.

        :param type: expected token type (aqa_assembly_simulator.lexer.TokenType.TokenType)
        :return: (boolean)
        """

        if self._is_at_end():
            return False

        return self._peek().get_type() == type

    def _move(self):
        """
        Increments current pointer for tokens list, if not at the end of tokens list.
        Returns the previous token.

        :return: (aqa_assembly_simulator.lexer.Token.Token)
        """

        if not self._is_at_end():
            self._current += 1

        return self._previous()

    def _error(self, token, message):
        """
        Constructs a parser error and appends it to the internal errors list.
        Returns constructed parser error.

        :param token: token that raised the error (aqa_assembly_simulator.lexer.Token.Token)
        :param message: error message (string)
        :return: (aqa_assembly_simulator.error.ParseError.ParseError)
        """

        self._errors.append(ParseError(token, message))
        return self._errors[-1]

    def _peek(self):
        """
        Returns the current token

        :return: (aqa_assembly_simulator.lexer.Token.Token)
        """

        return self._tokens[self._current]

    def _previous(self):
        """
        Returns the previous token

        :return: (aqa_assembly_simulator.lexer.Token.Token)
        """

        return self._tokens[self._current - 1]

    def _is_at_end(self):
        """
        Returns whether the parser is at the end of the tokens list.

        :return: (boolean)
        """

        return self._peek().get_type() == TokenType.EOF

    def _synchronise(self):
        """
        Synchronises current pointer to a statement starting token. Used to prevent consecutive errors produced when
        one error occurs.

        :return: (None)
        """

        self._move()

        while not self._is_at_end():
            if self._peek().get_type() not in [
                TokenType.REGISTER,
                TokenType.IMMEDIATE_ADDRESS,
                TokenType.DIRECT_ADDRESS,
                TokenType.OPERAND,
                TokenType.COLON,
                TokenType.COMMA
            ]:
                return

            self._move()
