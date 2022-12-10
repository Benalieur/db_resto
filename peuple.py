# CRÉATION D'UNE BASE DE DONNÉES ALÉATOIRE SUR LES RESTAURANTS

import pandas as pd
import random as rd

from db import create_db

create_db()

from db import engine

## RESTAURANTS

df_resto = pd.read_csv("csv/data_resto.csv")

df_resto["espace_enfant"] = df_resto["espace_enfant"].apply(lambda x: 1 if x == "Yes" else x)
df_resto["espace_enfant"] = df_resto["espace_enfant"].apply(lambda x: 0 if x == "No" else x)

df_resto["service_rapide"] = df_resto["service_rapide"].apply(lambda x: 1 if x == "Yes" else x)
df_resto["service_rapide"] = df_resto["service_rapide"].apply(lambda x: 0 if x == "No" else x)

df_resto["parking"] = df_resto["parking"].apply(lambda x: 1 if x == "Yes" else x)
df_resto["parking"] = df_resto["parking"].apply(lambda x: 0 if x == "No" else x)

df_resto["accessibilite"] = df_resto["accessibilite"].apply(lambda x: 1 if x == "Yes" else x)
df_resto["accessibilite"] = df_resto["accessibilite"].apply(lambda x: 0 if x == "No" else x)


## EMPLOYÉS
##### Création de la liste des employés.

code_postal = df_resto["code_postal"].unique()

df_employes = pd.read_csv("csv/data_employes.csv")

df_employes['id_employee'] = df_employes.index
df_employes['code_postal'] = ''

df_employes['code_postal'] = df_employes['code_postal'].apply(lambda x : code_postal[rd.randint(0, len(code_postal)-1)])
del df_employes['telephone']
del df_employes['email']


## PAYS

list_pays_block = [df_resto["pays"].unique()]
list_pays = df_resto["pays"].unique()

df_pays = pd.DataFrame()

for pays in range(len(list_pays_block)):
    df_pays["pays"] = list_pays_block[pays]
    

## INGRÉDIENTS
#Ingrédients pour les plats

df_ingredient_plat = pd.DataFrame({
    "ingredient": ["pain", "steak", "nugguet", "fish", "salade", "tomate", "cornichon", "s_mayo", "s_ketchup", "s_barbecue", "fromage"], 
    "prix": [0.49, 0.99, 1.19, 1.49, 0.29, 0.29, 0.09, 0.19, 0.19, 0.19, 0.39]
    })


#Ingrédients pour les desserts

df_fruit = pd.DataFrame({
    "ingredient": ["banane", "pomme", "orange"], 
    "prix": [0.99, 0.49, 0.49]
    })

df_glace = pd.DataFrame({
    "ingredient": ["glace_van", "glace_choco", "glace_pist"], 
    "prix": [0.69, 0.99, 0.99]
    })

df_sauce = pd.DataFrame({
    "ingredient": ["s_choco", "s_caramel", "s_café", "croustille"], 
    "prix": [0.19, 0.19, 0.19, 0.09]
    })

df_ingredient_dessert = pd.concat([df_fruit, df_glace, df_sauce]).reset_index()
del df_ingredient_dessert['index']

df_ingredient = pd.concat([df_ingredient_plat, df_ingredient_dessert]).set_index("ingredient")


## RECETTE

nb_plat = 50
nb_dessert = 50
list_plat = []
list_dessert = []

for plat in range (nb_plat):
    rd_viande = rd.randint(1,3)
    nb_viande = rd.randint(1,2)
    rd_crudites = rd.randint(4,6)
    rd_sauce = rd.randint(7,9)
    nb_fromage = rd.randint(0,3)

    list_plat.append({
        "nom_item": "Plat n°" + str(plat + 1),
        "ingredients": [df_ingredient_plat.ingredient[0], df_ingredient_plat.ingredient[rd_viande], df_ingredient_plat.ingredient[rd_crudites], df_ingredient_plat.ingredient[rd_sauce], df_ingredient_plat.ingredient[10]],
        "prix": round((df_ingredient_plat.prix[0] + nb_viande * df_ingredient_plat.prix[rd_viande] + df_ingredient_plat.prix[rd_crudites] + df_ingredient_plat.prix[rd_sauce]) + nb_fromage *  df_ingredient_plat.prix[10] + 1.49, 2),
        "type": "plat"
    })
    
for dessert in range (nb_dessert):
    rd_fruit = rd.randint(0, len(df_fruit)-1)
    rd_glace = rd.randint(0, len(df_glace)-1)
    rd_sauce = rd.randint(0, 2)
    rd_boule = rd.randint(1, 3)

    list_dessert.append({
        "nom_item": "Dessert n°" + str(dessert + 1),
        "ingredients": [df_fruit.ingredient[rd_fruit], df_glace.ingredient[rd_glace], df_sauce.ingredient[rd_sauce], df_sauce.ingredient[3]],
        "prix": round((df_fruit.prix[rd_fruit] + rd_boule * df_glace.prix[rd_glace] + df_sauce.prix[rd_sauce] + df_sauce.prix[3]) + 0.49, 2),
        "type": "dessert"
    })

list_recette = list_plat + list_dessert

df_boisson = pd.DataFrame({
    "nom_item": ["coca_p", "coca_zero_p", "fanta_orange_p", "fanta_citron_p", "sprite_p", "vittel_p", "san_pellegrino_p", "jus_orange_p", "jus_pomme_p", "heinneken_p", 
    "coca_zero_m", "fanta_orange_m", "fanta_citron_m", "sprite_m", "vittel_m", "san_pellegrino_m", "jus_orange_m", "jus_pomme_m", "heinneken_m",
    "coca_g", "coca_zero_g", "fanta_orange_g", "fanta_citron_g", "sprite_g", "vittel_g", "san_pellegrino_g", "jus_orange_g", "jus_pomme_g", "heinneken_g"
    ],
    "prix": [1.49, 0.99, 1.49, 1.49, 0.99, 0.99, 1.49, 1.99, 1.99, 2.99,
    0.99*1.25, 1.49*1.25, 1.49*1.25, 0.99*1.25, 0.99*1.25, 1.49*1.25, 1.99*1.25, 1.99*1.25, 2.99*1.25,
    1.49*1.5, 0.99*1.5, 1.49*1.5, 1.49*1.5, 0.99*1.5, 0.99*1.5, 1.49*1.5, 1.99*1.5, 1.99*1.5, 2.99*1.5
    ],
    "type" : "boisson"
    })

df_boisson["prix"] = round(df_boisson["prix"], 2)

list_boisson = []

for boisson in df_boisson.nom_item:
    list_boisson.append(boisson)

list_stock = []
for i in range (len(df_ingredient)):
    list_stock.append(rd.randint(50,500))

df_stock = df_ingredient.copy()
del df_stock['prix']

df_stock['code_postal'] = ''
df_stock['code_postal'] = df_stock['code_postal'].apply(lambda x : code_postal[rd.randint(0, len(code_postal)-1)])

df_stock['quantité'] = ''
df_stock['quantité'] = df_stock['quantité'].apply(lambda x : list_stock[rd.randint(0, len(list_stock)-1)])

df_stock.quantité.sans = 0
df_stock.quantité['pain']
df_recette = pd.DataFrame()

for recette in list_recette:
    for ingredient in recette["ingredients"]:
        df = pd.DataFrame({
            "nom_item": [recette["nom_item"]], 
            "ingredient": [ingredient],
            "quantité": df_stock.quantité[ingredient]
            })
        df_recette = pd.concat([df_recette, df])


## ITEM

df_item = pd.DataFrame(list_recette)
del df_item["ingredients"]

df_item = pd.concat([df_item, df_boisson])


## CARTE ITEM

df_carte_item = df_item.copy()
carte_item = []

for pays in range(0,3):
    for item in df_carte_item.nom_item:
        carte_item.append({
            "id_item": item,
            "pays": list_pays[rd.randint(0, len(list_pays))-1]
        })

list_item = []

for item in carte_item:
    change_item = [item['id_item'], item['pays']]
    list_item.append(change_item)


df_carte_item = pd.DataFrame(carte_item)
item_restant_list= list_item.copy()
selected_item_list= []


for pays in list_pays:
    for _ in range(80):
        for item in list_item:
            if item not in selected_item_list:
                if len(item_restant_list) > 0:
                    selected_item_list.append(item)
                    item_restant_list.remove(item)

df_carte_item = pd.DataFrame(selected_item_list)

df_carte_item = df_carte_item.rename(columns={0:"id_item",1:"pays"})

df_carte_item = df_carte_item.sort_values("id_item")


## MENU
#Prix total des plats, boissons, desserts, moins 10%

df_plat = pd.DataFrame(list_plat)
df_dessert = pd.DataFrame(list_dessert)
list_plat = []

for plat in df_plat.nom_item:
    list_plat.append(plat)

#list_plat

list_dessert = []

for plat in df_dessert.nom_item:
    list_dessert.append(plat)

#list_dessert

del df_plat['ingredients']

del df_dessert['ingredients']

menu1 = []
menu2 = []
menu3 = []
menu4 = []
menu5 = []
menu6 = []
menu7 = []
menu8 = []
menu9 = []
menu10 = []

list_menu = [menu1, menu2, menu3, menu4, menu5, menu6, menu7, menu8, menu9, menu10]

for menu in list_menu:
    menu.append(list_plat[rd.randint(0,len(list_plat)-1)])
    menu.append(list_boisson[rd.randint(0,len(list_boisson)-1)])
    menu.append(list_dessert[rd.randint(0,len(list_dessert)-1)])

df_menu_item_prix = df_item.set_index("nom_item")

df_menu = pd.DataFrame(list_menu)

df_menu = df_menu.rename(columns={0:"plat",1:"boisson",2:"dessert"})

df_menu['id_menu'] = df_menu.index

df_menu["prix"] = 0

def list_prix_fonc (list = list):
    prix = 0
    for i in range(len(list)):
        prix = prix + list[i]
    return prix * 0.9

list_prix = []

for menu in list_menu:
    list_prix.append(round(list_prix_fonc(df_menu_item_prix.prix[menu]),2))

df_menu["prix"] = list_prix


## CARTE MENU

list_carte_menu = []

for pays in list_pays:   
    for menu in df_menu.id_menu:
      list_carte_menu.append({
        "pays":pays,
        "id_menu":menu
      })

df_carte_menu = pd.DataFrame(list_carte_menu)


## Convert to SQL

df_resto.to_sql(name='Restaurant', con=engine, if_exists = 'append', index=False)

df_employes.to_sql(name='Employee', con=engine, if_exists = 'append', index=False)

df_pays.to_sql(name='Pays', con=engine, if_exists = 'append', index=False)
df_ingredient = df_ingredient.reset_index()

df_ingredient.to_sql(name='Ingredient', con=engine, if_exists = 'append', index=False)

df_item.to_sql(name='Item', con=engine, if_exists = 'append', index=False)
df_stock = df_stock.reset_index()

df_stock.sort_values(by="code_postal")
df_stock.to_sql(name='Stock', con=engine, if_exists = 'append', index=False)

df_recette.to_sql(name='Recette', con=engine, if_exists = 'append', index=False)

df_carte_item.to_sql(name='CarteItem', con=engine, if_exists = 'append', index=False)

df_menu.to_sql(name='Menu', con=engine, if_exists = 'append', index=False)

df_carte_menu.to_sql(name='CarteMenu', con=engine, if_exists = 'append', index=False)