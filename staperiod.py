from tkinter import *
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class TOS:
    def __init__(self):
        # Exécutez une requête SQL pour récupérer les données de vente pour une période spécifique
        connection = sqlite3.connect("Alimentation.db")
        df = pd.read_sql_query("SELECT strftime('%Y-%m',date) as mois, SUM(quantiter) as total_vendue FROM listevente GROUP BY mois",connection)
        # Fermez la connexion à la base de données
        connection.close()
        plt.bar(df["mois"], df["total_vendue"], color='b')
        # Ajouter les étiquettes et le titre
        plt.xlabel("Mois", fontsize=14)
        plt.ylabel("Quantité de Vente", fontsize=14)
        plt.title("Ventes mensuelles")
        # Ajouter une légende
        plt.legend(['Quantité de vente'])
        # Afficher le graphique
        plt.xticks(rotation=00)
        plt.show()
if __name__ == "__main__":
    root = Tk()
    system = TOS()