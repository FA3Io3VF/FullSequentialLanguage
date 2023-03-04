from antlr4 import *
from antlr4.tree import *

# Load the grammar file
input_stream = FileStream("FullSeq.g4")
lexer = FullSeqLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = FullSeqParser(stream)

# Generate the parser code
tree = parser.grammarSpec()
lisp_tree_str = TreeFormatter().format(tree)
print(lisp_tree_str)

"""
    
pip install antlr4-python3-runtime

"""
