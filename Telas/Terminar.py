# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Terminar.ui'
#
# Created: Fri Aug 21 16:12:18 2015
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

class Ui_JanelaTermino(object):
    def setupUi(self, JanelaTermino):
        JanelaTermino.setObjectName(_fromUtf8("JanelaTermino"))
        JanelaTermino.resize(400, 148)
        self.horizontalLayoutWidget = QtGui.QWidget(JanelaTermino)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 90, 191, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtGui.QLabel(JanelaTermino)
        self.label.setGeometry(QtCore.QRect(10, 30, 351, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(JanelaTermino)
        QtCore.QMetaObject.connectSlotsByName(JanelaTermino)

    def retranslateUi(self, JanelaTermino):
        JanelaTermino.setWindowTitle(_translate("JanelaTermino", "Dialog", None))
        self.pushButton_2.setText(_translate("JanelaTermino", "Reiniciar", None))
        self.pushButton.setText(_translate("JanelaTermino", "Sair", None))
        self.label.setText(_translate("JanelaTermino", "Texto de Derrota ou Empate", None))

