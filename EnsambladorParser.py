# Generated from Ensamblador.g4 by ANTLR 4.13.2
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
        4,1,26,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,2,0,18,19,21,21,
        60,0,17,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,40,1,0,0,0,8,45,1,0,
        0,0,10,50,1,0,0,0,12,57,1,0,0,0,14,60,1,0,0,0,16,18,3,2,1,0,17,16,
        1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,
        21,22,5,0,0,1,22,1,1,0,0,0,23,29,3,4,2,0,24,29,3,6,3,0,25,29,3,8,
        4,0,26,29,3,10,5,0,27,29,3,12,6,0,28,23,1,0,0,0,28,24,1,0,0,0,28,
        25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,1,0,
        0,31,32,3,14,7,0,32,33,5,16,0,0,33,38,3,14,7,0,34,35,5,14,0,0,35,
        36,5,7,0,0,36,37,5,11,0,0,37,39,5,19,0,0,38,34,1,0,0,0,38,39,1,0,
        0,0,39,5,1,0,0,0,40,41,5,6,0,0,41,42,3,14,7,0,42,43,5,15,0,0,43,
        44,5,19,0,0,44,7,1,0,0,0,45,46,5,8,0,0,46,47,3,14,7,0,47,48,5,12,
        0,0,48,49,3,14,7,0,49,9,1,0,0,0,50,51,5,9,0,0,51,52,3,14,7,0,52,
        53,5,17,0,0,53,54,3,14,7,0,54,55,5,10,0,0,55,56,5,20,0,0,56,11,1,
        0,0,0,57,58,5,10,0,0,58,59,5,20,0,0,59,13,1,0,0,0,60,61,7,0,0,0,
        61,15,1,0,0,0,3,19,28,38
    ]

class EnsambladorParser ( Parser ):

    grammarFileName = "Ensamblador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "OPERACION_ARITMETICA", "SUMAR", "RESTAR", 
                      "MULTIPLICAR", "DIVIDIR", "MOVER", "GUARDAR", "COMPARAR", 
                      "SI", "IR_A", "EN", "CON", "DE", "Y", "A", "OPERADOR", 
                      "COMPARADOR", "NUMERO", "REGISTRO", "ETIQUETA", "VARIABLE", 
                      "SEPARADOR", "ESPACIO", "SALTO_LINEA", "COMENTARIO", 
                      "ERROR" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_operacion_aritmetica = 2
    RULE_operacion_movimiento = 3
    RULE_operacion_comparacion = 4
    RULE_operacion_condicional = 5
    RULE_operacion_salto = 6
    RULE_operando = 7

    ruleNames =  [ "programa", "instruccion", "operacion_aritmetica", "operacion_movimiento", 
                   "operacion_comparacion", "operacion_condicional", "operacion_salto", 
                   "operando" ]

    EOF = Token.EOF
    OPERACION_ARITMETICA=1
    SUMAR=2
    RESTAR=3
    MULTIPLICAR=4
    DIVIDIR=5
    MOVER=6
    GUARDAR=7
    COMPARAR=8
    SI=9
    IR_A=10
    EN=11
    CON=12
    DE=13
    Y=14
    A=15
    OPERADOR=16
    COMPARADOR=17
    NUMERO=18
    REGISTRO=19
    ETIQUETA=20
    VARIABLE=21
    SEPARADOR=22
    ESPACIO=23
    SALTO_LINEA=24
    COMENTARIO=25
    ERROR=26

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.instruccion()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1858) != 0)):
                    break

            self.state = 21
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
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.operacion_aritmetica()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.operacion_movimiento()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.operacion_comparacion()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.operacion_condicional()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
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

        def OPERACION_ARITMETICA(self):
            return self.getToken(EnsambladorParser.OPERACION_ARITMETICA, 0)

        def operando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnsambladorParser.OperandoContext)
            else:
                return self.getTypedRuleContext(EnsambladorParser.OperandoContext,i)


        def OPERADOR(self):
            return self.getToken(EnsambladorParser.OPERADOR, 0)

        def Y(self):
            return self.getToken(EnsambladorParser.Y, 0)

        def GUARDAR(self):
            return self.getToken(EnsambladorParser.GUARDAR, 0)

        def EN(self):
            return self.getToken(EnsambladorParser.EN, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

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
            self.state = 30
            self.match(EnsambladorParser.OPERACION_ARITMETICA)
            self.state = 31
            self.operando()
            self.state = 32
            self.match(EnsambladorParser.OPERADOR)
            self.state = 33
            self.operando()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 34
                self.match(EnsambladorParser.Y)
                self.state = 35
                self.match(EnsambladorParser.GUARDAR)
                self.state = 36
                self.match(EnsambladorParser.EN)
                self.state = 37
                self.match(EnsambladorParser.REGISTRO)


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

        def MOVER(self):
            return self.getToken(EnsambladorParser.MOVER, 0)

        def operando(self):
            return self.getTypedRuleContext(EnsambladorParser.OperandoContext,0)


        def A(self):
            return self.getToken(EnsambladorParser.A, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(EnsambladorParser.MOVER)
            self.state = 41
            self.operando()
            self.state = 42
            self.match(EnsambladorParser.A)
            self.state = 43
            self.match(EnsambladorParser.REGISTRO)
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

        def COMPARAR(self):
            return self.getToken(EnsambladorParser.COMPARAR, 0)

        def operando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnsambladorParser.OperandoContext)
            else:
                return self.getTypedRuleContext(EnsambladorParser.OperandoContext,i)


        def CON(self):
            return self.getToken(EnsambladorParser.CON, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(EnsambladorParser.COMPARAR)
            self.state = 46
            self.operando()
            self.state = 47
            self.match(EnsambladorParser.CON)
            self.state = 48
            self.operando()
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

        def SI(self):
            return self.getToken(EnsambladorParser.SI, 0)

        def operando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnsambladorParser.OperandoContext)
            else:
                return self.getTypedRuleContext(EnsambladorParser.OperandoContext,i)


        def COMPARADOR(self):
            return self.getToken(EnsambladorParser.COMPARADOR, 0)

        def IR_A(self):
            return self.getToken(EnsambladorParser.IR_A, 0)

        def ETIQUETA(self):
            return self.getToken(EnsambladorParser.ETIQUETA, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(EnsambladorParser.SI)
            self.state = 51
            self.operando()
            self.state = 52
            self.match(EnsambladorParser.COMPARADOR)
            self.state = 53
            self.operando()
            self.state = 54
            self.match(EnsambladorParser.IR_A)
            self.state = 55
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

        def IR_A(self):
            return self.getToken(EnsambladorParser.IR_A, 0)

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
            self.state = 57
            self.match(EnsambladorParser.IR_A)
            self.state = 58
            self.match(EnsambladorParser.ETIQUETA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

        def VARIABLE(self):
            return self.getToken(EnsambladorParser.VARIABLE, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperando" ):
                listener.enterOperando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperando" ):
                listener.exitOperando(self)




    def operando(self):

        localctx = EnsambladorParser.OperandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operando)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2883584) != 0)):
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





