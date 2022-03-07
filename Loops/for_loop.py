'''
coding_languages = ['Python', 'Java', 'Go', 'C++', 'Pascal']
for  language in coding_languages:
    print("You need 5 months of experience using " + language)

dict_languages = {'Python': 5, 'Java': 6, 'Go':  3, 'C++': 10, 'Pascal': 15}
for language in dict_languages: #placeholder will take value of keys
    print(language, dict_languages[language]) #keys will only be printed unless value is specified

#using item method of dictionary
for k, v in dict_languages.items(): #tuple keys and values 
    print(f'You need {v} months of experience using {k}')

#iterating through loop a specified number of times
x = range(10) #range(stop)
print(x)
print(type(x))
print(list(x)) #prints list from 0 to 9

for x in range(3, 5): #range(start, stop)
    print(x) #prints 3 and 4 (starts at 3 and finishes up to but does not include 5)

for x in range(100):
    print(x)
    if x == 20:
        break #breaks out of loop once above condition is met

for x in range(5):
    pass #acts as a placeholder when working on new code and wanting to avoid syntax errors
    print("I am out of the loop")

for x in range(5):
    print('before', x)
    if x % 2 == 0:
        continue #will go to the next iteration
    print('after', x)

#list comprehension
cube = []
for i in range(1, 11):
    cube.append(i**3) #prints cube numbers from 1 to 10
print(cube)

cube = [i **3 for i in range(1, 11)]
print(cube) #prints cube numbers from 1 to 10

#dictionary comprehension
cube_dict = {i: i **3 for i in range(1,11)}
print(cube_dict) #prints cube numbers from 1 to 10 but with keys

'''
#total of even numbers
sum = 0
for num in range(1,100):
    if num % 2 ==0: #even numbers between 1 and (but not including) 100
        #print(num) 
        sum += num  #add all even numbers together
print(sum) #total of even numbers added together - needs to be outside of for loop to show final total only

#total of odd numberss
sum = 0
for num in range(1,100):
    if num % 2 ==0: #any even numbers between 1 and (but not including) 100 will be ignored
        pass
    else:
        #print(num) #prints list of odd numbers only
        sum += num  #add all odd numbers together
print(sum) #total of odd numbers added together - needs to be outside of for loop to show final total only