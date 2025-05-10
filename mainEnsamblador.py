from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from EnsambladorLexer import EnsambladorLexer
from EnsambladorParser import EnsambladorParser


# Manejador de errores personalizado
class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error sintáctico en línea {line}:{column} - {msg}")


def main():
    # Prueba 1: "Sumar 5 y 3 y guardar en registro A"
    print("Prueba 1: Sumar 5 y 3 y guardar en registro A")
    input_text = "Sumar 5 y 3 y guardar en registro A\n"
    input_stream = InputStream(input_text)

    lexer = EnsambladorLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    stream = CommonTokenStream(lexer)

    parser = EnsambladorParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.programa()
    print(tree.toStringTree(recog=parser))
    print()

    # Prueba 2: "Sumar 5 de 3 y guardar en registro A"
    print("Prueba 2: Sumar 5 de 3 y guardar en registro A")
    input_text = "Sumar 5 de 3 y guardar en registro A\n"
    input_stream = InputStream(input_text)

    lexer = EnsambladorLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    stream = CommonTokenStream(lexer)

    parser = EnsambladorParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.programa()
    print(tree.toStringTree(recog=parser))
    print()

    # Prueba 3: "Sumar 5 y 3"
    print("Prueba 3: Sumar 5 y 3")
    input_text = "Sumar 5 y 3\n"
    input_stream = InputStream(input_text)

    lexer = EnsambladorLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    stream = CommonTokenStream(lexer)

    parser = EnsambladorParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.programa()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()