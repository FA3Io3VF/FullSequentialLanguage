grammar FullSeq;

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
