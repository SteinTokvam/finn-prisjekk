import requests
from bs4 import BeautifulSoup
import csv
import sys

url = str(sys.argv[1])
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

priser = []
adresser = []

for pris in soup.find_all(class_="mt-4 sm:mt-8 text-12 text-gray-500 flex flex-col sm:block"):
    tmp = pris.text.replace(" ", "")[10:20]
    tmp = tmp.replace(u'\xa0', u'')
    priser.append(tmp)

for adresse in soup.find_all("span", {"class" : "text-14 text-gray-500"}):
    tmp = adresse.text.split(",")
    adresser.append(tmp[0])

del adresser[0]

print("Har funnet: " + str(len(priser)) + " boligannonser.")
print("Ser etter boligannonser vi allerede har lagt til...")

with open('boligpriser.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
       lestAdresse = row[1:]
       
       if lestAdresse[0] in adresser:
        index = adresser.index(lestAdresse[0])
        adresser.remove(lestAdresse[0])
        del priser[index]

if len(priser) == 0:
    print("Ingen priser igjen å legge til.")
else:
    print("legger til " + str(len(priser)) + " boligannonser.")
    i = 0
    with open("boligpriser.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Pris", "Adresse"])
        for pris in priser:
            writer.writerow([pris, adresser[i]])
            i = i + 1

