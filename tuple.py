""" name=('shimul',)
print(type(name))
name=('shimul','mustafa',5,6)
print(name)
print(name[0])
try:
 name[0]='rifat'
except Exception:
    print("Tuple are unchangeable and not allow add items")"""

#  --------------------------Update ----------------
old=('shimul',7,'mustafa',8)
new=list(old)
new.append('rifat')
print(tuple(new)) 

old=('shimul',7,'mustafa',8,'rifat',1)
change=('riyan','likhon')
old+=change
print(old)
# """ -----------------------tuple unpack--------------- """
(name,roll,*brotherandNephue,vaste)=old
print(name)
print(roll)
print(brotherandNephue)
print(vaste)