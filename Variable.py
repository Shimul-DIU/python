a=8
print(id(a))
a=9
print(id(a))
_number =7
print(type(_number))
int_numbers=[9,0,8]
print(type(int_numbers))
intNumber=9
print(id(intNumber))
# Assign multiple Values
a,b,c=8,9,0
print(a,b,c)
print(a,b)
# Assign one value to multiple variables
a=b=c=8
print(a,b,c)
int_list=[9,8,9,0]
num1,num2,*num3,num4=int_list
print(num1,num2,num3,num4)
#Global and Local Variable
x=8
def show():
    # x=7
    print(x)
show()
print(x)
# Global
x=9
def show():
    global x
    x=8
    print(x)
show()
print('global is',x)
binary=4
x=bin(binary)
print(x[2:])
binary=5
x=format(binary,'b')
print(x)
num=7
x=f"{num:b}"
print(x)
x='A'
try:
  y=int(x)
  print(type(y))
except Exception:
   print('error')
print('shimul')
print(ord('a'))
print(chr(65))
