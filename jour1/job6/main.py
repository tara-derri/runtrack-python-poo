class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"L'âge de l'animal est : {self.age}")

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_prenom):
        self.prenom = nouveau_prenom
        print(f"L'animal est maintenant nommé : {self.prenom}")

mon_animal = Animal()

mon_animal.afficherAge()

mon_animal.vieillir()

mon_animal.afficherAge()

mon_animal.nommer("minou")

mon_animal.afficherAge()
