task_00_abc.py =
    1- Créer une classe abstraite nommée « Animal » à l'aide du package « ABC ». Cette classe doit avoir une méthode abstraite appelée « sound ».
    2- Créer deux sous-classes de « Animal » : « Dog » et « Cat ». Implémentez la méthode « sound » danschaque sous-classe pour renvoyer respectivement les chaînes « Bark » et « Meow ».

task_01_duck_typing.py =
    1- Créer une classe abstraite nommée « Shape » avec deux méthodes abstraites : « area » et « perimeter ».
    2- Implémenter deux classes concrètes : « Circle » et « Rectangle », toutes deux héritant de « Shape ». Chaque classe doit fournir des implémentations pour les méthodes « area » et de « perimeter ».
    3- Écrire une fonction autonome nommée « shape_info » qui accepte un objet de type « Shape » (en tapant du canard) et imprime sa zone et son périmètre.
    4- Tester la fonction « shape_info » avec des instances de « Circle » et de « Rectangle ».

task_02_verboselist.py = Créer une classe nommée « VerboseList » qui étend la classe « list » Python. Cette classe personnalisée doit imprimer un message de notification chaque fois qu'un élément est ajouté (à l'aide des méthodes « append » ou « extend ») ou supprimé (à l'aide des méthodes « remove » ou « pop »).

task_03_countediterator.py = Créer une classe nommée « CountedIterator » qui étend l'itérateur intégré obtenu à partir de la fonction « iter ». Le « CountedIterator » doit garder une trace du nombre d’éléments qui ont été itérés. Plus précisément, vous devrez remplacer la méthode « __next__ » pour incrémenter un compteur à chaque fois qu'un élément est récupéré.

task_04_flyingfish.py = Construire une classe « FlyingFish » qui hérite à la fois d’une classe « Fish » et d’une classe « Bird ». Dans « FlyingFish », remplacez les méthodes des deux parents. L'objectif est de comprendre l'héritage multiple et la façon dont Python détermine l'ordre de résolution des méthodes.

task_05_dragon.py = Concevoir deux classes mixin, « SwimMixin » et « FlyMixin », chacune équipée des méthodes « swim » et « fly » respectivement. Ensuite, construisez une classe « Dragon » qui hérite de ces deux mixins. Votre objectif est de montrer qu'une instance de « Dragon » peut à la fois nager et voler.
