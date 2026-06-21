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
        self._stats: "Plant.Stats" = self.Stats()

    def __str__(self) -> str:
        s = (
            f"{self._name.capitalize()}: "
            f"{self._height:.1f}cm, {self._age} days old"
        )
        return s

    def show(self) -> None:
        self._stats._show_calls += 1
        print(self)

    def age(self) -> None:
        self._age += 1
        self._stats._age_calls += 1

    def grow(self, watered: bool) -> None:
        if watered:
            self._height += self._growth_rate
            self._stats._grow_calls += 1

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

    @staticmethod
    def more_than_year(age: int) -> bool:
        return age >= 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("unknown plant", 0, 0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def __str__(self) -> str:
            s = (
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )
            return s

        def display(self) -> None:
            print(self)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str,
    ):
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._bloom = False

    def __str__(self) -> str:
        first_line = super().__str__()
        s = f"{first_line}\nColor: {self._color}\n"
        if self._bloom:
            return f"{s}{self._name.capitalize()} is blooming beautifully!"
        else:
            return f"{s}{self._name.capitalize()} has not bloomed yet"

    def bloom(self) -> None:
        self._bloom = True


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str,
    ):
        super().__init__(name, height, age, growth_rate, color)
        self._seeds = 0

    def __str__(self) -> str:
        s = super().__str__()
        return f"{s}\nSeeds: {self._seeds}"

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        trunk_diameter: float,
    ):
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = self.Stats()

    def __str__(self) -> str:
        first_line = super().__str__()
        return f"{first_line}\nTrunk diameter: {self._trunk_diameter:.1f}cm"

    def produce_shade(self) -> None:
        self._stats._produce_shade_calls += 1
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls = 0

        def __str__(self) -> str:
            first_line = super().__str__()
            return f"{first_line}\n{self._produce_shade_calls} shade"


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        harvest_season: str,
    ):
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def __str__(self) -> str:
        first_line = super().__str__()
        return (
            f"{first_line}\n"
            f"Harvest season: {self._harvest_season.capitalize()}\n"
            f"Nutritional value: {self._nutritional_value}"
        )

    def grow(self, watered: bool) -> None:
        super().grow(watered)
        self._nutritional_value += 1


def display_stats(plant: Plant) -> None:
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.more_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.more_than_year(400)}")
    print("\n=== Flower")
    rose = Flower("rose", 15, 10, 8, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(True)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("\n=== Tree")
    oak = Tree("oak", 200, 365, 1, 5)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80, 45, 1, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(True)
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)
