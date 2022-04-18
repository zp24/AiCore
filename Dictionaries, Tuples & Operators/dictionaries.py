one_deep_dictionary = {
    'start here':1,
    'k1':[1,2,3, #k1 is a list
    {'k2':[1,2,
    {'k3':['keep going', {'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]
    }

d = one_deep_dictionary

#print('Python' in one_deep_dictionary) #reads False
print(d['start here']) # 1
print(d['k1']) #[1, 2, 3, {'k2': [1, 2, {'k3': ['keep going', {'further': [1, 2, 3, 4, [{'k4': 'Python'}]]}]}]}]
print(d['k1'][0]) #1
print(d['k1'][1]) #2
print(d['k1'][2]) #3
print(d['k1'][3]) #{'k2': [1, 2, {'k3': ['keep going', {'further': [1, 2, 3, 4, [{'k4': 'Python'}]]}]}]}
print(d['k1'][3]['k2']) #[1, 2, {'k3': ['keep going', {'further': [1, 2, 3, 4, [{'k4': 'Python'}]]}]}]
print(d['k1'][3]['k2'][0]) #1
print(d['k1'][3]['k2'][1]) #2
print(d['k1'][3]['k2'][2]['k3']) #['keep going', {'further': [1, 2, 3, 4, [{'k4': 'Python'}]]}]
print(d['k1'][3]['k2'][2]['k3'][0]) #keep going
print(d['k1'][3]['k2'][2]['k3'][1]) #{'further': [1, 2, 3, 4, [{'k4': 'Python'}]]}
print(d['k1'][3]['k2'][2]['k3'][1]['further']) #[1, 2, 3, 4, [{'k4': 'Python'}]]
print(d['k1'][3]['k2'][2]['k3'][1]['further'][0]) #1
print(d['k1'][3]['k2'][2]['k3'][1]['further'][1]) #2
print(d['k1'][3]['k2'][2]['k3'][1]['further'][2]) #3
print(d['k1'][3]['k2'][2]['k3'][1]['further'][3]) #4
print(d['k1'][3]['k2'][2]['k3'][1]['further'][4]) #[{'k4': 'Python'}]
print(d['k1'][3]['k2'][2]['k3'][1]['further'][4][0]) #{'k4': 'Python'}
print(d['k1'][3]['k2'][2]['k3'][1]['further'][4][0]['k4']) #Python

print(type(d['k1'][3])) #<class 'dict'>

x = 10
user_input = int(input("pick a number: "))
n = user_input

if n > x:
    print(f"{n} is greater than {x}") #add f in otherwise {n} and {x} will just print
else:
    print("None", f"{n} is not greater than {x} ")
    

print(99 > 5) #True
print(0 == False) #True
print(1 == True) #True
print(6.2 < 7) #True
print(9 >= 9) #True
print(False < True) #True

print('AAA' > 'BBB') #False
print('AAB' > 'AAA') #True
print('aaa' > 'AAA') #True 

