
import sys
import pickle
from PyQt6 import QtWidgets
from GUI.horario import Ui_MainWindow


class Ventana(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        # Implementación de Ui_VentanaPrincipal
        self.setupUi(self)

        # Conectar la señal al método correspondiente
        self.guardarButton.clicked.connect(self.guardar_horario)
        self.cargarButton.clicked.connect(self.cargar_horario)

    def guardar_horario(self):
        horario = self.lineEditHorario.text()

        with open("horario.pickle", "wb") as file:
            pickle.dump(horario, file)

    def cargar_horario(self):
        try:
            with open("horario.pickle", "rb") as file:
                horario = pickle.load(file)
                self.lineEditHorario.setText(horario)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    vista = Ventana()
    vista.show()
    app.exec()
