
class AccountSubBox:

    '''
    def __init__(self, nome, cognome, email, password, percorso):
        self._nome = nome
        self._cognome = cognome
        self._email = email
        self._password = password
        self._percorso = percorso
    '''

    nome     = ""
    cognome  = ""
    email    = ""
    password = ""
    percorso = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def delNome(self):
        del self.nome

    def getCognome(self):
        return self.cognome

    def setCognome(self, cognome):
        self.cognome = cognome

    def delCognome(self):
        del self.cognome

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def delEmail(self):
        del self.email

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def delPassword(self):
        del self.password

    def getPercorso(self):
        return self.percorso

    def setPercorso(self, percorso):
        self.percorso = percorso



    
  