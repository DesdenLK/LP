# Generated from Exercici2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Exercici2Parser import Exercici2Parser
else:
    from Exercici2Parser import Exercici2Parser

# This class defines a complete generic visitor for a parse tree produced by Exercici2Parser.

class Exercici2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercici2Parser#root.
    def visitRoot(self, ctx:Exercici2Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici2Parser#multORdiv.
    def visitMultORdiv(self, ctx:Exercici2Parser.MultORdivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici2Parser#numero.
    def visitNumero(self, ctx:Exercici2Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici2Parser#pot.
    def visitPot(self, ctx:Exercici2Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici2Parser#sumaORresta.
    def visitSumaORresta(self, ctx:Exercici2Parser.SumaORrestaContext):
        return self.visitChildren(ctx)



del Exercici2Parser