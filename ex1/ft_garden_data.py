class Plant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        s = f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
        return s

    def show(self) -> None:
        print(self)


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
