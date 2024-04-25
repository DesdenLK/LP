# Generated from Exercici4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Exercici4Parser import Exercici4Parser
else:
    from Exercici4Parser import Exercici4Parser

# This class defines a complete generic visitor for a parse tree produced by Exercici4Parser.

class Exercici4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercici4Parser#root.
    def visitRoot(self, ctx:Exercici4Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#AssignStmt.
    def visitAssignStmt(self, ctx:Exercici4Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#writeStmt.
    def visitWriteStmt(self, ctx:Exercici4Parser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#exprStmt.
    def visitExprStmt(self, ctx:Exercici4Parser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#identExpr.
    def visitIdentExpr(self, ctx:Exercici4Parser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#multORdiv.
    def visitMultORdiv(self, ctx:Exercici4Parser.MultORdivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#numero.
    def visitNumero(self, ctx:Exercici4Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#pot.
    def visitPot(self, ctx:Exercici4Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici4Parser#sumaORresta.
    def visitSumaORresta(self, ctx:Exercici4Parser.SumaORrestaContext):
        return self.visitChildren(ctx)



del Exercici4Parser