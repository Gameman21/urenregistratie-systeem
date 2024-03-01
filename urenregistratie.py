#gemaakt door: Chris Kettmann

import csv
import os

def vragen_stellen():
    naam = input("Voer je naam in: ")
    datum = input("Voer de datum in (bijv. YYYY-MM-DD): ")
    gewerkte_uren = float(input("Hoeveel uur heb je vandaag gewerkt? "))
    project = input("Aan welk project heb je gewerkt? ")

    return naam, datum, gewerkte_uren, project

def gegevens_opslaan(naam, datum, gewerkte_uren, project):
    if not os.path.exists('urenregistratie.csv'):
        with open('urenregistratie.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Naam", "Datum", "Gewerkte Uren", "Project"])
    with open('urenregistratie.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([naam, datum, gewerkte_uren, project])
    print("Gegevens succesvol opgeslagen!")

def main():
    print("Welkom bij het urenregistratiesysteem.")
    while True:
        keuze = input("Wil je je uren registreren? (ja/nee): ").lower()
        if keuze == 'ja' or keuze == 'j':
            naam, datum, gewerkte_uren, project = vragen_stellen()
            gegevens_opslaan(naam, datum, gewerkte_uren, project)
        elif keuze == 'nee' or keuze == 'n':
            print("Bedankt voor het gebruik van het urenregistratiesysteem.")
            break
        else:
            print("Ongeldige invoer. Probeer opnieuw.")

if __name__ == "__main__":
    main()