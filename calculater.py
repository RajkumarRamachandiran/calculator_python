def calculater():
 a=int(input("enter the value:"))
 b=int (input("enter the value:"))
 add=1
 sub=2
 mul=3
 div=4
 print("1)add")
 print( "2)sub")
 print("3)mul")
 print("4)div")
 c=int(input("enter the option:"))
 if(add==c):
    print(a+b)
 elif(sub==c):
    print(a-b)
 elif(mul==c):
    print(a*b)
 elif(div==c):
    print(a/b)
calculater()
