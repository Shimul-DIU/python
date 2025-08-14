""" def total(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    print(total_sum)

n = int(input("Given how many numbers: "))
num = [int(input()) for i in range(n)]
total(num)

def total(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    print(total_sum)

n = int(input("Given how many numbers: "))
num=[]
for i in range(n):
    num.append(int(input()))
total(num)
even_nums = [if x % 2 == 0 for x in range(10) ]
print(even_nums)  # [0, 2, 4, 6, 8]
 """

""" s='shimul'
print(id(s))
s+='d'
print(id(s))
print("mutable")
li=[9,0,9]
print(id(li))
li.append(7)
print(id(li))
num=9
print(id(num))
num=8
print(id(num)) """

print(pow(4,4))



