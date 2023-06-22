
import sys
from PyQt6 import QtWidgets
from GUI.despedir import Ui_MainWindow


class Ventana2(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana2, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana2()
    vista.show()
    app.exec()