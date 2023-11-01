from tkinter import *
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class POS:
    def __init__(self):
        self.root = Tk()
        self.root.title("Point de Vente")

        # Récupérez et affichez les statistiques de vente
        self.afficher_statistiques_vente()

        self.root.mainloop()

    def afficher_statistiques_vente(self):
        # Récupérez les données et créez la figure Matplotlib
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT nomproduit, SUM(quantiter) as tota FROM listevente GROUP BY nomproduit")
        data = cursor.fetchall()
        connection.close()
        nomproduit = [row[0] for row in data]
        quantiter = [row[1] for row in data]

        # Créez une figure Matplotlib
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        ax.bar(nomproduit, quantiter, color='b', edgecolor='black', alpha=0.8, linewidth=1)
        ax.set_title("Statistiques de vente par produit", fontsize=16, fontweight='bold')
        ax.set_xlabel("Nom des Produits", fontsize=12)
        ax.set_ylabel("Quantité de Vente", fontsize=12)

        # Créez un canevas tkinter pour la figure Matplotlib
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    system = POS()
