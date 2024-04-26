class student:
    def __init__ (self,name="",usn="",marks=[]):
        self.name = name
        self.usn = usn
        self.marks = list()

    def getmarks(self):
        a=int(input("enter marks of s1"))
        self.marks.append(a)
        b=int(input("enter marks of s2"))
        self.marks.append(b)
        c=int(input("enter marks of s3"))
        self.marks.append(c)

    def getDetails(self):
        self.name = input("enter name: ")
        self.usn = input("enter usn: ")

    def display(self):
        print("Name: ",self.name)
        print("usn: ",self.usn)
        print("marks: ",self.marks)
        total = 0
        for x in self.marks:
            total+=x
        print("Total Marks: ",total,"\tpercentage: ",total/3,"%")

x = student()
x.getDetails()
x.getmarks()
x.display()