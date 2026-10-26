
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
            height: float = 1,
            age_in_days: int = 1) -> None:
        if name not in self.growth_behavior:
            growth = float(input(f"Unknown plant({name}), please define her growth per day: "))
            self.growth_behavior[name] = growth
        self.name = name
        self.height = height
        self.age_in_days = age_in_days

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.age_in_days} days old"
            f"({self.growth_behavior[self.name]}cm per day)"
        )

    def grow(self) -> None:
        self.height = round(self.height + self.growth_behavior[self.name], 1)

    def age(self, days : int) -> None:
        period = range(1, days)
        for x in period:
            self.grow()
            print(f"=== Day {x} ===")
            self.show()
            self.age_in_days += 1



def main() -> None:
    plant_a = Plant("Rose", 3, 2)
    plant_b = Plant("Sunflower", 30, 7)
    plant_c = Plant("Cactus", 5, 4)
    plant_d = Plant("Dandelion", 10, 25)
    print("=== Garden Plant Growth ===")
    plant_a.age(4)
    plant_b.age(4)
    plant_c.age(4)
    plant_d.age(4)




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