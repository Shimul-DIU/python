info={
    'name':'Md.Shimul',
    'roll':7,
    'cgpa':3.55
}
print(info[0][1])
for key,value in info.items():
    print(key,value)
x=info.get('roll')
print(info.keys,info.values)