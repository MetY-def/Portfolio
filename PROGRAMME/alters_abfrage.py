"""
Datei: alters_abfrage.py
Created by: MetY-def
"""


from datetime import date

heute = date.today()
achtzehn = heute.replace(year=heute.year - 18)


def alter_pruefen():
    jahr = int(input("Geburtsjahr eingeben (jjjj): "))
    monat = int(input("Geburtsmonat eingeben (mm): "))
    tag = int(input("Geburtstag eingeben (tt): "))

    geburtstag = date(jahr, monat, tag)

    if geburtstag <= achtzehn:
        print("Die Person ist Volljährig")
    else:
        print("Die Person ist nicht Volljährig")


def menue():
    while True:
        print("Was möchtest du tun?")
        print("1 = Alter Überprüfen")
        print("2 = beenden")

        auswahl = int(input("Bitte wähle (1/2)"))

        if auswahl == 1:
            alter_pruefen()
        elif auswahl == 2:
            print("Programm_beendet")
            break
        else:
            print("ungültige Eingabe")


menue()
