class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
class Summa:
    def __init__(self, sovelluslogiikka, operandi):
        self.sovelluslogiikka = sovelluslogiikka
        self.operandi = operandi
        self.edellinen_arvo = self.sovelluslogiikka.arvo()

    def suorita(self):
        self.sovelluslogiikka.plus(self.operandi)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)
        
class Erotus:
    def __init__(self, sovelluslogiikka, operandi):
        self.sovelluslogiikka = sovelluslogiikka
        self.operandi = operandi
        self.edellinen_arvo = self.sovelluslogiikka.arvo()

    def suorita(self):
        self.sovelluslogiikka.miinus(self.operandi)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, edellinen_komento):
        self.sovelluslogiikka = sovelluslogiikka
        self.edellinen_komento = edellinen_komento

    def suorita(self):
        self.edellinen_komento.kumoa()