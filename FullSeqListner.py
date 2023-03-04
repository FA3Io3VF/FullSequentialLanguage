# Generated from .\venv\code\FullSeq.g4 with ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FullSeqParser import FullSeqParser
else:
    from FullSeqParser import FullSeqParser

# This class defines a complete listener for a parse tree produced by FullSeqParser.
class FullSeqListener(ParseTreeListener):

    # Enter a parse tree produced by FullSeqParser#program.
    def enterProgram(self, ctx:FullSeqParser.ProgramContext):
        pass

    # Exit a parse tree produced by FullSeqParser#program.
    def exitProgram(self, ctx:FullSeqParser.ProgramContext):
        pass


    # Enter a parse tree produced by FullSeqParser#blockDefinition.
    def enterBlockDefinition(self, ctx:FullSeqParser.BlockDefinitionContext):
        pass

    # Exit a parse tree produced by FullSeqParser#blockDefinition.
    def exitBlockDefinition(self, ctx:FullSeqParser.BlockDefinitionContext):
        pass


    # Enter a parse tree produced by FullSeqParser#endBlock.
    def enterEndBlock(self, ctx:FullSeqParser.EndBlockContext):
        pass

    # Exit a parse tree produced by FullSeqParser#endBlock.
    def exitEndBlock(self, ctx:FullSeqParser.EndBlockContext):
        pass


    # Enter a parse tree produced by FullSeqParser#varList.
    def enterVarList(self, ctx:FullSeqParser.VarListContext):
        pass

    # Exit a parse tree produced by FullSeqParser#varList.
    def exitVarList(self, ctx:FullSeqParser.VarListContext):
        pass


    # Enter a parse tree produced by FullSeqParser#var.
    def enterVar(self, ctx:FullSeqParser.VarContext):
        pass

    # Exit a parse tree produced by FullSeqParser#var.
    def exitVar(self, ctx:FullSeqParser.VarContext):
        pass


    # Enter a parse tree produced by FullSeqParser#statementList.
    def enterStatementList(self, ctx:FullSeqParser.StatementListContext):
        pass

    # Exit a parse tree produced by FullSeqParser#statementList.
    def exitStatementList(self, ctx:FullSeqParser.StatementListContext):
        pass


    # Enter a parse tree produced by FullSeqParser#statement.
    def enterStatement(self, ctx:FullSeqParser.StatementContext):
        pass

    # Exit a parse tree produced by FullSeqParser#statement.
    def exitStatement(self, ctx:FullSeqParser.StatementContext):
        pass


    # Enter a parse tree produced by FullSeqParser#assignment.
    def enterAssignment(self, ctx:FullSeqParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FullSeqParser#assignment.
    def exitAssignment(self, ctx:FullSeqParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FullSeqParser#ifStatement.
    def enterIfStatement(self, ctx:FullSeqParser.IfStatementContext):
        pass

    # Exit a parse tree produced by FullSeqParser#ifStatement.
    def exitIfStatement(self, ctx:FullSeqParser.IfStatementContext):
        pass


    # Enter a parse tree produced by FullSeqParser#concatenation.
    def enterConcatenation(self, ctx:FullSeqParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by FullSeqParser#concatenation.
    def exitConcatenation(self, ctx:FullSeqParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by FullSeqParser#expression.
    def enterExpression(self, ctx:FullSeqParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FullSeqParser#expression.
    def exitExpression(self, ctx:FullSeqParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FullSeqParser#functionCall.
    def enterFunctionCall(self, ctx:FullSeqParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by FullSeqParser#functionCall.
    def exitFunctionCall(self, ctx:FullSeqParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by FullSeqParser#expressionList.
    def enterExpressionList(self, ctx:FullSeqParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by FullSeqParser#expressionList.
    def exitExpressionList(self, ctx:FullSeqParser.ExpressionListContext):
        pass



del FullSeqParser
