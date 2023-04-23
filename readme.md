# Finn

## Linje 1-4 

er imports. det er biblioteker som gir meg funksjonalitet slik at jeg slipper å implementere det selv. requests er for å hente innhold fra internett. BeautifulSoup(bs4) er for å finne innhild i html, csv er for å åpne/lese/skrive .csv filer og sys er for å få tilgang til systemet som koden kjører på.

## Linje 6-11 
Er oppsett. url til finn sendes med når jeg kjører koden. f.eks python3 finn.py finn.no

priser og adresser er nå 2 tomme lister som jeg skal fylle med priser og tilhørende addresser.

## Linje 13-22

I linje 13-16 så går først igjennom html filen jeg henter fra finn etter priser på boligene og legger resultatet inn i priser-listen

I Linje 18-20 så gjøre jeg det samme igjen, bare denne gangen for adresser.

Til slutt i linje 22 så fjerner jeg første adressen, for den klarte å finne adressen for "ukens bolig", noe som jeg ikke gjør med prisen. Var og et par andre tilfeller hvor dette ikke funket helt, men er nå det det er.

## Linje 24-25
Så printer jeg ut priser og adresser den har funnet til terminalen.

## Linje 27-38
Så åpner jeg en fil som heter boligpriser.csv og går igjennom innholdet i den for alle boliger jeg allerede har funnet. De som jeg allerede har fra før fjerner jeg fra de 2 listene mine. Printer ut at det ikke er noen flere å legge inn til slutt dersom alle boligene er fjernet fra listen over nye boliger. Programmet avsluttes.

## Linje 39-47
Hvis det er igjen boliger å legge til så printer jeg til terminalen hvor mange det er. Så åpnes boligpriser.csv på nytt og pris og adresse på nye boliger legges inn på dette formatet:

Pris, Adresse

På linje 45 så har jeg en for løkke. Den går igjennom alle prisene i priser listen og legger de inn i filen. i tillegg så har jeg på linje 41 en variabel i som settes til 0. Denne bruker jeg for å kunne hente tilsvarende element i adresser listen som jeg er på i priser listen. Lister starter påå 0.