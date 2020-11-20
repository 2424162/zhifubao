import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ,{ 'a' : 2, 'b' : 3, 'c' : 4, 'd' : 5, 'e' : 6 }]

data2 = json.dumps(data)
print(type(data2))
print(data2)


list1  = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
print(str(list1))
print(type(str(list1)))