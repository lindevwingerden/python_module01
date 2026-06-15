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
    rose = Plant("rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    start_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow(True)
        rose.show()
    print(f"Growth this week: {rose.height - start_height:.1f}cm")
