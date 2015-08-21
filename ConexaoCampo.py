# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:17:08 2015

@author: Raul
"""

# Classe responsavel por realizar as conexões entre o campo e mouse.

import sys
sys.path.append("Telas")
from Campo import Ui_campo
from PyQt4 import QtGui, QtCore
class ConexaoCampo(QtGui.QMainWindow,Ui_campo):
    #Variáveis que vão guardar o camininho das imagens para: 
    X=None#X
    O=None#O
    matriz = [[]]
    
    def __init__(self,parent=None):
        super(ConexaoCampo, self).__init__(parent)
        self.setupUi(self)
        #Conenecta todos os botões a função de por X ou O
        for bt in self.__dict__:
            if bt.startswith("pushButton_"):
                getattr(self, bt).clicked.connect(self.XorO)
        
    def XorO(self):
        #self.pushButton.setStyleSheet("border-image: url(:/Imagens/Grid3.png);")
        print("funciona")
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = ConexaoCampo()
    av.show()
    sys.exit(app.exec_())