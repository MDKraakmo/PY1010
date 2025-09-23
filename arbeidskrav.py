#programmet regner ut årlig kostnad for bensinbil og elbil, samt differansen mellom disse

#variabler for regnestykket
totalAntallKm = 10000
forsikringElbil = 5000
forsikringBensinbil = 7500
trafikkforsikringsavgift = 8.38 * 365
strømpris = 2
drivstoffElbil = 0.2 * totalAntallKm * strømpris
drivstoffBensinbil = 1 * totalAntallKm
bomavgiftElbil = 0.1 * totalAntallKm
bomavgiftBensinbil = 0.3 * totalAntallKm

'''
Regnestykket for årlig bruk av bensinbil.
Bruker float-funksjonen for å forsikre meg om at regnestykket blir et desimaltall
'''
bensinbilKostnad = float(forsikringBensinbil + trafikkforsikringsavgift + drivstoffBensinbil + bomavgiftBensinbil)

#Regnestykket for årlig bruk av elbil
elbilKostnad = float(forsikringElbil + trafikkforsikringsavgift + bomavgiftElbil + drivstoffElbil)

'''
Bruker en if-statement for å gå gjennom de ulike alternativene.
Bruker '%.2f' til å representere verdiene som skal fylles inn, med 2 desimaler.
Bruker '\n' slik at en ny setning representeres på en ny linje.
'''

if elbilKostnad < bensinbilKostnad:
    print("Elbil er billigere enn bensinbil.\nÅrlig utgift på elbil er %.2f, mens på bensinbil er det %.2f.\nDifferansen i kostnad er %.2f" % (elbilKostnad, bensinbilKostnad, (bensinbilKostnad - elbilKostnad)))
elif bensinbilKostnad < elbilKostnad:
    print("Bensinbil er billigere enn elbil.\nÅrlig utgift på bensinbil er %.2f, mens på elbil er det %.2f.\nDifferansen i kostnad er %.2f" % (bensinbilKostnad, elbilKostnad, (elbilKostnad - bensinbilKostnad)))
else:
    print("Det er like dyrt, med en pris på %.2f" % (bensinbilKostnad)) #Dersom hverken if- eller elif-statementen er sanne printes dette. 
