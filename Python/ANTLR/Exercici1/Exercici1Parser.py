# Generated from Exercici1.g4 by ANTLR 4.13.1
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
        4,1,7,24,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,0,1,2,2,0,2,0,2,
        1,0,2,3,1,0,4,5,24,0,4,1,0,0,0,2,6,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,
        0,6,7,6,1,-1,0,7,8,5,6,0,0,8,20,1,0,0,0,9,10,10,4,0,0,10,11,5,1,
        0,0,11,19,3,2,1,4,12,13,10,3,0,0,13,14,7,0,0,0,14,19,3,2,1,4,15,
        16,10,2,0,0,16,17,7,1,0,0,17,19,3,2,1,3,18,9,1,0,0,0,18,12,1,0,0,
        0,18,15,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,
        0,0,0,22,20,1,0,0,0,2,18,20
    ]

class Exercici1Parser ( Parser ):

    grammarFileName = "Exercici1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUM=6
    WS=7

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

        def expr(self):
            return self.getTypedRuleContext(Exercici1Parser.ExprContext,0)


        def getRuleIndex(self):
            return Exercici1Parser.RULE_root




    def root(self):

        localctx = Exercici1Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
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
            return Exercici1Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultORdivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici1Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici1Parser.ExprContext,i)



    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici1Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(Exercici1Parser.NUM, 0)


    class PotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici1Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici1Parser.ExprContext,i)



    class SumaORrestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Exercici1Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercici1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exercici1Parser.ExprContext,i)




    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Exercici1Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Exercici1Parser.NumeroContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 7
            self.match(Exercici1Parser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = Exercici1Parser.PotContext(self, Exercici1Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 9
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 10
                        self.match(Exercici1Parser.T__0)
                        self.state = 11
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = Exercici1Parser.MultORdivContext(self, Exercici1Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 13
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 14
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = Exercici1Parser.SumaORrestaContext(self, Exercici1Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 16
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 17
                        self.expr(3)
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




