# ----------------not  allow dublicate----------------
set1={1,True,0,False,5,7,7}
print(set1)
# ----------------unorder-----------
set2={4,3,34,6}
set3=list(set2)
set3.sort()
print(set(set3))
# ----------------add and remove---------------
set1.add(5)
print(set1)
set1.remove(5)
print(set1)
set1.update([3,5,2])
print(set1)
try:
 set1.remove(-1)
except Exception:
 print("-1 is not avaliable")
print(set1)
set1.discard(-1)
print(set1)
# ----------------join set------------------

print("set2-> ",set2)
set1.update(set2)
print(set1)
print("set1-> ",set1)
print("set3-> ",set3)
set1.intersection_update(set3)
set1.update([11,22])
print("set1",set1)
print("set2",set2)
set2.difference_update(set1)
set2.update([99,7,5.5,1,11,22])
print("set2",set2)
print("set1",set1)
set1.symmetric_difference_update(set2)
print(set1)
nums1={6,7,8}
nums2={6,7,8,9,0}
print(nums1.issubset(nums2))
print(nums2.issuperset(nums1))
print(nums1.isdisjoint(nums2))
arr4={4,5,6,7,True,1}
arr5={7,8,5,5,False,0}
arr4.add(8)
print(arr4)
arr4.update([9])
print('update after add 9',arr4)
arr4.intersection_update(arr5)
print(arr4)

