import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import date, timedelta
from prettytable import PrettyTable
import datetime
from ttkthemes import ThemedStyle


class Expiration:
    def __init__(self, root):
        self.root = root
        self.root.title("ALERTES D'EXPIRATION")
        self.root.geometry("700x480+300+0")
        self.root.config(bg="lightgray")
        style = ThemedStyle(root)
        style.set_theme("plastik")

        # Titre de l'application
        gestion_title = tk.Label(self.root, text="ALERTE D'EXPIRATION", font=("Algerian", 25, "bold"), bg="lightgray", fg="black")
        gestion_title.pack(pady=10)

        # Frame pour les résultats
        result_frame = ttk.Frame(self.root, borderwidth=5, relief=tk.GROOVE)
        result_frame.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)

        # Tableau
        columns = ("nom_produit", "quantites_vente", "jour_restant")
        self.tableau_resultats = ttk.Treeview(result_frame, columns=columns, show="headings")
        self.tableau_resultats.heading("nom_produit", text="Nom du Produit")
        self.tableau_resultats.heading("quantites_vente", text="Quantité Restante")
        self.tableau_resultats.heading("jour_restant", text="Jours Restants")
        self.tableau_resultats.pack(fill=tk.BOTH, expand=True)

        self.remplir_tableau_resultats()

    def remplir_tableau_resultats(self):
        datelimite = date.today() + timedelta(days=30)
        connection = sqlite3.connect("Alimentation.db")
        cur = connection.cursor()
        cur.execute("SELECT nomproduit, quantiter, expiration FROM listeproduit WHERE expiration <= ?", (datelimite,))
        resultats = cur.fetchall()
        tableau = PrettyTable()
        tableau.field_names = ["nom", "quantiter", "jour restant"]

        for row in resultats:
            nomproduit = row[0]
            quantiter = row[1]
            date1 = datetime.datetime.strptime(row[2], "%Y-%m-%d").date()
            reste = (date1 - date.today()).days
            tableau.add_row([nomproduit, quantiter, reste])
            self.tableau_resultats.insert("", tk.END, values=[nomproduit, quantiter, reste])

        connection.commit()
        connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = Expiration(root)
    root.mainloop()
