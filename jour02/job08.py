import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="***",
  database="zoo"
)

# Définition de la classe Animal
class Animal:
  def __init__(self, id, nom, race, id_cage, date_naissance, pays_origine):
    self.id = id
    self.nom = nom
    self.race = race
    self.id_cage = id_cage
    self.date_naissance = date_naissance
    self.pays_origine = pays_origine

  def afficher_animaux():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM animal")
    result = cursor.fetchall()
    for row in result:
      print(row)

  def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    cursor = mydb.cursor()
    sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, race, id_cage, date_naissance, pays_origine)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "animal ajouté")

  def supprimer_animal(id):
    cursor = mydb.cursor()
    sql = "DELETE FROM animal WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "animal supprimé")

  def modifier_animal(id, nom, race, id_cage, date_naissance, pays_origine):
    cursor = mydb.cursor()
    sql = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
    val = (nom, race, id_cage, date_naissance, pays_origine, id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "animal modifié")

# Définition de la classe Cage
class Cage:
  def __init__(self, id, superficie, capacite_max):
    self.id = id
    self.superficie = superficie
    self.capacite_max = capacite_max

  def afficher_cages():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM cage")
    result = cursor.fetchall()
    for row in result:
      print(row)

  def calculer_superficie_totale():
    cursor = mydb.cursor()
    cursor.execute("SELECT SUM(superficie) FROM cage")
    result = cursor.fetchone()
    print("La superficie totale des cages est de", result[0], "m²")

# Menu principal
while True:
    print("Menu principal :")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher les animaux")
    print("5. Afficher les cages")
    print("6. Calculer la superficie totale")
    print("7. Quitter")
    choix = input("Entrez votre choix (1-7) : ")

    if choix == "1":
        nom = input("Entrez le nom de l'animal : ")
        race = input("Entrez la race de l'animal : ")
        id_cage = input("Entrez l'ID de la cage : ")
        date_naissance = input("Entrez la date de naissance de l'animal (format YYYY-MM-DD) : ")
        pays_origine = input("Entrez le pays d'origine de l'animal : ")
        Animal.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)
    
    elif choix == "2":
        id = input("Entrez l'ID de l'animal à supprimer : ")
        Animal.supprimer_animal(id)

    elif choix == "3":
        id = input("Entrez l'ID de l'animal à modifier : ")
        nom = input("Entrez le nouveau nom de l'animal : ")
        race = input("Entrez la nouvelle race de l'animal : ")
        id_cage = input("Entrez le nouvel ID de la cage : ")
        date_naissance = input("Entrez la nouvelle date de naissance de l'animal (format YYYY-MM-DD) : ")
        pays_origine = input("Entrez le nouveau pays d'origine de l'animal : ")
        Animal.modifier_animal(id, nom, race, id_cage, date_naissance, pays_origine)

    elif choix == "4":
        Animal.afficher_animaux()

    elif choix == "5":
        Cage.afficher_cages()

    elif choix == "6":
        Cage.calculer_superficie_totale()

    elif choix == "7":
        break
    else:
        print("Choix invalide. Veuillez entrer un choix valide (1-7).")
