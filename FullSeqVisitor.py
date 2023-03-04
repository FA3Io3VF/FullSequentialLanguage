from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FullSeqParser import FullSeqParser
else:
    from FullSeqParser import FullSeqParser

# This class defines a complete generic visitor for a parse tree produced by FullSeqParser.

class FullSeqVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FullSeqParser#program.
    def visitProgram(self, ctx:FullSeqParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#blockDefinition.
    def visitBlockDefinition(self, ctx:FullSeqParser.BlockDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#endBlock.
    def visitEndBlock(self, ctx:FullSeqParser.EndBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#varList.
    def visitVarList(self, ctx:FullSeqParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#var.
    def visitVar(self, ctx:FullSeqParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#statementList.
    def visitStatementList(self, ctx:FullSeqParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#statement.
    def visitStatement(self, ctx:FullSeqParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#assignment.
    def visitAssignment(self, ctx:FullSeqParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#ifStatement.
    def visitIfStatement(self, ctx:FullSeqParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#concatenation.
    def visitConcatenation(self, ctx:FullSeqParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#expression.
    def visitExpression(self, ctx:FullSeqParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#functionCall.
    def visitFunctionCall(self, ctx:FullSeqParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FullSeqParser#expressionList.
    def visitExpressionList(self, ctx:FullSeqParser.ExpressionListContext):
        return self.visitChildren(ctx)



del FullSeqParser
