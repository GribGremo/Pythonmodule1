class Plant:
    def __init__(
            self,
            name: str = "DefaultName",
            height: int = 1,
            age: int = 1) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.age} days old"
        )


def main() -> None:
    plant_a = Plant("Rose", 25, 30)
    plant_b = Plant("Sunflower", 80, 45)
    plant_c = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant_a.show()
    plant_b.show()
    plant_c.show()


if __name__ == "__main__":
    main()


# $> python3 ft_garden_data.py
# === Garden Plant Registry ===
# Rose: 25cm, 30 days old
# Sunflower: 80cm, 45 days old
# Cactus: 15cm, 120 days old
