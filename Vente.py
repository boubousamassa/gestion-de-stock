from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
from time import strftime
import tkinter as tk
import random
from datetime import date
import tkinter
from ttkthemes import ThemedStyle
import tempfile

class Sales:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Gestion des Ventes")
        self.root.config(bg="white")
        self.root.focus_force()
        start_color = 'bisque4'
        end_color = '#FFE5B4'
        background_frame = tk.Frame(self.root, bg='bisque4', height=200, width=400)
        background_frame.pack(fill='both', expand=True)
        canvas = tk.Canvas(background_frame, bg='bisque4', height=200, width=400)
        canvas.pack(fill='both', expand=True)
        canvas.create_rectangle(0, 0, 1400, 1200, fill=start_color, tags='gradient')
        canvas.create_rectangle(0, 0, 400, 0, fill=end_color, tags='gradient')
        title = Label(canvas, text="Enregistrement de Vente", font=("Algerian", 25, "bold"), bg="green", fg="black")
        title.pack(side=TOP, fill=X)
        style = ThemedStyle(self.root)
        style.set_theme("plastik")

# pour deplacer le contenue de l'heure par heur
        def heure():
            affi_heur = strftime("%H:%M:%S")
            affi_heure.configure(text=affi_heur)
            affi_heure.after(1000, heure)

# heure affichage
        affi_heure = Label(self.root, text="HH:MM:SS", font=("times new roman", 20, "bold"), bg="lightgray", fg="black")
        affi_heure.place(x=0, y=10, width=120, height=25)
        heure()

# les variables
        self.c_nom = StringVar()
        self.c_conta = StringVar()
        self.c_email = StringVar()
        self.v_code_barre = StringVar()
        self.v_nom = StringVar()
        self.v_spin_quantites = IntVar()
        self.rech_factu = StringVar()
        self.prixe = IntVar()  # prix des produits
        self.prixee = IntVar()
        self.qte = IntVar()
        self.produit = StringVar()
        self.totalbrit = StringVar()  # somme client
        self.taxe = StringVar()  # somme des produits
        self.totalnet = StringVar()  # resultat
        self.prix_client = IntVar()
        self.somme_produit = StringVar()
        self.date = StringVar()
        self.v_spin_quantites_sans = StringVar()
        self.v_nome = StringVar()

# puis que la facture est aleatoir
        self.n_factu = StringVar()
        z = random.randint(1000, 9999)
        self.n_factu.set(z)

# date
        self.date = date.today()

# client label
        client_Home = LabelFrame(self.root, text="client", font=("times new roman", 15), bg="white")
        client_Home.place(x=10, y=50, width=335, height=150)
        # client label
        self.affi_contact = Label(client_Home, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        self.affi_contact.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.affi_nomclient = Label(client_Home, text="Nom Client", font=("times new roman", 15, "bold"), bg="white")
        self.affi_nomclient.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.affi_email = Label(client_Home, text="E-mail", font=("times new roman", 15, "bold"), bg="white")
        self.affi_email.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        # client entry
        self.entr_nomclient = ttk.Entry(client_Home, textvariable=self.c_nom, font=("times new roman", 15))
        self.entr_nomclient.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.entr_contact = ttk.Entry(client_Home, textvariable=self.c_conta, font=("times new roman", 15))
        self.entr_contact.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.entr_email = ttk.Entry(client_Home, textvariable=self.c_email, font=("times new roman", 15))
        self.entr_email.grid(row=2, column=1, sticky=W, padx=5, pady=2)

# FRAME VENTE
        client_Home = LabelFrame(self.root, text="Produit avec Code", font=("times new roman", 20), bg="white", )
        client_Home.place(x=350, y=50, width=360, height=150)
        # Label vente
        self.code_barre = Label(client_Home, text="Code Barre", font=("times new roman", 15, "bold"), bg="white")
        self.code_barre.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.affi_nomproduit = Label(client_Home, text="Nom Produit", font=("times new roman", 15, "bold"), bg="white")
        self.affi_nomproduit.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.affi_qte = Label(client_Home, text="Quantité", font=("times new roman", 15, "bold"), bg="white")
        self.affi_qte.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        # entry vente
        self.entr_code_barre = ttk.Entry(client_Home, textvariable=self.v_code_barre, font=("times new roman", 15))
        self.entr_code_barre.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.entr_nomproduit = ttk.Entry(client_Home, font=("times new roman", 15), state="readonly")
        self.entr_nomproduit.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.entr_qte = tkinter.Spinbox(client_Home, textvariable=self.v_spin_quantites, from_=1, to=1000,font=("times new roman", 15))
        self.entr_qte.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        # mes btn vente_facture
        self.vendrecode = Button(self.root, text="Vendrer", height=2, command=self.vendreaveccode, font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.vendrecode.place(x=50, y=210)
        self.ajouterfacture = Button(self.root, text="Ajouter a la facture", height=2, command=self.ajoutercodefacture,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.ajouterfacture.place(x=240, y=210)
        self.reinitialiser = Button(self.root, text="Reinitialiser", height=2, command=self.rein,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.reinitialiser.place(x=430, y=210)

# FRAME VENTE sans code
        client_produit = LabelFrame(self.root, text="Produit sans Code", font=("times new roman", 20), bg="white", )
        client_produit.place(x=150, y=300, width=360, height=100)
        # Label vente
        self.affi_nomproduit = Label(client_produit, text="Nom Produit", font=("times new roman", 15, "bold"),bg="white")
        self.affi_nomproduit.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.affi_qte = Label(client_produit, text="Quantité", font=("times new roman", 15, "bold"), bg="white")
        self.affi_qte.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        ## entry vente
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT nomproduit FROM listeproduit WHERE codebarre='0' ORDER BY nomproduit")
        rows = cursor.fetchall()
        rows.insert(0, ("Choisir un produits"))
        self.entr_nomproduit = ttk.Combobox(client_produit, textvariable=self.v_nome, font=("times new roman", 15),state="readonly")
        self.entr_nomproduit["values"] = rows
        self.entr_nomproduit.current(0)
        self.entr_nomproduit.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.entr_qte = tkinter.Spinbox(client_produit, textvariable=self.v_spin_quantites_sans, from_=1, to=1000,font=("times new roman", 15))
        self.entr_qte.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        # BOUTON sans code
        self.vendresanscode = Button(self.root, text="Vendrer", height=2, command=self.vendresanscode,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.vendresanscode.place(x=150, y=410)
        self.ajoutersansfacture = Button(self.root, text="Ajouter a la facture", height=2, command=self.ajoufacturesanscode,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.ajoutersansfacture.place(x=340, y=410)

#creation du page en bas des resultats
        enbas_Home = LabelFrame(self.root, font=("times new roman", 15, "bold"), bg="white")
        enbas_Home.place(x=180, y=480, width=300, height=100)
        # les bouton des resultas
        self.affi_totaclient = Label(enbas_Home, text="Client", font=("times new roman", 15, "bold"), bg="white")
        self.affi_totaclient.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.affi_somme_produit = Label(enbas_Home, text="Somme", font=("times new roman", 15, "bold"), bg="white")
        self.affi_somme_produit.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.affi_totalnet = Label(enbas_Home, text="Total Net", font=("times new roman", 15, "bold"), bg="white")
        self.affi_totalnet.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.entr_prix_client = ttk.Entry(enbas_Home, font=("times new roman", 15), textvariable=self.prix_client,width=15)
        self.entr_prix_client.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.entr_somme_prod = ttk.Entry(enbas_Home, font=("times new roman", 15), textvariable=self.somme_produit,width=15, state="readonly")
        self.entr_somme_prod.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.entr_totalnet = ttk.Entry(enbas_Home, font=("times new roman", 15), textvariable=self.totalnet, width=15,state="readonly")
        self.entr_totalnet.grid(row=2, column=1, sticky=W, padx=5, pady=2)

# recherche de facture
        recher_Home = Frame(self.root, bd=3, bg="white")
        recher_Home.place(x=940, y=50, width=420, height=50)
        self.affi_recherche = Label(recher_Home, text="N Fatcture", font=("times new roman", 23, "bold"), bg="white")
        self.affi_recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.entr_recherche = ttk.Entry(recher_Home, textvariable=self.rech_factu, font=("times new roman", 23, "bold"),width=7)
        self.entr_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.btn_recherch = Button(recher_Home, text="RECHERCHE", command=self.rechercher, height=2,font=("times new roman", 12, "bold"), bg="green", width=10, cursor="hand2")
        self.btn_recherch.place(x=300, y=0)

# Espace fatcture
        Facture_label = LabelFrame(self.root, text="Factutre", font=("times new roman", 15, "bold"), bg="white")
        Facture_label.place(x=755, y=110, width=600, height=496)
        # creation du scrol barre
        scroll_y = Scrollbar(Facture_label, orient=VERTICAL)
        self.textarea = Text(Facture_label, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"),bg="white", fg="black")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        # btn Facture
        self.generer = Button(self.root, text="Générer", command=self.genererFacture, height=2,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.generer.place(x=757, y=610)
        self.sauvegarder = Button(self.root, text="Sauvegarder", height=2, command=self.sauvegarder,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.sauvegarder.place(x=960, y=610)
        self.imprimer = Button(self.root, text="Imprimer", command=self.imprimer, height=2,font=("times new roman", 15, "bold"), bg="green", width=14, cursor="hand2")
        self.imprimer.place(x=1160, y=610)
# bienvenu
        self.bienvenue()
        self.l = []

    def bienvenue(self):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "\t\tSAMASSA FACTURE")
        self.textarea.insert(END, f"\nNuméro Facture : {self.n_factu.get()}")
        self.textarea.insert(END, f"\nNom Client      : {self.c_nom.get()}")
        self.textarea.insert(END, f"\nNumero Client : {self.c_conta.get()}")
        self.textarea.insert(END, "\n********************************************************")
        self.textarea.insert(END, f"\nProduits\t\tQte\t\tPrix")
        self.textarea.insert(END, "\n********************************************************\n")



    def ajoutercodefacture(self):
        # Se connecter à la base de données
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()

        # Récupérer le code-barres saisi par l'utilisateur
        code_barre = self.v_code_barre.get()

        # Vérifier si le produit existe dans la base de données
        cursor.execute(f"SELECT nomproduit, prix FROM listeproduit WHERE codebarre = {code_barre}")
        produit_info = cursor.fetchone()

        if produit_info:
            # Récupérer le nom et le prix du produit
            nom_produit, prix_produit = produit_info

            # Mettre à jour les variables de contrôle
            self.v_nom.set(nom_produit)
            self.prixe.set(prix_produit)

            # Calculer le montant pour le produit actuel
            montant_produit = self.v_spin_quantites.get() * prix_produit

            # Ajouter le montant à la liste des montants
            self.l.append(montant_produit)

            # Afficher le produit dans le textarea
            self.textarea.insert(END, f"\n{nom_produit}\t\t{self.v_spin_quantites.get()}\t\t{prix_produit}")

            # Mettre à jour le montant total des produits et le total net
            self.somme_produit.set(str("%.0f" % (sum(self.l))))
            self.totalnet.set(str("%.0f" % ((sum(self.l) - self.prix_client.get()) * (-1))))

            # Effectuer d'autres actions liées à l'ajout du produit (non spécifiées dans le code fourni)
            self.ajouterlistevente()
            self.modifielisteventecode()
            self.ajoutgraph()
            self.rein3()

        else:
            # Le produit n'a pas été trouvé dans la base de données
            messagebox.showerror("Erreur", "Produit introuvable. Veuillez ajouter ou scanner un produit.", parent=self.root)

        # Fermer la connexion à la base de données
        connection.commit()
        connection.close()


    def ajoufacturesanscode(self):
        # Se connecter à la base de données
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        # Récupérer le nom du produit saisi par l'utilisateur
        nom_produit = self.v_nome.get()
        # Vérifier si le produit existe dans la base de données
        cursor.execute(f"SELECT nomproduit, prix FROM listeproduit WHERE nomproduit LIKE '{nom_produit}'")
        produit_info = cursor.fetchone()
        if produit_info:
            # Récupérer le nom et le prix du produit
            nom_produit, prix_produit = produit_info
            # Mettre à jour les variables de contrôle
            self.v_nom.set(nom_produit)
            self.prixe.set(prix_produit)
            # Calculer le montant pour le produit actuel
            montant_produit = self.v_spin_quantites.get() * prix_produit
            # Ajouter le montant à la liste des montants
            self.l.append(montant_produit)
            # Afficher le produit dans le textarea
            self.textarea.insert(END, f"\n{nom_produit}\t\t{self.v_spin_quantites.get()}\t\t{prix_produit}")
            # Mettre à jour le montant total des produits et le total net
            self.somme_produit.set(str("%.0f" % (sum(self.l))))
            self.totalnet.set(str("%.0f" % ((sum(self.l) - self.prix_client.get()) * (-1))))
            # Effectuer d'autres actions liées à l'ajout du produit (non spécifiées dans le code fourni)
            self.ajouterlisteventesanscode()
            self.modifierlisteventesanscode()
            self.ajoutgraphesanscode()
            self.rein2()
        else:
            # Le produit n'a pas été trouvé dans la base de données
            messagebox.showerror("Erreur", "Produit introuvable. Veuillez ajouter ou scanner un produit.",parent=self.root)
        # Fermer la connexion à la base de données
        connection.commit()
        connection.close()

    import sqlite3

    def modifielisteventecode(self):
        # Se connecter à la base de données
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        # Récupérer le code-barres saisi par l'utilisateur
        code_barre = self.v_code_barre.get()
        # Vérifier si le produit existe dans la base de données
        cursor.execute(f"SELECT codebarre FROM listeproduit WHERE codebarre = {code_barre}")
        produit_info = cursor.fetchone()
        if produit_info:
            # Récupérer la quantité du produit dans la base de données
            cursor.execute(f"SELECT quantiter FROM listeproduit WHERE codebarre = {code_barre}")
            quantite_produit = cursor.fetchone()[0]
            # Calculer la nouvelle quantité du produit après la vente
            nouvelle_quantite = quantite_produit - int(self.v_spin_quantites.get())
            # Mettre à jour la quantité du produit dans la base de données
            cursor.execute(f"UPDATE listeproduit SET quantiter = {nouvelle_quantite} WHERE codebarre = {code_barre}")
            # Enregistrer les modifications dans la base de données
            connection.commit()
        else:
            # Le produit n'a pas été trouvé dans la base de données
            print("Produit introuvable. Impossible de mettre à jour les quantités.")

        # Fermer la connexion à la base de données
        connection.close()

    def genererFacture(self):
        if self.prix_client.get() == 0:
            messagebox.showerror("Erreur", "Veuillez saisir la somme donnée par le client", parent=self.root)
            return
        else:
            # Récupérer le texte actuel du textarea
            current_text = self.textarea.get(10.0, END).strip()
            # Insérer une séparation si le textarea est déjà rempli
            if current_text:
                self.textarea.insert(END, "\n" + "*" * 56)
            # Insérer les données de la facture dans le textarea
            self.textarea.insert(END, f"\nSomme Client :\t\t{self.prix_client.get()}")
            self.textarea.insert(END, f"\nSomme produit :\t\t{self.somme_produit.get()}")
            self.totalnet.set(str("%.0f" % (((sum(self.l)) - (self.prix_client.get())) * (-1))))
            self.textarea.insert(END, f"\nTotal Net :\t\t{self.totalnet.get()}")

        # Réinitialiser les champs après la génération de la facture
        self.rein3()



    def imprimer(self):
        # Récupérer le contenu du textarea
        content = self.textarea.get("1.0", END).strip()
        # Vérifier que le contenu n'est pas vide avant de procéder à l'impression
        if content:
            # Créer un fichier temporaire pour stocker le contenu
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
                temp_file.write(content.encode("utf-8"))
                # Fermer le fichier temporaire pour s'assurer qu'il est bien écrit avant de l'imprimer
                temp_file.close()
                try:
                    # Ouvrir le fichier avec le programme par défaut associé à l'extension .txt et l'imprimer
                    os.startfile(temp_file.name, "print")
                except Exception as e:
                    print("Erreur lors de l'impression :", e)
        else:
            print("Le contenu est vide, rien à imprimer.")


    def sauvegarder(self):
        op = messagebox.askyesno("Sauvegarder", "Voulez-vous sauvegarder la facture?", parent=self.root)
        if op:
            donnee_facture = self.textarea.get("1.0", END)
            nom_fichier = f"facture{self.n_factu.get()}.txt"
            try:
                with open(nom_fichier, "w") as fichier:
                    fichier.write(donnee_facture)
                messagebox.showinfo("Sauvegarder",f"La facture numéro {self.n_factu.get()} a été enregistrée avec succès.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la sauvegarde :\n{e}", parent=self.root)


    def rechercher(self):
        trouver = False
        numero_facture = self.rech_factu.get()
        for nom_fichier in os.listdir("facture"):
            if nom_fichier.split(".")[0] == numero_facture:
                try:
                    with open(f"facture/{nom_fichier}", "r") as f1:
                        contenu_facture = f1.read()
                        self.textarea.delete("1.0", END)
                        self.textarea.insert("1.0", contenu_facture)
                    trouver = True
                except Exception as e:
                    messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la lecture de la facture :\n{e}", parent=self.root)
                break

        if not trouver:
            messagebox.showerror("Erreur", "La facture n'existe pas.", parent=self.root)

    def rein(self):
        self.c_nom.set("")
        self.c_conta.set("")
        self.c_email.set("")
        self.v_code_barre.set("")
        self.v_nom.set("")
        self.v_spin_quantites.set(1)

    def rein2(self):
        self.v_nome.set("Choisire")
        self.v_spin_quantites.set(1)

    def rein3(self):
        self.v_code_barre.set("")
        self.v_spin_quantites.set(1)

    def ajouterlistevente(self):
        try:
            connection = sqlite3.connect("Alimentation.db")
            cursor = connection.cursor()
            insertion = (self.v_code_barre.get(), self.v_nom.get(), self.prixe.get(), self.v_spin_quantites.get(), self.date)
            cursor.execute("INSERT INTO listevente VALUES (?,?,?,?,?)", (insertion))
            connection.commit()
        except Exception as e:
            print("[ERREUR]", e)

    def ajouterlisteventesanscode(self):
        try:
            connection = sqlite3.connect("Alimentation.db")
            cursore = connection.cursor()
            cursore.execute(f"SELECT codebarre FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
            rowsee = cursore.fetchone()
            cursoree = connection.cursor()
            cursoree.execute(f"SELECT prix FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
            rowseee = cursoree.fetchone()
            cursor = connection.cursor()
            insertion = (rowsee[0], self.v_nome.get(), rowseee[0], self.v_spin_quantites_sans.get(), self.date)
            cursor.execute("INSERT INTO listevente VALUES (?,?,?,?,?)", (insertion))
            connection.commit()
        except Exception as e:
            print("[ERREUR]", e)

    def ajoutgraph(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        insertion = (self.v_code_barre.get(), self.v_nom.get(), self.v_spin_quantites.get())
        cursor.execute("INSERT INTO graphedevente VALUES (?,?,?)", (insertion))
        connection.commit()

    def ajoutgraphesanscode(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT codebarre FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
        rowsee = cursor.fetchone()
        insertion = (rowsee[0], self.v_nome.get(), self.v_spin_quantites_sans.get())
        cursore = connection.cursor()
        cursore.execute("INSERT INTO graphedevente VALUES (?,?,?)", (insertion))
        connection.commit()

    def vendreaveccode(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT codebarre FROM listeproduit")
        rows = cursor.fetchall()
        for row in rows:
            if str(row[0]) == str(self.v_code_barre.get()):
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute(f"SELECT nomproduit FROM listeproduit where codebarre={self.v_code_barre.get()}")
                rowsee = cursor.fetchone()
                self.v_nom.set(rowsee[0])
                break
        cursore = connection.cursor()
        cursore.execute("SELECT codebarre FROM listeproduit")
        rows = cursore.fetchall()
        for row in rows:
            if str(row[0]) == str(self.v_code_barre.get()):
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute(f"SELECT prix FROM listeproduit where codebarre={self.v_code_barre.get()}")
                rowsee = cursor.fetchone()
                self.prixe.set(rowsee[0])
                break
        self.n = self.prixe.get()
        self.m = self.v_spin_quantites.get() * self.n
        self.l.append(self.m)
        if self.v_nom.get() == "":
            messagebox.showerror("Erreur", "Ajouter  ou scanner un produit ", parent=self.root)
        else:
            self.somme_produit.set(str("%.0f" % (sum(self.l))))
            self.totalnet.set(str("%.0f" % ((sum(self.l) - (self.prix_client.get())) * (-1))))
            self.ajouterlistevente()
            self.modifielisteventecode()
            self.ajoutgraph()
            self.rein3()
        connection.commit()
        connection.close()

    def vendresanscode(self):
        connection = sqlite3.connect("Alimentation.db")
        cursore = connection.cursor()
        cursore.execute("SELECT nomproduit FROM listeproduit")
        rows = cursore.fetchall()
        for row in rows:
            if str(row[0]) == str(self.v_nome.get()):
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute(f"SELECT prix FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
                rowsee = cursor.fetchone()
                self.prixe.set(rowsee[0])
                break
        self.n = self.prixe.get()
        self.m = self.v_spin_quantites.get() * self.n
        self.l.append(self.m)
        if self.v_nome.get() == "":
            messagebox.showerror("Erreur", "Ajouter  ou scanner un produit ", parent=self.root)
        else:
            self.somme_produit.set(str("%.0f" % (sum(self.l))))
            self.totalnet.set(str("%.0f" % ((sum(self.l) - (self.prix_client.get())) * (-1))))
            self.ajouterlisteventesanscode()
            self.modifierlisteventesanscode()
            self.ajoutgraphesanscode()
            self.rein2()
        connection.commit()
        connection.close()

    def modifierlisteventesanscode(self):
        connection = sqlite3.connect("Alimentation.db")
        cursor = connection.cursor()
        cursor.execute("SELECT nomproduit FROM listeproduit")
        rows = cursor.fetchall()
        for row in rows:
            if str(row[0]) == self.v_nome.get():
                connection = sqlite3.connect("Alimentation.db")
                cursor = connection.cursor()
                cursor.execute(f"SELECT quantiter FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
                rowse = cursor.fetchone()
                self.quantiter_recupere = str(int(rowse[0]) - int(self.v_spin_quantites_sans.get()))
                cursor.execute(f"SELECT prix FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
                self.prix_recupere = cursor.fetchone()
                cursor.execute(f"SELECT codebarre FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
                self.code_recupere = cursor.fetchone()
                cursor.execute(f"SELECT date FROM listeproduit where nomproduit LIKE '{str(self.v_nome.get())}'")
                self.date_recupere = cursor.fetchone()
                self.recupere = (
                    str(self.code_recupere), str(self.prix_recupere), str(self.quantiter_recupere),
                    str(self.date_recupere))
                cursor.execute(
                    f"UPDATE listeproduit set codebarre=?,prix=?,quantiter=?,date=? where nomproduit LIKE '{str(self.v_nome.get())}' ",
                    (str(self.code_recupere[0]), str(self.prix_recupere[0]), str(self.quantiter_recupere),
                     str(self.date_recupere[0])))
                connection.commit()
                break
        connection.commit()
        connection.close()


if __name__ == "__main__":
    root = Tk()
    system = Sales(root)
    root.mainloop()
