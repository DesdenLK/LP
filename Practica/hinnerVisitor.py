# Generated from hinner.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hinnerParser import hinnerParser
else:
    from hinnerParser import hinnerParser

# This class defines a complete generic visitor for a parse tree produced by hinnerParser.

class hinnerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hinnerParser#root.
    def visitRoot(self, ctx:hinnerParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#exprStmt.
    def visitExprStmt(self, ctx:hinnerParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#TypeDefStmt.
    def visitTypeDefStmt(self, ctx:hinnerParser.TypeDefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#singleType.
    def visitSingleType(self, ctx:hinnerParser.SingleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#TypeAssocRight.
    def visitTypeAssocRight(self, ctx:hinnerParser.TypeAssocRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#ParType.
    def visitParType(self, ctx:hinnerParser.ParTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#operadorINFIX.
    def visitOperadorINFIX(self, ctx:hinnerParser.OperadorINFIXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#funcio.
    def visitFuncio(self, ctx:hinnerParser.FuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#aplicacioExpr.
    def visitAplicacioExpr(self, ctx:hinnerParser.AplicacioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#numero.
    def visitNumero(self, ctx:hinnerParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#abstraccioExpr.
    def visitAbstraccioExpr(self, ctx:hinnerParser.AbstraccioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#ident.
    def visitIdent(self, ctx:hinnerParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#parenthesis.
    def visitParenthesis(self, ctx:hinnerParser.ParenthesisContext):
        return self.visitChildren(ctx)



del hinnerParser