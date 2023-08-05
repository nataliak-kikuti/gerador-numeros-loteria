import random
from PyQt5 import uic,QtWidgets,QtCore

def sortear():
    numeros = list(range(1, 61))
    random.shuffle(numeros)
    
    tela.label.setText(str(numeros[0]))
    tela.label.setAlignment(QtCore.Qt.AlignCenter)
    tela.label_2.setText(str(numeros[1]))
    tela.label_2.setAlignment(QtCore.Qt.AlignCenter)
    tela.label_3.setText(str(numeros[2]))
    tela.label_3.setAlignment(QtCore.Qt.AlignCenter)
    tela.label_4.setText(str(numeros[3]))
    tela.label_4.setAlignment(QtCore.Qt.AlignCenter)
    tela.label_5.setText(str(numeros[4]))
    tela.label_5.setAlignment(QtCore.Qt.AlignCenter)
    tela.label_6.setText(str(numeros[5]))
    tela.label_6.setAlignment(QtCore.Qt.AlignCenter)
    
app = QtWidgets.QApplication([])
tela = uic.loadUi("tela-loteria.ui")

tela.pushButton.clicked.connect(sortear)

tela.show()
app.exec()