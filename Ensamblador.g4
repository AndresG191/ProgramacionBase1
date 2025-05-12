// ===================
//   LEXER RULES
// ===================

// Palabras clave (insensibles a mayúsculas)
OPERACION_ARITMETICA : SUMAR | RESTAR | MULTIPLICAR | DIVIDIR ;
SUMAR                : [Ss] 'umar' ;
RESTAR               : [Rr] 'estar' ;
MULTIPLICAR          : [Mm] 'ultiplicar' ;
DIVIDIR              : [Dd] 'ividir' ;

MOVER                : [Mm] 'over' ;
GUARDAR              : [Gg] 'uardar' ;
COMPARAR             : [Cc] 'omparar' ;
SI                   : [Ss] 'i' ;
IR_A                 : [Ii] 'r_a' ;
EN                   : [Ee] 'n' ;
CON                  : [Cc] 'on' ;
DE                   : [Dd] 'e' ;       // aún útil para detectar errores
Y                    : [Yy] ;
A                    : [Aa] ;

// Operadores aritméticos
OPERADOR             : '+' | '-' | '*' | '/' ;

// Operadores de comparación
COMPARADOR           : '<=' | '>=' | '==' | '!=' | '<' | '>' ;

// Tipos de operandos
NUMERO               : '-'? [0-9]+ ('.' [0-9]+)? ;
REGISTRO             : [Rr][A-Z] ;                      // e.g., RA, RB
ETIQUETA             : [A-Z][a-zA-Z0-9_]* ;             // comienza en mayúscula
VARIABLE             : [a-z_][a-zA-Z0-9_]* ;            // comienza en minúscula o guion bajo

// Separadores y símbolos
SEPARADOR            : ',' ;

// Ignorar espacios, saltos de línea y comentarios
ESPACIO              : [ \t]+ -> skip ;
SALTO_LINEA          : [\r\n]+ -> skip ;
COMENTARIO           : '#' ~[\r\n]* -> skip ;

// Captura cualquier carácter inesperado
ERROR                : . ;
