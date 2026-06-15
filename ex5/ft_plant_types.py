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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, color: str):
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._bloom = False

    def __str__(self) -> str:
        first_line = super().__str__()
        s = f"{first_line}\nColor: {self._color}\n"
        if self._bloom == True:
            return f"{s}Rose is blooming beautifully!"
        else:
            return f"{s}Rose has not bloomed yet"

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, trunk_diameter: float):
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
    
    def __str__(self) -> str:
        first_line = super().__str__()
        return f"{first_line}\nTrunk diameter: {self._trunk_diameter:.1f}cm"
    
    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")#Of dit in main? onduidelijk
        print(f"Tree {self._name.capitalize()} now produces a shade of {self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, harvest_season: str):
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def __str__(self) -> str:
        first_line = super().__str__()
        return f"{first_line}\nHarvest season: {self._harvest_season.capitalize()}\nNutritional value: {self._nutritional_value}"

    def age() -> None:
        super.age()
        self._nutritional_value += 1


if __name__ == "__main__":#dit nog aanpassen
    print("=== Garden Security System ===")
    rose = Plant("rose", 15, 10, 0.8)
    print(f"Plant created: {rose}\n")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-10)
    print(f"\nCurrent state: {rose}")
