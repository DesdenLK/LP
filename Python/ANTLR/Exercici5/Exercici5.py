from sys import argv
from antlr4 import *
from Exercici5Lexer import Exercici5Lexer
from Exercici5Parser import Exercici5Parser
from EvalVisitor import EvalVisitor



if __name__ == "__main__":
    if (len(argv) > 1):
        input_stream = FileStream(argv[1])
    else:
        input_stream = InputStream(input('? '))
    lexer = Exercici5Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Exercici5Parser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        eval = EvalVisitor()
        eval.visit(tree)
    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))