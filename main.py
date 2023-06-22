
import sys
from PyQt6 import QtWidgets
from typing import TypeVar
from login import Ui_MainWindow
from maintrabajador import ventana3
from maingenrente import ventana2

class Ventana(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.pushButton.clicked.connect(self.conectar)

   
    def conectar(self, *args, obj=None, **kwargs):
        texto = self.lineEdit.text().lower()
        texto1= self.lineEdit.text().lower()
        if texto == "julio" :
            print("Bienveo Gerente Julio")
            self.ventana2 = ventana2()
            self.ventana2.show()
        if texto1 == "andres" :
            self.ventana3 = ventana3()
            self.ventana3.show()
            print("Bienvdo Trabajador Andres")

    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()