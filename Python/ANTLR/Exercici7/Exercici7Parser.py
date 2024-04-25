# Generated from Exercici7.g4 by ANTLR 4.13.1
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
        4,1,17,68,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,1,1,
        3,1,41,8,1,1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,0,
        1,4,3,0,2,4,0,2,1,0,9,10,1,0,11,12,77,0,9,1,0,0,0,2,40,1,0,0,0,4,
        45,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,1,1,0,0,0,11,9,1,0,0,0,12,13,5,15,0,0,13,14,5,1,0,0,14,
        41,3,4,2,0,15,16,5,2,0,0,16,41,3,4,2,0,17,18,5,3,0,0,18,19,3,4,2,
        0,19,23,5,4,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,
        1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,5,0,0,
        27,41,1,0,0,0,28,29,5,6,0,0,29,30,3,4,2,0,30,34,5,7,0,0,31,33,3,
        2,1,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,
        37,1,0,0,0,36,34,1,0,0,0,37,38,5,5,0,0,38,41,1,0,0,0,39,41,3,4,2,
        0,40,12,1,0,0,0,40,15,1,0,0,0,40,17,1,0,0,0,40,28,1,0,0,0,40,39,
        1,0,0,0,41,3,1,0,0,0,42,43,6,2,-1,0,43,46,5,16,0,0,44,46,5,15,0,
        0,45,42,1,0,0,0,45,44,1,0,0,0,46,64,1,0,0,0,47,48,10,7,0,0,48,49,
        5,8,0,0,49,63,3,4,2,7,50,51,10,6,0,0,51,52,7,0,0,0,52,63,3,4,2,7,
        53,54,10,5,0,0,54,55,7,1,0,0,55,63,3,4,2,6,56,57,10,4,0,0,57,58,
        5,13,0,0,58,63,3,4,2,5,59,60,10,3,0,0,60,61,5,14,0,0,61,63,3,4,2,
        4,62,47,1,0,0,0,62,50,1,0,0,0,62,53,1,0,0,0,62,56,1,0,0,0,62,59,
        1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,0,0,0,66,
        64,1,0,0,0,7,9,23,34,40,45,62,64
    ]

class Exercici7Parser ( Parser ):

    grammarFileName = "Exercici7.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'if'", "'then'", "'end'", 
                     "'while'", "'do'", "'^'", "'*'", "'/'", "'+'", "'-'", 
                     "'='", "'<>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "WS" ]

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
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    NUM=16
    WS=17

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
                return self.getTypedRuleContexts(Exercici7Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.StatementContext,i)


        def getRuleIndex(self):
            return Exercici7Parser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = Exercici7Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 98380) != 0):
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
            return Exercici7Parser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Exercici7Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Exercici7Parser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Exercici7Parser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Exercici7Parser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(Exercici7Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Exercici7Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = Exercici7Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = Exercici7Parser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(Exercici7Parser.ID)
                self.state = 13
                self.match(Exercici7Parser.T__0)
                self.state = 14
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = Exercici7Parser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(Exercici7Parser.T__1)
                self.state = 16
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = Exercici7Parser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(Exercici7Parser.T__2)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(Exercici7Parser.T__3)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 98380) != 0):
                    self.state = 20
                    self.statement()
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 26
                self.match(Exercici7Parser.T__4)
                pass

            elif la_ == 4:
                localctx = Exercici7Parser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(Exercici7Parser.T__5)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(Exercici7Parser.T__6)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 98380) != 0):
                    self.state = 31
                    self.statement()
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 37
                self.match(Exercici7Parser.T__4)
                pass

            elif la_ == 5:
                localctx = Exercici7Parser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
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
            return Exercici7Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Exercici7Parser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentExpr" ):
                return visitor.visitIdentExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class MultORdivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultORdiv" ):
                return visitor.visitMultORdiv(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(Exercici7Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class PotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPot" ):
                return visitor.visitPot(self)
            else:
                return visitor.visitChildren(self)


    class SumaORrestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaORresta" ):
                return visitor.visitSumaORresta(self)
            else:
                return visitor.visitChildren(self)


    class DiffContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici7Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici7Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici7Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiff" ):
                return visitor.visitDiff(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Exercici7Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = Exercici7Parser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(Exercici7Parser.NUM)
                pass
            elif token in [15]:
                localctx = Exercici7Parser.IdentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(Exercici7Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = Exercici7Parser.PotContext(self, Exercici7Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 48
                        self.match(Exercici7Parser.T__7)
                        self.state = 49
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = Exercici7Parser.MultORdivContext(self, Exercici7Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = Exercici7Parser.SumaORrestaContext(self, Exercici7Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = Exercici7Parser.EqualContext(self, Exercici7Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 57
                        self.match(Exercici7Parser.T__12)
                        self.state = 58
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = Exercici7Parser.DiffContext(self, Exercici7Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        self.match(Exercici7Parser.T__13)
                        self.state = 61
                        self.expr(4)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




