class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"name:{self.name},roll no:{self.roll_no},marks:{self.marks}")
s1=student("alice",1,85)
s2=student("bob",2,90)
s1.display()
s2.display()