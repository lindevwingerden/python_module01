class Plant:

    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self._name = name
        if height < 0:
            self._height = 0.0
            print(
                f"{self._name.capitalize()}: Error, height can't be negative"
            )
            print("Height set to zero")
        else:
            self._height = height
        if age < 0:
            self._age = 0
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age set to zero")
        else:
            self._age = age
        self._growth_rate = growth_rate

    def __str__(self) -> str:
        s = (
            f"{self._name.capitalize()}: "
            f"{self._height:.1f}cm, {self._age} days old"
        )
        return s

    def show(self) -> None:
        print(self)

    def age(self) -> None:
        self._age += 1

    def grow(self, watered: bool) -> None:
        if watered:
            self._height += self._growth_rate

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self._name.capitalize()}: Error, height can't be negative"
            )
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height:.1f}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15, 10, 0.8)
    print(f"Plant created: {rose}\n")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-10)
    print(f"\nCurrent state: {rose}")
