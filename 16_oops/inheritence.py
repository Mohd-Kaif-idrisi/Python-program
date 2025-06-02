class animal:
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        print("animal speaking")

class breed(animal):
    def cat(self):
        # super().sound()  #super is use to call parental function in child class
        print("meow")

a = animal("perian")
d = breed("persian")

a.sound()
d.cat()
    