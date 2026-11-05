class Plant:
    def __init__(self, name, height, age):
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{name}: Error, age can't be negative\n")
        else:
            self._age = age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False

        self._height = float(height)
        print(f"Height updated: {self._height}cm")
        return True

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False

        self._age = age
        if self._age < 2 and age > 0:
            print(f"Age updated: {self._age} day")
            return True
        else:
            print(f"Age updated: {self._age} day")
            return True

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def __str__(self):
        return f"{self.name}: {self._height}cm, {self._age} days old"


print("=== Garden Security System ===")

flower = Plant("Rose", 15.0, 10)
print(f"Plant created: {flower}\n")

flower.set_height(25)
flower.set_age(30)
flower._age = -80
print()
flower.set_height(-25)
flower.set_age(-30)
print()

print(f"Current state: {flower}")