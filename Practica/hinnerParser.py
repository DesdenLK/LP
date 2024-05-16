# Generated from hinner.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,27,8,2,1,
        2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,1,3,1,3,1,3,1,3,3,3,42,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,4,1,4,5,4,56,8,
        4,10,4,12,4,59,9,4,1,4,0,2,4,8,5,0,2,4,6,8,0,0,63,0,10,1,0,0,0,2,
        18,1,0,0,0,4,26,1,0,0,0,6,41,1,0,0,0,8,51,1,0,0,0,10,11,3,2,1,0,
        11,12,5,0,0,1,12,1,1,0,0,0,13,19,3,8,4,0,14,15,3,8,4,0,15,16,5,6,
        0,0,16,17,3,4,2,0,17,19,1,0,0,0,18,13,1,0,0,0,18,14,1,0,0,0,19,3,
        1,0,0,0,20,21,6,2,-1,0,21,27,5,8,0,0,22,23,5,2,0,0,23,24,3,4,2,0,
        24,25,5,3,0,0,25,27,1,0,0,0,26,20,1,0,0,0,26,22,1,0,0,0,27,33,1,
        0,0,0,28,29,10,2,0,0,29,30,5,5,0,0,30,32,3,4,2,2,31,28,1,0,0,0,32,
        35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,5,1,0,0,0,35,33,1,0,0,
        0,36,42,5,7,0,0,37,38,5,4,0,0,38,39,5,8,0,0,39,40,5,5,0,0,40,42,
        3,8,4,0,41,36,1,0,0,0,41,37,1,0,0,0,42,7,1,0,0,0,43,44,6,4,-1,0,
        44,45,5,2,0,0,45,46,3,8,4,0,46,47,5,3,0,0,47,52,1,0,0,0,48,52,3,
        6,3,0,49,52,5,1,0,0,50,52,5,8,0,0,51,43,1,0,0,0,51,48,1,0,0,0,51,
        49,1,0,0,0,51,50,1,0,0,0,52,57,1,0,0,0,53,54,10,4,0,0,54,56,3,8,
        4,5,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,9,
        1,0,0,0,59,57,1,0,0,0,6,18,26,33,41,51,57
    ]

class hinnerParser ( Parser ):

    grammarFileName = "hinner.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'\\'", "'->'", 
                     "'::'" ]

    symbolicNames = [ "<INVALID>", "NUM", "LPAR", "RPAR", "SLASH", "ARROW", 
                      "DOTS", "OPERADOR", "ID", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_defType = 2
    RULE_abstraccio = 3
    RULE_expr = 4

    ruleNames =  [ "root", "statement", "defType", "abstraccio", "expr" ]

    EOF = Token.EOF
    NUM=1
    LPAR=2
    RPAR=3
    SLASH=4
    ARROW=5
    DOTS=6
    OPERADOR=7
    ID=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(hinnerParser.StatementContext,0)


        def EOF(self):
            return self.getToken(hinnerParser.EOF, 0)

        def getRuleIndex(self):
            return hinnerParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hinnerParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.statement()
            self.state = 11
            self.match(hinnerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class TypeDefStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)

        def DOTS(self):
            return self.getToken(hinnerParser.DOTS, 0)
        def defType(self):
            return self.getTypedRuleContext(hinnerParser.DefTypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDefStmt" ):
                return visitor.visitTypeDefStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = hinnerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = hinnerParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = hinnerParser.TypeDefStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(hinnerParser.DOTS)
                self.state = 16
                self.defType(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_defType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleTypeContext(DefTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.DefTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hinnerParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleType" ):
                return visitor.visitSingleType(self)
            else:
                return visitor.visitChildren(self)


    class TypeAssocRightContext(DefTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.DefTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def defType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hinnerParser.DefTypeContext)
            else:
                return self.getTypedRuleContext(hinnerParser.DefTypeContext,i)

        def ARROW(self):
            return self.getToken(hinnerParser.ARROW, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAssocRight" ):
                return visitor.visitTypeAssocRight(self)
            else:
                return visitor.visitChildren(self)


    class ParTypeContext(DefTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.DefTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hinnerParser.LPAR, 0)
        def defType(self):
            return self.getTypedRuleContext(hinnerParser.DefTypeContext,0)

        def RPAR(self):
            return self.getToken(hinnerParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParType" ):
                return visitor.visitParType(self)
            else:
                return visitor.visitChildren(self)



    def defType(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hinnerParser.DefTypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_defType, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = hinnerParser.SingleTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(hinnerParser.ID)
                pass
            elif token in [2]:
                localctx = hinnerParser.ParTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(hinnerParser.LPAR)
                self.state = 23
                self.defType(0)
                self.state = 24
                self.match(hinnerParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hinnerParser.TypeAssocRightContext(self, hinnerParser.DefTypeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_defType)
                    self.state = 28
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 29
                    self.match(hinnerParser.ARROW)
                    self.state = 30
                    self.defType(2) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AbstraccioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_abstraccio

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncioContext(AbstraccioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.AbstraccioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SLASH(self):
            return self.getToken(hinnerParser.SLASH, 0)
        def ID(self):
            return self.getToken(hinnerParser.ID, 0)
        def ARROW(self):
            return self.getToken(hinnerParser.ARROW, 0)
        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncio" ):
                return visitor.visitFuncio(self)
            else:
                return visitor.visitChildren(self)


    class OperadorINFIXContext(AbstraccioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.AbstraccioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPERADOR(self):
            return self.getToken(hinnerParser.OPERADOR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorINFIX" ):
                return visitor.visitOperadorINFIX(self)
            else:
                return visitor.visitChildren(self)



    def abstraccio(self):

        localctx = hinnerParser.AbstraccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_abstraccio)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = hinnerParser.OperadorINFIXContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(hinnerParser.OPERADOR)
                pass
            elif token in [4]:
                localctx = hinnerParser.FuncioContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(hinnerParser.SLASH)
                self.state = 38
                self.match(hinnerParser.ID)
                self.state = 39
                self.match(hinnerParser.ARROW)
                self.state = 40
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AplicacioExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hinnerParser.ExprContext)
            else:
                return self.getTypedRuleContext(hinnerParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacioExpr" ):
                return visitor.visitAplicacioExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hinnerParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class AbstraccioExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def abstraccio(self):
            return self.getTypedRuleContext(hinnerParser.AbstraccioContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccioExpr" ):
                return visitor.visitAbstraccioExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hinnerParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hinnerParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(hinnerParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hinnerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = hinnerParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(hinnerParser.LPAR)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(hinnerParser.RPAR)
                pass
            elif token in [4, 7]:
                localctx = hinnerParser.AbstraccioExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.abstraccio()
                pass
            elif token in [1]:
                localctx = hinnerParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(hinnerParser.NUM)
                pass
            elif token in [8]:
                localctx = hinnerParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(hinnerParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hinnerParser.AplicacioExprContext(self, hinnerParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 53
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 54
                    self.expr(5) 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.defType_sempred
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def defType_sempred(self, localctx:DefTypeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




