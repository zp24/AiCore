order_list = [("tom", 0.87, 4), ("sug", 1.09, 3), 
          
          ("ws", 0.29, 4), ("juc", 1.89, 1), 
          
          ("fo", 1.29, 2)]

names = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "juc":"Juice","fo":"Foil"}

budget = 10.00

running_total = 0

receipt = []

x = running_total

items_and_prices = zip(names.values(), order_list)
print(list(items_and_prices))
'''
for k, v, z in order_list.items():
    print("Item Code: {}\nPrice: £{}\n".format(k, v, z))
    if x > budget:
     print("Budget Exceeded!")
    else:
     print("Adding full name of item (quantity)")
     '''

my_list = [34, 52, 71, 39, 22, 73, 92]
for num in my_list:
    if num %2 ==0: #only looks at even numbers
        print(f"square of {num} is {num**2}") #shows number and its square
    else: #any other number
        x = num + 1 #adds 1 to the number
        print(f"add 1 to {num} to get {x}, and the square of this is {x**2}")

'''my_list = [34, 52, 71, 39, 22, 73, 92]
for i in my_list:
    if i %2 ==0:
     y = my_list.append(i**2) #prints cube numbers from 1 to 10
     print("even numbers", y)
    else:
     x = i +1
     w = my_list.append(x**2)
     print("odd numbers", w)'''

my_list = [34, 52, 71, 39, 22, 73, 92]

for x in my_list:
    
    squares = x**2 if x%2==0  else (x+1)**2
    y = x+1
    print(f"{y} is squared to {squares}")
'''if x%2 ==0:
   my_list.append(x**2)

  else:
    y = x + 1
    my_list.append(y**2)
    print(my_list)'''

