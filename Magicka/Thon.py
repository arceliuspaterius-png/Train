slownik = {
    "klucz": "wartosc"
}

print(slownik['klucz'])

#rzymskie = {
#    "I": 1,
#    "II": 2,
#    "III": 3,
#    "IV": 4,
#    "V": 5,
#    "VI": 6,
#    "VII": 7,
#    "VIII": 8,
#    "IX": 9,
#    "X": 10,
#    "XI": 11

#}

#rzymskie.pop('XI')

#rzymskie['M'] = 1000

#print(rzymskie['VII'])

#print(rzymskie)

def utworz_samochod():
    pobrana_wartosc = input("tekst od wyswietlenia: ")
    samochod = {}
    color = {}
    silnik ={}
    model = {}
    marka = {}
    samochod['klucz'] = pobrana_wartosc
    samochod['klucz1'] = color
    samochod['klucz2'] = silnik
    samochod['klucz3'] = model
    samochod['klucz4'] = marka
    return pobrana_wartosc

print(utworz_samochod())