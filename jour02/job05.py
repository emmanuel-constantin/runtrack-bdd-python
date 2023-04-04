import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***",
    database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT SUM(superficie) FROM etage")

result = mycursor.fetchone()

superficie_totale = result[0]

print("La superficie de La Plateforme est de", superficie_totale, "m2")

mydb.close()
