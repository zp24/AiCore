
shop_dict = {"tom":0.87, "sug":1.09, "ws":0.29, "cc":1.89, "ccz":1.29}

shop_dict.keys()

names_dict = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "cc":"Coca-Cola", "ccz":"Coca-Cola Zero"}
filtered_shop = []

for key, value in shop_dict.items():
    if value > 1.00: #only values which are more than 1.00 will be printed
        print("Values above 1.00:", key, value)
        filtered_shop.append(names_dict[key]) #add items with a value more than 1.00 to list by name
print(filtered_shop) #print list of items with a value above 1.00