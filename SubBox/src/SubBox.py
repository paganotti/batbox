import os
import sys
from datetime import datetime
from FSEvents import *

from PyQt4          import QtGui,QtCore
from SetupUi        import SetupUi
from TLogin         import TLogin
from SvnRepository  import SvnRepository
from Events         import MonitorFsEvents



pathDb =  unicode(QtCore.QDir.homePath()) + "/.subbox/SubBox.db"
urlRepo = 'http://gekoinformatica.net/svn/prova'
#urlRepo = 'http://192.168.2.123/project-subbox'

class SystemTrayIcon(QtGui.QSystemTrayIcon):
    
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        
        apriCartellaSubBoxAction = menu.addAction("Apri la cartella SubBox")
        lanciaSubBoxAction = menu.addAction("Lancia SubBox.it")
        sincronizzaOraAction = menu.addAction("Sincronizza Adesso")
        menu.addSeparator()
        preferenzeAction = menu.addAction("Preferenze")
        menu.addSeparator()
        chiudiAction = menu.addAction("Chiudi")
        QtCore.QObject.connect(chiudiAction,QtCore.SIGNAL("triggered()"), self.quit)
        
        self.setContextMenu(menu)
    
    def quit(self):
        QtGui.QApplication.quit()

def callback(event):

    print str(event.mask) + " " + event.name + " sec: " + str(datetime.now())

    login = TLogin(pathDb)
    credenziali = login.getCredenziali()

    client = SvnRepository(urlRepo,credenziali[0],credenziali[1],login.getPercorso())

    if event.name.find("/.svn") == -1 and event.name.find("/.DS_Store") == -1:

        if event.mask == 512:
            #cancellato il file o la cartella
            client.remove(event.name)

        elif event.mask == 256:
            #aggiunto il file o la cartella
            error = client.add(event.name)

        elif event.mask == 2:
            #modificato un file
            error = client.modify(event.name)

        elif event.mask == 64:
            #cancello in vecchio file (nel caso della rinnomina)
            client.remove(event.name)

        elif event.mask == 128:
            #aggiungo il file rinnominato
            error = client.add(event.name)

    '''
    client = pysvn.Client()
    client.callback_get_login = get_login
    sta = client.status('/Users/paganotti/checkout/testRepo/',True,False)
    for item in sta:
        print 'path   = ' , item.path
        print 'status = ' , item.text_status
    '''

def risultaPrimoAvvio():

    primoAvvio = True

    #controllo se esiste il database
    print pathDb
    
    if QtCore.QFile.exists(pathDb) == True:
        #il database esiste
        primoAvvio = False
    else:
        primoAvvio = True
    
    #se esiste in database verifico che esista anche la cartella
    #estraggo il percorso
    if primoAvvio == False:

        log = TLogin(pathDb)
        pathSubBox = log.getPercorso()
    
        if os.path.isdir(pathSubBox):
            primoAvvio = False
            
        else:
            #rimuovo anche il db perche ce discrepanza tra db e cartella
            QtCore.QFile.remove(pathDb)
            primoAvvio = True

    return primoAvvio

if __name__ == '__main__':


    def main():

        app = QtGui.QApplication(sys.argv)

        w = QtGui.QWidget()
        trayIcon = SystemTrayIcon(QtGui.QIcon("/Users/paganotti/Documents/Progetti/Python/SubBox/images/SubBoxIcon.png"), w)

        trayIcon.show()

        #controllo se si tratta del primo avvio
        #verifico se e presente un account salvato e se esiste la cartella di sincronizzazione
        if risultaPrimoAvvio() == True:
            ui = SetupUi()
            ui.inizializza()
            ui.show()
        else:
            
            if QtCore.QDir.exists(QtCore.QDir(QtCore.QDir.homePath() + "/SubBox/")) == False:
                createDir =  QtCore.QDir( QtCore.QDir.homePath() )
                createDir.mkdir("SubBox")

            monitor = MonitorFsEvents()
            monitor.StartEvents()

        sys.exit(app.exec_())

    main()