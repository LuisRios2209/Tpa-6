
import sys
from PyQt6 import QtWidgets
import pickle
from atencion import Ui_MainWindow


class Ventana2(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana2, self).__init__(*args, **kwargs)
        # Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.pushButton.clicked.connect(self.guardar_solicitud)

    def guardar_solicitud(self):
        motivo = self.textEdit.toPlainText()
        with open("solicitudes.pickle", "ab") as file:
            pickle.dump(motivo, file)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    vista = Ventana2()
    vista.show()
    app.exec()
