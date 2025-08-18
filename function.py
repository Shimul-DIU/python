""" # -------------------------xargs------------------
def add(*nums):
    sum=0
    for i in nums:
        sum+=i
    return sum
total=add(3,3,4,5,6)
# ----------------------xxagrs----------------------
print("total is ",total)
def info(**args):
    for key ,value in args.items():
        print(key,value)
info(name='shimul',age=25,roll=8)
# ---------------------default perameter value--------------------
def myfanction(country='bangladesh'):
    print("My country name is :",country)
myfanction()
myfanction('india')
# -------------------------list pass in function----------------
def numsint(num):
    for i in num:
        print(i)
nums=[3,4,5,6,7]
numsint(nums) """
# ------------------------recursion----------------------
def show(n):
    if n==1:
        return 1
    else:
        return n*show(n-1)
   
result=show(6)
print(result)