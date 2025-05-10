from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser

def main():
    data = "Hola Mundo!"
    input_stream = InputStream(data)
    lexer = HelloLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = HelloParser(token_stream)
    tree = parser.hello()

    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
