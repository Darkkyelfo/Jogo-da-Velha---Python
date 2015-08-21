# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:34:24 2015

@author: Raul
"""
import sys
sys.path.append("Telas")
from Terminar import Ui_JanelaTermino
from PyQt4 import QtGui, QtCore

class ConexaoTelaTerminar(QtGui.QMainWindow,Ui_JanelaTermino):
    def __init__(self,parent=None):
        super(ConexaoTelaTerminar, self).__init__(parent)
        self.setupUi(self)
        