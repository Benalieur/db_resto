from sqlalchemy import create_engine 
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.sqlite", echo=True)
base = declarative_base()

class Pays (base):

    __tablename__ = "Pays"

    pays = Column(String(255),primary_key=True)

    def __init__(self, pays):
        self.pays = pays


class Restaurant (base):

    __tablename__ = "Restaurant"

    code_postal = Column(String(255), nullable=False,primary_key=True)
    pays = Column(String(255), ForeignKey('Pays.pays'))
    capacite = Column(Integer())
    espace_enfant = Column(Integer())
    service_rapide = Column(Integer())
    parking = Column(Integer, default=1)
    accessibilite = Column(Integer())

    def __init__(self, code_postal, pays, capacite, espace_enfant, service_rapide, parking, accessibilite):
        self.code_postal = code_postal
        self.pays = pays
        self.capacite = capacite
        self.espace_enfant = espace_enfant
        self.service_rapide = service_rapide
        self.parking = parking
        self.accessibilite = accessibilite


class Employee (base):

    __tablename__ = "Employee"

    id_employee = Column(Integer(),primary_key=True)
    code_postal = Column(String(200), ForeignKey('Restaurant.code_postal'))
    poste = Column(String(200),nullable=False)
    nom = Column(String(200),nullable=False)
    adresse = Column(String(200), nullable=False)
    note = Column(Integer())

    def __init__(self, id_employee, code_postal, poste, nom, adresse, note):
        self.id_employee = id_employee
        self.code_postal = code_postal
        self.poste = poste
        self.nom = nom
        self.adresse = adresse
        self.note = note


class Rib (base):

    __tablename__ = "Rib"

    id_employee = Column(Integer(),ForeignKey('Employee.id_employee'), nullable=False,primary_key=True)
    iban = Column(String(255),nullable=False)
    bic = Column(String(),nullable=False)
    propriètaire = Column(String(),nullable=False)
    adresse = Column(String(), nullable=False)

    def __init__(self, id_employee, iban, bic, propriètaire, adresse):
        self.id_employee = id_employee
        self.iban = iban
        self.bic = bic
        self.propriètaire = propriètaire
        self.adresse = adresse


class Paie (base):

    __tablename__ = "Paie"

    id_employee = Column(Integer(),ForeignKey('Employee.id_employee'), nullable=False,primary_key=True)
    date = Column(String(),nullable=False)
    salaire_net = Column(Float(),nullable=False)

    def __init__(self, id_employee, date, salaire_net):
        self.id_employee = id_employee
        self.date = date
        self.salaire_net = salaire_net


class CarteMenu (base):

    __tablename__ = "CarteMenu"

    pays = Column(Integer(),ForeignKey('Pays.pays'), nullable=False,primary_key=True)
    id_menu = Column(Integer(),ForeignKey('Menu.id_menu'),primary_key=True,nullable=False)
    salaire_net = Column(Float(),nullable=False)

    def __init__(self, pays, id_menu, salaire_net):
        self.pays = pays
        self.id_menu = id_menu
        self.salaire_net = salaire_net


class Menu (base):

    __tablename__ = "Menu"

    id_menu = Column(Integer(), nullable=False,primary_key=True)
    boisson = Column(String(),ForeignKey('Item.nom_item'),nullable=False)
    plat = Column(String(),ForeignKey('Item.nom_item'),nullable=False)
    dessert = Column(String(),ForeignKey('Item.nom_item'),nullable=False)
    prix = Column(Float(),nullable=False)

    def __init__(self, id_menu, boisson, plat, dessert, prix):
        self.id_menu = id_menu
        self.boisson = boisson
        self.plat = plat
        self.dessert = dessert
        self.prix = prix


class Item (base):

    __tablename__ = "Item"

    nom_item = Column(String(), nullable=False,primary_key=True)
    type = Column(String(),nullable=False)
    prix = Column(Float(),nullable=False)

    def __init__(self, nom_item, type, prix):
        self.nom_item = nom_item
        self.type = type
        self.prix = prix

class CarteItem (base):

    __tablename__ = "CarteItem"

    pays = Column(Integer(),ForeignKey('Pays.pays'), nullable=False,primary_key=True)
    id_item = Column(Integer(),ForeignKey('Item.nom_item'),primary_key=True,nullable=False)

    def __init__(self, pays, id_item):
        self.pays = pays
        self.id_item = id_item


class PanierMenu (base):

    __tablename__ = "PanierMenu"

    id_bill = Column(Integer(),ForeignKey('Bill.id_bill'), nullable=False,primary_key=True)
    id_menu = Column(Integer(),ForeignKey('Menu.id_menu'),nullable=False)
    quantité = Column(Float(),nullable=False)

    def __init__(self, id_bill, id_menu, quantité):
        self.id_bill = id_bill
        self.id_menu = id_menu
        self.quantité = quantité

class PanierItem (base):

    __tablename__ = "PanierItem"

    nom_item = Column(String(),ForeignKey('Item.nom_item'), nullable=False,primary_key=True)
    id_bill = Column(Integer(),ForeignKey('Bill.id_bill'),nullable=False)
    quantité = Column(Float(),nullable=False)

    def __init__(self, nom_item, id_bill, quantité):
        self.nom_item = nom_item
        self.id_bill = id_bill
        self.quantité = quantité


class Bill (base):

    __tablename__ = "Bill"

    id_bill = Column(Integer(),primary_key=True, nullable=False)
    code_postal = Column(String(255), ForeignKey('Restaurant.code_postal'),nullable=False)
    id_vendeur = Column(Integer(),ForeignKey('Employee.id_employee'),nullable=False)
    born = Column(Integer(),nullable=False)
    moyen_paiment = Column(String(),nullable=False)
    prix_total = Column(Float(),nullable=False)

    def __init__(self, id_bill, code_postal, id_vendeur, born, moyen_paiment, prix_total):
        self.code_postal = id_bill
        self.code_postal = code_postal
        self.id_vendeur = id_vendeur
        self.born = born
        self.moyen_paiment = moyen_paiment
        self.prix_total = prix_total


class Recette (base):

    __tablename__ = "Recette"

    nom_item = Column(String(),ForeignKey('Item.nom_item'), nullable=False,primary_key=True)
    nom_ingredient = Column(String(),ForeignKey('Ingredient.nom_ingredient'),nullable=False,primary_key=True)
    quantité = Column(Integer(),nullable=False)

    def __init__(self, nom_item, nom_ingredient, quantité):
        self.nom_item = nom_item
        self.nom_ingredient = nom_ingredient
        self.quantité = quantité


class Ingredient (base):

    __tablename__ = "Ingredient"

    nom_ingredient = Column(String(),nullable=False,primary_key=True)
    cout = Column(Float(),nullable=False)

    def __init__(self, nom_ingredient, cout):
        self.nom_ingredient = nom_ingredient
        self.cout = cout


class Stock (base):

    __tablename__ = "Stock"

    nom_ingredient = Column(String(),ForeignKey('Ingredient.nom_ingredient'),nullable=False)
    code_postal = Column(String(),ForeignKey('Restaurant.code_postal'),nullable=False, primary_key=True)
    quantité = Column(Integer())

    def __init__(self, nom_ingredient, code_postal, quantité):
        self.nom_ingredient = nom_ingredient
        self.code_postal = code_postal
        self.quantité = quantité










base.metadata.create_all(engine)
