from antlr4 import *
from Exercici3Lexer import Exercici3Lexer
from Exercici3Parser import Exercici3Parser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor



if __name__ == "__main__":
    input_stream = InputStream(input('? '))
    lexer = Exercici3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Exercici3Parser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = TreeVisitor()
        visitor.visit(tree)
        eval = EvalVisitor()
        eval.visit(tree)
    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))