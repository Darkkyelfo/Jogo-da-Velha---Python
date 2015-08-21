# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:17:08 2015

@author: Raul
"""

# Classe responsavel por realizar as conexões entre o campo e mouse.

import sys
sys.path.append("Telas")
from Campo import Ui_campo
from ConexaoTelaTerminar import ConexaoTelaTerminar
from PyQt4 import QtGui, QtCore

class ConexaoCampo(QtGui.QMainWindow,Ui_campo):
    #Variáveis que vão guardar o camininho das imagens para: 
    X=None#X
    O=None#O
    matriz = []#Matriz que armazenará os estado das casas(se está com X, O ou vazia)
    turno = False #boleano que realiza a troca de turnos
    
    def __init__(self,parent=None):
        super(ConexaoCampo, self).__init__(parent)
        self.setupUi(self)
        self.inicializarMatriz()
        #Conenecta todos os botões a função de por X ou O
        for bt in self.__dict__:
            if bt.startswith("pushButton_"):
                getattr(self, bt).clicked.connect(self.XorO)
                
    #Marca na GUI as casas clicadas com X ou O.
    #Também verifica se o jogo acabou ou não através da matriz
    def XorO(self):
        i=self.sender().objectName()[-2]
        j=self.sender().objectName()[-1]
        
        if self.turno == False:
            self.sender().setStyleSheet("border-image: url(:/Imagens/X.png);")
            self.matriz[int(i)][int(j)]="X"
            self.turno =True
        else:
            self.sender().setStyleSheet("border-image: url(:/Imagens/O.png);")
            self.matriz[int(i)][int(j)]="O"
            self.turno= False
        self.terminarJogo()
    
    def inicializarMatriz(self):
        for i in range(0,3):
            self.matriz.append([])
            for j in range(0,3):
                self.matriz[i].append("")
            
    #Percorre a matriz na Horizontal
    def percMatrizHoriznontal(self):
        temp = []
        resultado = False
        for i in range(0,3):
            for j in range(0,3):
                temp.append(self.matriz[i][j])
            if temp.count("X")==3 or temp.count("O")==3:
                resultado = True
                break
            temp=[]
        return resultado
    #Percorre a matriz na Vertical
    def percMatrizVertical(self):
        temp = []
        resultado = False
        for i in range(0,3):
            for j in range(0,3):
                temp.append(self.matriz[j][i])
            if temp.count("X")==3 or temp.count("O")==3:
                resultado = True
                break
            temp=[]
        return resultado

    def percMatrizDiagonal(self):
        resultado = False
        diagonal1=[self.matriz[0][0],self.matriz[1][1],self.matriz[2][2]]
        diagonal2=[self.matriz[0][2],self.matriz[1][1],self.matriz[2][0]]
        if diagonal1.count("X")==3 or diagonal1.count("O")==3:
            resultado =True
        elif diagonal2.count("X")==3 or diagonal2.count("O")==3:
            resultado =True
        
        return resultado
        
    
    def terminarJogo(self):
        if self.percMatrizHoriznontal()==True or self.percMatrizVertical()==True or self.percMatrizDiagonal()==True:
            print("acabou!!")
            t = ConexaoTelaTerminar()
            t.show()
            t.exec_()