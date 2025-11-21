
class Student:
    def __init__(self,name,roll,gpa):
        self.x=name
        self.y=roll
        self.z=gpa
    def __str__(self):
        return f"{self.x}   {self.y}   {self.z}"
    def __eq__(self, value):
        return self.x==value.x and self.y==value.y and self.z==value.z
        
student1=Student('shimul',7,4.34)
student2=Student('shimul',7,4.34)
student3=Student('Mustafa',8,4.44)
print(student1==student2==student3)