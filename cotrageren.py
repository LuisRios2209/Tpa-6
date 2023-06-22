
import sys
from PyQt6 import QtWidgets
from GUI.centro_contra import Ui_MainWindow


class Ventana3(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana3, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana3()
    vista.show()
    app.exec()