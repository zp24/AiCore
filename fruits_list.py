fruits = ['banana', 'pineapple', 'apple', 'orange', 'strawberry']

#sorted(fruits, key=reversed) #results in an error

#sorted(fruits, key=True)#results in error - bool object is not callable
#fruits.reverse() #reverses list

#fruits.sort() #puts list in alphabetical order

fruits.sort(reverse=True) #reverses list but in alphabetical order, starting with strawberry
#fruits.sorted()
#fruits.sorted(reverse=True)

print(fruits)

#########

tup = (1, 5, 4, 1, 8, 1, 5, 2, 2, 2, 1, 8)
print(set(list(tup)))
print(set(tup))

fruits = {'apple', 'banana', 'cherry'}

#fruits_2 = {"banana", "cherry", "durian"}, fruits.update(fruits_2)

print(fruits)