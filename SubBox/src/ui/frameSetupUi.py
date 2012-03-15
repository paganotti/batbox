# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/paganotti/Documents/Progetti/Qt/Setup2/Setup2/setupui.ui'
#
# Created: Wed Apr 20 17:10:45 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SetupUi(object):
    def setupUi(self, SetupUi):
        SetupUi.setObjectName(_fromUtf8("SetupUi"))
        SetupUi.resize(540, 410)
        SetupUi.setMinimumSize(QtCore.QSize(540, 410))
        SetupUi.setMaximumSize(QtCore.QSize(540, 410))
        self.lbTitolo = QtGui.QLabel(SetupUi)
        self.lbTitolo.setGeometry(QtCore.QRect(20, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbTitolo.setFont(font)
        self.lbTitolo.setObjectName(_fromUtf8("lbTitolo"))
        self.bAvanti = QtGui.QPushButton(SetupUi)
        self.bAvanti.setGeometry(QtCore.QRect(410, 370, 114, 32))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bAvanti.sizePolicy().hasHeightForWidth())
        self.bAvanti.setSizePolicy(sizePolicy)
        self.bAvanti.setObjectName(_fromUtf8("bAvanti"))
        self.frmSetup = QtGui.QFrame(SetupUi)
        self.frmSetup.setGeometry(QtCore.QRect(20, 50, 501, 301))
        self.frmSetup.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmSetup.setFrameShadow(QtGui.QFrame.Raised)
        self.frmSetup.setObjectName(_fromUtf8("frmSetup"))
        self.gridLayoutWidget = QtGui.QWidget(self.frmSetup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 80, 183, 130))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rbCreaAccount = QtGui.QRadioButton(self.gridLayoutWidget)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.rbCreaAccount.sizePolicy().hasHeightForWidth())
        #self.rbCreaAccount.setSizePolicy(sizePolicy)
        self.rbCreaAccount.setChecked(True)
        self.rbCreaAccount.setObjectName(_fromUtf8("rbCreaAccount"))
        self.gridLayout.addWidget(self.rbCreaAccount, 1, 0, 1, 1)
        self.rbPossiedoAccount = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rbPossiedoAccount.setObjectName(_fromUtf8("rbPossiedoAccount"))
        self.gridLayout.addWidget(self.rbPossiedoAccount, 2, 0, 1, 1)
        self.bIndietro = QtGui.QPushButton(SetupUi)
        self.bIndietro.setEnabled(False)
        self.bIndietro.setGeometry(QtCore.QRect(300, 370, 114, 32))
        self.bIndietro.setObjectName(_fromUtf8("bIndietro"))

        self.retranslateUi(SetupUi)
        QtCore.QMetaObject.connectSlotsByName(SetupUi)
        self.gridLayoutWidget.hide()

    def retranslateUi(self, SetupUi):
        SetupUi.setWindowTitle(QtGui.QApplication.translate("SetupUi", "Setup SubBox", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTitolo.setText(QtGui.QApplication.translate("SetupUi", "Benvenuti in SubBox", None, QtGui.QApplication.UnicodeUTF8))
        self.bAvanti.setText(QtGui.QApplication.translate("SetupUi", "Avanti", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SetupUi", "SubBox", None, QtGui.QApplication.UnicodeUTF8))
        self.rbCreaAccount.setText(QtGui.QApplication.translate("SetupUi", "Crea Account", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPossiedoAccount.setText(QtGui.QApplication.translate("SetupUi", "Possiedo un Account", None, QtGui.QApplication.UnicodeUTF8))
        self.bIndietro.setText(QtGui.QApplication.translate("SetupUi", "Indietro", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SetupUi = QtGui.QDialog()
    ui = Ui_SetupUi()
    ui.setupUi(SetupUi)
    SetupUi.show()
    sys.exit(app.exec_())

