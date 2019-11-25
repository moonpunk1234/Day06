#Tuple

fruits = ("Mango","Banana","Orange","Mango","Mango")
print(fruits)
#Accessing Elements in a List
print(fruits[1]) #display Banana
#Can not Modify List
#fruits[0] = 'Jambura'
#print(fruits)
x=fruits.index('Banana')
print("Index of Banana : ",x)

print("Index of Orange : ",fruits.index('Orange',0,3))
print("Total Mango :",fruits.count('Mango'))

#print(help(fruits.extend))
print(dir(tuple))
#'count', 'index'
