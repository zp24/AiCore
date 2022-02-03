
shop = {'prices': {'tomato': 0.87, "sugar": 1.09, "sponge": 0.29, "juice" : 1.89, "foil" : 1.29,
'pack_sizes': {"tomato" : 6, "sugar": 0.5, "sponge": 10, "juice": 1.5, "foil" : 30}}}

a = shop
print(a)
print(type(a)) #<class 'dict'>

tomato = 0.87 * 3
b = tomato
sponge = 0.29 * 2
c = sponge
juice = 1.89 * 3
d = juice
foil = 1.29 * 4
e = foil
sugar = 1.09 * 4
f = sugar

order_subtotal = b + c + d + e + f
print("Order subtotal: ", "£", order_subtotal, "excl. VAT")

print(shop["prices"]) #{'tomato': 0.87, 'sugar': 1.09, 'sponge': 0.29, 'juice': 1.89, 'foil': 1.29, 'pack_sizes': {'tomato': 6, 'sugar': 0.5, 'sponge': 10, 'juice': 1.5, 'foil': 30}}
print(shop["prices"]["pack_sizes"]) #{'tomato': 6, 'sugar': 0.5, 'sponge': 10, 'juice': 1.5, 'foil': 30}
print(shop["prices"]["pack_sizes"]['tomato']/6,) #divides tomato pack size by 6
tomatoes_total_price = shop["prices"]['tomato'] * 3
#print("total price of tomatoes & sponge: ", "£", tomatoes_total_price)
sponge_total_price = shop["prices"]['sponge'] * 2
juice_total_price = shop["prices"]['juice'] * 3
foil_total_price = shop["prices"]['foil'] * 4
sugar_total_price = shop["prices"]['sugar'] * 4

g = tomatoes_total_price
h = sponge_total_price
j = juice_total_price
k = foil_total_price
l = sugar_total_price

order_subtotal1 = g + h + j + k + l
order_total = order_subtotal1 * 1.2 #multiply by 1.2 to get VAT
format_float = "{:.2f}".format(order_total)
print("Total including VAT: ", "£", format_float)
#print(order_total)

print(type(shop["prices"]["tomato"])) #<class 'float'>


tup= ([1,2], [3,4], [5,6])
tup = (1, 5, 4, 1, 8, 1, 5, 2, 2, 2, 1, 8)
print(tup[2:3])
