# Generated from Exercici5.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Exercici5Parser import Exercici5Parser
else:
    from Exercici5Parser import Exercici5Parser

# This class defines a complete generic visitor for a parse tree produced by Exercici5Parser.

class Exercici5Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercici5Parser#root.
    def visitRoot(self, ctx:Exercici5Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#AssignStmt.
    def visitAssignStmt(self, ctx:Exercici5Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#writeStmt.
    def visitWriteStmt(self, ctx:Exercici5Parser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#ifStmt.
    def visitIfStmt(self, ctx:Exercici5Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#exprStmt.
    def visitExprStmt(self, ctx:Exercici5Parser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#identExpr.
    def visitIdentExpr(self, ctx:Exercici5Parser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#equal.
    def visitEqual(self, ctx:Exercici5Parser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#multORdiv.
    def visitMultORdiv(self, ctx:Exercici5Parser.MultORdivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#numero.
    def visitNumero(self, ctx:Exercici5Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#pot.
    def visitPot(self, ctx:Exercici5Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici5Parser#sumaORresta.
    def visitSumaORresta(self, ctx:Exercici5Parser.SumaORrestaContext):
        return self.visitChildren(ctx)



del Exercici5Parser