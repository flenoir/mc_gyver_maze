
# explication projet "mac_gyver_maze"

Selon les indication du projet, il faut créer le labyrinthe sous forme de fichier. Je créer un fichier excel qui me permet de visualiser le labyrinthe que je veux créer.  A partir de ce fichier, je crée un fichier texte qui sera utilisé par mon application pour afficher le labyrinthe en mode console. Mon mentor me consielme donc de créer la logique en mode console avant d'attaquer la partie graphique avec Pygame. 

Il est aussi essentiel de programmer en paradigme objet et pas en procédural.

Chaque mur est symbolisé par le lettre x et chaque espace vide est symbolisé par le chiffre 0. Mac Gyver est symbolisé par la lettre M, le gardien par G et les objets (items) par I

La zone de jeu est défini par 15 cases horizontales et 15 case verticales. Ici on va naviguer dans le labyrinthe en sélectionnant une des 15 lignes puis une des 15 positions dans chaque ligne.






Je réalise donc une structure autour du pseudo code afin d’utiliser la POO :

------------------

#Pseudo code

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

-------------------

j'ai pu réaliser la structure en affichage console en faisant un print d'un fichier texte qui contentait des X pour symboliser les mur. J'ai aussi "loggé" la position de Mac Gyver afin de sélectionner sa position précédente pour remplacer sa position par un 0.

J'ai pu faire le déplacement de Mac Gyver avec des tuples demandées au travers d'un input dans la console. J'ai pu ensuite empêcher le déplacement sur les murs et ensuite ajouter la logique du jeu qui veut que Mac Gyver ne gagne que s'il se présente devant le gardien avec les 3 items. 

Au fur et à mesure j'i utilisé git pour versionner mon code.

Dans mes classes, le déplacement se faisait dans la classe du labyrinthe mais je me suis dis que cela n'était pas logique. Je l'ai retravaillé ensuite pour qu'elle soit dans la méthode de déplacement des personnages. Cela m'a permis de bien appréhender les interactions entres les classes.

Mon mentor m'a aussi conseillé d'encapsuler le niveau du labyrinthe avant de passer à la réalisation du jeu avec Pygame. J'ai donc fait cette encapsulation. 

 Je suis donc passé sur Pygame.

Il m'a fallu  installer Pygame mais il faut que ce soit une version Python 3 mais en 32 bits. J'ai donc dû désinstaller Python 3 en version 64 bits.

Ensuite, je suis parti sur des nouvelles classes similaires au précédentes afin de reproduire les logiques dans les classes. 

 J'ai modifié le constructeur du labyrinthe afin d'avoir aussi un tuple correspondant aux indexes de lignes et d'emplacement.  Avant je n'avais que le tuple de position et ensuite j'avais aussi la lettre correspondant à cette position. Cela m'a permis d'afficher les murs du jeu en multipliant chaque valeur des tuples par 45 (pixels)

J'ai pu ensuite passer à l'affichage et au déplacement de Mac Gyver. j'ai créé une méthode de vérification des déplacements afin de pouvoir "mapper" les résultat de l’événement de la touche tapé sur les déplacements et vérifier si c'est possible (sur un emplacement de mur ou non). Et aussi surtout éviter les répétitions dans le code.

J'ai essayé aussi de voir si je faisais l'affichage dans le constructeur avec juste un rafraîchissement des mouvements des personnages mais je suis resté sur une logique dans la méthode "move" car j'ai rencontré des problèmes dans la logique d'affichage entre l’initialisation et l'affichage du labyrinthe a chaque tour. Je pense qu'il y a moyen d'améliorer cette partie pour ne pas avoir à ré-afficher les murs à chaque tour, mais j'ai préféré me concentrer sur la suite des livrables demandés dans le jeu.

Je suis ensuite passé à l'affichage des items et à leur disparition quand Mac Gyver passe dessus. J'ai eu un léger problème d'icone qui se ré-affectaient différemment à l'affichage dès que je prenait un objet mais je l'ai corrigé ensuite. il y a avait un affichage aléatoire et je devais afficher le bon objet.

Je passe donc à l'incrémentation d'un compteur pour collecter les 3 objets et ensuite  ajouter la condition de victoire ou de défaite en rencontrant le gardien. 

je pense ensuite finir le projet en ajoutant un conteur d'objets collectés à l'écran puis un écran d'accueil du jeu. 

J'ai pu assez facilement ajouter un compteur d'objets en bas à droite. 

J'ai pu ensuite créer un écran de démarrage du jeu qui demande d'appuyer sur la touche "S" pour commencer. J'ai eu 2 difficultés : la gestion des boucles entre l'écran de démarrage du jeu et le jeu puis la taille différente entre la fenêtre de lancement du jeu et le jeu en soi. 

Pour la problème des boucles, j'ai discuté sur le forum Discord et j'ai pu avoir des indications que j'ai pu mettre en pratique rapidement. Pour le problème de taille, en réfléchissant et en allant voir la doc de pygame j'ai pu trouver une solution car je tenais à avoir un taille différente sur ces fenêtres. 

 J'ai ensuite ajouté un son, quand on collecte les items. et je suis en train de voir comment afficher une boite indiquant la fin du jeu quand on gagne ou on perd. 