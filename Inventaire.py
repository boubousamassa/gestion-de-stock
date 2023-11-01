import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from ttkthemes import ThemedStyle
import datetime
from dateutil.parser import parse


class Category:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Gestion des Catégories")
        self.root.config(bg="white")
        self.root.focus_force()

        # Dégradé de couleur en arrière-plan
        style = ThemedStyle(root)
        style.set_theme("plastik")

        start_color = 'bisque4'
        end_color = '#FFE5B4'
        background_frame = tk.Frame(root, bg='bisque4', height=200, width=400)
        background_frame.pack(fill='both', expand=True)
        canvas = tk.Canvas(background_frame, bg='bisque4', height=200, width=400)
        canvas.pack(fill='both', expand=True)
        canvas.create_rectangle(0, 0, 1400, 1200, fill=start_color, tags='gradient')
        canvas.create_rectangle(0, 0, 400, 0, fill=end_color, tags='gradient')

        # Titre
        gestion_title = tk.Label(root, text="INVENTAIRE", font=("Algerian", 25, "bold"), bg="green", fg="black")
        gestion_title.place(x=150, y=3 , width=1000)

        # Entrées pour les dates
        date_label = tk.Label(root, text="Date  : Du", font=("times new roman", 20), bg="lightgray")
        date_label.place(x=300, y=130)
        self.date_debut = tk.Entry(root, font=("times new roman", 15))
        self.date_debut.place(x=430, y=130, width=150, height=38)
        date_label = tk.Label(root, text="Au", font=("times new roman", 20), bg="lightgray")
        date_label.place(x=620, y=130)
        self.date_fin = tk.Entry(root, font=("times new roman", 15))
        self.date_fin.place(x=670, y=130, width=150, height=38)

        # Bouton Recherche
        btn_ok = tk.Button(root, text="RECHERCHE", font=("times new roman", 15), command=self.on_submit, bd=10,relief=tk.GROOVE, bg="green")
        btn_ok.place(x=520, y=185, width=150)

        # Affichage
        result_Frame = tk.Frame(root, bd=5, relief=tk.GROOVE, bg="gray")
        result_Frame.place(x=10, y=250, width=1300, height=375)

        # Tableau pour afficher les données
        scroll_x = tk.Scrollbar(result_Frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(result_Frame, orient=tk.VERTICAL)
        self.tabl_resul = ttk.Treeview(result_Frame, columns=("nom_produit", "prix_unit", "quantites_vente", "date"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabl_resul.pack(fill=tk.BOTH, expand=1)
        scroll_x.config(command=self.tabl_resul.xview)
        scroll_y.config(command=self.tabl_resul.yview)

        # Entête du tableau
        self.tabl_resul.heading("nom_produit", text="Nom Produit")
        self.tabl_resul.heading("prix_unit", text="Prix Unit")
        self.tabl_resul.heading("quantites_vente", text="Quantités de vente")
        self.tabl_resul.heading("date", text="Date")
        self.tabl_resul["show"] = "headings"

        # Largeur de chaque colonne
        self.tabl_resul.column("nom_produit", width=300)
        self.tabl_resul.column("prix_unit", width=300)
        self.tabl_resul.column("quantites_vente", width=300)
        self.tabl_resul.column("date", width=300)

        # Variables pour les totaux
        self.totalinventaire = tk.StringVar()
        self.totalinventairebotique = tk.StringVar()

        # Affichage du total de vente
        total_label = tk.Label(root, text="Total de Vente :", font=("times new roman", 20), bg="lightgray")
        total_label.place(x=410, y=650)
        id_total = tk.Entry(root, textvariable=self.totalinventaire, font=("times new roman", 20), bg="lightgray",state="readonly")
        id_total.place(x=610, y=650, width=200)

        self.totalinventairebotique = tk.StringVar()
        self.totalinventairebotique.set("0")  # Vous pouvez définir une valeur initiale si nécessaire
        connection = sqlite3.connect("Alimentation.db")
        cur = connection.cursor()
        cur.execute(f"select * from listevente ")
        rows = cur.fetchall()
        totale = sum([row[2] * row[3] for row in rows])
        self.totalinventairebotique.set(totale)  # Utilisez .set() pour mettre à jour la valeur de la variable StringVar
        connection.commit()
        connection.close()

        id_total_boutique = tk.Label(root, text=f"Produits non Vendus : {totale} FCFA",font=("times new roman", 20), bg="lightgray")
        id_total_boutique.place(x=150, y=70, width=850, height=50)

    def afficher_erreurA(self):
        messagebox.showerror("Erreur", "Premier format incorrect. Veuillez utiliser le format JJ/MM/AAAA",parent=self.root)
    def afficher_erreurB(self):
        messagebox.showerror("Erreur", "Deuxième format incorrect. Veuillez utiliser le format JJ/MM/AAAA",parent=self.root)

    def on_submit(self):
        user_input_debut = self.date_debut.get()
        user_input_fin = self.date_fin.get()
        try:
            date1 = datetime.datetime.strptime(user_input_debut, "%d/%m/%Y").date()
        except ValueError:
            self.afficher_erreurA()
        try:
            date2 = datetime.datetime.strptime(user_input_fin, "%d/%m/%Y").date()
        except ValueError:
            self.afficher_erreurB()
        if date2 >= date1:
            try:
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute("SELECT nomproduit, prix, quantiter, date FROM listevente WHERE date >= ? AND date <= ?",(date1, date2))
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.tabl_resul.delete(*self.tabl_resul.get_children())
                    for row in rows:
                        self.tabl_resul.insert("", tk.END, values=row)
                else:
                    messagebox.showinfo("Information", "Aucune donnée trouvée pour cette période.", parent=self.root)
            except sqlite3.Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la requête SQL : {e}", parent=root)
            finally:
                connection.close()
                self.calculetotal()
        else:
            messagebox.showerror("Erreur","Votre demande est impossible car votre première date est plus récente que la deuxième date saisie", parent=root)


    def calculetotal(self):
        user_input_debut = self.date_debut.get()
        user_input_fin = self.date_fin.get()
        try:
            user_date = parse(user_input_debut)
            date_debut = user_date.date()
            try:
                user_date = parse(user_input_fin)
                date_fin = user_date.date()
                if date_fin >= date_debut:
                    connection = sqlite3.connect("Alimentation.db")
                    cur = connection.cursor()
                    cur.execute(f"select * from listevente where date>=? and date<=?", (date_debut, date_fin))
                    rows = cur.fetchall()
                    total = sum([row[2] * row[3] for row in rows])
                    self.totalinventaire.set(total)
                    connection.commit()
                    connection.close()
                else:
                    messagebox.showerror("Erreur","Votre demande est impossible car votre premier date est plus récente que la deuxième date saisie", parent=root)
            except ValueError:
                messagebox.showerror("Erreur", "Deuxième format invalide", parent=root)
        except ValueError:
            messagebox.showerror("Erreur", "Premier format invalide", parent=root)


if __name__ == "__main__":
    root = tk.Tk()
    system = Category(root)
    root.mainloop()
