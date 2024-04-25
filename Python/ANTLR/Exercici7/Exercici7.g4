grammar Exercici7;
root : (statement)*            // l'etiqueta ja és root
     ;

statement : ID ':=' expr #AssignStmt
    | 'write' expr      #writeStmt
    | 'if' expr 'then' (statement)* 'end' #ifStmt
    | 'while' expr 'do' (statement)* 'end' #whileStmt
    | expr                #exprStmt
    ;

    
expr : <assoc=right> expr '^' expr #pot
    | expr ('*' | '/') expr    # multORdiv
    | expr ('+' | '-') expr    # sumaORresta
    | expr '=' expr            #equal
    | expr '<>' expr           #diff
    | NUM              # numero
    | ID               #identExpr
    ;

ID : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;