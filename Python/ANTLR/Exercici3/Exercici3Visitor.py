# Generated from Exercici3.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Exercici3Parser import Exercici3Parser
else:
    from Exercici3Parser import Exercici3Parser

# This class defines a complete generic visitor for a parse tree produced by Exercici3Parser.

class Exercici3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercici3Parser#root.
    def visitRoot(self, ctx:Exercici3Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici3Parser#multORdiv.
    def visitMultORdiv(self, ctx:Exercici3Parser.MultORdivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici3Parser#numero.
    def visitNumero(self, ctx:Exercici3Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici3Parser#pot.
    def visitPot(self, ctx:Exercici3Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici3Parser#sumaORresta.
    def visitSumaORresta(self, ctx:Exercici3Parser.SumaORrestaContext):
        return self.visitChildren(ctx)



del Exercici3Parser