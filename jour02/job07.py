import mysql.connector

class Employe:

    def __init__(self, nom, prenom, salaire, id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="***",
            database="entreprise"
        )
        self.mycursor = self.mydb.cursor()

    def create(self):
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        val = (self.nom, self.prenom, self.salaire, self.id_service)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def read(self):
        sql = "SELECT * FROM employes WHERE id = %s"
        val = (self.id,)
        self.mycursor.execute(sql, val)
        result = self.mycursor.fetchone()
        print(result)

    def update(self):
        sql = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        val = (self.nom, self.prenom, self.salaire, self.id_service, self.id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def delete(self):
        sql = "DELETE FROM employes WHERE id = %s"
        val = (self.id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def read_all():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="***",
            database="entreprise"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM employes")
        results = mycursor.fetchall()
        for result in results:
            print(result)
        mydb.close()

nouvel_employe = Employe("Dupont", "Pierre", 3500.00, 1)
nouvel_employe.create()

employe = Employe(nom=None, prenom=None, salaire=None, id_service=None)
employe.id = 1
employe.read()

employe.nom = "Martin"
employe.prenom = "Marie"
employe.salaire = 2900.00
employe.id_service = 2
employe.update()

employe.delete()

Employe.read_all()
