from PyQt4          import QtGui,QtCore
from TLogin         import TLogin
from SvnRepository  import SvnRepository
import os
from FSEvents import *

pathDb =  unicode(QtCore.QDir.homePath()) + "/.subbox/SubBox.db"
urlRepo = 'http://gekoinformatica.net/svn/prova'

class MonitorFsEvents:

    def fsevents_callback(self,streamRef, clientInfo, numEvents, eventPaths, eventMasks, eventIDs):
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

            if path.find("/.svn") == -1 and path.find("/.DS_Store") == -1:

                print "percorso = " , path


                login = TLogin(pathDb)
                credenziali = login.getCredenziali()

                client = SvnRepository(urlRepo,credenziali[0],credenziali[1],login.getPercorso())
                client.sync(path)

    def my_FSEventStreamCreate(self,path):

        sinceWhen = -1 #kFSEventStreamEventIdSinceNow
        flags     = 0
        flush_seconds = -1
        latency = 3.0

        streamRef = FSEventStreamCreate(kCFAllocatorDefault,
                                        self.fsevents_callback,
                                        path,
                                        [path],
                                        sinceWhen,
                                        latency,
                                        flags)
        if streamRef is None:
            print "ERROR: FSEVentStreamCreate() => NULL"
            return None

        return streamRef

    def StartEvents(self):
        #faccio il checkout del progetto
        login = TLogin(pathDb)
        credenziali = login.getCredenziali()

        client = SvnRepository(urlRepo,credenziali[0],credenziali[1],login.getPercorso())

        if os.listdir(login.getPercorso()) == []:
            client.checkout()
        else:
            client.sync(login.getPercorso())

        print login.getPercorso()

        streamRef = self.my_FSEventStreamCreate(login.getPercorso())

        FSEventStreamScheduleWithRunLoop(streamRef, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode)

        startedOK = FSEventStreamStart(streamRef)
        if not startedOK:
            print "Errore FSEventStreamStart"
            return

  