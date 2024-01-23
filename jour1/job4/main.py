class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

personne1 = Personne("Bob", "Eponge")
personne2 = Personne("Will", "Smith")
personne3 = Personne("Martin", "Matin")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
