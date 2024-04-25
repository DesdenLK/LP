from antlr4 import *
from Exercici2Lexer import Exercici2Lexer
from Exercici2Parser import Exercici2Parser
from TreeVisitor import TreeVisitor



if __name__ == "__main__":
    input_stream = InputStream(input('? '))
    lexer = Exercici2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Exercici2Parser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = TreeVisitor()
        visitor.visit(tree)
    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))