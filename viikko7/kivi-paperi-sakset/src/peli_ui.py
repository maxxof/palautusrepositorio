from kps import KiviPaperiSakset
from luo_peli import luo_peli

class PeliUI:
    def kaynnista():
        while True:
            print("Valitse pelataanko"
                    "\n (a) Ihmistä vastaan"
                    "\n (b) Tekoälyä vastaan"
                    "\n (c) Parannettua tekoälyä vastaan"
                    "\nMuilla valinnoilla lopetetaan"
                    )
            
            valinta = input()
            peli = KiviPaperiSakset.valitse_peli(valinta, luo_peli)
            if not peli:
                break

            peli.pelaa()