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