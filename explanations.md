
# explication projet "mac_gyver_maze"

Selon les indication du projet, il faut cr�er le labyrinthe sous forme de fichier. Je cr� un fichier excel qui me permet de visualiser le labyrinthe que je veux cr�er.

A partir de ce fichier, je cr�e un fichier texte qui sera utilis� par mon application pour afficher le labyrinthe en mode console. Mon mentor me conseille donc de cr�er la logique en mode console avant d'attaquer la partie graphique avec Pygame. 

Il est aussi essentiel de programmer en paradigme objet et pas en proc�dural.

Chaque mur est symbolis� par le lettre x et chaque espace vide est symbolis� par le chiffre 0. Mac Gyver est symbolis� par la lettre M, le gardien par G et les objets (items) par I

La zone de jeu est d�fini par 15 cases horizontales et 15 case verticales. Ici on va naviguer dans le labyrinthe en s�lectionnant une des 15 lignes puis une des 15 positions dans chaque ligne.




Je r�alise aussi une structure autour du pseudo code afin d�utiliser la POO :

------------------

#Pseudo code

```
ask player to select a level
create maze based on level
display maze

#create a loop until game is finished
    # ask player to move mcgyver character (do not allow to move outside maze or on a wall)
    # reload maze with new mcgyver position

    #create condition inside loop
    # if mac gyver move on an item , he fills his bag
    # if mac Gyver faces guardian without all items he looses (game is finished)
    # else he wins (game is finished)


#objects

#Level (attributes file | method create, method display) -> hint : display method should be called after each move
#character (attributes name, position, symbol, movable, bag | method move ? )
```

-------------------

j'ai pu r�aliser la structure en affichage console en faisant un print d'un fichier texte qui contentait des X pour symboliser les mur. J'ai aussi "logg�" la position de Mac Gyver afin de s�lectionner sa position pr�c�dente pour remplacer sa position par un 0.

J'ai pu faire le d�placement de Mac Gyver avec des tuples demand�es au travers d'un input dans la console. J'ai pu ensuite emp�cher le d�placement sur les murs et ensuite ajouter la logique du jeu qui veut que Mac Gyver ne gagne que s'il se pr�sente devant le gardien avec les 3 items. 

Au fur et � mesure j'ai utilis� git pour versionner mon code. puis , par la suite aussi pour ajouter des issues afin de savoir ce que je dois continuer à implémenter.

Dans mes classes, le d�placement se faisait dans la classe du labyrinthe mais je me suis dis que cela n'�tait pas logique. Je l'ai retravaill� ensuite pour qu'elle soit dans la m�thode de d�placement des personnages. Cela m'a permis de bien appr�hender les interactions entres les classes. utiliser l'instance de la classe Maze pour la passer comme argument lors de la création des instances des personnages.

Mon mentor m'a aussi conseill� d'encapsuler le niveau du labyrinthe avant de passer � la r�alisation du jeu avec Pygame. J'ai donc fait cette encapsulation. 

 Je suis donc pass� sur Pygame.

Il m'a fallu  installer Pygame mais il faut que ce soit une version Python 3 mais en 32 bits. J'ai donc d� d�sinstaller Python 3 en version 64 bits. Je suis sous windows  et j'ai essayé plusieurs choses (exe, chocolatey et pip)

Ensuite, je suis parti sur des nouvelles classes similaires au pr�c�dentes afin de reproduire les logiques dans les classes. 

J'ai modifi� le constructeur du labyrinthe afin d'avoir aussi un tuple correspondant aux indexes de lignes et d'emplacements.  Avant je n'avais que le tuple de position et ensuite j'avais aussi la lettre correspondant � cette position ('x', 0, 1).A noter que j'ai modifié ces tuples en listes ensuite pour pouvoir modifier les premières valeurs. Cela m'a permis d'afficher les murs du jeu en multipliant chaque valeur des tuples par 45 (pixels)

J'ai pu ensuite passer � l'affichage et au d�placement de Mac Gyver. j'ai cr�� une m�thode de v�rification des d�placements afin de pouvoir "mapper" les r�sultat de l��v�nement de la touche tap� sur les d�placements et v�rifier si c'est possible (sur un emplacement de mur ou non). Et aussi surtout �viter les r�p�titions dans le code.

J'ai essay� aussi de voir si je faisais l'affichage dans le constructeur avec juste un rafra�chissement des mouvements des personnages mais je suis rest� sur une logique dans la m�thode "move" car j'ai rencontr� des probl�mes dans la logique d'affichage entre l�initialisation et l'affichage du labyrinthe a chaque tour. Je pense qu'il y a moyen d'am�liorer cette partie pour ne pas avoir � r�-afficher les murs � chaque tour, mais j'ai pr�f�r� me concentrer sur la suite des livrables demand�s dans le jeu.

Je suis ensuite pass� � l'affichage des items et � leur disparition quand Mac Gyver passe dessus. J'ai eu un l�ger probl�me d'icone qui se r�-affectaient diff�remment � l'affichage d�s que je prenait un objet mais je l'ai corrig� ensuite. il y a avait un affichage al�atoire et je devais afficher le bon objet.

J'ai aussi ajouté, à ce moment, les recommandations PEP8 ( indentation espaces entre les lignes, docstrings, etc...)

Je passe donc � l'incr�mentation d'un compteur pour collecter les 3 objets et ensuite  ajouter la condition de victoire ou de d�faite en rencontrant le gardien. 

J'ai pu assez facilement ajouter un compteur d'objets en bas � droite en étandant la taille de la zone de jeu et en ajoutant une boite et un texte "blité" dessus.

J'ai pu ensuite cr�er un �cran de d�marrage du jeu qui demande d'appuyer sur la touche "S" pour commencer. J'ai eu 2 difficult�s : la gestion des boucles entre l'�cran de d�marrage du jeu et le jeu puis la taille diff�rente entre la fen�tre de lancement du jeu et le jeu en soi. 

Pour la probl�me des boucles, j'ai discut� sur le forum Discord et j'ai pu avoir des indications que j'ai pu mettre en pratique rapidement ( finir une premlière boucle pour entrer dans une seconde). Pour le probl�me de taille, en r�fl�chissant et en allant voir la doc de pygame j'ai pu trouver une solution car je tenais � avoir un taille diff�rente sur ces fen�tres. ( ré-utilisation de display et lieu de scale)

 J'ai ensuite ajout� un son, quand on collecte les items. 

 J'ai enfin ajouter, au centre de l'écran une boite et un message quand on termine le jeu. J'ai ajouté un delai avant de ferme l'application.

 Enfin, j'ai pu aller à un meetup Python et j'ai pu discuter de ce projet. A cette occasion j'ai refactoré le déplacement des personnages dans une fonction afin de rendre le code plus propre.