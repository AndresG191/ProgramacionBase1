lexer grammar analizadorLexer;

IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]*;  // Identificadores de variables o nombres

WS: [ \t\r\n] -> skip; // Ignorar espacios en blanco
