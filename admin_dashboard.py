from tkinter import *
from tkinter import ttk, messagebox
from employee import Employee
from Fournisseur import Supplier
from Inventaire import Category
from Enregistrement import Producte
from Vente import Sales
from staprod import POS
from staperiod import TOS
from note import Note
from Expiration import Expiration
import subprocess
from Alerte import Alerte
import sqlite3
from ttkthemes import ThemedStyle
import os
import glob
from datetime import date,timedelta


class StockManager:
    def __init__(self, root_win):
        self.supp_manager = None
        self.sales_manager = None
        self.staprod_manager = None
        self.staperiod_manager = None
        self.expiration_manager = None
        self.category_manager = None
        self.alerte_manager = None
        self.product_manager = None
        self.note_manager = None
        self.new_window = None
        self.emp_manager = None
        self.root = root_win
        self.root.geometry("1350x700+0+0")
        self.root.title("Système de Gestion de Stock")
        self.root.config(bg="bisque4")
        style = ThemedStyle(root)
        style.set_theme("plastik")
# screen Title
        title = Label(self.root, text="Tableau de Bord", font=("Lato", 26, "bold"), bg="white", fg="#343A40",anchor="w", padx=20)  # may add anchor here to center left
        title.place(x=220, y=0, relwidth=1, height=70)
# logout button
        logout_btn = Button(self.root, text="déconnexion", command=self.logout, font=("Lato", 11, "bold"), bd=0,bg="#F66B0E", fg="white")
        logout_btn.place(x=1180, y=10, height=40, width=120)
# Menu
        menu_frame = Frame(self.root, bd=0, bg="#23282c", relief=RIDGE)
        menu_frame.place(x=0, y=0, width=240, height=400, relheight=1)
        menu_label = Label(menu_frame, text="Menu", font=("Lato", 15, "bold"), fg="#313552", bg="#23ba9b")
        menu_label.pack(side=TOP)

        employee_btn = Button(menu_frame, text="Enployer", command=self.employee, font=("Lato", 20, "normal"),bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        employee_btn.pack(side=TOP ,anchor="w")
        supplier_btn = Button(menu_frame, text="Fournisseurs/clients", command=self.supplier, bg="#23282c",font=("Lato", 18, "normal"), fg="#a7acb2", bd=0, cursor="hand2")
        supplier_btn.pack(side=TOP ,anchor="w")
        product_btn = Button(menu_frame, text="Enregistrement", command=self.product, font=("Lato", 18, "normal"),bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        product_btn.pack(side=TOP ,anchor="w")
        category_btn = Button(menu_frame, text="Inventaire", command=self.category, font=("Lato", 18, "normal"),bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        category_btn.pack(side=TOP ,anchor="w")
        sales_btn = Button(menu_frame, text="Ventes", command=self.sales, font=("Lato", 18, "normal"), bg="#23282c",fg="#a7acb2", bd=0, cursor="hand2")
        sales_btn.pack(side=TOP ,anchor="w")
        staprod_btn = Button(menu_frame, text="Statistique-produit", command=self.staprod, font=("Lato", 18, "normal"), bg="#23282c",fg="#a7acb2", bd=0, cursor="hand2")
        staprod_btn.pack(side=TOP ,anchor="w")
        staperiod_btn = Button(menu_frame, text="Statistique-periode", command=self.staperiod, font=("Lato", 18, "normal"),bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        staperiod_btn.pack(side=TOP ,anchor="w")
        expiration_btn = Button(menu_frame, text="Péremption", command=self.expiration,font=("Lato", 18, "normal"), bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        expiration_btn.pack(side=TOP ,anchor="w")
        alerte_btn = Button(menu_frame, text="Alerte", command=self.alerte, font=("Lato", 18, "normal"), bg="#23282c",fg="#a7acb2", bd=0, cursor="hand2")
        alerte_btn.pack(side=TOP, anchor="w")
        quit_btn = Button(menu_frame, text="Quitter", font=("Lato", 18, "normal"), bg="#23282c", fg="#a7acb2", bd=0,cursor="hand2")
        quit_btn.pack(side=TOP )
# dashboard content
        self.employee_label = Label(self.root, text="Total des Employés\n1", font=("Lato", 15, "bold"), fg="white",bg="#f27b53", bd=5)
        self.employee_label.place(x=300, y=80, width=300, height=100)
        self.supplier_label = Label(self.root, text="Total des Fournisseurs\n0", font=("Lato", 15, "bold"), fg="white",bg="#dc587d", bd=5)
        self.supplier_label.place(x=650, y=80, width=300, height=100)
        self.product_label = Label(self.root, text="Total des Produits\n0", font=("Lato", 15, "bold"), fg="white",bg="#847cc5", bd=5)
        self.product_label.place(x=1000, y=80, width=300, height=100)
        self.category_label = Label(self.root, text="Total des Catégories\n0", font=("Lato", 15, "bold"), fg="white",bg="#fbb168", bd=5)
        self.category_label.place(x=300, y=200, width=300, height=100)
        self.sales_label = Label(self.root, text="Total des Ventes\n0", font=("Lato", 15, "bold"), fg="white",bg="#23ba9b", bd=5)
        self.sales_label.place(x=650, y=200, width=300, height=100)
        self.new_label = Label(self.root, text="Alertes de péremption \n0", font=("Lato", 15, "bold"), fg="white",bg="#11ba9b", bd=5)
        self.new_label.place(x=1000, y=200, width=300, height=100)
        self.update_content()

        title = Label(self.root, text="Ventes  Recents", font=("Lato", 26, "bold"), bg="white", fg="#343A40",anchor="w", padx=20)  # may add anchor here to center left
        title.place(x=300, y=350)
# Créer le cadre pour la liste des ventes
        sales_list_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_list_frame.place(x=300, y=400, width=520, height=280)
# Créer les barres de défilement verticale et horizontale
        scroll_y = Scrollbar(sales_list_frame, orient=VERTICAL)
        scroll_x = Scrollbar(sales_list_frame, orient=HORIZONTAL)
# Placer les barres de défilement dans le cadre
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
# Définir les colonnes pour la liste des ventes
        sales_list_columns = ("Nom", "Prix", "Quantité", "Date")
# Créer le tableau Treeview pour afficher les données des ventes
        self.sales_list_table = ttk.Treeview(sales_list_frame, columns=sales_list_columns,yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
# Placer le tableau dans le cadre et permettre à celui-ci de s'étendre pour remplir l'espace disponible
        self.sales_list_table.pack(fill=BOTH, expand=1)
# Configurer les barres de défilement pour contrôler le défilement du tableau
        scroll_x.config(command=self.sales_list_table.xview)
        scroll_y.config(command=self.sales_list_table.yview)
# Définir les en-têtes de colonne pour le tableau
        self.sales_list_table.heading("Nom", text="Nom")
        self.sales_list_table.heading("Prix", text="Prix")
        self.sales_list_table.heading("Quantité", text="Quantité")
        self.sales_list_table.heading("Date", text="Date")
# Afficher uniquement les en-têtes du tableau (pas les lignes vides)
        self.sales_list_table["show"] = "headings"
# Définir la largeur des colonnes du tableau
        self.sales_list_table.column("Nom", width=100)
        self.sales_list_table.column("Prix", width=100)
        self.sales_list_table.column("Quantité", width=100)
        self.sales_list_table.column("Date", width=100)
# Appeler la fonction "show_sales()" pour remplir le tableau avec les données des ventes
        self.show_sales()

################################################################################################################################

        title = Label(self.root, text="Facture Recents", font=("Lato", 26, "bold"), bg="white", fg="#343A40",anchor="w", padx=20)  # may add anchor here to center left
        title.place(x=875, y=350)
# Créer le cadre pour la liste des ventes
        sales_list_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_list_frame.place(x=875, y=400, width=420, height=280)
# Créer les barres de défilement verticale et horizontale
        scroll_y = Scrollbar(sales_list_frame, orient=VERTICAL)
        scroll_x = Scrollbar(sales_list_frame, orient=HORIZONTAL)
# Placer les barres de défilement dans le cadre
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        sales_list_columns = ("Numero du facture",)

        self.sales_list_table = ttk.Treeview(sales_list_frame, columns=sales_list_columns,yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.sales_list_table.pack(fill=BOTH, expand=1)
        scroll_x.config(command=self.sales_list_table.xview)
        scroll_y.config(command=self.sales_list_table.yview)
        self.sales_list_table.heading("Numero du facture", text="Nom du facture")
        self.sales_list_table["show"] = "headings"
        self.sales_list_table.column("Numero du facture", width=400)
        self.load_factures()

    def load_factures(self):
        # Supprimer les données existantes du tableau
        for row in self.sales_list_table.get_children():
            self.sales_list_table.delete(row)

        # Chemin du dossier contenant les factures
        facture_folder = "facture"

        # Liste des fichiers txt dans le dossier
        txt_files = glob.glob(os.path.join(facture_folder, "*.txt"))


        for file_path in txt_files:
            # Obtenir le nom du fichier sans l'extension .txt
            file_name = os.path.basename(file_path).replace(".txt", "")

            # Ajouter le nom du fichier au tableau
            self.sales_list_table.insert("", "end", values=(file_name,))

    def on_facture_click(self, event):
        # Obtenir l'élément sélectionné dans le tableau
        selected_item = self.sales_list_table.selection()

        # S'assurer qu'un élément est sélectionné
        if selected_item:
            # Obtenir le nom du fichier de la facture sélectionnée
            file_name = self.sales_list_table.item(selected_item)["values"][0]

            # Chemin complet du fichier de la facture
            file_path = os.path.join("facture", file_name + ".txt")

            # Vérifier si le fichier existe avant de l'ouvrir
            if os.path.exists(file_path):
                try:
                    # Ouvrir le fichier avec le programme par défaut associé à l'extension .txt
                    subprocess.run(["xdg-open", file_path])  # Pour les systèmes Linux
                except subprocess.CalledProcessError as e:
                    print("Erreur lors de l'ouverture du fichier :", e)
                except Exception as e:
                    print("Une erreur inattendue s'est produite :", e)
            else:
                print("Le fichier de facture n'existe pas :", file_name)
        else:
            print("Aucun élément sélectionné dans le tableau.")

    def run(self):
        self.root.mainloop()

    def employee(self):
        self.new_window = Toplevel(root)
        self.emp_manager = Employee(self.new_window)

    def supplier(self):
        self.new_window = Toplevel(root)
        self.supp_manager = Supplier(self.new_window)

    def category(self):
        self.new_window = Toplevel(root)
        self.category_manager = Category(self.new_window)

    def product(self):
        self.new_window = Toplevel(root)
        self.product_manager = Producte(self.new_window)

    def sales(self):
        self.new_window = Toplevel(root)
        self.sales_manager = Sales(self.new_window)
    def staprod(self):
        self.staprod_manager = POS()
    def staperiod(self):
        self.staperiod_manager = TOS()

    def expiration(self):
        self.new_window = Toplevel(root)
        self.expiration_manager = Expiration(self.new_window)
    def alerte(self):
        self.new_window = Toplevel(root)
        self.alerte_manager = Alerte(self.new_window)
    def note(self):
        self.new_window = Toplevel(root)
        self.note_manager = Note(self.new_window)
    def update_content(self):
        con = sqlite3.connect("Alimentation.db")
        cur = con.cursor()
        try:
            cur.execute("select COUNT(*) from listeproduit where alerte>=quantiter ")
            p = cur.fetchone()[0]
            self.employee_label.config(text=f"Stock critique\n{p}")

            cur.execute("SELECT COUNT(*) FROM supplier")
            supp = cur.fetchone()[0]
            self.supplier_label.config(text=f"Total des Fournisseurs\n{supp}")

            cur.execute("SELECT COUNT(*) FROM listeproduit")
            prd = cur.fetchone()[0]
            self.product_label.config(text=f"Total des Produits\n{prd}")

            cur.execute("SELECT COUNT(*) FROM category")
            cat = cur.fetchone()[0]
            self.category_label.config(text=f"Total des Catégories\n{cat}")

            datelimite = date.today() + timedelta(days=30)
            cur.execute(f"select COUNT(*) from listeproduit where expiration<=?", (datelimite,))
            resultats = cur.fetchone()[0]
            self.new_label.config(text=f"Alertes de péremption\n{resultats}")

            cur.execute("SELECT COUNT(*)  FROM listevente WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now');")
            jeu=cur.fetchone()[0]
            self.sales_label.config(text=f"Total des Ventes par Mois\n{jeu}")

            self.root.after(2000, self.update_content)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur: {str(ex)}", parent=root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")
    def show_sales(self):
        con = sqlite3.connect("Alimentation.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT nomproduit,prix,quantiter,date FROM listevente ORDER BY date DESC ")
            rows = cur.fetchall()
            self.sales_list_table.delete(*self.sales_list_table.get_children())
            for row in rows:
                self.sales_list_table.insert('', END, values=row)
                self.sales_list_table.bind("<ButtonRelease-1>", self.on_facture_click)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur: {str(ex)}", parent=root)

if __name__ == "__main__":
    root = Tk()
    system = StockManager(root)
    root.mainloop()
