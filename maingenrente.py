import sys
from PyQt6 import QtWidgets
from GUI.cotrageren import Ventana3
from GUI.despedirgren import Ventana2
from GUI.gestion_horageren import Ventana
from GUI.venta_Gerente import Ui_MainWindowGerente

class ventana2(QtWidgets.QMainWindow, Ui_MainWindowGerente):
    def __init__(self, *args, obj=None, **kwargs):
        super(ventana2, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)


        self.pushButton_1.clicked.connect(self.conectar)
        self.pushButton_2.clicked.connect(self.conectar2)
        self.pushButton_3.clicked.connect(self.conectar3)
    
    def conectar(self, *args, obj=None, **kwargs):
        self.ventana = Ventana()
        self.ventana.show()
        
    def conectar2(self, *args, obj=None, **kwargs):
        self.ventana2 = Ventana2()
        self.ventana2.show()


    def conectar3(self, *args, obj=None, **kwargs):
         self.ventana3 = Ventana3()
         self.ventana3.show()

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = ventana2()
    vista.show()
    app.exec()