###################################### OOP IN PART ONE #######################

'''class Student:
    name = "nasim"

s1 = Student()
print(s1.name)'''


'''class Student:
    
    def __init__(self,fullname):
        self.name = fullname
        print("this is oop in python")

s1 = Student("nasim")
print(s1.name)

s2 = Student("robi")
print(s2.name)'''

'''class Student:
    collage_name = "Magura polytechnic institute"  # class attribute

    def __init__(self,name,mark):
        self.name = name                      # obj attribute
        self.mark = mark
        print("adding the student database")
        
s1 = Student("nasim",97)
print(s1.name,s1.mark)
s2 = Student("robi",88)
print(s2.name,s2.mark)

print(Student.collage_name)'''


'''class Student:
    collage_name = "Magura polytechnic institute"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Hi! Welcome",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Nasim",97)

s1.welcome()

print(s1.get_marks())'''


'''class Student:
    collage_name = "Magura polytechnic institute"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Hi! Welcome",self.name)


    def get_marks(self):
        print("Your marks is",self.marks)

s1 = Student("Nasim",97)

s1.welcome()

s1.get_marks()'''


################################# pactices qs ###############################

'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi!",self.name,"Your avg marks is ",sum /3)


s1 = Student("Nasim",[98,90,95])

s1.get_avg()'''


'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi!",self.name,"Your avg marks is ",sum /3)


s1 = Student("Nasim",[98,90,95])

s1.get_avg()

s1.name = ("Nasim Uddin")

s1.get_avg()'''


############################## staticmethod ########################

 
'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi!",self.name,"Your avg marks is ",sum /3)


s1 = Student("Nasim",[98,90,95])

s1.hello()
s1.get_avg()

s1.name = ("Nasim Uddin")

s1.get_avg()'''

######################## Abstraction ##############################

'''class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Start the car")

c = Car()
c.start()'''

####################### pactices qs #########################


'''class Accaunt:
    def __init__(self,bal,acc):
        self.balance = bal
        self.accunt_no = acc

    def dabit(self,amount):
        self.balance -= amount
        print("Rs",amount,"is dabit")
        print("total balance = ",self.get_price())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"is credit")
        print("total balance = ",self.get_price())

    def get_price(self):
        return self.balance




acc1 = Accaunt(10000,12345)
acc1.dabit(1000)
acc1.credit(500)
acc1.credit(1500)'''


'''class Accaunt:
    def __init__(self,bal,acc):
        self.balance = bal
        self.accaunt_no = acc

    def dabit(self,amount):
        self.balance -= amount
        print("Rs",amount,"is dabit")
        print("Total balnce",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"is credit")
        print("Total balnce",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Accaunt(10000,12345)
acc1.dabit(500)
acc1.credit(1500)'''









































        
