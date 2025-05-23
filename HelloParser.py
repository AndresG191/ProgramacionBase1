# Generated from C:/ANTLR/Hello.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,7,2,0,7,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,5,0,2,1,0,0,0,2,
        3,5,1,0,0,3,4,5,3,0,0,4,5,5,2,0,0,5,1,1,0,0,0,0
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Hola'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_hello = 0

    ruleNames =  [ "hello" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HelloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_hello

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHello" ):
                listener.enterHello(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHello" ):
                listener.exitHello(self)




    def hello(self):

        localctx = HelloParser.HelloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_hello)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.T__0)
            self.state = 3
            self.match(HelloParser.ID)
            self.state = 4
            self.match(HelloParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





