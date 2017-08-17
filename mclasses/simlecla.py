class Student:
    def __init__(self,first,last,email,mobile,address):
        self.first = first
        self.last = last
        self.email = email
        self.mobile = mobile
        self.address = address
    def fullname(self):
        return "{} {}".format(self.first,self.last)

st1=Student('santhosh','kumar','ysk@gmail.com',123456,'ipm')

print "fulludetails:",st1.first,st1.last,st1.email,st1.address

print st1.fullname()
