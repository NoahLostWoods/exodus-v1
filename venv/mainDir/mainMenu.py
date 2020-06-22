import os as o
import time as t
from pandas.errors import EmptyDataError
import pandas as pd
from TeleBot.brain import *


def menu_iniziale():
    print('''
    Benvenuto!
    1) Carica dataset di prova.
    2) Carica dataset da path.
    3) Avvia bot.
    0) Exit.
    ''')

    toss = input("Seleziona: ")

    if toss == "1":
        try:
            dataset = pd.read_csv("data/iris.csv")
            t.sleep(0.5)
            print("Dataset OK")
            t.sleep(10.0)
            print(dataset)
            bott = input("press (q): ")
            if bott.startswith("q"):
                return menu_iniziale()
        except EmptyDataError:
            print("Errore di caricamento del dataset.")
            return menu_iniziale()


    elif toss == "2":
        try:
            path = input("Inserire il path: ")
            dataset = pd.read_csv(path)
            print("Dataset importato con successo")
            t.sleep(10.0)
            print(dataset)
            bott = input("press q")
            if bott.startswith("q"):
                return menu_iniziale()
        except BaseException:
            print("Errore di caricamento del dataset. ")
            return menu_iniziale()

    elif toss == "3":
        print("Avvio bot in corso...")
        t.sleep(0.5)
        botaut()
        print()
        bott = input("Press q: ")
        if "q":
            t.sleep(0.5)
            return menu_iniziale()




    elif toss == "0":
        print("A presto!")
        exit(0)


if __name__ == '__main__':
    menu_iniziale()
