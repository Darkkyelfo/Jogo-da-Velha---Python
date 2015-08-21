# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:00:57 2015

@author: Raul
"""

import ConexaoCampo
from PyQt4 import QtGui, QtCore


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = ConexaoCampo.ConexaoCampo()
    av.show()
    sys.exit(app.exec_())