

class Plant:
    growth_behavior = {
        "DefaultName": 0,
        "Rose": 0.8,
        "Sunflower": 1.5,
        "Cactus": 0.4,
    }
    def __init__(
            self,
            name: str = "DefaultName",
            initial_height: float = 1,
            initial_age: int = 1,
        ) -> None:
        if name.capitalize() not in self.growth_behavior:
            growth = float(input(f"Unknown plant({name}), please define her growth per day: "))
            self.growth_behavior[name.capitalize()] = growth
        self.setName(name.capitalize())
        self.setInitialHeight(initial_height)
        self.setInitialAge(initial_age)
        self.setCurrentHeight(initial_height)
        self.setCurrentAge(initial_age)
        print(f"Created: ", end="")
        self.show()

    #Getters
    def getName(self):
        return self._name
    def getInitialHeight(self):
        return self._initial_height
    def getInitialAge(self):
        return self._initial_age
    def getCurrentHeight(self):
        return self._current_height
    def getCurrentAge(self):
        return self._current_age
    
    # Setters
    def setName(self, name:str):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be a string")
    def setInitialHeight(self, initial_height: float):
        if isinstance(initial_height, float):
            if initial_height < 0:
                raise ValueError("initial_height cannot be negative")
            self._initial_height = initial_height
        else:
            raise TypeError("inital_height must be a float")
    def setInitialAge(self, initial_age: int):
        if isinstance(initial_age, int):
            if initial_age <= 0:
                raise ValueError("initial_age cannot be negative or 0")
            self._initial_age = initial_age
        else:
            raise TypeError("initial_age must be a int")
    def setCurrentAge(self, current_age: int):
        if isinstance(current_age, int):
            if current_age <= 0:
                raise ValueError("current_age cannot be negative or 0")
            self._current_age = current_age
        else:
            raise TypeError("current_age must be a int")
    def setCurrentHeight(self, current_height: float):
        if isinstance(current_height, float):
            if current_height < 0:
                raise ValueError("current_height cannot be negative")
            self._current_height = current_height
        else:
            raise TypeError("current_height must be a float")

    #Properties
    name = property(getName, setName)
    initial_height = property(getInitialHeight, setInitialHeight)
    initial_age = property(getInitialAge, setInitialAge)
    current_age = property(getCurrentAge, setCurrentAge)
    current_height = property(getCurrentHeight, setCurrentHeight)

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
        print(
            f"{self._name}: "
            f"{self._current_height}cm, "
            f"{self._current_age} days old "
            f"({self.growth_behavior[self._name]}cm per day)"
        )

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
        self._current_height = round(self._current_height + self.growth_behavior[self._name], 1)

    def age(self) -> None:
        self._current_age += 1


def main() -> None:


if __name__ == "__main__":
    main()

# TODO
# Tester getter/setter traditionnal and property, see diff, ...
# Tester erreur input height dico



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

# Divers
# https://www.ionos.com/digitalguide/websites/web-development/python-tutorial/