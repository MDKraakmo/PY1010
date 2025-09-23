'''
Beregning av årlig kostnad av Elbil og Bensinbil
Marte Djupvik Kråkmo
'''

#variabler for regnestykket
totalAntallKm = 10000 #[km]
forsikringElbil = 5000 #[kr/år]
forsikringBensinbil = 7500 #[kr/år]
trafikkforsikringsavgift = 8.38 * 365 #[kr/år] fordi vi multipliserer med 365
strømpris = 2 #[kr/kWh]
drivstoffElbil = 0.2 * totalAntallKm * strømpris #[kr], beregning for totalkostnad av drifstoff for elbil
drivstoffBensinbil = 1 * totalAntallKm #[kr], beregning for totalkostnad av drivstoff for bensinbil
bomavgiftElbil = 0.1 * totalAntallKm #[kr], beregning for totalkostnad av bomavgift for elbil
bomavgiftBensinbil = 0.3 * totalAntallKm #[kr], beregning for totalkostnad av bomavgift for bensinbil

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
    print("Elbil er billigere enn bensinbil.\nÅrlig utgift på elbil er %.2f kr, mens på bensinbil er det %.2f kr.\nDifferansen i kostnad er %.2f kr" % (elbilKostnad, bensinbilKostnad, (bensinbilKostnad - elbilKostnad)))
elif bensinbilKostnad < elbilKostnad:
    print("Bensinbil er billigere enn elbil.\nÅrlig utgift på bensinbil er %.2f kr, mens på elbil er det %.2f kr.\nDifferansen i kostnad er %.2f kr" % (bensinbilKostnad, elbilKostnad, (elbilKostnad - bensinbilKostnad)))
else:
    print("Det er like dyrt, med en pris på %.2f kr" % (bensinbilKostnad)) #Dersom hverken if- eller elif-statementen er sanne printes dette. 
