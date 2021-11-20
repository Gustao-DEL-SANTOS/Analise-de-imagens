from PyQt5 import uic, QtWidgets


def segunda_tela():
    nivel_um_tela.show()
    a = 'ola amiginhos \n'
    nivel_um_tela.textEdit.setText(a)
    nivel_um_tela.pushButton.clicked.connect(escrever)
def escrever():
    # nivel_um_tela.QFrame.minimumSize()

app = QtWidgets.QApplication([])
login_tela = uic.loadUi('login.ui')
nivel_um_tela = uic.loadUi('nivel_um.ui')

login_tela.pushButton.clicked.connect(segunda_tela)

login_tela.show()
app.exec()
