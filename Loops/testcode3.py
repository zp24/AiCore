order_list = [("tom", 0.87, 4), ("sug", 1.09, 3), 
          
          ("ws", 0.29, 4), ("juc", 1.89, 1), 
          
          ("fo", 1.29, 2)]

names = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "juc":"Juice","fo":"Foil"}

budget = 10
running_total = 0

receipt = []
remaining_budget = budget - running_total

shop = True
while shop:

 for k, v, z in order_list:
    #block continues until there are no more values to go through
    for i in names.values():
     names[k] = i  #k is the item code
    #by adding names[k], each element will be cycled through, otherwise it is last element only (fo/foil)
    if running_total <= 10:  #will loop until budget has exceeded
        print("\nItem Code: {}\nPrice: £{}".format(k, v, z))
           
        print(f"Adding {i}, quantity {z}") #show product name and quantity 
        print(f'Full price is £{v * z}.') #full price is quantity * price

        budget = budget - v #subtract price from budget
        running_total +=v #add price to running total
            
        print(f"Remaining budget £{budget:02f}".format(float), f"running total: {running_total}")
    
    else:
        print("\nBudget Exceeded!")
        shop = False
        break

receipt.append(running_total) #add running total to receipt
print("Receipt: £", receipt) #print receipt 