from cmath import sqrt
import os


list1 = ["Hello", "World"]

for word in list1:
    print(word.upper()) #prints each word in list in all caps

for x in range(100):
    if x % 5 == 0: #prints out each number that is a multiple of 5
        print(x)

square_dict = dict()
for num in range(1, 15):
    square_dict[num] = num*num
print(square_dict)

### list comprehension ###

listcomp = [x.upper() for x in ["Hello", "World"]] 
print("list comprehension1:", listcomp)

numlist = [x for x in range(100) if x%5==0] 
print("list comprehension2: ", numlist)

### dictionary comprehension ###
# minimal syntax is dictionary = {key: value for vars in iterable}
squares = {num: num**2 for num in range(1, 15)}
print(squares)
print(squares.items()) #dict_items
#items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs
#items() takes no arguments

#inverse_squares = {num: sqrt(num) for num in squares.items()}

for item in squares.items():
   inverse_squares = {item: sqrt(item) for item in range(1, 15)}
print(inverse_squares) #print square root of numbers between 1 and 15
print(inverse_squares.items()) #dict_items

#list of dictionaries
nameList = [
    {"name":"Bob"},
    {"name": "Jeff"},
    {"name": "Sam"}
]
print(nameList) #[{'name': 'Bob'}, {'name': 'Jeff'}, {'name': 'Sam'}]

for my_dictionary in nameList:
    print(my_dictionary["name"]) #Bob, Jeff, Sam


#test = os.getmy_lib()
cwd = os.getcwd()
print(cwd) #C:\Users\Zoya\Desktop\AiCoreScripts #current working directory
#print(test)

file_check = os.listdir("my_lib") #check list of files in my_lib
#not specifying a folder/directory will just list all the files in the current working directory
print(file_check)