"""
Datei: alters_abfrage.py
Created by: MetY-def
"""


def alter_pruefen():
    alter = int(input("Gib ein Alter ein "))

    if alter >= 18:
        print("Die Person ist Volljährig")
    else:
        print("Die Person ist Minderjährig")


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
