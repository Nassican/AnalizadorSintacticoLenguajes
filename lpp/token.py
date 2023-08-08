from enum import (
    auto,
    Enum,
    unique,
)
from typing import NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto() # =
    COMMA = auto() # ,
    EOF = auto() #Termina el archivo // -> FinPrograma
    FUNCTION = auto() #Uno funcion NoteTalves no se use#
    IDENT = auto() #Identificador o nombre de nuestras variables
    ILLEGAL = auto() #Cuando un token no peretenece a nuestro lenguaje
    RBRACE = auto() #Llave izquierda
    LET = auto() #Definicion de variables
    LPAREN = auto()
    LBRACE = auto() # llave derecha
    PLUS = auto() #Simbolo de suma
    RPAREN = auto() #Parentesis derecho
    SEMICOLON = auto() # punto y coma ;
    RETURN = auto() # Retorna
    LT = auto() # Menor que
    MT = auto() # Mayor que
    TRUE = auto() # verdadero
    FALSE = auto() # falso
    MINUS = auto() # Signo Menos
    DIVIDE = auto() # Signo Dividir
    MULT = auto() # Signo Multiplicacion
    NOT = auto() # not
    EQUALS = auto() # es ==
    NOTEQUALS = auto() # es !=
    COLON = auto() # es :
    
    #--------------------------------
    IF = auto()     # if - Si
    THEN = auto()   # Entonces
    ELSE = auto()   # si_no -> Sino
    ENDIF = auto()  # FinSi
    #--------------------------------
    WHILE = auto()      # Mientras
    ENDWHILE = auto()   # FinMientras
    #--------------------------------
    FOR = auto()    # Para
    TO = auto()     # hasta
    ENDFOR = auto() # FinPara
    #--------------------------------
    ASPER = auto()      # Segun
    DO = auto()         # hacer
    OTHERMODE = auto()
    ENDASPER = auto()   # FinSegun
    #--------------------------------
    REAL = auto()   # Es un # real
    INT = auto()    # Es un # entero
    FLOAT = auto()  # Es un # float
    STRING = auto() # Es un # string
    DOUBLE = auto() # Es un # double
    #--------------------------------
    LETREAL = auto()   # Es un # real
    LETINT = auto()    # Es un # entero
    LETFLOAT = auto()  # Es un # float
    LETSTRING = auto() # Es un # string
    LETDOUBLE = auto() # Es un # double
    #--------------------------------
    READ = auto()
    WRITE = auto()
    #--------------------------------
    SOP = auto()
    EOP = auto()
    #--------------------------------






class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str: #Funcion que regresa un str
        return f'Type: {self.token_type}, literal: {self.literal}'
    
# Funcion auxiliar dentro del token que nos permite saber si 
# estamos dentro de un keyboard o un identificador ( nombre de la variable)
def lookup_token_type(literal: str) -> TokenType:
    #Diccionario, con llaves str y valores TokenType
    keywords: dict[str, TokenType] = {
        'falso': TokenType.FALSE,           # Ya estaba
        'verdadero': TokenType.TRUE,        # Ya estaba
        'retorna': TokenType.RETURN,        # Ya estaba
        'variable': TokenType.LET,          # Ya estaba
        # variable -> variable x = 5;
        'funcion': TokenType.FUNCTION,      # Ya estaba
        #-----------------PSEUDOCODIGO---------------------------------
        #-----------------DEICISION IF---------------------------------
        'Si': TokenType.IF,                 # Ya estaba
        'Entonces': TokenType.THEN,         # OK
        'Sino': TokenType.ELSE,             # cambio de si_no -> Sino
        'FinSi': TokenType.ENDIF,           # OK
        #-----------------CICLO-WHILE----------------------------------
        'Mientras': TokenType.WHILE,        # OK
        #'Hacer': TokenType.DO,
        'FinMientras': TokenType.ENDWHILE , # OK
        #------------------CICLO-PARA----------------------------------
        'Para': TokenType.FOR,              # cambio de para -> Para
        'hasta': TokenType.TO,              # OK
        'FinPara': TokenType.ENDFOR,        # OK
        #------------------CICLO-SEGUN----------------------------------
        'Segun': TokenType.ASPER,           # OK
        'hacer': TokenType.DO,              # OK
        'DeOtroModo': TokenType.OTHERMODE,   # OK
        'FinSegun': TokenType.ENDASPER,     # OK 
        #--------------------VARIABLES----------------------------------
        'Real': TokenType.LETREAL,             # OK
        'Entero': TokenType.LETINT,         # OK
        'Doble': TokenType.LETDOUBLE,         # OK
        'Flotante': TokenType.LETFLOAT,           # Ya estaba el FLOAT ---
        'Cadena': TokenType.LETSTRING,         # OK
        #--------------------ACCIONES----------------------------------
        'Leer': TokenType.READ,             # OK
        'Escribir': TokenType.WRITE,         # OK
        #--------------------PROGRAMA----------------------------------
        'Programa': TokenType.SOP,
        'FinPrograma': TokenType.EOP,

    }

    return keywords.get(literal, TokenType.IDENT)

'''
Real x, y, z;
Entero x, y, z;
Doble x, y, z;
Cadena x, y, z;
Flotante x, y, z;


    OK      Programa      -> Es SOP
    OK      FinPrograma   -> Es EOP.

    OK      Tipo -> 

    Real, 
    Entero, 
    Double, 
    Float, 
    String

    OK      Leer
    OK      Escribir
    OK      Si
    OK      Entonces
    OK      Sino
    OK      FinSi
    OK      Mientras
    OK      FinMientras
    OK      Para
    OK      hasta
    OK      FinPara
    OK      Segun
    OK      Hacer
    OK      FinSegun

'''
