import sys
import os

from PyQt4      import QtGui,QtCore
from fsevents   import Observer
from fsevents   import Stream
from SetupUi    import SetupUi

from SetupWizzard import SetupWizzard

import pysvn

class SystemTrayIcon(QtGui.QSystemTrayIcon):
    
    ob = 0
    st = 0
    
    def __init__(self, icon, obs, str, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.ob = obs
        self.st = str
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
        self.ob.unschedule(self.st)
        self.ob.stop()
        QtGui.QApplication.quit()

def callback(event):
    print event.name
    print event.mask

def get_login( realm, username, may_save ):
    return True, "nicola.paganotti", "passwd123", False

def risultaPrimoAvvio():

    primoAvvio = True

    out_file = open("/salva.txt","w")
    bundlePath = QtCore.QCoreApplication.applicationDirPath()
    #print bundlePath
    #print bundlePath.mid(0 ,bundlePath.indexOf("SubBox.app"))
    bundlePath = bundlePath.mid(0 ,bundlePath.indexOf("SubBox.app")) + "SubBox.app/Contents/Resources/"
    #print bundlePath
    out_file.write(bundlePath)


    #controllo se esiste il database
    nomeDb = "SubBox.db"
    
    if os.path.isfile(bundlePath + nomeDb) == True:
        #il database esiste
        primoAvvio = False
        out_file.write("esiste")
    else:
        primoAvvio = True
        out_file.write("non esiste")

    out_file.close()

    return primoAvvio

if __name__ == '__main__':


    def main():
        app = QtGui.QApplication(sys.argv)

        observer = Observer()
        stream = Stream(callback, '/Users/paganotti/SubBox', file_events=True)

        w = QtGui.QWidget()
        trayIcon = SystemTrayIcon(QtGui.QIcon("/Users/paganotti/Documents/Progetti/Python/SubBox/images/SubBoxIcon.png"), observer, stream, w)

        trayIcon.show()
        print "ciaociao"

        #controllo se si tratta del primo avvio
        #verifico se e presente un account salvato e se esiste la cartella di sincronizzazione
        if risultaPrimoAvvio() == True:
            out_file = open("/ciao.txt","w")
            out_file.write("scritto")
            out_file.close()
            ui = SetupUi()

            out_file = open("/setup.txt","w")
            out_file.write("setup")
            out_file.close()

            ui.inizializza()

            out_file = open("/inzializza.txt","w")
            out_file.write("setup")
            out_file.close()

            ui.show()

        out_file = open("/dopo.txt","w")
        out_file.write("dopo")
        out_file.close()

        observer.schedule(stream)
        observer.start()

        #faccio il checkout del progetto
        #client = pysvn.Client()
        #client.callback_get_login = get_login
        #client.checkout('http://gekoinformatica.net/svn/prova/','/Users/paganotti/checkout/testRepo')

        sys.exit(app.exec_())
    main()