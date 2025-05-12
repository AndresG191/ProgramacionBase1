# Generated from Ensamblador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EnsambladorParser import EnsambladorParser
else:
    from EnsambladorParser import EnsambladorParser

# This class defines a complete listener for a parse tree produced by EnsambladorParser.
class EnsambladorListener(ParseTreeListener):

    # Enter a parse tree produced by EnsambladorParser#programa.
    def enterPrograma(self, ctx:EnsambladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#programa.
    def exitPrograma(self, ctx:EnsambladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#instruccion.
    def enterInstruccion(self, ctx:EnsambladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#instruccion.
    def exitInstruccion(self, ctx:EnsambladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operacion_aritmetica.
    def enterOperacion_aritmetica(self, ctx:EnsambladorParser.Operacion_aritmeticaContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operacion_aritmetica.
    def exitOperacion_aritmetica(self, ctx:EnsambladorParser.Operacion_aritmeticaContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operacion_movimiento.
    def enterOperacion_movimiento(self, ctx:EnsambladorParser.Operacion_movimientoContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operacion_movimiento.
    def exitOperacion_movimiento(self, ctx:EnsambladorParser.Operacion_movimientoContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operacion_comparacion.
    def enterOperacion_comparacion(self, ctx:EnsambladorParser.Operacion_comparacionContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operacion_comparacion.
    def exitOperacion_comparacion(self, ctx:EnsambladorParser.Operacion_comparacionContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operacion_condicional.
    def enterOperacion_condicional(self, ctx:EnsambladorParser.Operacion_condicionalContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operacion_condicional.
    def exitOperacion_condicional(self, ctx:EnsambladorParser.Operacion_condicionalContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operacion_salto.
    def enterOperacion_salto(self, ctx:EnsambladorParser.Operacion_saltoContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operacion_salto.
    def exitOperacion_salto(self, ctx:EnsambladorParser.Operacion_saltoContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operando.
    def enterOperando(self, ctx:EnsambladorParser.OperandoContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operando.
    def exitOperando(self, ctx:EnsambladorParser.OperandoContext):
        pass



del EnsambladorParser