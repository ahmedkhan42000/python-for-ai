class Animal:
    def __init__(self, name):
        self.name = name

    def Bark(self):
        print("says Woof!")

    def Meow(self):
        print("says Meow!")


ali = Animal("ali")
ali.Bark()
ali.Meow()
