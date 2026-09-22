"""
Toteuta seuraava luokkahierarkia Python-kielellä:
Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

"""


class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name)


class Book(Publication):
    def __init__(self, name, author, number_of_pages):
        self.author = author
        self.number_of_pages = number_of_pages

        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(self.author, self.number_of_pages)


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor

        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(self.chief_editor)


def main():
    publications = []
    publications.append(Magazine("Aku Ankka", "Aki Hyyppä"))
    publications.append(Book("Hytti n:o 6", "Rosa Liksom", 200))

    for i in publications:
        i.print_information()


main()
