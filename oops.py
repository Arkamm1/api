class student:
    roll_number=123
    def writing(self):
      print(self.roll_number)
a=student()
b=student()
a.writing()
b.writing()

class student:
    # roll_number=int(input("enter roll number"))
    # name=input("enter name")
    address="mumbai"
    branch="quastech"
    def python(self):
        pfees=30000
        roll_number = int(input("enter roll number"))
        name = input("enter name")
        dis=pfees*5/ 100
        print(roll_number,name,self.address,self.branch,dis)


    def java(self):
        jfees=25000
        roll_number = int(input("enter roll number"))
        name = input("enter name")
        dis = jfees - jfees / 100 * 20
        print(roll_number,name,self.address,self.branch,dis)


    def wd(self):
        wfees=40000
        roll_number = int(input("enter roll number"))
        name = input("enter name")
        dis= wfees - wfees / 100 * 25
        print(roll_number,name,self.address,self.branch,dis)


a=student()
b=student()
c=student()
a.python()
b.java()
c.wd()
