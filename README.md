# FullSequentialLanguage (FullSeq)

A toy programming language with *Python 3* and *Antlr 4*

#Code Structure:

```
(BlockName)(inputVar1, inputVar2, ...) | statement1 => (OutputBlockName)

(IntermediateBlocks)....

(End) | outputVar1, outputVar2, ...
```



## Example:

```
(Rectangle)(base, height) | area = base * height => (Perimeter)
(Perimeter)(base, height) | perimeter = 2 * base + 2 * height => (End)
(End) | result = "Area: " + area + " - Perimeter: " + perimeter
```


## Reference Grammar:

```
program: blockDefinition+ endBlock ;

blockDefinition: '(' blockName=ID ')' '(' inputVars=varList '|' statements=statementList ')' '=>' blockNames=ID ;
endBlock: '(' 'End' ')' '(' outputVars=varList ')' ;

varList: var (',' var)* ;
var: ID ;
statementList: statement (',' statement)* ;
statement: assignment | ifStatement | concatenation ;
assignment: var '=' expression ;
ifStatement: 'if' expression 'then' statement 'else' statement ;
concatenation: var '=' STRING ;

expression: '(' expression ')' | expression op=('*' | '/' | '+' | '-' | '==' | '!=' | '<=' | '>=' | '<' | '>') expression | INT | FLOAT | var | functionCall ;
functionCall: functionName=ID '(' args=expressionList ')' ;
expressionList: (expression (',' expression)*)? ;

STRING: '\'' (~[\'\\\r\n]|'\\\\'|'\\\'')* '\'' ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
ID: [a-zA-Z][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
```
