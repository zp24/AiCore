
dict_list = [{"name": "Zoya", "skills": ["file handling", "negotiating", "tutoring"]},
 {"name": "Zoya P", "skills": ["coding", "legal", "customer service"] }]

print(type(dict_list))

for my_dictionary in dict_list:
    print("skills: ", my_dictionary["skills"]) #prints list skills from each dictionary
    print("Dictionary data: ", my_dictionary) #prints each dictionary
    print("Dictionary values: ", my_dictionary.values()) #prints values from each dictionary
    

for last_letter in my_dictionary["skills"]:
    if last_letter[-1] == "l":
        print(last_letter) #will print out any skills which end in l - legal

for test0 in my_dictionary["name"]:
    print("Hello:", test0) #prints name from second dictionary 

# find the last letter of the first skill of the last dictionary
for test1 in my_dictionary["skills"]:
    print("Skills:", test1) #prints skills from second dictionary

for test2 in my_dictionary["skills"][0]:
    print("Selected skill:", test2[-1]) #prints "coding" from second dictionary (per letter)

for test3 in my_dictionary["skills"][0][-1]:
    print("Last letter of selected skill:", test3[-1]) #prints "coding" from second dictionary


name_length = [len(name["name"]) for name in dict_list] #list comprehension
print("Name lengths:", name_length) #print length of names

for name in dict_list:
    length_total = len(name["name"]) + len(name["name"]) #add name lengths together
print("Sum of name lengths:", length_total) #print total characters of names 