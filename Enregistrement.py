from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import tkinter as tk
import datetime
from datetime import date,timedelta
import tkinter
from ttkthemes import ThemedStyle

class Producte:
    def __init__(self, root_win):
        root = root_win
        root.geometry("1350x700+0+0")
        root.title("Gestion des Produits")
        root.config(bg="white")
        root.focus_force()
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
        title = Label(canvas, text="Enregistrement des produits", font=("Algerian", 27, "bold"), bg="green",fg="black")
        title.pack(side=TOP, fill=X)
        # Ajout des widgets de la deuxième page
        label = tk.Label(root, text="ENREGISTREMENT")
        label.pack(pady=10)

# les variables
        self.icode_barre = StringVar()
        self.id_Nom_prod = StringVar()
        self.id_Prix_Produit = StringVar()
        self.quantites = StringVar()
        self.recherche = StringVar()
        self.com_m_produit = StringVar()
        self.com_m_perso = StringVar()
        self.chan_categorie=StringVar()
        self.combo_category=StringVar()
        self.spin_nombre = StringVar()
        self.categorie=StringVar()
        self.ichan_code_barre = StringVar()
        self.quantiter_recupere = StringVar()
        self.nom_recupere = StringVar()
        self.prix_recupere = StringVar()
        self.expitation = StringVar()
        self.alerte = StringVar()
        self.rech_factu = StringVar()
        self.recherch_par = StringVar()
        self.date = date.today()
        self.chan_mofi_categorie=StringVar()
# produit
        produit_Home = LabelFrame(root, text="Produit", font=("times new roman", 20), bg="lightgray")
        produit_Home.place(x=10, y=50, width=700, height=270)
        # produit affi
        self.affi__code_barre = Label(produit_Home, text="Code Barre", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi__code_barre.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.affi__nom_prod = Label(produit_Home, text="Nom Produit", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi__nom_prod.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.affi__expiration = Label(produit_Home, text="Expiration", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi__expiration.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.affi__prix = Label(produit_Home, text="Prix", font=("times new roman", 17, "bold"), bg="lightgray")
        self.affi__prix.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        self.affi__qte = Label(produit_Home, text="Quantité", font=("times new roman", 17, "bold"), bg="lightgray")
        self.affi__qte.grid(row=1, column=3, sticky=W, padx=5, pady=2)
        self.affi__alerte = Label(produit_Home, text="Alerte", font=("times new roman", 17, "bold"), bg="lightgray")
        self.affi__alerte.grid(row=2, column=3, sticky=W, padx=5, pady=2)
        self.affi_ = Label(produit_Home, text="", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi_.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        self.affi_categorie = Label(produit_Home, text="Categorie", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi_categorie.grid(row=3, column=1, sticky=W, padx=5, pady=2)
# produit entre
        self.entre_code_barre = ttk.Entry(produit_Home, textvariable=self.icode_barre, font=("times new roman", 15))
        self.entre_code_barre.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.entre_nom_prod = ttk.Entry(produit_Home, textvariable=self.id_Nom_prod, font=("times new roman", 15))
        self.entre_nom_prod.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.entre_expiration = ttk.Entry(produit_Home, textvariable=self.expitation, font=("times new roman", 15))
        self.entre_expiration.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.entre_prix = ttk.Entry(produit_Home, textvariable=self.id_Prix_Produit, font=("times new roman", 15))
        self.entre_prix.grid(row=0, column=4, sticky=W, padx=5, pady=2)
        self.entre_qte = ttk.Entry(produit_Home, textvariable=self.quantites, font=("times new roman", 15))
        self.entre_qte.grid(row=1, column=4, sticky=W, padx=5, pady=2)
        self.entre_alerte = ttk.Entry(produit_Home, textvariable=self.alerte, font=("times new roman", 15))
        self.entre_alerte.grid(row=2, column=4, sticky=W, padx=5, pady=2)
        #connection a la bd
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM category ORDER BY name")
        rowsee = cursor.fetchall()
        rowsee.insert(0, ("Category"))
        self.entre_categorie = ttk.Combobox(produit_Home, textvariable=self.categorie,font=("times new roman", 15), state="readonly")
        self.entre_categorie["values"] = rowsee
        self.entre_categorie.current(0)
        self.entre_categorie.place(x=285, y=110)
        # Button enregistre
        btn_enregistre = Button(produit_Home, text="ENREGISTRER", command=self.enregistre, font=("times new roman", 15), bd=10,relief=GROOVE, bg="green")
        btn_enregistre.place(x=100, y=160)
        # Button modifier
        btn_modifier = Button(produit_Home, text="ENREGISTRER LA MODIFICATION", command=self.modifier,font=("times new roman", 15), bd=10, relief=GROOVE, bg="green")
        btn_modifier.place(x=300, y=160)
# recherche
        recher_Home = Frame(root, bd=3, bg="white")
        recher_Home.place(x=740, y=50, width=570, height=55)
        self.recherche = ttk.Combobox(recher_Home, textvariable=self.recherch_par, font=("times new roman", 15),width=10, state="readonly")
        self.recherche["values"] = ("Par Code", "Par Nom")
        self.recherche.current(0)
        self.recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.entr_recherche = ttk.Entry(recher_Home, textvariable=self.rech_factu, font=("times new roman", 23, "bold"),width=7)
        self.entr_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.btn_recherch = Button(recher_Home, text="RECHERCHE", command=self.rechercher_enregistrement, height=2,font=("times new roman", 12, "bold"), bg="green", width=10, cursor="hand2")
        self.btn_recherch.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.btn_afficher = Button(recher_Home, text="TOUT AFFICHER", command=self.afficher, height=2,font=("times new roman", 12, "bold"), bg="green", width=15, cursor="hand2")
        self.btn_afficher.grid(row=0, column=3, sticky=W, padx=5, pady=2)
# Affichage du tableau
        result_Home = Frame(root, bd=5, relief=GROOVE, bg="gray")
        result_Home.place(x=730, y=128, width=636, height=530)
        # tableau
        scroll_x = Scrollbar(result_Home, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Home, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_Home, columns=("codebarre","nom_produit", "prix_unit", "quantites_dispo", "date","expiration","alerte","categorie"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.tabl_resul.pack(fill=BOTH, expand=1)
        scroll_x.config(command=self.tabl_resul.xview)
        scroll_y.config(command=self.tabl_resul.yview)
        # l'entete
        self.tabl_resul.heading("codebarre", text="Code barre")
        self.tabl_resul.heading("nom_produit", text="Nom Produit")
        self.tabl_resul.heading("prix_unit", text="Prix Unit")
        self.tabl_resul.heading("quantites_dispo", text="Quantités Dispo")
        self.tabl_resul.heading("date", text="Date d'enregistrement")
        self.tabl_resul.heading("expiration", text="Expiration")
        self.tabl_resul.heading("alerte", text="alerte")
        self.tabl_resul.heading("categorie", text="categorie")
        # afficher les elements dans l'entete
        self.tabl_resul["show"] = "headings"
        # la taille de chaque colone
        self.tabl_resul.column("codebarre", width=110)
        self.tabl_resul.column("nom_produit", width=145)
        self.tabl_resul.column("prix_unit", width=145)
        self.tabl_resul.column("quantites_dispo", width=145)
        self.tabl_resul.column("date", width=145)
        self.tabl_resul.column("expiration", width=145)
        self.tabl_resul.column("alerte", width=145)
        self.tabl_resul.column("categorie", width=145)
        self.tabl_resul.pack()
        self.tabl_resul.bind("<ButtonRelease-1>", self.information)
        # connection a la bd pour afficher les elements dans le tableau
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        selection = cursor.execute("SELECT codebarre, nomproduit,prix,quantiter,date,expiration,alerte,categorie FROM listeproduit")
        for row in selection:
            self.tabl_resul.insert('', END, values=row)

# categorie
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM category ORDER BY name")
        rows = cursor.fetchall()
        rows.insert(0, ("Category"))
        #afficher
        categorie_Home = LabelFrame(root, text="Categorie", font=("times new roman", 20), bg="lightgray")
        categorie_Home.place(x=10, y=326, width=700, height=120)
        self.affi_cree = Label(categorie_Home, text="Cree", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi_cree.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.affi_cree = Label(categorie_Home, text="Modifier", font=("times new roman", 17, "bold"), bg="lightgray")
        self.affi_cree.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.combo_categorie = ttk.Combobox(categorie_Home, textvariable=self.combo_category,font=("times new roman", 15), state="readonly")
        self.combo_categorie["values"] = rows
        self.combo_categorie.current(0)
        self.combo_categorie.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        #Entrer
        self.entry_cree = ttk.Entry(categorie_Home, textvariable=self.chan_categorie, font=("times new roman", 17, "bold"))
        self.entry_cree.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.enntry_combo_category = ttk.Entry(categorie_Home,textvariable=self.chan_mofi_categorie,font=("times new roman", 17, "bold"))
        self.enntry_combo_category.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        #boutton
        btn_categorie_combo = Button(categorie_Home, text="Modifier",command=self.modi_categorie,font=("times new roman", 10), bd=10, relief=GROOVE, bg="green")
        btn_categorie_combo.grid(row=1, column=3, sticky=W, padx=5, pady=2)
        btn_categorie_ajouter = Button(categorie_Home, text="Ajouter", command=self.ajou_categorie,font=("times new roman", 10), bd=10, relief=GROOVE, bg="green")
        btn_categorie_ajouter.grid(row=0, column=2, sticky=W, padx=5, pady=2)

#changement
        changement_Home = LabelFrame(root, text="Transfert", font=("times new roman", 20), bg="lightgray")
        changement_Home.place(x=10, y=453, width=700, height=200)
        # changement label
        self.affi_chan_produit = Label(changement_Home, text="Code", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi_chan_produit.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.affi_chan_espace = Label(changement_Home, text="", font=("times new roman", 17, "bold"), bg="lightgray")
        self.affi_chan_espace.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.affi_chan_num_alimentation = Label(changement_Home, text="Quantité", font=("times new roman", 17, "bold"),bg="lightgray")
        self.affi_chan_num_alimentation.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.affi_chan_boutique = Label(changement_Home, text="Boutique N=", font=("times new roman", 15, "bold"),bg="lightgray")
        self.affi_chan_boutique.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        # changement entry
        self.entre_chan_code_barre = ttk.Entry(changement_Home, textvariable=self.ichan_code_barre,font=("times new roman", 15))
        self.entre_chan_code_barre.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.entre_chan_ch_nombre = tkinter.Spinbox(changement_Home, textvariable=self.spin_nombre, from_=0, to=500,font=("times new roman", 15))
        self.entre_chan_ch_nombre.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.entre_chan_num_alimentation = ttk.Combobox(changement_Home, textvariable=self.com_m_perso,font=("times new roman", 15), state="readonly")
        self.entre_chan_num_alimentation["values"] = ("Alimentation", "Alimentation 1", "Alimentation 2", "Alimentation 3")
        self.entre_chan_num_alimentation.current(0)
        self.entre_chan_num_alimentation.grid(row=1, column=3, sticky=W, padx=5, pady=2)
        # changement boutton
        btn_ajouter = Button(changement_Home, text="Ajouter", font=("times new roman", 15), command=self.changeajouter, bd=10,relief=GROOVE, bg="green")
        btn_ajouter.place(x=230, y=110)
        btn_retire = Button(changement_Home, text="Retirer", font=("times new roman", 15), command=self.changeretire, bd=10,relief=GROOVE, bg="green")
        btn_retire.place(x=350, y=110)
#############################################################################################################################################################################
    def modi_categorie(self):
        # Se connecter à la base de données
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        # Utiliser un paramètre lié pour éviter l'injection SQL lors de la sélection de la catégorie
        categorie = self.combo_category.get()
        cursor.execute("SELECT name FROM category WHERE name=?", (categorie,))
        self.categorie_recupere = cursor.fetchone()
        # Assure-toi que la valeur a été trouvée avant de l'utiliser
        if self.categorie_recupere:
            # Utiliser un paramètre lié pour éviter l'injection SQL lors de la mise à jour
            cursor.execute(f"UPDATE category set name=? where name LIKE '{str(categorie)}'",(self.chan_mofi_categorie.get(),))
            connection.commit()
            messagebox.showinfo("Succés", "Modification Effectué", parent=root)
        else:
            # Gérer le cas où aucune valeur n'a été trouvée
            self.chan_mofi_categorie.set("Valeur non trouvée")
        # Enregistre les modifications dans la base de données et ferme la connexion
        connection.commit()
        connection.close()

    def ajou_categorie(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO category VALUES (?)",(self.chan_categorie.get(),))
        connection.commit()
        connection.close()

    def enregistre(self):
        user_input_debut = self.expitation.get()
        try:
            # date1= parse(user_input_debut)
            date1 = datetime.datetime.strptime(user_input_debut, "%d/%m/%Y").date()
            connection = sqlite3.connect("Alimentation.db")
            jour_restant = date1 - self.date
            restant = jour_restant.days
            # jour_restant=date1-self.date
            cursor = connection.cursor()
            insertion = (self.icode_barre.get(), self.id_Nom_prod.get(), self.id_Prix_Produit.get(), self.quantites.get(), self.date,date1, self.alerte.get(), self.categorie.get())
            cursor.execute("INSERT INTO listeproduit VALUES (?,?,?,?,?,?,?,?)", (insertion))
            connection.commit()
            self.afficherRechertat()
            self.rein_enregistrement()
        except Exception as e:
            print("[ERREUR]", e)

    def afficherRechertat(self):
        connection = sqlite3.connect("Alimentation.db")
        cur = connection.cursor()
        cur.execute("select * from listeproduit ORDER BY nomproduit ")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("", END, values=row)
        connection.commit()
        connection.close()

    def modifier(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        insertion = (self.id_Nom_prod.get(), self.id_Prix_Produit.get(), self.quantites.get(), self.date,self.expitation.get(),self.alerte.get(),self.categorie.get())
        cursor.execute(f"UPDATE listeproduit set nomproduit=?,prix=?,quantiter=?,date=?,expiration=?,alerte=?,categorie=? where codebarre={self.icode_barre.get()} ",(insertion))
        connection.commit()
        messagebox.showinfo("Succés", "Modification Effectué", parent=root)
        self.afficherRechertat()
        self.rein_enregistrement()
        connection.close()

    def information(self, ev):
        cursors_row = self.tabl_resul.focus()
        contents = self.tabl_resul.item(cursors_row)
        row = contents["values"]
        self.icode_barre.set(row[0])
        self.id_Nom_prod.set(row[1])
        self.id_Prix_Produit.set(row[2])
        self.quantites.set(row[3])
        self.expitation.set(row[5])
        self.alerte.set(row[6])
        self.categorie.set(row[7])

    def changeajouter(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT codebarre FROM listeproduit")
        rows = cursor.fetchall()
        for row in rows:
            if str(row[0]) == self.ichan_code_barre.get():
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute(f"SELECT quantiter FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                rowse = cursor.fetchone()
                self.quantiter_recupere = str(int(rowse[0]) + int(self.spin_nombre.get()))
                cursor.execute(f"SELECT prix FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.prix_recupere = cursor.fetchone()
                cursor.execute(f"SELECT nomproduit FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.nom_recupere = cursor.fetchone()
                cursor.execute(f"SELECT expiration FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.expiration_recupere = cursor.fetchone()
                cursor.execute(f"SELECT alerte FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.alerte_recupere = cursor.fetchone()
                self.recupere = (str(self.nom_recupere), str(self.prix_recupere), str(self.quantiter_recupere), str(self.date),str(self.expiration_recupere),str(self.alerte_recupere))
                cursor.execute(f"UPDATE listeproduit set nomproduit=?,prix=?,quantiter=?,date=?,expiration=?,alerte=? where codebarre={self.ichan_code_barre.get()} ",(str(self.nom_recupere[0]), str(self.prix_recupere[0]), str(self.quantiter_recupere),str(self.date),str(self.expiration_recupere[0]),str(self.alerte_recupere[0])))
                connection.commit()
                self.afficherRechertat()
                break
        connection.commit()
        connection.close()

    def changeretire(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT codebarre FROM listeproduit")
        rows = cursor.fetchall()
        for row in rows:
            if str(row[0]) == self.ichan_code_barre.get():
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute(f"SELECT quantiter FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                rowse = cursor.fetchone()
                self.quantiter_recupere = str(int(rowse[0]) - int(self.spin_nombre.get()))
                cursor.execute(f"SELECT prix FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.prix_recupere = cursor.fetchone()
                cursor.execute(f"SELECT nomproduit FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.nom_recupere = cursor.fetchone()
                cursor.execute(f"SELECT expiration FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.expiration_recupere = cursor.fetchone()
                cursor.execute(f"SELECT alerte FROM listeproduit where codebarre={self.ichan_code_barre.get()}")
                self.alerte_recupere = cursor.fetchone()
                self.recupere = (str(self.nom_recupere), str(self.prix_recupere), str(self.quantiter_recupere), str(self.date),str(self.expiration_recupere),str(self.alerte_recupere))
                cursor.execute(f"UPDATE listeproduit set nomproduit=?,prix=?,quantiter=?,date=? where codebarre={self.ichan_code_barre.get()} ",(str(self.nom_recupere[0]), str(self.prix_recupere[0]), str(self.quantiter_recupere),str(self.date),str(self.expiration_recupere[0]),str(self.alerte_recupere[0])))
                connection.commit()
                self.afficherRechertat()
                break
        connection.commit()
        connection.close()

    def rein_enregistrement(self):
        self.icode_barre.set("")
        self.id_Nom_prod.set("")
        self.expitation.set("")
        self.id_Prix_Produit.set("")
        self.quantites.set("")
        self.alerte.set("")
        self.categorie.set("Categorie")

    def rechercher_enregistrement(self):
        if self.recherch_par.get() == "Par Code":
            connection = sqlite3.connect("Alimentation.db")
            cur = connection.cursor()
            cur.execute(f"select * from listeproduit where codebarre LIKE '{str(self.rech_factu.get())}'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.tabl_resul.delete(*self.tabl_resul.get_children())
                for row in rows:
                    self.tabl_resul.insert("", END, values=row)
            connection.commit()
            connection.close()
        if self.recherch_par.get() == "Par Nom":
            connection = sqlite3.connect("Alimentation.db")
            cur = connection.cursor()
            cur.execute(f"select * from listeproduit where nomproduit LIKE '{str(self.rech_factu.get())}'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.tabl_resul.delete(*self.tabl_resul.get_children())
                for row in rows:
                    self.tabl_resul.insert("", END, values=row)
            connection.commit()
            connection.close()

    def afficher(self):
        connection = sqlite3.connect("Alimentation.db")
        cur = connection.cursor()
        cur.execute("select * from listeproduit ORDER BY nomproduit")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("", END, values=row)
        connection.commit()
        connection.close()



if __name__ == "__main__":
    root = Tk()
    system = Producte(root)
    root.mainloop()
