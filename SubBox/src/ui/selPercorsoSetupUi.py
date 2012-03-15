# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/paganotti/Documents/Progetti/Qt/Setup4/selpercorsosync.ui'
#
# Created: Thu Apr 21 21:37:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelPercorsoSync(object):
    def setupUi(self, SelPercorsoSync):
        SelPercorsoSync.setObjectName(_fromUtf8("SelPercorsoSync"))
        SelPercorsoSync.resize(540, 410)
        SelPercorsoSync.setMinimumSize(QtCore.QSize(540, 410))
        SelPercorsoSync.setMaximumSize(QtCore.QSize(540, 410))
        self.lbTitolo = QtGui.QLabel(SelPercorsoSync)
        self.lbTitolo.setGeometry(QtCore.QRect(20, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbTitolo.setFont(font)
        self.lbTitolo.setObjectName(_fromUtf8("lbTitolo"))
        self.frmSetup = QtGui.QFrame(SelPercorsoSync)
        self.frmSetup.setGeometry(QtCore.QRect(20, 50, 501, 301))
        self.frmSetup.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmSetup.setFrameShadow(QtGui.QFrame.Raised)
        self.frmSetup.setObjectName(_fromUtf8("frmSetup"))
        self.widget = QtGui.QWidget(self.frmSetup)
        self.widget.setGeometry(QtCore.QRect(70, 90, 387, 147))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.SelPercorsoVLayout = QtGui.QVBoxLayout(self.widget)
        self.SceltaHomeVLayout = QtGui.QVBoxLayout()
        self.rbCartellaHome = QtGui.QRadioButton(self.widget)
        self.rbSceltaPercorso = QtGui.QRadioButton(self.widget)
        self.CambiaGridLayout = QtGui.QGridLayout()
        self.lbPercorso = QtGui.QLabel(self.widget)
        self.bCambia = QtGui.QPushButton(self.widget)
        self.gridLayout = QtGui.QGridLayout()
        self.lbPercorsoHome = QtGui.QLabel(self.widget)

        self.SelPercorsoVLayout.setSpacing(0)
        self.SelPercorsoVLayout.setMargin(0)
        self.SelPercorsoVLayout.setObjectName(_fromUtf8("SelPercorsoVLayout"))

        self.SceltaHomeVLayout.setSpacing(40)
        self.SceltaHomeVLayout.setObjectName(_fromUtf8("SceltaHomeVLayout"))

        self.rbCartellaHome.setChecked(True)
        self.rbCartellaHome.setObjectName(_fromUtf8("rbCartellaHome"))
        self.SceltaHomeVLayout.addWidget(self.rbCartellaHome)

        self.rbSceltaPercorso.setObjectName(_fromUtf8("rbSceltaPercorso"))
        self.SceltaHomeVLayout.addWidget(self.rbSceltaPercorso)
        self.SelPercorsoVLayout.addLayout(self.SceltaHomeVLayout)

        self.CambiaGridLayout.setObjectName(_fromUtf8("CambiaGridLayout"))
        spacerItem = QtGui.QSpacerItem(10, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.CambiaGridLayout.addItem(spacerItem, 0, 0, 1, 1)

        self.lbPercorso.setObjectName(_fromUtf8("lbPercorso"))
        self.CambiaGridLayout.addWidget(self.lbPercorso, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(138, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.CambiaGridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.bCambia.setEnabled(False)
        self.bCambia.setObjectName(_fromUtf8("bCambia"))
        self.CambiaGridLayout.addWidget(self.bCambia, 0, 3, 1, 1)
        self.SelPercorsoVLayout.addLayout(self.CambiaGridLayout)

        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)

        self.lbPercorsoHome.setMinimumSize(QtCore.QSize(360, 0))
        self.lbPercorsoHome.setWordWrap(True)
        self.lbPercorsoHome.setObjectName(_fromUtf8("lbPercorsoHome"))
        self.gridLayout.addWidget(self.lbPercorsoHome, 0, 1, 1, 1)
        self.SelPercorsoVLayout.addLayout(self.gridLayout)


        self.bIndietro = QtGui.QPushButton(SelPercorsoSync)
        self.bIndietro.setEnabled(False)
        self.bIndietro.setGeometry(QtCore.QRect(300, 370, 114, 32))
        self.bIndietro.setObjectName(_fromUtf8("bIndietro"))
        self.bAvanti = QtGui.QPushButton(SelPercorsoSync)
        self.bAvanti.setGeometry(QtCore.QRect(410, 370, 114, 32))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bAvanti.sizePolicy().hasHeightForWidth())
        self.bAvanti.setSizePolicy(sizePolicy)
        self.bAvanti.setObjectName(_fromUtf8("bAvanti"))

        self.retranslateUi(SelPercorsoSync)
        QtCore.QMetaObject.connectSlotsByName(SelPercorsoSync)

    def retranslateUi(self, SelPercorsoSync):
        SelPercorsoSync.setWindowTitle(QtGui.QApplication.translate("SelPercorsoSync", "Percorso Cartella SubBox", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTitolo.setText(QtGui.QApplication.translate("SelPercorsoSync", "Percorso SubBox", None, QtGui.QApplication.UnicodeUTF8))
        self.rbCartellaHome.setText(QtGui.QApplication.translate("SelPercorsoSync", "Posiziona la cartella SubBox nella cartella home", None, QtGui.QApplication.UnicodeUTF8))
        self.rbSceltaPercorso.setText(QtGui.QApplication.translate("SelPercorsoSync", "Voglio scegliere dove mettere la cartella SuBox", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPercorso.setText(QtGui.QApplication.translate("SelPercorsoSync", "Percorso SubBox:", None, QtGui.QApplication.UnicodeUTF8))
        self.bCambia.setText(QtGui.QApplication.translate("SelPercorsoSync", "Cambia", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPercorsoHome.setText(QtGui.QApplication.translate("SelPercorsoSync", "/Users/paganotti/SubBox", None, QtGui.QApplication.UnicodeUTF8))
        self.bIndietro.setText(QtGui.QApplication.translate("SelPercorsoSync", "Indietro", None, QtGui.QApplication.UnicodeUTF8))
        self.bAvanti.setText(QtGui.QApplication.translate("SelPercorsoSync", "Avanti", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SelPercorsoSync = QtGui.QDialog()
    ui = Ui_SelPercorsoSync()
    ui.setupUi(SelPercorsoSync)
    SelPercorsoSync.show()
    sys.exit(app.exec_())

