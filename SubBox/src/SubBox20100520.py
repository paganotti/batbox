import sys
import os
from datetime import datetime

from PyQt4          import QtGui,QtCore
from FSEvents       import *
from SetupUi        import SetupUi
from TLogin         import TLogin
from SvnRepository  import SvnRepository



pathDb =  unicode(QtCore.QDir.homePath()) + "/.subbox/SubBox.db"
urlRepo = 'http://gekoinformatica.net/svn/prova'

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
            print primoAvvio

    return primoAvvio

def fsevents_callback(streamRef, clientInfo, numEvents, eventPaths, eventMasks, eventIDs):
    #settings.debug("fsevents_callback(streamRef = %s, clientInfo = %s, numEvents = %s)", streamRef, clientInfo, numEvents)
    #settings.debug("fsevents_callback: FSEventStreamGetLatestEventId(streamRef) => %s", FSEventStreamGetLatestEventId(streamRef))
    full_path = clientInfo

    for i in range(numEvents):
        path = eventPaths[i]
        if path[-1] == '/':
            path = path[:-1]

        if eventMasks[i] & kFSEventStreamEventFlagMustScanSubDirs:
            recursive = True

        elif eventMasks[i] & kFSEventStreamEventFlagUserDropped:
            print "BAD NEWS! We dropped events."
            print "Forcing a full rescan."
            recursive = 1
            path = full_path

        elif eventMasks[i] & kFSEventStreamEventFlagKernelDropped:
            print "REALLY BAD NEWS! The kernel dropped events."
            print "Forcing a full rescan."
            recursive = 1
            path = full_path

        else:
            recursive = False

        print "percorso = " , path

        login = TLogin(pathDb)
        credenziali = login.getCredenziali()

        client = SvnRepository(urlRepo,credenziali[0],credenziali[1],login.getPercorso())
        client.sync(path)


def my_FSEventStreamCreate(path):

    sinceWhen = -1 #kFSEventStreamEventIdSinceNow
    flags     = 0
    flush_seconds = -1
    latency = 3.0

    streamRef = FSEventStreamCreate(kCFAllocatorDefault,
                                    fsevents_callback,
                                    path,
                                    [path],
                                    sinceWhen,
                                    latency,
                                    flags)
    if streamRef is None:
        print "ERROR: FSEVentStreamCreate() => NULL"
        return None

    return streamRef

if __name__ == '__main__':


    def main():
        app = QtGui.QApplication(sys.argv)

        w = QtGui.QWidget()
        trayIcon = SystemTrayIcon(QtGui.QIcon("/Users/paganotti/Documents/Progetti/Python/SubBox/images/SubBoxIcon.png") , w)

        trayIcon.show()

        #controllo se si tratta del primo avvio
        #verifico se e presente un account salvato e se esiste la cartella di sincronizzazione
        if risultaPrimoAvvio() == True:
            ui = SetupUi()
            ui.inizializza()
            ui.show()

        #faccio il checkout del progetto
        login = TLogin(pathDb)
        credenziali = login.getCredenziali()

        client = SvnRepository(urlRepo,credenziali[0],credenziali[1],login.getPercorso())

        if os.listdir(login.getPercorso()) == []:
            client.checkout()
        else:
            client.sync(login.getPercorso())

        full_path = "/Users/paganotti/SubBox"

        streamRef = my_FSEventStreamCreate(full_path)

        FSEventStreamScheduleWithRunLoop(streamRef, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode)

        startedOK = FSEventStreamStart(streamRef)
        if not startedOK:
            print "Errore FSEventStreamStart"
            return

        # Run
        CFRunLoopRun()

        #Stop / Invalidate / Release
        FSEventStreamStop(streamRef)
        FSEventStreamInvalidate(streamRef)
  
        sys.exit(app.exec_())

    main()