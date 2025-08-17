nums=[7,8,9,0,4,5,4]
nums.append(8)
nums.reverse()
print(nums)
""" --------------------silceing items------------------ """
print(nums[:3])#
print(nums[2:])
print(nums[2:6])
print(nums[-1:-3])
print(nums[-3:-1])
print(nums[4:1:-2])
print(nums)
nums.pop()
print(nums)
nums.remove(4)
print(nums)
if 1 in nums:
    print("exist")
else:
    print("not exist")
# -----------------------------insert items-------------------------------------
items=['apple',5,'banana','mango']
items[1:3]=['cherry',3]
print(items)
items=[9,0,8,6,5]
items[1:4]=[7]
print(items)
items[1:2]=[4,6,7]
print(items)
items.insert(1,0)
print(items)
nums={
    0:1,
    'name':'shimul',
    'roll':7
}
items.extend(nums.values())
print(items)
""" -----------------------remove items ------------------------ """
items=[3,5,3,8,6,5,0]
items.pop(2)
print(items)
items.remove(5)
print(items)
del items[0]
print(items)
items.clear()
print(items)
# ---------------------list comprehention------------------------
nums=[2,4,5,6]
n=[x*2 if x%2==0 else x for x in nums]
print(n)
big=[i for i in nums if i<=4]
print(big)
# -----------------list sort---------------------------
nums=[9,0,8,6,5,4]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
def sort(n):
    return abs(n-50)
mylist=[40,9,8,65]
mylist.sort(key=sort)
print(mylist)
name=['shimul','mustafa','Rifat','riyan']
name.sort(key=str.lower)
print(name)
""" -----------------join list------------------- """
list1=[2,3,4,5,2]
list2=['a','n']
print(list1+list2)
""" ----------------------copylist----------------- """
list3=list1.copy()
print(list3)
""" -----------------count items-------------------- """
print(list1.count(2))
""" ----------------index items------------------------ """
print(list1.index(2))
num=[5,6,4,8,3]
num[1:1]=[5,8,9]
print(num)