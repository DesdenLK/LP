grammar hinner;
root : statement EOF          // l'etiqueta ja és root
     ;
statement : expr                         #exprStmt
          | expr DOTS defType            #TypeDefStmt
     ;

defType : TYPE                                #singleType
     |    <assoc=right> defType ARROW defType #TypeAssocRight
     |    LPAR defType RPAR                   #ParType
     ;   

abstraccio : OPERADOR                   #operadorINFIX
     | SLASH ID ARROW expr              #funcio
     ;
expr : LPAR expr RPAR                   #parenthesis
     | expr expr                        #aplicacioExpr
     | abstraccio                       #abstraccioExpr
     | NUM                              #numero
     | ID                               #ident
     ;
NUM : [0-9]+ ;
LPAR : '(';
RPAR : ')';
SLASH : '\\';
ARROW : '->';
DOTS  : '::';
TYPE  : ('a'..'z'|'A'..'Z');
OPERADOR : ('(+)'| '-');
ID : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
WS  : [ \t\n\r]+ -> skip ;