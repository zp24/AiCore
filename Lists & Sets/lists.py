#%%
my_list = [3.14, "mango", 24, "z", "f", "p", "February", 27]
my_list [0] #3.14 (is the 0th entry)


# %%
my_list [2] #24
# %%
my_list [-1] #27 (indexed from end)
# %%
my_list[0:8] 
#get all items from and including 0 and up to but not including 8
# %%
my_list[-1000:1000] #will go as far back and to the end as possible
# %%
my_list[:6]
# %%
my_list[4:]
# %%
#lists are mutable
my_list[0] = "hello"
# %%
len(my_list)
# %%
my_list.append("new final item")
#appends object to the end of the list
# %%
my_list[0:5:8]
# %%
my_list.extend([1,2,3]) 
#adds each item individually to end of the list
# %%
print(my_list) #prints full list
# %%
my_list.sort() #sort alphanumerically but doesn't return
# %%
my_list.reverse() #reverse order list
# %%
sorted(my_list) #will return something
# %%
