class Animal:
    def __init__(self, name):
        self.name = name

    def Bark(self):
        print("says Woof!")

    def Meow(self):
        print("says Meow!")

    def Run(self):
        print("says Run!")


ali = Animal("ali")
ali.Bark()
ali.Meow()
ali.Run()
