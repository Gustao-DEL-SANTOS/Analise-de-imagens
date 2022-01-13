from PyQt5 import uic, QtWidgets


def info_n(nivel):
    if nive == 1:
        n1 = '''
            Informações do nível 1 - Produção agrícola \n\n



            Nome da unidade produtora (produtor agrícola)\n 

            Endereço do produtor agrícola \n

            Produto(s) agrícolas produzidos \n

            Produção anual em quilogramas \n

            Destino da produção (mercado interno ou exportação) \n

            Número de empregados da unidade produtora \n

            Quantidade de máquinas e implementos aquícolas \n

            Nível de automação da unidade produtora \n
             '''
        return n1
    elif nivel == 2:
        n2 = '''
            Informações do nível 2 - Informações fiscais \n\n



            Incentivos fiscais recebidos \n

            Impostos municipais pagos \n

            Impostos estaduais recolhidos\n 

            Impostos federais pagos \n

            Taxas federais pagas
             '''
        return n2
    elif nive == 3:
        n3 = '''
            Informações do nível 3 - agrotóxicos \n\n



            Agrotóxicos empregados nas produções agrícolas \n



            Onde adquirir as informações: site do Ministério da agricultura,\n
            site do mistério do meio ambiente.\n
             '''
        return n3 

def segunda_tela():
    nivel_um_tela.show()
    a = 'ola amiginhos \n'
    nivel_um_tela.txt_nivel.setText(a)
    nivel_um_tela.pushButton.clicked.connect(escrever)
def escrever():
    # nivel_um_tela.QFrame.minimumSize()
    pass


app = QtWidgets.QApplication([])
login_tela = uic.loadUi('login.ui')
nivel_um_tela = uic.loadUi('nivel_um.ui')

login_tela.pushButton.clicked.connect(segunda_tela)

login_tela.show()
app.exec()
