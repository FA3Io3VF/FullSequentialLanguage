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
        4,1,25,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,55,8,3,10,3,
        12,3,58,9,3,1,4,1,4,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,9,5,1,6,
        1,6,1,6,3,6,73,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        99,8,10,1,10,1,10,1,10,5,10,104,8,10,10,10,12,10,107,9,10,1,11,1,
        11,1,11,1,11,1,11,1,12,1,12,1,12,5,12,117,8,12,10,12,12,12,120,9,
        12,3,12,122,8,12,1,12,0,1,20,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,1,1,0,11,20,122,0,27,1,0,0,0,2,33,1,0,0,0,4,44,1,0,0,0,6,51,1,
        0,0,0,8,59,1,0,0,0,10,61,1,0,0,0,12,72,1,0,0,0,14,74,1,0,0,0,16,
        78,1,0,0,0,18,85,1,0,0,0,20,98,1,0,0,0,22,108,1,0,0,0,24,121,1,0,
        0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,31,1,0,0,0,31,32,3,4,2,0,32,1,1,0,0,0,33,34,5,1,0,0,34,
        35,5,24,0,0,35,36,5,2,0,0,36,37,5,1,0,0,37,38,3,6,3,0,38,39,5,3,
        0,0,39,40,3,10,5,0,40,41,5,2,0,0,41,42,5,4,0,0,42,43,5,24,0,0,43,
        3,1,0,0,0,44,45,5,1,0,0,45,46,5,5,0,0,46,47,5,2,0,0,47,48,5,1,0,
        0,48,49,3,6,3,0,49,50,5,2,0,0,50,5,1,0,0,0,51,56,3,8,4,0,52,53,5,
        6,0,0,53,55,3,8,4,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,
        57,1,0,0,0,57,7,1,0,0,0,58,56,1,0,0,0,59,60,5,24,0,0,60,9,1,0,0,
        0,61,66,3,12,6,0,62,63,5,6,0,0,63,65,3,12,6,0,64,62,1,0,0,0,65,68,
        1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,11,1,0,0,0,68,66,1,0,0,0,
        69,73,3,14,7,0,70,73,3,16,8,0,71,73,3,18,9,0,72,69,1,0,0,0,72,70,
        1,0,0,0,72,71,1,0,0,0,73,13,1,0,0,0,74,75,3,8,4,0,75,76,5,7,0,0,
        76,77,3,20,10,0,77,15,1,0,0,0,78,79,5,8,0,0,79,80,3,20,10,0,80,81,
        5,9,0,0,81,82,3,12,6,0,82,83,5,10,0,0,83,84,3,12,6,0,84,17,1,0,0,
        0,85,86,3,8,4,0,86,87,5,7,0,0,87,88,5,21,0,0,88,19,1,0,0,0,89,90,
        6,10,-1,0,90,91,5,1,0,0,91,92,3,20,10,0,92,93,5,2,0,0,93,99,1,0,
        0,0,94,99,5,22,0,0,95,99,5,23,0,0,96,99,3,8,4,0,97,99,3,22,11,0,
        98,89,1,0,0,0,98,94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,
        0,0,0,99,105,1,0,0,0,100,101,10,5,0,0,101,102,7,0,0,0,102,104,3,
        20,10,6,103,100,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,
        1,0,0,0,106,21,1,0,0,0,107,105,1,0,0,0,108,109,5,24,0,0,109,110,
        5,1,0,0,110,111,3,24,12,0,111,112,5,2,0,0,112,23,1,0,0,0,113,118,
        3,20,10,0,114,115,5,6,0,0,115,117,3,20,10,0,116,114,1,0,0,0,117,
        120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,122,1,0,0,0,120,
        118,1,0,0,0,121,113,1,0,0,0,121,122,1,0,0,0,122,25,1,0,0,0,8,29,
        56,66,72,98,105,118,121
    ]

class FullSeqParser ( Parser ):

    grammarFileName = "FullSeq.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'|'", "'=>'", "'End'", 
                     "','", "'='", "'if'", "'then'", "'else'", "'*'", "'/'", 
                     "'+'", "'-'", "'=='", "'!='", "'<='", "'>='", "'<'", 
                     "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "INT", "FLOAT", "ID", "WS" ]

    RULE_program = 0
    RULE_blockDefinition = 1
    RULE_endBlock = 2
    RULE_varList = 3
    RULE_var = 4
    RULE_statementList = 5
    RULE_statement = 6
    RULE_assignment = 7
    RULE_ifStatement = 8
    RULE_concatenation = 9
    RULE_expression = 10
    RULE_functionCall = 11
    RULE_expressionList = 12

    ruleNames =  [ "program", "blockDefinition", "endBlock", "varList", 
                   "var", "statementList", "statement", "assignment", "ifStatement", 
                   "concatenation", "expression", "functionCall", "expressionList" ]

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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    STRING=21
    INT=22
    FLOAT=23
    ID=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endBlock(self):
            return self.getTypedRuleContext(FullSeqParser.EndBlockContext,0)


        def blockDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullSeqParser.BlockDefinitionContext)
            else:
                return self.getTypedRuleContext(FullSeqParser.BlockDefinitionContext,i)


        def getRuleIndex(self):
            return FullSeqParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FullSeqParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    self.blockDefinition()

                else:
                    raise NoViableAltException(self)
                self.state = 29 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 31
            self.endBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.blockName = None # Token
            self.inputVars = None # VarListContext
            self.statements = None # StatementListContext
            self.blockNames = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(FullSeqParser.ID)
            else:
                return self.getToken(FullSeqParser.ID, i)

        def varList(self):
            return self.getTypedRuleContext(FullSeqParser.VarListContext,0)


        def statementList(self):
            return self.getTypedRuleContext(FullSeqParser.StatementListContext,0)


        def getRuleIndex(self):
            return FullSeqParser.RULE_blockDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockDefinition" ):
                listener.enterBlockDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockDefinition" ):
                listener.exitBlockDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockDefinition" ):
                return visitor.visitBlockDefinition(self)
            else:
                return visitor.visitChildren(self)




    def blockDefinition(self):

        localctx = FullSeqParser.BlockDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_blockDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(FullSeqParser.T__0)
            self.state = 34
            localctx.blockName = self.match(FullSeqParser.ID)
            self.state = 35
            self.match(FullSeqParser.T__1)
            self.state = 36
            self.match(FullSeqParser.T__0)
            self.state = 37
            localctx.inputVars = self.varList()
            self.state = 38
            self.match(FullSeqParser.T__2)
            self.state = 39
            localctx.statements = self.statementList()
            self.state = 40
            self.match(FullSeqParser.T__1)
            self.state = 41
            self.match(FullSeqParser.T__3)
            self.state = 42
            localctx.blockNames = self.match(FullSeqParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.outputVars = None # VarListContext

        def varList(self):
            return self.getTypedRuleContext(FullSeqParser.VarListContext,0)


        def getRuleIndex(self):
            return FullSeqParser.RULE_endBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndBlock" ):
                listener.enterEndBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndBlock" ):
                listener.exitEndBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndBlock" ):
                return visitor.visitEndBlock(self)
            else:
                return visitor.visitChildren(self)




    def endBlock(self):

        localctx = FullSeqParser.EndBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_endBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(FullSeqParser.T__0)
            self.state = 45
            self.match(FullSeqParser.T__4)
            self.state = 46
            self.match(FullSeqParser.T__1)
            self.state = 47
            self.match(FullSeqParser.T__0)
            self.state = 48
            localctx.outputVars = self.varList()
            self.state = 49
            self.match(FullSeqParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullSeqParser.VarContext)
            else:
                return self.getTypedRuleContext(FullSeqParser.VarContext,i)


        def getRuleIndex(self):
            return FullSeqParser.RULE_varList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarList" ):
                listener.enterVarList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarList" ):
                listener.exitVarList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarList" ):
                return visitor.visitVarList(self)
            else:
                return visitor.visitChildren(self)




    def varList(self):

        localctx = FullSeqParser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.var()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 52
                self.match(FullSeqParser.T__5)
                self.state = 53
                self.var()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FullSeqParser.ID, 0)

        def getRuleIndex(self):
            return FullSeqParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = FullSeqParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(FullSeqParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullSeqParser.StatementContext)
            else:
                return self.getTypedRuleContext(FullSeqParser.StatementContext,i)


        def getRuleIndex(self):
            return FullSeqParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = FullSeqParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.statement()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 62
                self.match(FullSeqParser.T__5)
                self.state = 63
                self.statement()
                self.state = 68
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

        def assignment(self):
            return self.getTypedRuleContext(FullSeqParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(FullSeqParser.IfStatementContext,0)


        def concatenation(self):
            return self.getTypedRuleContext(FullSeqParser.ConcatenationContext,0)


        def getRuleIndex(self):
            return FullSeqParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = FullSeqParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.concatenation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(FullSeqParser.VarContext,0)


        def expression(self):
            return self.getTypedRuleContext(FullSeqParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FullSeqParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = FullSeqParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.var()
            self.state = 75
            self.match(FullSeqParser.T__6)
            self.state = 76
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FullSeqParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullSeqParser.StatementContext)
            else:
                return self.getTypedRuleContext(FullSeqParser.StatementContext,i)


        def getRuleIndex(self):
            return FullSeqParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = FullSeqParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(FullSeqParser.T__7)
            self.state = 79
            self.expression(0)
            self.state = 80
            self.match(FullSeqParser.T__8)
            self.state = 81
            self.statement()
            self.state = 82
            self.match(FullSeqParser.T__9)
            self.state = 83
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatenationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(FullSeqParser.VarContext,0)


        def STRING(self):
            return self.getToken(FullSeqParser.STRING, 0)

        def getRuleIndex(self):
            return FullSeqParser.RULE_concatenation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatenation" ):
                listener.enterConcatenation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatenation" ):
                listener.exitConcatenation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation" ):
                return visitor.visitConcatenation(self)
            else:
                return visitor.visitChildren(self)




    def concatenation(self):

        localctx = FullSeqParser.ConcatenationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_concatenation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.var()
            self.state = 86
            self.match(FullSeqParser.T__6)
            self.state = 87
            self.match(FullSeqParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullSeqParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FullSeqParser.ExpressionContext,i)


        def INT(self):
            return self.getToken(FullSeqParser.INT, 0)

        def FLOAT(self):
            return self.getToken(FullSeqParser.FLOAT, 0)

        def var(self):
            return self.getTypedRuleContext(FullSeqParser.VarContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(FullSeqParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return FullSeqParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FullSeqParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(FullSeqParser.T__0)
                self.state = 91
                self.expression(0)
                self.state = 92
                self.match(FullSeqParser.T__1)
                pass

            elif la_ == 2:
                self.state = 94
                self.match(FullSeqParser.INT)
                pass

            elif la_ == 3:
                self.state = 95
                self.match(FullSeqParser.FLOAT)
                pass

            elif la_ == 4:
                self.state = 96
                self.var()
                pass

            elif la_ == 5:
                self.state = 97
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = FullSeqParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 100
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 101
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2095104) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 102
                    self.expression(6) 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.functionName = None # Token
            self.args = None # ExpressionListContext

        def ID(self):
            return self.getToken(FullSeqParser.ID, 0)

        def expressionList(self):
            return self.getTypedRuleContext(FullSeqParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return FullSeqParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = FullSeqParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx.functionName = self.match(FullSeqParser.ID)
            self.state = 109
            self.match(FullSeqParser.T__0)
            self.state = 110
            localctx.args = self.expressionList()
            self.state = 111
            self.match(FullSeqParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullSeqParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FullSeqParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FullSeqParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = FullSeqParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360130) != 0):
                self.state = 113
                self.expression(0)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 114
                    self.match(FullSeqParser.T__5)
                    self.state = 115
                    self.expression(0)
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




