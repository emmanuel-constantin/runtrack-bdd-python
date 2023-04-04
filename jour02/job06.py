import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***",
    database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT SUM(capacite) FROM salles")

result = mycursor.fetchone()

somme_capacites = result[0]

print("La somme des capacités des salles est de :", somme_capacites)

mydb.close()
