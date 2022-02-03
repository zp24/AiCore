list_1 = [24, "apple", 0.5, "z", 5**3]

list_2 = [0] * 10 #creates a list of 10 0s

#list_3 = list_1 + list_2
#print(list_3)

#nesting list 1 and list 2 to make list 3
list_3 = [list_1, list_2]
print("list 3: ", list_3)

#print(list_1[3])
#print(list_2[3])
list_4 = [list_1[3], list_2[3]] #4th element from both lists will makeup list 4
print("list 4: ", list_4)

number_plates = ["G06 WTR", "WL11 WFL", "QW68 PQR"]

print(number_plates[2]) #prints 3rd element in list

plate_1 = number_plates[0]
plate_2 = number_plates[1]
plate_3 = number_plates[2]

#extract numbers from each plate
num_chars_1 = plate_1[1:3]
num_chars_2 = plate_2[2:4]
num_chars_3 = plate_3[2:4]

#print type above numbers (all string)
print(type(num_chars_1))
print(type(num_chars_2))
print(type(num_chars_3))

#convert above string to integers
print(int(num_chars_1))
print(int(num_chars_2))
print(int(num_chars_3))

#########

name_list = ["Zoya", "Pasha"]
set1 = set(name_list[0])
set2 = set(name_list[1])
name_char_check = set1.intersection(set2)
print("characters in both names: ", name_char_check) #a is in both names


list_1 = [0] * 10
set3 = set(list_1)
print("length of list_1: ", len(set3))

a = [1,5,"Hello", 8, 6]
b = a[2]
c = a[-1]
d = a[1:4]

print(b)
print(c)
print(d)

arr = [
[[1, 2], [3, 4]],
[[5, 6], [7, 8]]
]

arr1 = arr[-2]
#arr2 = att[-2]
print("arr1: ", arr1)