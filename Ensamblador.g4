grammar Ensamblador;

// Opciones de la gramática
options {
  language=Python3;
  caseInsensitive=true;
}

// Reglas sintácticas
programa: instruccion+ EOF;

instruccion
    : operacion_aritmetica
    | operacion_movimiento
    | operacion_comparacion
    | operacion_condicional
    | operacion_salto
    ;

operacion_aritmetica
    : OPERACION (NUMERO|VARIABLE|REGISTRO) OPERADOR (NUMERO|VARIABLE|REGISTRO) ('y' 'guardar' 'en' 'registro'? (REGISTRO|VARIABLE))? // Soporta "registro" opcional
    ;

operacion_movimiento
    : 'mover' (NUMERO|VARIABLE|REGISTRO) 'a' 'registro'? (REGISTRO|VARIABLE) // Ejemplo: "mover 42 a registro BX"
    ;

operacion_comparacion
    : 'comparar' (VARIABLE|REGISTRO) 'con' (NUMERO|VARIABLE|REGISTRO) // Ejemplo: "comparar Y con 100"
    ;

operacion_condicional
    : 'si' (REGISTRO|VARIABLE) COMPARADOR (NUMERO|VARIABLE|REGISTRO) 'ir_a' ETIQUETA // Ejemplo: "si AX mayor_que 0 ir_a etiqueta_loop"
    ;

operacion_salto
    : 'ir_a' ETIQUETA // Ejemplo: "ir_a etiqueta_loop"
    ;

// Reglas léxicas
OPERACION: 'sumar'|'restar'|'multiplicar'|'dividir'|'mover'|'comparar'|'ir_a'|'si'|'guardar';
OPERADOR: 'y'|'de'|'a'|'con'; // Prioridad alta
NUMERO: [0-9]+;
REGISTRO: 'AX'|'BX'|'CX'|'DX'|'A'|'B'|'C'|'D';
VARIABLE: [a-z][a-z0-9_]*; // Simplificado, solo letras minúsculas por caseInsensitive
COMPARADOR: 'mayor_que'|'menor_que'|'igual_a'|'distinto_de';
ETIQUETA: 'etiqueta_'[a-z0-9]+; // Simplificado, solo minúsculas y números
SEPARADOR: ',';
ESPACIO: [ \t]+ -> skip;
SALTO_LINEA: '\n' -> skip;
IGNORAR: ('el'|'la'|'los'|'las'|'en'|'registro') -> skip; // Ignora 'registro' excepto donde se usa
ERROR: .;