class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def rollover(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()
my_dog.rollover()

print("")

golden_retriever = Dog('Leo', 1)
print(f"The Golden Retriever name is {golden_retriever.name}.")
print(f"The Golden Retriever age is {golden_retriever.age}.")
golden_retriever.sit()
golden_retriever.rollover()