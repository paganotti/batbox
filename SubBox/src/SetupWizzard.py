from PyQt4      import QtGui,QtCore

class SetupWizzard(QtGui.QWizard):

    sceltaAccount       = 0
    #CreaAccount         = 0
    #Login               = 0
    #SelCartellaSinc     = 0
    
    def __init__(self, parent=None):

        QtGui.QWizard.__init__(self, parent)
        
        SceltaAccount   = SceltaAccountPage()
        #CreaAccount     = SceltaAccountPage()
        #Login           = SceltaAccountPage()
        #SelCartellaSinc = SceltaAccountPage()

        self.addPage(SceltaAccount)
        #self.addPage(CreaAccount)
        #self.addPage(Login)
        #self.addPage(SelCartellaSinc)

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle("SubBox Setup")


class SceltaAccountPage(QtGui.QWizardPage):

    def __init__(self, parent = None):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Benvenuto in SubBox")
        self.setGeometry(QtCore.QRect(0, 0, 100, 100))



        
  