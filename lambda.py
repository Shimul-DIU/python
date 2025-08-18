# ---------------simple function---------------
def add(j,k):
    result=j+k
    print(result)
add(8,9)
# ------------------lambda function-----------------
nums=[9,9,9,0,8]
num=list(map(lambda x:x+4,nums))
print(num)

def num(n):
    return lambda a :n*a
triple=num(2)
x=triple(3)
print(x)
ans=(lambda x,y:x+y)
print(ans(8,9))

# ------------------filter-----------------
nums=[3,4,5,6]
ans=list(filter(lambda x:x%2==0,nums))
print(ans)