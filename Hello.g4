grammar Hello;

hello: 'Hola' ID '!';

ID: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
