import sys

from PyQt6 import QtWidgets
from GUI.atenciontraba import Ventana2
from GUI.horariotraba import Ventana
from GUI.logintrabajador import Ui_MainWindow


class ventana3(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(ventana3, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)

        self.horario.clicked.connect(self.conectar)
        self.asistencia.clicked.connect(self.conectar2)
    
    def conectar(self, *args, obj=None, **kwargs):
         self.ventana2 = Ventana()
         self.ventana2.show()

    def conectar2(self, *args, obj=None, **kwargs):
         self.ventana3 = Ventana2()
         self.ventana3.show()


        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = ventana3()
    vista.show()
    app.exec()