class result:
    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject

    def info(self):
        print(f"{self.name} get {self.marks} marks in {self.subject}")

a = result("Irfan", 300, "Hindi")
b = result("Mohit", 400, "urdu")
c = result("nishita", 500, "sanskrit")
d = result("Kaif 144", 0, "Pakistani lanugage")

a.info()
b.info()
c.info()
d.info()

