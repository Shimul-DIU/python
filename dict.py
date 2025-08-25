info={
    'name':'Md.Shimul',
    'roll':7,
    'cgpa':3.55
}
for key,value in info.items():
    print(key,value)
x=info.get('roll')
print(info.keys(),info.values())
info.update({'id':5,5:4})
print(info)
# ------------------delete items------------------
info.pop('name')
print(info)
info.popitem()
print(info)
del info['roll']
print(info)
# -------------------nested dict()----------------------
cars={
    'volvo':{
        'id':454,
         'band':'vol',
         'name':'volvo'
    },
    'toyota':{
         'id':457,
         'band':'toyo',
         'name':'toyota'
    },
    'bugati':{
         'id':954,
         'band':'bugati',
         'name':'bugati'
    }
}
for x ,y in cars.items():
    print(x)
    for i,j in y.items():
        print(i+':',j)
""" ---------------------type check in dictionary -------------"""
students={
    'name':'shimul',
    'roll':7,
    'gpa':4.4
}
for info in students.items():
    print(info[2],'-',info[3])
dic_items=students.items()
print(students.items())
print(type(dic_items))
# print(list(dic_items)[0])
dic_items=list(dic_items)
print(dic_items[0])
arr=[2,'shimul']
print(type(arr[1]))
# ----------------loop in dic----------------
print("==================loop in dictionary=============")
print(students)
for info in students.items():
    print(f"{info[0]} -> {info[1]}")
print("==================loop in dictionary=============")
for key,value in students.items():
    print(f"{key} -> {value}")