class result:
    name = "irfan"
    marks = 400
    subject = "hindi"

    def info(self):
        
        print(f"{self.name} get {self.marks} marks in {self.subject}")

a = result()

b = a.name("kaif")

b.info()