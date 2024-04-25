# Generated from Exercici7.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Exercici7Parser import Exercici7Parser
else:
    from Exercici7Parser import Exercici7Parser

# This class defines a complete generic visitor for a parse tree produced by Exercici7Parser.

class Exercici7Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercici7Parser#root.
    def visitRoot(self, ctx:Exercici7Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#AssignStmt.
    def visitAssignStmt(self, ctx:Exercici7Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#writeStmt.
    def visitWriteStmt(self, ctx:Exercici7Parser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#ifStmt.
    def visitIfStmt(self, ctx:Exercici7Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#whileStmt.
    def visitWhileStmt(self, ctx:Exercici7Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#exprStmt.
    def visitExprStmt(self, ctx:Exercici7Parser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#identExpr.
    def visitIdentExpr(self, ctx:Exercici7Parser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#equal.
    def visitEqual(self, ctx:Exercici7Parser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#multORdiv.
    def visitMultORdiv(self, ctx:Exercici7Parser.MultORdivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#numero.
    def visitNumero(self, ctx:Exercici7Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#pot.
    def visitPot(self, ctx:Exercici7Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#sumaORresta.
    def visitSumaORresta(self, ctx:Exercici7Parser.SumaORrestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercici7Parser#diff.
    def visitDiff(self, ctx:Exercici7Parser.DiffContext):
        return self.visitChildren(ctx)



del Exercici7Parser