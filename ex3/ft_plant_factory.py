
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
        self.name = name.capitalize()
        self.initial_height = initial_height
        self.initial_age = initial_age
        self.current_height = initial_height
        self.current_age = initial_age
        print(f"Created: ", end="")
        self.show()


    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.current_height}cm, "
            f"{self.current_age} days old "
            f"({self.growth_behavior[self.name]}cm per day)"
        )

    def sim_week(self):
        self.show()
        r = range(1, 8)
        for x in r:
            print(f"=== Day {x} ===")
            self.grow()
            self.age()
            self.show()
        print(f"Growth this week: {round(self.current_height - self.initial_height, 1)}cm")

    def grow(self) -> None:
        self.current_height = round(self.current_height + self.growth_behavior[self.name], 1)

    def age(self) -> None:
        self.current_age += 1



def main() -> None:
    rose = Plant("rose", 25, 30)
    oak = Plant("oak", 200, 365)
    cactus = Plant("cactus", 5, 90)
    sunflower = Plant("sunflower", 80, 45)
    fern = Plant("fern", 15, 120)


if __name__ == "__main__":
    main()

# $> python3 ft_plant_factory.py
# === Plant Factory Output ===
# Created: Rose: 25.0cm, 30 days old
# Created: Oak: 200.0cm, 365 days old
# Created: Cactus: 5.0cm, 90 days old
# Created: Sunflower: 80.0cm, 45 days old
# Created: Fern: 15.0cm, 120 days old