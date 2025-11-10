grammar Grammar;
// asignaciones 
//Asignacion del programa
program:(statement NEWLINE)*EOF;

statement: assing |print|if_statement|for_statement;

/*asignaciones de id y operaroderes, para operaciones*/
assing:ID'='expr;
 
 /* Definimos print*/
 print:'print''('expr')';

/*Definimos if*/
if_statement:'if''('expr')'block;

//Definimos For
for_statement:'for''('assing';'expr';'assing')'block;

//Definimos block
block:'{'(statement NEWLINE)*'}';

//Definimos La exprecion
expr: expr op('*'|'/')expr;
    | expr op('+'|'-')expr;
    | expr op('>'|'<'|'>='|'<=')expr;
    | expr op('=='|'!=')expr;
    | ID
    | '('expr')'
    ;

    // Definicion de elmentos finales

ID:[a-zA-Z][a-zA-Z_0-9]*;
NEWLINE:[\r\n];
NEWLINE:[\t]->skip;
SEMI:';';