from antlr4 import *
from Exercici1Lexer import Exercici1Lexer
from Exercici1Parser import Exercici1Parser
input_stream = InputStream(input('? '))
lexer = Exercici1Lexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Exercici1Parser(token_stream)
tree = parser.root()
print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))