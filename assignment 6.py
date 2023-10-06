class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_jrt_method(self):
        print("This is a special method for Jack Russell Terrier.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_bulldog_method(self):
        print("This is a special method for Bulldog.")

dog1 = Dog("Buddy", 5, "Brown")
dog1.description()
dog1.get_info()

jrt_dog = JackRussellTerrier("Rex", 3, "White")
jrt_dog.description()
jrt_dog.get_info()
jrt_dog.special_jrt_method()

bulldog = Bulldog("Spike", 4, "Fawn")
bulldog.description()
bulldog.get_info()
bulldog.special_bulldog_method()