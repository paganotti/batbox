# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/paganotti/Documents/Progetti/Qt/Setup2/Setup2/setupui.ui'
#
# Created: Wed Apr 20 17:18:57 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from AccountSubBox import AccountSubBox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SetupUi(QtGui.QDialog):

    paginaCorrente = 1

    def inizializza(self):
        QtGui.QDialog.__init__(self, self, QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("Setup SubBox")
        self.resize(540, 410)
        self.setMinimumSize(QtCore.QSize(540, 410))
        self.setMaximumSize(QtCore.QSize(540, 410))

        self.acc = AccountSubBox()

        self.lbTitolo = QtGui.QLabel(self)
        self.lbTitolo.setGeometry(QtCore.QRect(20, 20, 191, 24))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbTitolo.setFont(font)

        self.bAvanti = QtGui.QPushButton(self)
        self.bAvanti.setGeometry(QtCore.QRect(410, 370, 114, 32))
        QtCore.QObject.connect(self.bAvanti, QtCore.SIGNAL('clicked()'), self.bAvantiCliccato)

        self.bIndietro = QtGui.QPushButton(self)
        self.bIndietro.setEnabled(False)
        self.bIndietro.setGeometry(QtCore.QRect(300, 370, 114, 32))
        self.bIndietro.setObjectName(_fromUtf8("bIndietro"))

        QtCore.QObject.connect(self.bIndietro, QtCore.SIGNAL('clicked()'), self.bIndietroCliccato)

        self.frmSetup = QtGui.QFrame(self)
        self.frmSetup.setGeometry(QtCore.QRect(20, 50, 501, 301))
        self.frmSetup.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmSetup.setFrameShadow(QtGui.QFrame.Raised)

        self.setTabOrder(self.bAvanti, self.bIndietro)

    #componenti prima pagina in cui si sceglie se si possiede gia un account o meno

        self.gridLayoutWidget   = QtGui.QWidget(self.frmSetup)

        self.gridLayout         = QtGui.QGridLayout(self.gridLayoutWidget)
        self.lbSubBox           = QtGui.QLabel(self.gridLayoutWidget)
        self.rbCreaAccount      = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rbPossiedoAccount  = QtGui.QRadioButton(self.gridLayoutWidget)

    #-------------------------------------------------------------------------------
    #componenti seconda pagina - creazione dell'account SubBox
        self.widget = QtGui.QWidget(self.frmSetup)
        self.creaAccountVLayout = QtGui.QVBoxLayout(self.widget)
        self.creaAccountFLayout = QtGui.QFormLayout()
        self.lbNomeCreaAccount = QtGui.QLabel(self.widget)
        self.txtNomeCreaAccount = QtGui.QLineEdit(self.widget)
        self.lbCognomeCreaAccount = QtGui.QLabel(self.widget)
        self.txtCognomeCreaAccount = QtGui.QLineEdit(self.widget)
        self.lbEmailCreaAccount = QtGui.QLabel(self.widget)
        self.txtEmailCreaAccount = QtGui.QLineEdit(self.widget)
        self.lbPassowordCreaAccount = QtGui.QLabel(self.widget)
        self.txtPassowordCreaAccount = QtGui.QLineEdit(self.widget)
        self.lbVerificaPassCreaAccount = QtGui.QLabel(self.widget)
        self.txtVerificaPassCreaAccount = QtGui.QLineEdit(self.widget)
        self.lbErrorCreaAccount = QtGui.QLabel(self.widget)
    #--------------------------------------------------------------------------------
    #componenti terza pagina - selezione del percorso della cartella SubBox

        self.widgetSelPercorso = QtGui.QWidget(self.frmSetup)
        self.SelPercorsoVLayout = QtGui.QVBoxLayout(self.widgetSelPercorso)
        self.SceltaHomeVLayout = QtGui.QVBoxLayout()

        self.rbCartellaHome = QtGui.QRadioButton(self.widgetSelPercorso)
        QtCore.QObject.connect(self.rbCartellaHome, QtCore.SIGNAL("toggled(bool)"), self.selezionatoCartellaHome)

        self.rbSceltaPercorso = QtGui.QRadioButton(self.widgetSelPercorso)
        QtCore.QObject.connect(self.rbSceltaPercorso, QtCore.SIGNAL("toggled(bool)"), self.selezionatoSceltaPercorso)

        self.CambiaGridLayout = QtGui.QGridLayout()
        self.lbPercorso = QtGui.QLabel(self.widgetSelPercorso)
        self.bCambia = QtGui.QPushButton(self.widgetSelPercorso)
        QtCore.QObject.connect(self.bCambia, QtCore.SIGNAL('clicked()'), self.bCambiaCliccato)

        self.selPercorsoGridLayout = QtGui.QGridLayout()
        self.lbPercorsoHome = QtGui.QLabel(self.widgetSelPercorso)

        self.lbTitolo.setText("Benvenuti in SubBox")
        self.bAvanti.setText("Avanti")
        self.bIndietro.setText("Indietro")
        self.lbSubBox.setText("SubBox")
        self.rbCreaAccount.setText("Crea Account")
        self.rbPossiedoAccount.setText("Possiedo un Account")

        self.lbTitolo.setText("Crea Account SubBox")
        self.lbNomeCreaAccount.setText("Nome:")
        self.lbCognomeCreaAccount.setText("Cognome:")
        self.lbEmailCreaAccount.setText("Email:")
        self.lbPassowordCreaAccount.setText("Password:")
        self.lbVerificaPassCreaAccount.setText("Verifica Password:")

        self.rbCartellaHome.setText("Posiziona la cartella SubBox nella cartella home")
        self.rbSceltaPercorso.setText("Voglio scegliere dove mettere la cartella SuBox")
        self.lbPercorso.setText("Percorso SubBox:")
        self.bCambia.setText("Cambia")
        self.lbPercorsoHome.setText("/Users/paganotti/SubBox")


        self.creaSetupPagina()
        self.creaAccountPagina()
        self.creaSelPercorsoPagina()

        self.impostaPagina()

    def creaSetupPagina(self):

        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 80, 183, 130))

        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(15)

        font = QtGui.QFont()
        font.setPointSize(48)
        font.setWeight(75)
        font.setBold(True)

        self.lbSubBox.setFont(font)
        self.gridLayout.addWidget(self.lbSubBox, 0, 0, 1, 1)

        self.rbCreaAccount.setChecked(True)
        self.gridLayout.addWidget(self.rbCreaAccount, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.rbPossiedoAccount, 2, 0, 1, 1)

        self.gridLayoutWidget.hide()

    def creaAccountPagina(self):

        self.widget.setGeometry(QtCore.QRect(40, 20, 421, 261))

        self.creaAccountVLayout.setSpacing(70)
        self.creaAccountVLayout.setMargin(0)

        self.creaAccountFLayout.setHorizontalSpacing(5)
        self.creaAccountFLayout.setVerticalSpacing(15)

        self.creaAccountFLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbNomeCreaAccount)

        self.txtNomeCreaAccount.setMinimumSize(QtCore.QSize(260, 0))
        self.creaAccountFLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtNomeCreaAccount)

        self.creaAccountFLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbCognomeCreaAccount)

        self.txtCognomeCreaAccount.setMinimumSize(QtCore.QSize(260, 0))
        self.creaAccountFLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtCognomeCreaAccount)

        self.creaAccountFLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbEmailCreaAccount)

        self.txtEmailCreaAccount.setMinimumSize(QtCore.QSize(260, 0))
        self.creaAccountFLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtEmailCreaAccount)

        self.creaAccountFLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbPassowordCreaAccount)

        self.txtPassowordCreaAccount.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassowordCreaAccount.setMinimumSize(QtCore.QSize(260, 0))
        self.creaAccountFLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtPassowordCreaAccount)

        self.creaAccountFLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbVerificaPassCreaAccount)

        self.txtVerificaPassCreaAccount.setEchoMode(QtGui.QLineEdit.Password)
        self.txtVerificaPassCreaAccount.setMinimumSize(QtCore.QSize(260, 0))

        self.creaAccountFLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtVerificaPassCreaAccount)
        self.creaAccountVLayout.addLayout(self.creaAccountFLayout)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbErrorCreaAccount.setFont(font)
        self.lbErrorCreaAccount.setText(_fromUtf8(""))
        self.lbErrorCreaAccount.setAlignment(QtCore.Qt.AlignCenter)
        self.creaAccountVLayout.addWidget(self.lbErrorCreaAccount)

        self.setTabOrder(self.txtNomeCreaAccount, self.txtCognomeCreaAccount)
        self.setTabOrder(self.txtCognomeCreaAccount, self.txtEmailCreaAccount)
        self.setTabOrder(self.txtEmailCreaAccount, self.txtPassowordCreaAccount)
        self.setTabOrder(self.txtPassowordCreaAccount, self.txtVerificaPassCreaAccount)
        self.setTabOrder(self.txtVerificaPassCreaAccount, self.bAvanti)
        self.setTabOrder(self.bAvanti, self.bIndietro)

        self.widget.hide()

    def creaSelPercorsoPagina(self):

        self.widgetSelPercorso.setGeometry(QtCore.QRect(70, 90, 387, 147))

        self.SelPercorsoVLayout.setSpacing(0)
        self.SelPercorsoVLayout.setMargin(0)

        self.SceltaHomeVLayout.setSpacing(40)

        self.rbCartellaHome.setChecked(True)
        self.SceltaHomeVLayout.addWidget(self.rbCartellaHome)

        self.SceltaHomeVLayout.addWidget(self.rbSceltaPercorso)
        self.SelPercorsoVLayout.addLayout(self.SceltaHomeVLayout)

        spacerItem = QtGui.QSpacerItem(10, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.CambiaGridLayout.addItem(spacerItem, 0, 0, 1, 1)

        self.CambiaGridLayout.addWidget(self.lbPercorso, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(138, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.CambiaGridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.bCambia.setEnabled(False)
        self.CambiaGridLayout.addWidget(self.bCambia, 0, 3, 1, 1)
        self.SelPercorsoVLayout.addLayout(self.CambiaGridLayout)

        spacerItem2 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.selPercorsoGridLayout.addItem(spacerItem2, 0, 0, 1, 1)

        self.lbPercorsoHome.setMinimumSize(QtCore.QSize(360, 0))
        self.lbPercorsoHome.setWordWrap(True)
        self.selPercorsoGridLayout.addWidget(self.lbPercorsoHome, 0, 1, 1, 1)
        self.SelPercorsoVLayout.addLayout(self.selPercorsoGridLayout)

    def chiudiSetup(self):
        self.hide()
        self.pulisciFormPercorso()
        self.pulisciFormCreaAccount()
        self.pulisciFormSelAccount()
        self.paginaCorrente = 1

    def impostaPagina(self):

        if self.paginaCorrente == 1:
            self.pulisciFormSelAccount()
            self.widget.hide()
            self.widgetSelPercorso.hide()
            self.gridLayoutWidget.show()

        elif self.paginaCorrente == 2:

            if self.rbPossiedoAccount.isChecked() == True:
                self.lbTitolo.setText("Log in SubBox")
            else:
                self.lbTitolo.setText("Crea Account SubBox")

            self.gridLayoutWidget.hide()
            self.widgetSelPercorso.hide()
            self.bAvanti.setText("Avanti")
            self.bIndietro.setEnabled(True)
            self.pulisciFormCreaAccount()

            if self.rbPossiedoAccount.isChecked() == True:
                self.lbNomeCreaAccount.hide()
                self.txtNomeCreaAccount.hide()
                self.lbCognomeCreaAccount.hide()
                self.txtCognomeCreaAccount.hide()
                self.lbVerificaPassCreaAccount.hide()
                self.txtVerificaPassCreaAccount.hide()
                self.txtEmailCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            else:
                self.lbNomeCreaAccount.show()
                self.txtNomeCreaAccount.show()
                self.lbCognomeCreaAccount.show()
                self.txtCognomeCreaAccount.show()
                self.lbVerificaPassCreaAccount.show()
                self.txtVerificaPassCreaAccount.show()
                self.txtNomeCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)

            self.widget.show()

        elif self.paginaCorrente == 3:

            self.pulisciFormPercorso()
            self.gridLayoutWidget.hide()
            self.widget.hide()
            self.widgetSelPercorso.show()

        elif self.paginaCorrente == 4:
            self.acc.nome = self.txtNomeCreaAccount.text()
            self.acc.cognome = self.txtCognomeCreaAccount.text()
            self.acc.email = self.txtEmailCreaAccount.text()
            self.acc.password = self.txtPassowordCreaAccount.text()

            if self.rbSceltaPercorso.isChecked() == True:
                self.acc.setPercorso(self.lbPercorsoHome.text())
            else:
                self.acc.setPercorso(QtCore.QDir.homePath().append("/SubBox"))

            print "Nome: " + self.acc.getNome()
            print "Cognome: " + self.acc.getCognome()
            print "Email: " + self.acc.getEmail()
            print "Password: " + self.acc.getPassword()
            print "Percorso: " + self.acc.getPercorso()

            self.chiudiSetup()

    def pulisciFormCreaAccount(self):
        self.txtNomeCreaAccount.setText("")
        self.txtCognomeCreaAccount.setText("")
        self.txtEmailCreaAccount.setText("")
        self.txtPassowordCreaAccount.setText("")
        self.txtVerificaPassCreaAccount.setText("")
        self.lbErrorCreaAccount.setText("")
        self.txtNomeCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)

    def pulisciFormPercorso(self):
        self.lbTitolo.setText("Percorso SubBox")
        self.rbCartellaHome.setChecked(True)
        self.lbPercorsoHome.setText(QtCore.QDir.homePath().append("/SubBox"))
        self.bAvanti.setText("Fatto")

    def pulisciFormSelAccount(self):
        self.lbTitolo.setText("Benvenuti in SubBox")
        self.rbCreaAccount.setChecked(True)
        self.bIndietro.setEnabled(False)

    def controllaLogin(self):
        campoDaCompletare = 0

        if self.txtEmailCreaAccount.text() == "":
            self.txtEmailCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -3
        elif self.txtPassowordCreaAccount.text() == "":
            self.txtPassowordCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -4

        if campoDaCompletare != 0:
            self.lbErrorCreaAccount.setText("<font color=red> Completare tutti i campi. </font>")

        if campoDaCompletare == 0:
            #controllo che l'indirizzo mail contenga la chiocciola
            if self.txtEmailCreaAccount.text().contains("@") == False:
                campoDaCompletare = -6
                self.lbErrorCreaAccount.setText("<font color=red> Indirizzo mail non valido. </font>")
                self.txtEmailCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)

        return campoDaCompletare

    def controllaCampiCreaAccount(self):

        campoDaCompletare = 0

        if self.txtNomeCreaAccount.text() == "":
            self.txtNomeCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -1
        elif self.txtCognomeCreaAccount.text() == "":
            self.txtCognomeCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -2
        elif self.txtEmailCreaAccount.text() == "":
            self.txtEmailCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -3
        elif self.txtPassowordCreaAccount.text() == "":
            self.txtPassowordCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -4
        elif self.txtVerificaPassCreaAccount.text() == "":
            self.txtVerificaPassCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)
            campoDaCompletare = -5

        if campoDaCompletare != 0:
            self.lbErrorCreaAccount.setText("<font color=red> Completare tutti i campi. </font>")

        if campoDaCompletare == 0:
            #controllo che l'indirizzo mail contenga la chiocciola
            if self.txtEmailCreaAccount.text().contains("@") == False:
                campoDaCompletare = -6
                self.lbErrorCreaAccount.setText("<font color=red> Indirizzo mail non valido. </font>")
                self.txtEmailCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)

            if campoDaCompletare == 0:
                #controllo la verifica della password
                if self.txtPassowordCreaAccount.text() != self.txtVerificaPassCreaAccount.text():
                    campoDaCompletare = -7
                    self.lbErrorCreaAccount.setText("<font color=red> Le password non corrispondono. </font>")
                    self.txtPassowordCreaAccount.setFocus(QtCore.Qt.OtherFocusReason)

        return campoDaCompletare

    def bAvantiCliccato(self):

        controllo = 0

        #Controllo che abbia inserito correttamente tutti i campi nel form Crea Account SubBox
        if self.paginaCorrente == 2:
            if self.rbCreaAccount.isChecked() == True:
                controllo = self.controllaCampiCreaAccount()
            else:
                controllo = self.controllaLogin()

        if controllo == 0:
            self.paginaCorrente = self.paginaCorrente + 1
            self.impostaPagina()

    def bIndietroCliccato(self):

            self.paginaCorrente = self.paginaCorrente - 1
            self.impostaPagina()

    def bCambiaCliccato(self):

        self.selpath = QtGui.QFileDialog.getExistingDirectory(self,"Seleziona un percorso SubBox", self.lbPercorsoHome.text(),QtGui.QFileDialog.ShowDirsOnly)

        if self.selpath == "":
            self.lbPercorsoHome.setText(QtCore.QDir.homePath().append("/SubBox"))
        else:
            self.lbPercorsoHome.setText(self.selpath)

    def selezionatoCartellaHome(self):
        if self.rbCartellaHome.isChecked() == True:
            self.bCambia.setEnabled(False)

    def selezionatoSceltaPercorso(self):
        if self.rbSceltaPercorso.isChecked() == True:
            self.bCambia.setEnabled(True)

    def anullaSetup(self):
        QtGui.QApplication.quit()


  