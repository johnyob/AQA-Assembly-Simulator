from enum import Enum as Enumerate

import aqa_assembly_simulator.parser.Statement as Statement


class TokenType(Enumerate):
    IDENTIFIER = 1

    LDR = 2
    STR = 3
    ADD = 4
    SUB = 5
    MOV = 6
    CMP = 7
    B = 8
    BEQ = 9
    BNE = 10
    BGT = 11
    BLT = 12
    AND = 13
    ORR = 14
    EOR = 15
    MVN = 16
    LSL = 17
    LSR = 18
    HALT = 19

    REGISTER = 20
    IMMEDIATE_ADDRESS = 21
    DIRECT_ADDRESS = 22
    OPERAND = 23
    COLON = 24
    COMMA = 25
    EOF = 26

KEYWORDS = {
    "LDR": TokenType.LDR,
    "STR": TokenType.STR,
    "ADD": TokenType.ADD,
    "SUB": TokenType.SUB,
    "MOV": TokenType.MOV,
    "CMP": TokenType.CMP,
    "B": TokenType.B,
    "BEQ": TokenType.BEQ,
    "BNE": TokenType.BNE,
    "BGT": TokenType.BGT,
    "BLT": TokenType.BLT,
    "AND": TokenType.AND,
    "ORR": TokenType.ORR,
    "EOR": TokenType.EOR,
    "MVN": TokenType.MVN,
    "LSL": TokenType.LSL,
    "LSR": TokenType.LSR,
    "HALT": TokenType.HALT
}

STATEMENTS = {
    2: Statement.Load,
    3: Statement.Store,
    4: Statement.Add,
    5: Statement.Subtract,
    6: Statement.Move,
    7: Statement.Compare,
    8: Statement.Branch,
    9: Statement.BranchEqual,
    10: Statement.BranchNotEqual,
    11: Statement.BranchGreaterThan,
    12: Statement.BranchLessThan,
    13: Statement.And,
    14: Statement.Or,
    15: Statement.Eor,
    16: Statement.Not,
    17: Statement.LeftShift,
    18: Statement.RightShift,
    19: Statement.Halt
}
