# Generated from Exercici4.g4 by ANTLR 4.13.1
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
        4,1,10,40,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,3,2,24,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,2,0,
        1,4,3,0,2,4,0,2,1,0,4,5,1,0,6,7,43,0,9,1,0,0,0,2,18,1,0,0,0,4,23,
        1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,
        0,0,0,10,1,1,0,0,0,11,9,1,0,0,0,12,13,5,8,0,0,13,14,5,1,0,0,14,19,
        3,4,2,0,15,16,5,2,0,0,16,19,3,4,2,0,17,19,3,4,2,0,18,12,1,0,0,0,
        18,15,1,0,0,0,18,17,1,0,0,0,19,3,1,0,0,0,20,21,6,2,-1,0,21,24,5,
        9,0,0,22,24,5,8,0,0,23,20,1,0,0,0,23,22,1,0,0,0,24,36,1,0,0,0,25,
        26,10,5,0,0,26,27,5,3,0,0,27,35,3,4,2,5,28,29,10,4,0,0,29,30,7,0,
        0,0,30,35,3,4,2,5,31,32,10,3,0,0,32,33,7,1,0,0,33,35,3,4,2,4,34,
        25,1,0,0,0,34,28,1,0,0,0,34,31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,
        0,36,37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,0,5,9,18,23,34,36
    ]

class Exercici4Parser ( Parser ):

    grammarFileName = "Exercici4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'^'", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2

    ruleNames =  [ "root", "statement", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    NUM=9
    WS=10

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Exercici4Parser.StatementContext,i)


        def getRuleIndex(self):
            return Exercici4Parser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = Exercici4Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 772) != 0):
                self.state = 6
                self.statement()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return Exercici4Parser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Exercici4Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Exercici4Parser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(Exercici4Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Exercici4Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = Exercici4Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = Exercici4Parser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(Exercici4Parser.ID)
                self.state = 13
                self.match(Exercici4Parser.T__0)
                self.state = 14
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = Exercici4Parser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(Exercici4Parser.T__1)
                self.state = 16
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = Exercici4Parser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.expr(0)
                pass


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
            return Exercici4Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Exercici4Parser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentExpr" ):
                return visitor.visitIdentExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultORdivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici4Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultORdiv" ):
                return visitor.visitMultORdiv(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(Exercici4Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class PotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici4Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPot" ):
                return visitor.visitPot(self)
            else:
                return visitor.visitChildren(self)


    class SumaORrestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici4Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaORresta" ):
                return visitor.visitSumaORresta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Exercici4Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = Exercici4Parser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(Exercici4Parser.NUM)
                pass
            elif token in [8]:
                localctx = Exercici4Parser.IdentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(Exercici4Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = Exercici4Parser.PotContext(self, Exercici4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 26
                        self.match(Exercici4Parser.T__2)
                        self.state = 27
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = Exercici4Parser.MultORdivContext(self, Exercici4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = Exercici4Parser.SumaORrestaContext(self, Exercici4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(4)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




