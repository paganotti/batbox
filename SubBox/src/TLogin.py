import sqlite3

class TLogin:
    def __init__(self, percorsoDb):
        self.con = sqlite3.connect(percorsoDb)
        self.cur = self.con.cursor()

    def crea(self):
        try:

            self.cur.execute("CREATE TABLE LOGIN (idLogin INTEGER PRIMARY KEY, nome TEXT, cognome TEXT, email TEXT, password TEXT, percorso TEXT); ")

        except sqlite3.OperationalError, msg:
            out_file = open("/TLoginError.txt","a")
            out_file.write("TLogin.crea: " + msg.args[0])
            out_file.close()


    def insert(self, account):
        try:

            self.cur.execute('INSERT INTO LOGIN (idLogin,nome,cognome,email,password,percorso) values (?,?,?,?,?,?);', \
            [ 0, unicode(account.nome), unicode(account.cognome), unicode(account.email), unicode(account.password), unicode(account.percorso) ]  )

        except sqlite3.OperationalError, msg:
            out_file = open("/TLoginError.txt","wa")
            out_file.write("TLogin.insert: " + msg.args[0])
            out_file.close()

    def delete(self,idlogin):
        idrecord = 1

    def getCredenziali(self):
        self.cur.execute("SELECT email,password from LOGIN WHERE idLogin = (select max(idLogin) from LOGIN) ")
        credenziali = self.cur.fetchone()

        return credenziali[0], credenziali[1]

    def getPercorso(self):
        self.cur.execute("SELECT percorso from LOGIN WHERE idLogin = (select max(idLogin) from LOGIN) ")
        pathSubBox = self.cur.fetchone()

        return pathSubBox[0].encode("ascii")

    def commit(self):
        self.con.commit()

    def rollback(self):
        self.con.rollback()

  