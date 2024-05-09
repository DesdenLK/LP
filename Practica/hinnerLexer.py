# Generated from hinner.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,23,8,0,11,0,12,0,24,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,
        7,3,7,45,8,7,1,8,1,8,5,8,49,8,8,10,8,12,8,52,9,8,1,9,4,9,55,8,9,
        11,9,12,9,56,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,1,0,4,1,0,48,57,2,0,65,90,97,122,4,0,48,57,65,90,95,95,97,
        122,3,0,9,10,13,13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,1,22,1,0,0,0,3,26,1,0,0,0,5,28,1,0,0,0,7,
        30,1,0,0,0,9,32,1,0,0,0,11,35,1,0,0,0,13,38,1,0,0,0,15,44,1,0,0,
        0,17,46,1,0,0,0,19,54,1,0,0,0,21,23,7,0,0,0,22,21,1,0,0,0,23,24,
        1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,2,1,0,0,0,26,27,5,40,0,0,
        27,4,1,0,0,0,28,29,5,41,0,0,29,6,1,0,0,0,30,31,5,92,0,0,31,8,1,0,
        0,0,32,33,5,45,0,0,33,34,5,62,0,0,34,10,1,0,0,0,35,36,5,58,0,0,36,
        37,5,58,0,0,37,12,1,0,0,0,38,39,7,1,0,0,39,14,1,0,0,0,40,41,5,40,
        0,0,41,42,5,43,0,0,42,45,5,41,0,0,43,45,5,45,0,0,44,40,1,0,0,0,44,
        43,1,0,0,0,45,16,1,0,0,0,46,50,7,1,0,0,47,49,7,2,0,0,48,47,1,0,0,
        0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,18,1,0,0,0,52,50,
        1,0,0,0,53,55,7,3,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,
        56,57,1,0,0,0,57,58,1,0,0,0,58,59,6,9,0,0,59,20,1,0,0,0,5,0,24,44,
        50,56,1,6,0,0
    ]

class hinnerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    LPAR = 2
    RPAR = 3
    SLASH = 4
    ARROW = 5
    DOTS = 6
    TYPE = 7
    OPERADOR = 8
    ID = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'\\'", "'->'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "LPAR", "RPAR", "SLASH", "ARROW", "DOTS", "TYPE", "OPERADOR", 
            "ID", "WS" ]

    ruleNames = [ "NUM", "LPAR", "RPAR", "SLASH", "ARROW", "DOTS", "TYPE", 
                  "OPERADOR", "ID", "WS" ]

    grammarFileName = "hinner.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


