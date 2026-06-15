class Plant:

    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self.height = height
        self._age = age
        self.growth_rate = growth_rate

    def __str__(self) -> str:
        s = (
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self._age} days old"
        )
        return s

    def show(self) -> None:
        print(self)

    def age(self) -> None:
        self._age += 1

    def grow(self, watered: bool) -> None:
        if watered:
            self.height += self.growth_rate


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25, 30, 0.8)
    print(f"Created: {rose}")
    oak = Plant("oak", 200, 365, 0.5)
    print(f"Created: {oak}")
    cactus = Plant("cactus", 5, 90, 0.1)
    print(f"Created: {cactus}")
    sunflower = Plant("sunflower", 80, 45, 1.8)
    print(f"Created: {sunflower}")
    fern = Plant("fern", 15, 120, 0.1)
    print(f"Created: {fern}")
