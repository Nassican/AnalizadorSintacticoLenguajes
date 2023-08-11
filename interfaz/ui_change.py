# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui-testwviDQE.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget, QAbstractButton, QStyle, QComboBox)

class Ui_home(QMainWindow):
    def setupUi(self, home, style_name=''):

        if not home.objectName():
            home.setObjectName(u"home")
        home.setEnabled(True)
        home.resize(1109, 750)
        
        '''
        label: Titulo

        label_2: Analisis Lexico

        label_5: Codigo Fuente

        label_3: Analisis Sintactico
        '''
        home.setCursor(QCursor(Qt.ArrowCursor))
        home.setAcceptDrops(False)
        home.setAutoFillBackground(True)
        home.setLocale(QLocale(QLocale.Spanish, QLocale.Panama))
        home.setAnimated(True)
        self.centralWidget = QWidget(home)
        self.centralWidget.setObjectName(u"centralWidget")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"padding: 10px;")
        self.label.setGeometry(QRect(20, 10, 1071, 60))
        font = QFont()
        font.setFamilies([u"Utopia"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        # Cuadro de texto de salida de analisis lexico
        self.horizontalLayoutWidget_2.setGeometry(QRect(570, 75, 520, 315))
        self.analisi = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.analisi.setSpacing(6)
        self.analisi.setContentsMargins(11, 11, 11, 11)
        self.analisi.setObjectName(u"analisi")
        self.analisi.setContentsMargins(0, 0, 0, 0)
        self.lexema = QVBoxLayout()
        self.lexema.setSpacing(6)
        self.lexema.setObjectName(u"lexema")
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Utopia"])
        font1.setPointSize(14)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.lexema.addWidget(self.label_2)

        self.tx_lexico = QTextEdit(self.horizontalLayoutWidget_2)
        self.tx_lexico.setReadOnly(True)
        self.tx_lexico.setStyleSheet("border: 1px solid black;")
        self.tx_lexico.setObjectName(u"tx_lexico")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tx_lexico.sizePolicy().hasHeightForWidth())
        self.tx_lexico.setSizePolicy(sizePolicy)
        
        #self.tx_lexico.setPalette(palette1)
        font2 = QFont()
        font2.setPointSize(12)
        self.tx_lexico.setFont(font2)

        self.lexema.addWidget(self.tx_lexico)


        self.analisi.addLayout(self.lexema)

        self.verticalLayoutWidget_3 = QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        # Cuadro de texto para el codigo fuente
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 70, 535, 570))
        self.fuente = QVBoxLayout(self.verticalLayoutWidget_3)
        self.fuente.setSpacing(7)
        self.fuente.setContentsMargins(11, 11, 11, 11)
        self.fuente.setObjectName(u"fuente")
        self.fuente.setSizeConstraint(QLayout.SetMaximumSize)
        self.fuente.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Utopia"])
        font3.setPointSize(16)
        font3.setItalic(True)
        self.label_5.setFont(font3)
        self.label_5.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.fuente.addWidget(self.label_5)

        self.tx_ingreso = QTextEdit(self.verticalLayoutWidget_3)
        self.tx_ingreso.setObjectName(u"tx_ingreso")
        self.tx_ingreso.setTabStopDistance(20)
        sizePolicy.setHeightForWidth(self.tx_ingreso.sizePolicy().hasHeightForWidth())
        self.tx_ingreso.setSizePolicy(sizePolicy)
        
        #self.tx_ingreso.setPalette(palette2)
        font4 = QFont()
        font4.setPointSize(18)
        self.tx_ingreso.setFont(font4)

        self.fuente.addWidget(self.tx_ingreso)

        self.horizontalLayoutWidget = QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        # Boton de analisis lexico
        self.horizontalLayoutWidget.setGeometry(QRect(95, 650, 300, 60))
        self.botones = QHBoxLayout(self.horizontalLayoutWidget)
        self.botones.setSpacing(0)
        self.botones.setContentsMargins(11, 11, 11, 11)
        self.botones.setObjectName(u"botones")
        self.botones.setContentsMargins(50, 0, 50, 5)
        self.bt_lexico = QPushButton(self.horizontalLayoutWidget)
        self.bt_lexico.setObjectName(u"bt_lexico")
        sizePolicy.setHeightForWidth(self.bt_lexico.sizePolicy().hasHeightForWidth())
        self.bt_lexico.setSizePolicy(sizePolicy)
        
        #self.bt_lexico.setPalette(palette3)
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.bt_lexico.setFont(font5)
        self.bt_lexico.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_lexico.setAutoFillBackground(False)
        #self.bt_lexico.setStyleSheet(u"border-radius: 10px; background-color: rgb(255, 255, 255);")

        self.botones.addWidget(self.bt_lexico)

        self.horizontalLayoutWidget_3 = QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        # Botones de archivo y borrar
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 650, 135, 57))
        self.archivo = QVBoxLayout(self.horizontalLayoutWidget_3)
        self.archivo.setSpacing(6)
        self.archivo.setContentsMargins(11, 11, 11, 11)
        self.archivo.setObjectName(u"archivo")
        self.archivo.setContentsMargins(10, 0, 10, 0)
        self.bt_archivo = QPushButton(self.horizontalLayoutWidget_3)
        
        #self.bt_archivo.setPalette(palette4)
        font6 = QFont()
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.bt_archivo.setFont(font6)
        self.bt_archivo.setObjectName(u"bt_archivo")
        self.bt_archivo.setCursor(QCursor(Qt.PointingHandCursor))
        iconoLetras = self.style().standardIcon(QStyle.SP_DirOpenIcon)
        self.bt_archivo.setIcon(iconoLetras)

        self.archivo.addWidget(self.bt_archivo)

        self.bt_limpiar = QPushButton(self.horizontalLayoutWidget_3)
        self.bt_limpiar.setObjectName(u"bt_limpiar")
        self.bt_limpiar.setCursor(QCursor(Qt.PointingHandCursor))
        iconoLetras = self.style().standardIcon(QStyle.SP_TrashIcon)
        self.bt_limpiar.setIcon(iconoLetras)

        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_limpiar.sizePolicy().hasHeightForWidth())
        self.bt_limpiar.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setBold(True)
        self.bt_limpiar.setFont(font7)
        self.bt_limpiar.setFocusPolicy(Qt.StrongFocus)
        self.bt_limpiar.setIconSize(QSize(16, 16))

        self.archivo.addWidget(self.bt_limpiar)

        self.layoutWidget = QWidget(self.centralWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        # Cuadro de texto de salida Semantico
        self.layoutWidget.setGeometry(QRect(570, 400, 520, 305))
        self.gramatica = QVBoxLayout(self.layoutWidget)
        self.gramatica.setSpacing(6)
        self.gramatica.setContentsMargins(11, 11, 11, 11)
        self.gramatica.setObjectName(u"gramatica")
        self.gramatica.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gramatica.addWidget(self.label_3)

        self.tx_sintactico = QTextEdit(self.layoutWidget)
        self.tx_sintactico.setObjectName(u"tx_sintactico")
        self.tx_sintactico.setReadOnly(True)
        self.tx_sintactico.setStyleSheet("border: 1px solid black;")
        sizePolicy.setHeightForWidth(self.tx_sintactico.sizePolicy().hasHeightForWidth())
        self.tx_sintactico.setSizePolicy(sizePolicy)
        
        #self.tx_sintactico.setPalette(palette5)
        self.tx_sintactico.setFont(font4)

        self.gramatica.addWidget(self.tx_sintactico)

        self.horizontalLayoutWidget_4 = QWidget(self.centralWidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        # Boton de analisis sintactico
        self.horizontalLayoutWidget_4.setGeometry(QRect(305, 650, 300, 60))
        self.botones_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.botones_2.setSpacing(100)
        self.botones_2.setContentsMargins(11, 11, 11, 11)
        self.botones_2.setObjectName(u"botones_2")
        self.botones_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.botones_2.setContentsMargins(50, 0, 50, 5)
        self.bt_sintactico = QPushButton(self.horizontalLayoutWidget_4)
        self.bt_sintactico.setObjectName(u"bt_sintactico")
        sizePolicy.setHeightForWidth(self.bt_sintactico.sizePolicy().hasHeightForWidth())
        self.bt_sintactico.setSizePolicy(sizePolicy)
        
        #self.bt_sintactico.setPalette(palette6)
        self.bt_sintactico.setFont(font5)
        self.bt_sintactico.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sintactico.setLayoutDirection(Qt.LeftToRight)

        self.botones_2.addWidget(self.bt_sintactico)


        self.horizontalOpciones = QWidget(self.centralWidget)
        self.horizontalOpciones.setObjectName(u"horizontalOpciones")
        # Boton de analisis sintactico
        self.horizontalOpciones.setGeometry(QRect(20, 20, 100, 60))
        self.opciones = QComboBox(self.horizontalOpciones)
        self.opciones.addItems(["Default","Fusion", "Windows", "dark_fusion", "white_fusion"])

        home.setCentralWidget(self.centralWidget)
        self.estado = QStatusBar(home)
        self.estado.setObjectName(u"estado")
        font8 = QFont()
        font8.setFamilies([u"NanumGothicExtraBold"])
        font8.setPointSize(14)
        font8.setBold(True)
        self.estado.setFont(font8)
        home.setStatusBar(self.estado)

        self.retranslateUi(home)
        QMetaObject.connectSlotsByName(home)
        home.setTabOrder(self.bt_lexico, self.bt_sintactico)
        home.setTabOrder(self.bt_sintactico, self.tx_lexico)
        home.setTabOrder(self.tx_lexico, self.tx_sintactico)
        home.setTabOrder(self.tx_sintactico, self.bt_archivo)
        home.setTabOrder(self.bt_archivo, self.bt_limpiar)
        home.setTabOrder(self.bt_limpiar, self.tx_ingreso)

        # activamos la paleta en la aplicación
        
        
        #activamos la paleta en la aplicación
        #home.setPalette(dark_fusion)
    # setupUi
        

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"Analizador lexico y sintactico", None))
        self.label.setText(QCoreApplication.translate("home", u"Analizador - Lexico - Sintactico", None))
        self.label_2.setText(QCoreApplication.translate("home", u"Resultado Analisis Lexico", None))
        self.tx_lexico.setHtml(QCoreApplication.translate(
                "home", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "li.unchecked::marker { content: \"\\2610\"; }\n"
                "li.checked::marker { content: \"\\2612\"; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:5px; padding-left: 5px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:10pt;\"><br /></p></body></html>", None))
        self.tx_lexico.setPlaceholderText(QCoreApplication.translate("home", u"Analisis de lexemas", None))
        self.label_5.setText(QCoreApplication.translate("home", u"Codigo Fuente", None))
        self.tx_ingreso.setHtml(QCoreApplication.translate(
                "home", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "li.unchecked::marker { content: \"\\2610\"; }\n"
                "li.checked::marker { content: \"\\2612\"; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:10pt;\"><br /></p></body></html>", None))
        self.tx_ingreso.setPlaceholderText(QCoreApplication.translate("home", u"Ingrese el texto a analizar o suba un archivo", None))
        self.bt_lexico.setText(QCoreApplication.translate("home", u"Analizar Lexico", None))
        self.bt_archivo.setText(QCoreApplication.translate("home", u"Subir Archivo", None))
        self.bt_limpiar.setText(QCoreApplication.translate("home", u"Borrar", None))
        self.label_3.setText(QCoreApplication.translate("home", u"Resultado Analisis Sintactico", None))
        self.tx_sintactico.setPlaceholderText(QCoreApplication.translate("home", u"Analisis de Sintaxis", None))
        self.bt_sintactico.setText(QCoreApplication.translate("home", u"Analisis Sintactico", None))
    # retranslateUi

