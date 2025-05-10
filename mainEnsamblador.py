from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from EnsambladorLexer import EnsambladorLexer
from EnsambladorParser import EnsambladorParser


# Manejador de errores personalizado
class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error sintáctico en línea {line}:{column} - {msg}")


def print_tokens(lexer):
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_name = lexer.symbolicNames[token.type] if 0 <= token.type < len(
            lexer.symbolicNames) else f"UNKNOWN({token.type})"
        print(f"Token: {token_name} Text: {token.text}")
        token = lexer.nextToken()


def main():
    # Prueba 1: "Sumar 5 y 3 y guardar en registro A"
    print("Prueba 1: Sumar 5 y 3 y guardar en registro A")
    input_text = "Sumar 5 y 3 y guardar en registro A\n"
    input_stream = InputStream(input_text)

    lexer = EnsambladorLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    print("Tokens generados:")
    print_tokens(lexer)

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

    print("Tokens generados:")
    print_tokens(lexer)

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

    print("Tokens generados:")
    print_tokens(lexer)

    stream = CommonTokenStream(lexer)

    parser = EnsambladorParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.programa()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()