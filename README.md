# POO 
POO signifie Programmation Orientée Object, et est un modèle de programmation qui permet de créer et gérer des classes et objets. Ceci peut être utilisé dans différents langage de programmation. La POO permet également d’avoir un code plus lisible, de qualité. À travers cette documentation, nous allons voir les différentes notions de la POO à travers des exemples de livre pour une librairie.

## Les classes
La classe permet de définir les fonctions et attributs. Il faut le voir comme un modèle pour la suite de notre code. Ici, je souhaite créer ma classe livre :

```python
class Livre :
    def __init__(self):
```

Ma méthode __init__() est mon constructeur et va me permettre de définir mon livre et comment je veux qu'il soit modelé à chaque fois. Pour ma part, je veux qu'il possède un titre, un auteur, un prix, un nombre de pages, un éditeur, un genre. Pour plus de clarté et pour éviter des erreurs, je précise si les données attendues sont des string, des integer, des float ...

```python
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
```

## Les objets
Ma classe Livre est prête, mais je n'ai pas de livres de créé en soit, je n'ai que son modèle. En POO, il s'agit de créer un objet livre.

```python
livre1 = Livre(
    "Harry Potter",
    "J.K. Rowling",
    260,
    "Gallimard",
    "jeunesse",
    8.5
)
```

Ici, notre premier livre reprend totalement les caractéristiques que nous avons fourni lorsque nous avons défini notre classe Livre. Si je voulais créer un second livre, il respecterait ce même moule.

```python
livre2 = Livre(
    "Les Misérables",
    "Victor Hugo",
    650,
    "Folio classiques",
    "classiques",
    3
)
```

Nous pouvons aussi tester cela :
```input
# Input
print(livre1.titre)
# Output
Harry Potter```

```input
# Input
print(livre2.auteur)
# Output
Victor Hugo
```

## Les méthodes
La méthode est davantage un comportement à exécuter sur un objet. Dans notre exemple, imaginons que nous avons beaucoup d'objet livre et que nous voulons afficher toutes les caractéristiques de l'un d'eux pour rapidement s'y trouver. Nous allons d'abord définir cela dans la classe.

```python
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
```

```input
# Input
livre2.afficher()
# Output
Titre:  Les Misérables
Auteur:  Victor Hugo
Nombre de pages:  650
Editeur:  Folio classiques
Genre:  classiques
Prix:  3
```

## Les propriétés
Une propriété est un attribut accessible par une méthode, et permet de contrôler les accès aux données d'un objet. Dans notre exemple, imaginons que nous souhaitons un moment rapide pour accéder au prix TTC de notre livre (et en admettons aussi que le prix que nous avons indiqué dans nos instances sont en HT) :

```python
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

    @property
    def get_prix_ttc(self):
        return self.prix * 1.2
```

```input
# Input
print(livre1.get_prix_ttc)
# Output
10.2
```

## L'héritage
Par le biais de l'héritage, il est possible de créer une nouvelle classe tout en gardant le modèle existant avec une précédente classe de faite. Par exemple, nous pouvons faire une nouvelle classe Album, qui reprendra toutes les caractéristiques de Livre (donc, avec toujours un titre, un auteur, un nombre de pages ...), mais nous pourrons rajouter des caractéristiques supplémentaires, qui seront propres à l'album.

```python
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
```

et voici ce que ça donne lorsqu'on veut créer un objet album : 

```python
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
```

```input
# Input
album1.afficher()
print(album1.pop_up)
# Output
Titre:  Histoires japonaises
Auteur:  Benjamin Lacombe
Nombre de pages:  25
Editeur:  Gallimard illustrations
Genre:  imaginaire
Prix:  25.5
False
```

Ici, lorsqu'on utilise la méthode afficher() qui provient de la classe mère(Livre), il est possible d'avoir toutes les caractéristiques définies dans la classe Livre.

## Polymorphisme
Assez semblable à l'héritage, cela permet d'hériter aussi des méthodes. Voyons voir comment on pourrait réutiliser notre exemple précédent pour qu'il puisse aussi afficher les caractéristiques propre à Album, et pas seulement les caractéristiques de la classe mère(Livre).

```python
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
```

```input
# Input
album1.afficher_album()
# Output
Titre:  Histoires japonaises
Auteur:  Benjamin Lacombe
Nombre de pages:  25
Editeur:  Gallimard illustrations
Genre:  imaginaire
Prix:  25.5
Illustrateur:  Benjamin Lacombe
Pop-up:  False
Thématique:  folfklore japonais
```

# Design patterns & Composite
Le design patter(ou modèle de conception) est un élément de la POO. C'est une infrastructure logicielle avec des petites quantités de classes qui permet de régler des problèmes techniques.

Dans le cas du Composite, il s'agit de représenter une structure arborescentes d'objets et de traiter des objets individuels.

Toujours si l'on souhaite garder l'exemple des livres : admettons que l'on souhaite représenter une bibliothèque avec des livres et des collections de livres, une collection de livres est un objet composite qui peut contenir d'autres collections de livres ou des livres individuels, là où un livre est un objet simple qui ne que contenir lui-même

```python
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
```

Ici, on refait une classe Book avec quelques caractéristiques primaires, puis nous faisons deux classes pour des collections (policiers et BD) qui vont contenir des objets Book.

```python
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
```

```input
# Input
print(collection_policier)
print(collection_bd)
# Output
romans policiers (contient 3 livres)
bandes dessinées (contient 3 livres)
```
