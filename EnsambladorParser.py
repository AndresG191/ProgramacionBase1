# Generated from Ensamblador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
from typing import TextIO

def serializedATN():
    return [
        4,1,22,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,2,3,2,40,8,2,1,
        3,1,3,1,3,1,3,3,3,46,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,13,
        15,1,0,14,15,65,0,15,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,41,1,0,
        0,0,8,49,1,0,0,0,10,54,1,0,0,0,12,61,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,
        19,20,5,0,0,1,20,1,1,0,0,0,21,27,3,4,2,0,22,27,3,6,3,0,23,27,3,8,
        4,0,24,27,3,10,5,0,25,27,3,12,6,0,26,21,1,0,0,0,26,22,1,0,0,0,26,
        23,1,0,0,0,26,24,1,0,0,0,26,25,1,0,0,0,27,3,1,0,0,0,28,29,5,11,0,
        0,29,30,7,0,0,0,30,31,5,12,0,0,31,39,7,0,0,0,32,33,5,1,0,0,33,34,
        5,2,0,0,34,36,5,3,0,0,35,37,5,4,0,0,36,35,1,0,0,0,36,37,1,0,0,0,
        37,38,1,0,0,0,38,40,7,1,0,0,39,32,1,0,0,0,39,40,1,0,0,0,40,5,1,0,
        0,0,41,42,5,5,0,0,42,43,7,0,0,0,43,45,5,6,0,0,44,46,5,4,0,0,45,44,
        1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,7,1,0,0,48,7,1,0,0,0,49,
        50,5,7,0,0,50,51,7,1,0,0,51,52,5,8,0,0,52,53,7,0,0,0,53,9,1,0,0,
        0,54,55,5,9,0,0,55,56,7,1,0,0,56,57,5,16,0,0,57,58,7,0,0,0,58,59,
        5,10,0,0,59,60,5,17,0,0,60,11,1,0,0,0,61,62,5,10,0,0,62,63,5,17,
        0,0,63,13,1,0,0,0,5,17,26,36,39,45
    ]

class EnsambladorParser ( Parser ):

    grammarFileName = "Ensamblador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'y'", "'guardar'", "'en'", "'registro'", 
                     "'mover'", "'a'", "'comparar'", "'con'", "'si'", "'ir_a'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OPERACION", 
                      "OPERADOR", "NUMERO", "REGISTRO", "VARIABLE", "COMPARADOR", 
                      "ETIQUETA", "SEPARADOR", "ESPACIO", "SALTO_LINEA", 
                      "IGNORAR", "ERROR" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_operacion_aritmetica = 2
    RULE_operacion_movimiento = 3
    RULE_operacion_comparacion = 4
    RULE_operacion_condicional = 5
    RULE_operacion_salto = 6

    ruleNames =  [ "programa", "instruccion", "operacion_aritmetica", "operacion_movimiento", 
                   "operacion_comparacion", "operacion_condicional", "operacion_salto" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    OPERACION=11
    OPERADOR=12
    NUMERO=13
    REGISTRO=14
    VARIABLE=15
    COMPARADOR=16
    ETIQUETA=17
    SEPARADOR=18
    ESPACIO=19
    SALTO_LINEA=20
    IGNORAR=21
    ERROR=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EnsambladorParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnsambladorParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(EnsambladorParser.InstruccionContext,i)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = EnsambladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.instruccion()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3744) != 0)):
                    break

            self.state = 19
            self.match(EnsambladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacion_aritmetica(self):
            return self.getTypedRuleContext(EnsambladorParser.Operacion_aritmeticaContext,0)


        def operacion_movimiento(self):
            return self.getTypedRuleContext(EnsambladorParser.Operacion_movimientoContext,0)


        def operacion_comparacion(self):
            return self.getTypedRuleContext(EnsambladorParser.Operacion_comparacionContext,0)


        def operacion_condicional(self):
            return self.getTypedRuleContext(EnsambladorParser.Operacion_condicionalContext,0)


        def operacion_salto(self):
            return self.getTypedRuleContext(EnsambladorParser.Operacion_saltoContext,0)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = EnsambladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.operacion_aritmetica()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.operacion_movimiento()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.operacion_comparacion()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.operacion_condicional()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                self.operacion_salto()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacion_aritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERACION(self):
            return self.getToken(EnsambladorParser.OPERACION, 0)

        def OPERADOR(self):
            return self.getToken(EnsambladorParser.OPERADOR, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.NUMERO)
            else:
                return self.getToken(EnsambladorParser.NUMERO, i)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.VARIABLE)
            else:
                return self.getToken(EnsambladorParser.VARIABLE, i)

        def REGISTRO(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.REGISTRO)
            else:
                return self.getToken(EnsambladorParser.REGISTRO, i)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operacion_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion_aritmetica" ):
                listener.enterOperacion_aritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion_aritmetica" ):
                listener.exitOperacion_aritmetica(self)




    def operacion_aritmetica(self):

        localctx = EnsambladorParser.Operacion_aritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operacion_aritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(EnsambladorParser.OPERACION)
            self.state = 29
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 30
            self.match(EnsambladorParser.OPERADOR)
            self.state = 31
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 32
                self.match(EnsambladorParser.T__0)
                self.state = 33
                self.match(EnsambladorParser.T__1)
                self.state = 34
                self.match(EnsambladorParser.T__2)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 35
                    self.match(EnsambladorParser.T__3)


                self.state = 38
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacion_movimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.VARIABLE)
            else:
                return self.getToken(EnsambladorParser.VARIABLE, i)

        def REGISTRO(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.REGISTRO)
            else:
                return self.getToken(EnsambladorParser.REGISTRO, i)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operacion_movimiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion_movimiento" ):
                listener.enterOperacion_movimiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion_movimiento" ):
                listener.exitOperacion_movimiento(self)




    def operacion_movimiento(self):

        localctx = EnsambladorParser.Operacion_movimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operacion_movimiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(EnsambladorParser.T__4)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
            self.match(EnsambladorParser.T__5)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 44
                self.match(EnsambladorParser.T__3)


            self.state = 47
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacion_comparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.VARIABLE)
            else:
                return self.getToken(EnsambladorParser.VARIABLE, i)

        def REGISTRO(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.REGISTRO)
            else:
                return self.getToken(EnsambladorParser.REGISTRO, i)

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operacion_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion_comparacion" ):
                listener.enterOperacion_comparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion_comparacion" ):
                listener.exitOperacion_comparacion(self)




    def operacion_comparacion(self):

        localctx = EnsambladorParser.Operacion_comparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operacion_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(EnsambladorParser.T__6)
            self.state = 50
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 51
            self.match(EnsambladorParser.T__7)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacion_condicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARADOR(self):
            return self.getToken(EnsambladorParser.COMPARADOR, 0)

        def ETIQUETA(self):
            return self.getToken(EnsambladorParser.ETIQUETA, 0)

        def REGISTRO(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.REGISTRO)
            else:
                return self.getToken(EnsambladorParser.REGISTRO, i)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.VARIABLE)
            else:
                return self.getToken(EnsambladorParser.VARIABLE, i)

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operacion_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion_condicional" ):
                listener.enterOperacion_condicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion_condicional" ):
                listener.exitOperacion_condicional(self)




    def operacion_condicional(self):

        localctx = EnsambladorParser.Operacion_condicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operacion_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(EnsambladorParser.T__8)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.match(EnsambladorParser.COMPARADOR)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self.match(EnsambladorParser.T__9)
            self.state = 59
            self.match(EnsambladorParser.ETIQUETA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacion_saltoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ETIQUETA(self):
            return self.getToken(EnsambladorParser.ETIQUETA, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operacion_salto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion_salto" ):
                listener.enterOperacion_salto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion_salto" ):
                listener.exitOperacion_salto(self)




    def operacion_salto(self):

        localctx = EnsambladorParser.Operacion_saltoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operacion_salto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(EnsambladorParser.T__9)
            self.state = 62
            self.match(EnsambladorParser.ETIQUETA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





