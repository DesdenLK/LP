grammar hinner;
root : statement EOF          // l'etiqueta ja és root
     ;
statement : expr                         #exprStmt
          | expr DOTS defType            #TypeDefStmt
     ;

defType : ID                                #singleType
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
OPERADOR : ('(+)'| '-');
ID : ('a'..'z'|'A'..'Z')+;
WS  : [ \t\n\r]+ -> skip ;