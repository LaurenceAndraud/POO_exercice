class Livre:
    def __init__(
            self, 
            titre:str, 
            auteur:str, 
            nbre_pages:int, 
            éditeur:str, 
            genre:str, 
            prix:float):
        self.titre = titre
        self.auteur = auteur
        self.nbre_pages = nbre_pages
        self.éditeur = éditeur
        self.genre = genre
        self.prix = prix

    def afficher(self):
        print("Titre: ", self.titre)
        print("Auteur: ", self.auteur)
        print("Nombre de pages: ", self.nbre_pages)
        print("Editeur: ", self.éditeur)
        print("Genre: ", self.genre)
        print("Prix: ", self.prix)

    @property
    def get_prix_ttc(self):
        return self.prix * 1.2
    
class Album(Livre):
    def __init__(
            self,
            titre:str, 
            auteur:str, 
            nbre_pages:int, 
            éditeur:str, 
            genre:str, 
            prix:float, 
            illustrateur:str, 
            pop_up:bool, 
            thématique:str):
        super().__init__(titre, auteur, nbre_pages, éditeur, genre, prix)
        self.illustrateur = illustrateur
        self.pop_up = pop_up
        self.thématique = thématique

    def afficher_album(self):
        super().afficher()
        print("Illustrateur: ", self.illustrateur)
        print("Pop-up: ", self.pop_up)
        print("Thématique: ", self.thématique)


livre1 = Livre(
    "Harry Potter",
    "J.K. Rowling",
    260,
    "Gallimard",
    "jeunesse",
    8.5
)

print(livre1.titre)
print(livre1.get_prix_ttc)

livre2 = Livre(
    "Les Misérables",
    "Victor Hugo",
    650,
    "Folio classiques",
    "classiques",
    3
)

print(livre2.auteur)
livre2.afficher()

album1 = Album(
    "Histoires japonaises",
    "Benjamin Lacombe",
    25,
    "Gallimard illustrations",
    "imaginaire",
    25.5,
    "Benjamin Lacombe",
    False,
    "folfklore japonais"
)

album1.afficher()
print(album1.pop_up)
album1.afficher_album()

######## Composite ##########

class Book:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} par {self.auteur}"
    
class CollectionPolicier:
    def __init__(self, titre):
        self.titre = titre
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def __str__(self):
        return f"{self.titre} (contient {len(self.children)} livres)"
    
class CollectionBD:
    def __init__(self, titre):
        self.titre = titre
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def __str__(self):
        return f"{self.titre} (contient {len(self.children)} livres)"
    
collection_policier = CollectionPolicier("romans policiers")
collection_bd = CollectionBD("bandes dessinées")

livre1 = Book("Le chat noir", "Edgar Allan Poe")
livre2 = Book("Le chien des Baskerville", "Arthr Conan Doyle")
livre3 = Book("Le mystère de la chambre jaune", "Gaston Leroux")
livre4 = Book("Astérix", "Goscinny")
livre5 = Book("Tintin", "Hergé")
livre6 = Book("L'arabe du futur", "Riad Sattouf")
collection_policier.add(livre1)
collection_policier.add(livre2)
collection_policier.add(livre3)
collection_bd.add(livre4)
collection_bd.add(livre5)
collection_bd.add(livre6)

print(collection_policier)
print(collection_bd)



