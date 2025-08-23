# --------------for loop------------------
for i in range(33):
    print(i)
for i in range(2,33,4):
    if i%2==0:
        print("even:",i)
    else:
        print("odd:",i)
nums=[x*2 if x%2==0 else x for x in range(10)]
print(nums)
nums=[3,2,3,4,'scg']
for i in nums:
    if i==3:
        continue
    print(i)
else:
    print("finished")
# -------------------while loop -------------------------
i=0
while i<10:
    if i==3:
        i+=1
        continue
    print(i*i)
    i+=1
    if i==5:
      break
j=1
while j<10:
    print(j)
    j+=1
else:
    print("last number is 10")
for i in range(5):
    """ if i%2==0:
        print("even",i)
     """
    print(i%2)
num=[9,0,8]
print(num*2)