# Generated from C:/ANTLR/Hello.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#hello.
    def enterHello(self, ctx:HelloParser.HelloContext):
        pass

    # Exit a parse tree produced by HelloParser#hello.
    def exitHello(self, ctx:HelloParser.HelloContext):
        pass



del HelloParser