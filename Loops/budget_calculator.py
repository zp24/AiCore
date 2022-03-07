order_list = [("tom", 0.87, 4), ("sug", 1.09, 3), 
          
          ("ws", 0.29, 4), ("juc", 1.89, 1), 
          
          ("fo", 1.29, 2)]

names = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "juc":"Juice","fo":"Foil"}

budget = 0

running_total = 0

receipt = []
print(type(order_list))
items_and_prices = zip(names.values(), order_list)
#print(list(items_and_prices))

'''for item in range(0,5):
    receipt.append(order_list[item][1]*float(order_list[item][2]))
    
    print(receipt)'''

############
shop = True
while budget < 10:
 for k, v, z in order_list:
    #block continues until there are no more values to go through
    for i in names.values():
     names[k] = i 
    #by adding names[k], each element will be cycled through, otherwise it is last element only (fo/foil)
    '''y = float(v)*z
    
    
    running_total += float(y)
    remaining_budget = budget - running_total
    #receipt = running_total
    print("\nItem Code: {}\nPrice: £{}".format(k, v, z))
    
    if running_total >= budget:
     print("\nBudget Exceeded!")
     receipt.append(running_total)
     break
    else:
     
     print(f"Adding {k}, quantity {z}")
     print(f'Full price is £{y}.'.format(float),f'Running total is £{running_total}. Remaining budget is £{remaining_budget}'.format(float))'''

    if 0< running_total <= 10:
        print("\nItem Code: {}\nPrice: £{}".format(k, v, z))
        #y = budget - v
    
        #running_total = y
        remaining_budget = budget - running_total
        
        print(f"Adding {k}, quantity {z}")
        print(f'Full price is £{v * z}.')

        budget = budget - v #remaining budget
        running_total +=v #what has been spent so far
        
        print(f"Remaining budget £{budget:02f}".format(float))
        
    if budget == 10:
        print("\nBudget Exceeded!")
        shop = False
    #break
receipt.append(running_total)
print("Receipt: £", receipt)



     

'''my_list = [34, 52, 71, 39, 22, 73, 92]
for num in my_list:
    if num %2 ==0: #only looks at even numbers
        print(f"square of {num} is {num**2}") #shows number and its square
    else: #any other number
        x = num + 1 #adds 1 to the number
        print(f"add 1 to {num} to get {x}, and the square of this is {x**2}")



my_list = [34, 52, 71, 39, 22, 73, 92]

for x in my_list:
    #y = x+1
    squares = [x**2 if x%2==0  else (x+1)**2]
    print(squares)
    if x%2==0:
     print(f"{x} is squared to {squares}")
    else:
     print(f"{x} is squared to {squares} when you add one before squaring")'''

####

    
'''def calculate_price(*args, **kwargs):
    order_total = args[0]
    running_total = 0
    budget = 10.0
    for k, v, z in order_list:
        print("\nItem Code: {}\nPrice: £{}".format(k, v, z))
        running_total += v
        
        print(f"Adding {k} to the list. Running total is {running_total}")
        budget -= v
        print(f"Remaining budget is", budget)
    return order_total * running_total

cost = calculate_price(1.1, tomatoes = 1.2, potatoes = 0.75, chocolate = 3.2)
print("new", round(cost, 2)) '''
