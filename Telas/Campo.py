# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Campo2.ui'
#
# Created: Fri Aug 21 14:30:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_campo(object):
    def setupUi(self, campo):
        campo.setObjectName(_fromUtf8("campo"))
        campo.resize(300, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(campo.sizePolicy().hasHeightForWidth())
        campo.setSizePolicy(sizePolicy)
        campo.setStyleSheet(_fromUtf8("background-image: url(:/Imagens/Grid3.png);"))
        self.gridLayoutWidget = QtGui.QWidget(campo)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_00 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_00.sizePolicy().hasHeightForWidth())
        self.pushButton_00.setSizePolicy(sizePolicy)
        self.pushButton_00.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_00.setText(_fromUtf8(""))
        self.pushButton_00.setObjectName(_fromUtf8("pushButton_00"))
        self.gridLayout.addWidget(self.pushButton_00, 0, 0, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 2, 0, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_20 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_20.setText(_fromUtf8(""))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.gridLayout.addWidget(self.pushButton_20, 4, 0, 1, 1)
        self.pushButton_22 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_22.setText(_fromUtf8(""))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.gridLayout.addWidget(self.pushButton_22, 4, 4, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_12.setText(_fromUtf8(""))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout.addWidget(self.pushButton_12, 2, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.pushButton_21 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_21.setText(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.gridLayout.addWidget(self.pushButton_21, 4, 2, 1, 1)
        self.pushButton_01 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_01.sizePolicy().hasHeightForWidth())
        self.pushButton_01.setSizePolicy(sizePolicy)
        self.pushButton_01.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_01.setText(_fromUtf8(""))
        self.pushButton_01.setObjectName(_fromUtf8("pushButton_01"))
        self.gridLayout.addWidget(self.pushButton_01, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.pushButton_02 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_02.sizePolicy().hasHeightForWidth())
        self.pushButton_02.setSizePolicy(sizePolicy)
        self.pushButton_02.setStyleSheet(_fromUtf8("border-image: url(:/Imagens/Fundo Branco.jpg);"))
        self.pushButton_02.setText(_fromUtf8(""))
        self.pushButton_02.setObjectName(_fromUtf8("pushButton_02"))
        self.gridLayout.addWidget(self.pushButton_02, 0, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        self.retranslateUi(campo)
        QtCore.QMetaObject.connectSlotsByName(campo)

    def retranslateUi(self, campo):
        campo.setWindowTitle(_translate("campo", "Jogo da Velha", None))

import ProjImgs_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    campo = QtGui.QWidget()
    ui = Ui_campo()
    ui.setupUi(campo)
    campo.show()
    sys.exit(app.exec_())

