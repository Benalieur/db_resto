from sqlalchemy import create_engine 
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.sqlite", echo=True)
base = declarative_base()

class Pays (base):

    __tablename__ = "Pays"

    pays = Column(String(255),primary_key=True)


class Restaurant (base):

    __tablename__ = "Restaurant"

    code_postal = Column(String(255), nullable=False,primary_key=True)
    pays = Column(String(255), ForeignKey('Pays.pays'))
    capacite = Column(Integer())
    espace_enfant = Column(Integer())
    service_rapide = Column(Integer())
    parking = Column(Integer, default=1)
    accessibilite = Column(Integer())


class Employee (base):

    __tablename__ = "Employee"

    id_employee = Column(Integer(),primary_key=True)
    code_postal = Column(String(200), ForeignKey('Restaurant.code_postal'))
    poste = Column(String(200),nullable=False)
    nom = Column(String(200),nullable=False)
    adresse = Column(String(200), nullable=False)
    note = Column(Integer())
    experience = Column(DateTime())


class Rib (base):

    __tablename__ = "Rib"

    id_employee = Column(Integer(),ForeignKey('Employee.id_employee'), nullable=False,primary_key=True)
    iban = Column(String(255),nullable=False)
    bic = Column(String(),nullable=False)
    propriètaire = Column(String(),nullable=False)
    adresse = Column(String(), nullable=False)


class Paie (base):

    __tablename__ = "Paie"

    id_employee = Column(Integer(),ForeignKey('Employee.id_employee'), nullable=False,primary_key=True)
    date = Column(String(),nullable=False)
    salaire_net = Column(Float(),nullable=False)


class CarteMenu (base):

    __tablename__ = "CarteMenu"

    pays = Column(Integer(),ForeignKey('Pays.pays'), nullable=False,primary_key=True)
    id_menu = Column(Integer(),ForeignKey('Menu.id_menu'),primary_key=True,nullable=False)


class Menu (base):

    __tablename__ = "Menu"

    id_menu = Column(Integer(), nullable=False,primary_key=True)
    boisson = Column(String(),ForeignKey('Item.nom_item'),nullable=False)
    plat = Column(String(),ForeignKey('Item.nom_item'),nullable=False)
    dessert = Column(String(),ForeignKey('Item.nom_item'),nullable=False)
    prix = Column(Float(),nullable=False)


class Item (base):

    __tablename__ = "Item"

    nom_item = Column(String(), nullable=False,primary_key=True)
    type = Column(String(),nullable=False)
    prix = Column(Float(),nullable=False)


class CarteItem (base):

    __tablename__ = "CarteItem"

    pays = Column(Integer(),ForeignKey('Pays.pays'), nullable=False,primary_key=True)
    id_item = Column(Integer(),ForeignKey('Item.nom_item'),primary_key=True,nullable=False)


class PanierMenu (base):

    __tablename__ = "PanierMenu"

    id_bill = Column(Integer(),ForeignKey('Bill.id_bill'), nullable=False,primary_key=True)
    id_menu = Column(Integer(),ForeignKey('Menu.id_menu'),nullable=False)
    quantité = Column(Float(),nullable=False)


class PanierItem (base):

    __tablename__ = "PanierItem"

    nom_item = Column(String(),ForeignKey('Item.nom_item'), nullable=False,primary_key=True)
    id_bill = Column(Integer(),ForeignKey('Bill.id_bill'),nullable=False)
    quantité = Column(Float(),nullable=False)


class Bill (base):

    __tablename__ = "Bill"

    id_bill = Column(Integer(),primary_key=True, nullable=False)
    code_postal = Column(String(255), ForeignKey('Restaurant.code_postal'),nullable=False)
    id_vendeur = Column(Integer(),ForeignKey('Employee.id_employee'),nullable=False)
    born = Column(Integer(),nullable=False)
    moyen_paiment = Column(String(),nullable=False)
    prix_total = Column(Float(),nullable=False)


class Recette (base):

    __tablename__ = "Recette"

    nom_item = Column(String(),ForeignKey('Item.nom_item'), nullable=False,primary_key=True)
    ingredient = Column(String(),ForeignKey('Ingredient.ingredient'),nullable=False,primary_key=True)
    quantité = Column(Integer(),nullable=False)


class Ingredient (base):

    __tablename__ = "Ingredient"

    ingredient = Column(String(),nullable=False,primary_key=True)
    prix = Column(Float(),nullable=False)


class Stock (base):

    __tablename__ = "Stock"

    ingredient = Column(String(),ForeignKey('Ingredient.ingredient'),nullable=False, primary_key=True)
    code_postal = Column(String(),ForeignKey('Restaurant.code_postal'),nullable=False, primary_key=True)
    quantité = Column(Integer())



base.metadata.create_all(engine)