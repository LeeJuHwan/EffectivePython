class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f"The {name} says, 'Hello!'")


class RollOverMixin:
    def roll_over(self):
        print("Did a barrel roll!")


class Dog(SpeakMixin, RollOverMixin):
    def __init__(self, dog_name):
        print(f"Hello, I'm {dog_name}")


dog = Dog("Yangoon")
dog.speak()
dog.roll_over()
