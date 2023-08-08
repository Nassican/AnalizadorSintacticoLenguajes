# from lpp.repl import start_repl
# 
# def main() -> None:
#     print('Lenguajes Formales y Automatas | Jesus David Benavides Chicaiza')
#     print('Digita tu codigo a continuacion.')
# 
#     start_repl()
# 
# 
# if __name__ == '__main__':
#     main()

import sys

from PySide6.QtWidgets import *

""" Importamos todas nuetras Ventana y funciones utiles"""
from lpp.ast import Program
from lpp.lexer import Lexer
from lpp.parser import Parser
from lpp.token import (
    Token,
    TokenType,
)

# from interfaz.home import *
from interfaz.ui_change import *

EOF_TOKEN: Token = Token(TokenType.EOF, '')

def _print_parse_errors(errors: list[str]):
    for error in errors:
        print(error)

class Main(QMainWindow):
    """ Clase principal de nuestra app"""
    def __init__(self):
        """ Incializamos nuestra app"""
        QMainWindow.__init__(self)

        # Instaciamos nuestra ventanas widget home
        self.home = Ui_home()
        self.home.setupUi(self)
        # icon = QIcon("./interfaz/logo.png")  # Cambia "icono.png" por la ruta a tu archivo de icono
        # self.setWindowIcon(icon)

        # Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)

        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)
        self.home.estado.showMessage("Analizador Sintactico | Jesus David Benavides | Yorth Ortegon | Universidad de Nariño | 2023")


    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        :return: 
        '''
        # print("lexico")

        # limpiamos el campo
        self.home.tx_lexico.setText('')

        #Obtenemos los datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()

        # analizamos la lexemas de los datos ingresados
        
        lexer: Lexer = Lexer(datos)
        resultado_lexico = ''
        posicion = 0
        while (token := lexer.next_token()) != EOF_TOKEN:
            posicion += 1
            resultado_lexico += 'Posicion: '  + str(posicion) + ' | ' + str(token) + '\n'
       # self.home.tx_lexico.setText("Analizando lexico")
        

        self.home.tx_lexico.setText(resultado_lexico)

    def ev_sintactico(self):
        '''
        Manejo de analisis gramatico
        :return: 
        '''
        # print("sintactico")

        # limpiamos el campo
        self.home.tx_sintactico.setText('')
        #Obtenemos los datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()

        #analizamos la gramatica de los datos ingresados
        lexer: Lexer = Lexer(datos)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        resultado_sintactico = str(program)

        cadena = ''

        #Armanos la cadena a mostrar
        for item in resultado_sintactico:
            cadena += item + "" 

        if len(parser.errors) > 0:
            cadena += '\n\nERRORES: ' + str(parser.errors)
        # mostramos en pantalla

        self.home.tx_sintactico.setText(cadena)

    def ev_archivo(self):
        '''
        Manejo de subir archivo 
        :return: 
        '''
        dlg = QFileDialog()

        if dlg.exec():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read().strip()
                if data:
                    self.home.tx_ingreso.setPlainText(data + "\n")

    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        :return: 
        '''
        self.home.tx_ingreso.setText('')
        self.home.tx_lexico.setText('')
        self.home.tx_sintactico.setText('')

if __name__ == "__main__":
    # Instaciamos nuestro app por defecto esto no cambia
    app = QApplication(sys.argv)
    # Instaciomos nuestro ventana
    ventana = Main()
    # Mostramos nuestra app
    ventana.show()
    #Controlamos el cierre de la app
    sys.exit(app.exec())

'''
variable x = 5;
variable y = 10;
variable resultado = suma(x, y);

# Programa

variable <identifier> =  <expression>;  # Statement

-- Una expresion regresa un valor pero un statement no

# LetStateMent -> Es un caso especifico de un statement


Si (x != y) Entonces x; Sino y; FinSi

'''