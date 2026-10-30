

class Plant:
    _growth_behavior = {
        "DefaultName": 0,
        "Rose": 0.8,
        "Sunflower": 1.5,
        "Cactus": 0.4,
    }
    def __init__(
            self,
            name: str = "DefaultName",
            initial_height: float | int = 1,
            initial_age: int = 1,
        ) -> None:
        if name.capitalize() not in self._growth_behavior:
            growth = float(input(f"Unknown plant({name}), please define her growth per day: "))
            self._growth_behavior[name.capitalize()] = growth
        self._set_name(name.capitalize())
        self._set_initial_height(initial_height)
        self._set_initial_age(initial_age)
        self._current_height = self.initial_height
        self._current_age = self.initial_age
        print("Created:", self)
        # print(f"Created: ", end="")
        # self.show()

    #Getters
    def get_name(self):
        return self._name
    def get_initial_height(self):
        return self._initial_height
    def get_initial_age(self):
        return self._initial_age
    def get_height(self):
        return self._current_height
    def get_age(self):
        return self._current_age
    
    # Setters
    def _set_name(self, name:str):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be a string")
    def _set_initial_height(self, initial_height: int | float):
        if isinstance(initial_height, (float, int)):
            if initial_height < 0:
                print(f"{self.name}: InitError, height can't be negative")
                self._initial_height = 1
                print("Height set to DefaultValue")
                return
                # raise ValueError("initial_height cannot be negative")
            self._initial_height = initial_height
        else:
            raise TypeError("initial_height must be a float or int")
    def _set_initial_age(self, initial_age: int):
        if isinstance(initial_age, int):
            if initial_age <= 0:
                print(f"{self.name}: InitError, age can't be negative")
                self._initial_age = 1
                print("Age set to DefaultValue")
                return
                # raise ValueError("initial_age cannot be negative or 0")
            self._initial_age = initial_age
        else:
            raise TypeError("initial_age must be a int")
    def set_age(self, age: int):
        if isinstance(age, int):
            if age <= 0:
                print(f"{self.name}: Error, age can't be negative")
                print("Age update rejected")
                return
                # raise ValueError("current_age cannot be negative or 0")
            self._current_age = age
            print(f"Age updated: {self.current_age} days")
        else:
            raise TypeError("current_age must be a int")
    def set_height(self, current_height: int | float):
        if isinstance(current_height, (float, int)):
            if current_height < 0:
                print(f"{self.name}: Error, height can't be negative")
                print("Height update rejected")
                return
                # raise ValueError("current_height cannot be negative")
            self._current_height = current_height
            print(f"Height updated: {self.current_height}cm")
        else:
            raise TypeError("current_height must be a float or int")

    #Properties
    name = property(get_name)
    initial_height = property(get_initial_height)
    initial_age = property(get_initial_age)
    current_age = property(get_age, set_age)
    current_height = property(get_height, set_height)

    # Other method for property
    # Both have to be named the same
    # @property
    # def name(self):
    #   return self._name
    # @name.setter
    # def name(self, name)
    # if isinstance(name, str):
    #   self._name = name
    # else:
    #   raise TypeError("name must be a string")
    # Usage:
    # myinst.name = "bulbizarre" (use the name() "setter")
    # myinst.name (use the name() "getter")

    # Methods
    def show(self) -> None:
        print("Current state:", self)

    def sim_week(self):
        self.show()
        r = range(1, 8)
        for x in r:
            print(f"=== Day {x} ===")
            self.grow()
            self.age()
            self.show()
        print(f"Growth this week: {round(self._current_height - self._initial_height, 1)}cm")

    def grow(self) -> None:
        self._current_height = round(self._current_height + self._growth_behavior[self._name], 1)

    def age(self) -> None:
        self._current_age += 1

    # Dunder
    def __str__(self):
        return (f"{self._name}: "
                f"{self._current_height}cm, "
                f"{self._current_age} days old "
                f"({self._growth_behavior[self._name]}cm per day)")


def main() -> None:
    print("~~~~~BASIC TESTS~~~~~")
    print("=== Garden Security System ===")
    base = Plant("Rose", 15, 10)
    base.current_height = 25
    base.current_age = 30
    base.current_height = -1
    base.current_age = -1
    base.show()

    print("~~~~~INIT TESTS~~~~~")
    print("Init1:")
    init1 = Plant("Init1", -5, 5)
    print()
    print("Init2:")
    init2 = Plant("Init2", 5, -5)
    print()
    print("Init3:")
    init3 = Plant("Init3", -5, -5)
    print()
    print("Init4:")
    init4 = Plant("Init4", 1.0, 1)
    print()
    print("Init5:")
    init5 = Plant("init5")
    print()

    print("Show state:")
    init1.show()
    init2.show()
    init3.show()
    init4.show()
    init5.show()
    

if __name__ == "__main__":
    main()

# TODO
# Tester getter/setter traditionnal and property, see diff, ...
# Tester erreur input height dico
# ajouter une methode add_growth_behavior


# NOTIONS 
# You can delete and add property to a class, no need for them to be declare in the class, python whatever
# No clear private status, you can still access even with mangling __
# Python property turn class attributes into properties, which are called “managed attributes”.
# ChatGPT statement: La philosophie de Python, en gros : on te donne beaucoup de liberté, mais c'est à toi de définir les garde-fous. 😄

# Getters/setters
# https://realpython.com/python-getter-setter/

# Private/mangling
# https://www.datacamp.com/tutorial/python-private-methods-explained
# https://www.datacamp.com/tutorial/role-underscore-python

# Properties
# https://www.docstring.fr/glossaire/propriete/
# https://www.ionos.com/digitalguide/websites/web-development/python-property/

# Decorators
# https://www.ionos.com/digitalguide/websites/web-development/python-decorators/

# Protected?
# https://www.tutorialsteacher.com/python/public-private-protected-modifiers

# Dunder Methods(__str__, repr)
# It looks a bit like operator in c++ with way more possibilities
# https://www.docstring.fr/glossaire/str/
# https://docs.python.org/3/reference/datamodel.html?utm_source=chatgpt.com#special-method-names

# Divers
# https://www.ionos.com/digitalguide/websites/web-development/python-tutorial/


# Expected outputs
# $> python3 ft_garden_security.py
# === Garden Security System ===
# Plant created: Rose: 15.0cm, 10 days old
# Height updated: 25cm
# Age updated: 30 days
# Rose: Error, height can't be negative
# Height update rejected
# Rose: Error, age can't be negative
# Age update rejected
# Current state: Rose: 25.0cm, 30 days old





#TEMP
# J'aurais pas pu faire un setter avec 2 arguments, les verifier, verifier si la Key existe toujours, etc
# ChatGPT said:

# Si, absolument ! Et même, c'est une très bonne approche si tu souhaites permettre l'ajout de nouvelles plantes tout en contrôlant les modifications du dictionnaire.

# Tu peux créer une méthode dédiée qui joue le rôle de setter pour ton dictionnaire.
# 1. Une méthode d'ajout contrôlée

# Par exemple :
# python

# class Plant:
#     _growth_behavior = {
#         "DefaultName": 0,
#         "Rose": 0.8,
#         "Sunflower": 1.5,
#         "Cactus": 0.4,
#     }

#     @classmethod
#     def add_growth_behavior(cls, name: str, growth: float):
#         if not isinstance(name, str):
#             raise TypeError("name must be a string")

#         if not isinstance(growth, (int, float)) or isinstance(growth, bool):
#             raise TypeError("growth must be a number")

#         name = name.capitalize()

#         if name in cls._growth_behavior:
#             raise ValueError(f"{name} already exists")

#         if growth < 0:
#             raise ValueError("growth cannot be negative")

#         cls._growth_behavior[name] = float(growth)

# J'utilise ici @classmethod parce que ton dictionnaire est un attribut de classe partagé entre toutes les instances.
# 2. Utilisation
# python

# Plant.add_growth_behavior("Tulip", 0.6)
# Plant.add_growth_behavior("Rose", 1.2)  # ValueError
# Plant.add_growth_behavior("Orchid", -1)  # ValueError

# Tu contrôles ainsi :

#     Le type du nom.

#     Le type de la croissance.

#     L'existence préalable de la clé.

#     La validité de la valeur.

#     La normalisation du nom.

# 3. Pourquoi classmethod plutôt que staticmethod ?

# C'est intéressant à connaître :
# python

# @classmethod
# def add_growth_behavior(cls, name, growth):

# cls représente la classe elle-même.

# Cela te permet de manipuler :
# python

# cls._growth_behavior

# Plutôt que de coder en dur :
# python

# Plant._growth_behavior

# C'est également plus propre si tu crées un jour une classe qui hérite de Plant.

# Mon conseil : dans ton projet, je trouve cette solution plus intéressante qu'un setter de property.

# Pourquoi ? Parce que tu ne modifies pas une propriété d'une plante individuelle : tu modifies une configuration commune à toute la classe.

# Une méthode add_growth_behavior() exprime donc beaucoup mieux l'intention de ton code qu'un setter classique.