import sqlite3

class DatabaseLocale:

    def __init__(self,percorsoDb):
        self.con = sqlite3.connect(percorsoDb)
        self.cur = self.con.cursor()

    def creaTLogin(self):
        TLogin = 1

    def getTLogin(self):
        TRecord = 1

    def apriConn(self):
        apri = 1

    def chiudiConn(self):
        chiudi = 1




  