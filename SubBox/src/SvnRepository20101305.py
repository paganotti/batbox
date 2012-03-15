#updateDir
#updateFile
#add
#delete

import pysvn
from datetime import datetime
import logging
import os

class SvnRepository:
    def __init__(self, urlRepo, username, password, pathSync):
        logging.basicConfig(format='%(asctime)s %(message)s')
        self.logger = logging.getLogger('SvnRepository')
        self.logger.setLevel(logging.INFO)

        self.urlRepo  = urlRepo
        self.username = username
        self.password = password
        self.pathSync = pathSync

        self.client = pysvn.Client()
        self.client.callback_get_login = self.getLogin
        self.client.callback_get_log_message = self.getLogMessage

    def getLogin( realm, username, may_save ):
        return True, self.username, self.password, True


    def getLogMessage(self):
        return True, str(datetime.now())

    def checkout(self):
        self.client.checkout(self.urlRepo,self.pathSync)

    def updateFile(self, file):
        self.client.update(file)
        #gestione file modificati da diversi utenti

    def statusFile(self, file):
        sta = self.client.status(file,True,False)
        for item in sta:
            print  'status =' , item.text_status , 'path =' , item.path
            #print 'text_status = ' , item.text_status

    def sync(self,path):
        listStatus = self.client.status(path,True,False)
        for item in listStatus:
            if item.path.find("/.svn") == -1 and item.path.find("/.DS_Store") == -1:
                print  'path =' , item.path , 'status =' , item.text_status
                if item.text_status == pysvn.wc_status_kind.unversioned:
                    error = self.add(item.path)
                    print "errore = ", error

                elif item.text_status == pysvn.wc_status_kind.missing:
                    self.remove(item.path)

                elif item.text_status == pysvn.wc_status_kind.modified:
                    self.modify(item.path)

    #ritorna il numero di revisione del file aggiunto
    #se si verifica un errore il numero di revisione e' negativo
    def add(self, file):

        error = 0
        #controllo se il file esiste fisicamente
        if os.path.exists(file) == False:
            error = -1
            return erorr

        listStatus = self.client.status(file,True,False)
        print listStatus
        
        #self.logger.info('add - count: %d',len(listStatus))


        if len(listStatus) != 1:
            #self.logger.warning('add - count: %d',len(listStatus))
            error = -2
            return error
        
        item = listStatus[0]
        #self.logger.info('add - status: %s',item.text_status)

        if item.text_status != pysvn.wc_status_kind.unversioned:
            self.logger.info('add - status: %s',item.text_status)

        if len(listStatus) == 1 and item.text_status == pysvn.wc_status_kind.unversioned:
            self.client.add(file)
            revision = self.client.checkin(file,str(datetime.now()))

        self.logger.info('add - errore: %d',error )

        if error < 0:
            self.logger.warning('add - errore: %d',error)

        return error

    def remove(self, file):

        print file

        listStatus = self.client.status(file,True,False)

        revision = -1

        self.logger.info('remove - count: %d',len(listStatus))


        if len(listStatus) != 1:
            self.logger.warning('remove - count: %d',len(listStatus))
            error = -2
            return error

        item = listStatus[0]

        self.logger.info('remove - status: %s',item.text_status)

        if item.text_status != pysvn.wc_status_kind.missing:
            self.logger.warning('remove - status: %s',item.text_status)

        if len(listStatus) == 1 and item.text_status == pysvn.wc_status_kind.missing:

            info = self.client.info2( file, recurse=False)
            print info
            
            print "info kind = ",info[0][1].kind

            if info[0][1].kind == pysvn.node_kind.file:
                print "isfile"
                self.client.remove(file)
                self.client.checkin(file,str(datetime.now()))
            else:
                #remove from repository
                #urlrem = self.urlRepo + file[len(self.pathSync):]
                #print "isdir"
                #print urlrem
                #self.client.remove(urlrem)
                print "isdir"
                pathMenuUno = os.path.split(file)
                print "head = " , pathMenuUno[0]
                self.client.remove(file)
                self.client.checkin(pathMenuUno[0],str(datetime.now()))

    def modify(self,file):
        error = -1

        listStatus = self.client.status(file,True,False)

        self.logger.info('modify - count: %d',len(listStatus))

        if len(listStatus) != 1:
            self.logger.warning('modify - count: %d',len(listStatus))
            return error

        item = listStatus[0]
        self.logger.info('modify - status: %s',item.text_status)

        if item.text_status != pysvn.wc_status_kind.modified:
            self.logger.info('modify - status: %s',item.text_status)

        if len(listStatus) == 1 and item.text_status == pysvn.wc_status_kind.modified:
            revision = self.client.checkin(file,str(datetime.now()))

        return error


        







  