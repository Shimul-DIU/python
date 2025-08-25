""" multiplication=1
while True:
    n=int(input())
    if n==0:
        break
    else:
        multiplication*=n
print(multiplication)
# -----------------------count how many items are you given ------------------------
"""
""" shopping=[]
while True:
    n=input()
    if n=='done':
        break
    else:
        shopping.append(n)
print(len(shopping))
 """
students={}
while True:
    name=input()
    if name=='stop':
        break
    else:
        score=int(input())
        students.update({name:score})
print(students)
