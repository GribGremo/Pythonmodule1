
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
        if name not in self.growth_behavior:
            growth = float(input(f"Unknown plant({name}), please define her growth per day: "))
            self.growth_behavior[name] = growth
        self.name = name
        self.initial_height = initial_height
        self.initial_age = initial_age
        self.current_height = initial_height
        self.current_age = initial_age

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
    plant_a = Plant("Rose", 25, 30)
    plant_b = Plant("Sunflower", 30, 7)
    plant_c = Plant("Cactus", 5, 4)
    plant_d = Plant("Dandelion", 10, 25)
    print("=== Garden Plant Growth ===")
    plant_a.sim_week()
    plant_b.sim_week()
    plant_c.sim_week()
    plant_d.sim_week()


if __name__ == "__main__":
    main()

# $> python3 ft_plant_growth.py
# === Garden Plant Growth ===
# Rose: 25.0cm, 30 days old
# === Day 1 ===
# Rose: 25.8cm, 31 days old
# === Day 2 ===
# Rose: 26.6cm, 32 days old
# === Day 3 ===
# Rose: 27.4cm, 33 days old
# === Day 4 ===
# Rose: 28.2cm, 34 days old
# === Day 5 ===
# Rose: 29.0cm, 35 days old
# === Day 6 ===
# Rose: 29.8cm, 36 days old
# === Day 7 ===
# Rose: 30.6cm, 37 days old
# Growth this week: 5.6cm