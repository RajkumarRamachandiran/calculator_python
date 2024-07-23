class parent():
    def add(self,a,b):
        c=a+b
        print("answer is:",a,"+",b,"=",c)
class child(parent):
    def sub(self,a,b):
        c=a-b
        print("answer is:",a,"-",b,"=",c)
class child1(child):
    def mul(self,a,b):
        c=a*b
        print("answer is:",a,"*",b,"=",c)
class child2(child1):
    def div(self, a, b):
        c=a / b
        print("answer is:",a,"/",b,"=",c)

a=int(input("enter the value first number:"))
b=int(input("enter the value second number:"))
print("add = +")
print("sub= -")
print("mul= *")
print("div= /")
z=input("enter the option")
result=child2()

if z=="+":
    result.add(a,b)
elif z=="-":
    result.sub(a,b)
elif z=="*":
    result.mul(a,b)
elif z=="/":
    result.div(a,b)
else:
    print("it is not valid")

    