grammar Exercici2;
root : expr             // l'etiqueta ja és root
     ;
expr : <assoc=right> expr '^' expr #pot
     | expr ('*' | '/') expr    # multORdiv
     | expr ('+' | '-') expr    # sumaORresta
     | NUM              # numero
     ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;