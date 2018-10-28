class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        if new_age:
            self.age = new_age
        return new_age

    def set_name(self, new_name=""):
        self.name = new_name
        return new_name

    def __str__(self):
        return "animal:{}:{}".format(self.name, self.age)


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:{}:{}".format(self.name, self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")

    def __str__(self):
        return "rabbit:{}:{}".format(self.name, self.age)
my_animal = Animal(3)

jelly = Cat(1)
print(jelly.get_name())
jelly.set_name("jelly-belly")
print(jelly)


