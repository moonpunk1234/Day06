#Dictionaries
#==================================

#A dictionary in Python is a collection of key-value pairs. Each key is connected 
#to a value, and you can use a key to access the value associated with that key. 

#'clear', 'copy', 'get', 'items', 'keys', 'update', 'values'

#variable = {}
#dict.update(dictValue)
#del dict[Key]
#dict.items() dict_items([('Rahim', 12), ('Karim', 12), ('Joya', 25), ('Sarah', 9)])
#dict.keys()
#dict.values()
#list(dict.items())

#Students = list(Dict.keys())
#Students.sort()
#len(dict))

# Add three key-value tuples to the dictionary.
#dict[key] = value
#dict.get(key)
#dict.get(key, defaultValue)
# Sort the keys from the dictionary.
#keys = sorted(hits.keys())
# Loop and display tuple items.

"""
for rentItem in rentItems:
    print("Place:", rentItem[0])
    print("Cost:", rentItem[1])
    print("")

# Create a dictionary.
data = {"a": 1, "b": 2, "c": 3}
# Loop over items and unpack each item.
for k, v in data.items():
    # Display key and value.
    print(k, v)
"""

person = {'1':'Ali','2':'Chand','3':'Moon','4':'Munaz','5':'Nazmul',}
print(person)

person.update({'6':'Hridita'}) #if exist then change if not then add
print(person)

person.update({'6':'Ali'}) #if exist then change if not then add
print(person)
del person['6']
print(person)

print(person['3'])

#dict.keys()
for var in person.keys():
  print(var)  
  
for var in person.values():
	print(var)
	
for var in person.keys():
  print(var,person[var])
 
 #list(dict.items())
for var in list(person.items()):
   print(var)

boys={'3':'Moon','1':'Rony','5':'John','4':'Cony','2':'Conte'}   
#Students = list(Dict.keys())

students = list(boys.keys())
print(students)

#students sort
students.sort()
print(students)

for key in students:
	print(key,boys[key])

print(len(boys))	
	
animal={}

animal[1]= 'Lion'
animal[2]= 'Tiger'
animal[3]= 'Elephant'
animal[4]= 'Fox'
print(animal)

print(animal.get(1))
print(animal.get(10))
print(animal.get(10,'No data found'))


#keys = sorted(hits.keys())

keys = sorted(animal.keys())
for key in keys:
	print(key)
