# Generated from analizadorLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,16,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,1,1,1,1,1,1,1,0,0,2,1,1,3,2,1,0,3,3,0,65,90,95,95,97,122,4,0,48,
        57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,16,0,1,1,0,0,0,0,3,1,
        0,0,0,1,5,1,0,0,0,3,12,1,0,0,0,5,9,7,0,0,0,6,8,7,1,0,0,7,6,1,0,0,
        0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,2,1,0,0,0,11,9,1,0,0,
        0,12,13,7,2,0,0,13,14,1,0,0,0,14,15,6,1,0,0,15,4,1,0,0,0,2,0,9,1,
        6,0,0
    ]

class analizadorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFICADOR = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFICADOR", "WS" ]

    ruleNames = [ "IDENTIFICADOR", "WS" ]

    grammarFileName = "analizadorLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


