Algos

Bogdan Verkhovod


Algoritmipeli

Pelin idea ja tavoite

Tämä on tekstipohjainen seikkailupeli. Pelaaja liikkuu huoneiden välillä ja ratkaisee pieniä Python-algoritmeihin liittyviä tehtäviä. Huoneissa on kaksi legendaarista esinettä: Excalibur ja Mjolnir.

Pelin tavoitteena on ratkaista molempien huoneiden tehtävät ja kerätä esineet inventaarioon. Esineen voi kerätä vasta, kun huoneen tehtävään on annettu oikea vastaus.

Pelaaminen

Peliä ohjataan kirjoittamalla valikossa näkyviä komentoja. Pelaaja voi:

- tarkistaa nykyisen huoneen;
- siirtyä toiseen huoneeseen;
- ratkaista huoneen tehtävän;
- kerätä esineen;
- tarkistaa inventaarion;
- poistaa esineen inventaariosta;
- tarkistaa pelaajan tiedot.

Pelin alussa pelaaja antaa nimensä ja ikänsä. Alle 12-vuotias pelaaja ei voi aloittaa peliä.

Tehtävässä näytetään lyhyt Python-algoritmi. Pelaajan pitää päätellä, minkä tuloksen algoritmi tulostaa. Jos vastaus on oikein, huoneen esine vapautuu. Väärän vastauksen jälkeen tehtävää voi yrittää uudelleen.

Tallentaminen

Kun pelaaja kirjoittaa "lopeta", peli tallennetaan automaattisesti tiedostoon "tallennus.txt". Pelaaja saa kuusinumeroisen jatkokoodin. Seuraavalla pelikerralla pelaamista voi jatkaa antamalla tämän koodin.

Tallennukseen kuuluvat pelaajan nimi, ikä, sijainti, inventaario ja ratkaistut tehtävät.

Ohjelman rakenne

Ohjelmassa käytetään neljää luokkaa: "Item", "Room", "Player" ja "Menu". Tallennukset käsitellään JSON-muodossa. Peli käyttää vain Pythonin tavallisia moduuleja, joten ylimääräisiä ohjelmia tai kirjastoja ei tarvitse asentaa.

Kestävä kehitys

Peli on kevyt eikä tarvitse tehokasta tietokonetta tai erillistä pelimoottoria. Tekstipohjainen peli kuluttaa vähän tietokoneen resursseja. Tallennustoiminnon ansiosta peliä voi jatkaa myöhemmin ilman, että kaikki täytyy aloittaa alusta.
