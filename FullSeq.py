from antlr4 import *
from FullSeqLexer import FullSeqLexer
from FullSeqParser import FullSeqParser
from FullSeqVisitor import FullSeqVisitor

class FullSeq(FullSeqVisitor):
    def __init__(self):
        self.variables = {}

    def visitBlockDefinition(self, ctx: FullSeqParser.BlockDefinitionContext):
        block_name = ctx.blockName.text
        input_vars = [var.text for var in ctx.inputVars.var]
        statements = ctx.statements.statement
        output_block_name = ctx.blockNames.text

        def block_func(*args): #Add the input variables to the variable dictionary
            if not args:
                for input_var in input_vars:
                    value = input(f"Enter a value for {input_var}: ")
                    self.variables[input_var] = float(value) if '.' in value else int(value)
            else:
                for i, arg in enumerate(args):
                    self.variables[input_vars[i]] = arg

            #Exec_statements
            for statement in statements:
                self.visit(statement)

            #Call the next block and pass output variables to it
            next_block_func = getattr(self, output_block_name)
            output_vars = [self.variables[var.text] for var in ctx.statements.var]
            next_block_func(*output_vars)

        #Add the block function to the interpreter's attributes
        setattr(self, block_name, block_func)

    def visitEndBlock(self, ctx: FullSeqParser.EndBlockContext):
        #Print the output variable
        output_vars = [self.variables[var.text] for var in ctx.outputVars.var]
        print("Output: ", output_vars)

    def visitAssignment(self, ctx: FullSeqParser.AssignmentContext):
        var_name = ctx.var.text
        var_value = self.visit(ctx.expression)
        self.variables[var_name] = var_value

    def visitIfStatement(self, ctx: FullSeqParser.IfStatementContext):
        condition = self.visit(ctx.expression)
        if condition:
            self.visit(ctx.statement[0])
        else:
            self.visit(ctx.statement[1])

    def visitConcatenation(self, ctx: FullSeqParser.ConcatenationContext):
        var_name = ctx.var.text
        string_value = ctx.STRING.text[1:-1]  # Remove the quotes around the string
        self.variables[var_name] = string_value

    def visitFunctionCall(self, ctx: FullSeqParser.FunctionCallContext):
        func_name = ctx.functionName.text
        func_args = [self.visit(expr) for expr in ctx.args.expression]
        return getattr(self, func_name)(*func_args)
 
    def visitINT(self, ctx: FullSeqParser.INTContext):
        return int(ctx.getText())

    def visitFLOAT(self, ctx: FullSeqParser.FLOATContext):
        return float(ctx.getText())

    def visitVar(self, ctx: FullSeqParser.VarContext):
        var_name = ctx.text
        if var_name not in self.variables:
            raise ValueError(f"Undefined variable {var_name}")
        return self.variables[var_name]


if __name__ == '__main__':
    
    lexer = FullSeqLexer(InputStream("(Rectangle)(base, altezza) | area = base * altezza => Perimetro\n"
                                        "(Perimetro)(base, altezza) | perimetro = 2 * base + 2 * altezza => Fine\n"
                                        "(Fine) | risultato = "Area: " + area + " - Perimetro: " + perimetro"),
                                        antlr4.InputStream)

    stream = CommonTokenStream(lexer)
    parser = FullSeqParser(stream)
    tree = parser.program()
    interpreter = FullSeq()
    interpreter.visit(tree)
    
"""
antlr4 -Dlanguage=Python3 .\venv\code\FullSeq.g4

antlr4 -Dlanguage=Python3 -visitor MyLanguage.g4

"""
