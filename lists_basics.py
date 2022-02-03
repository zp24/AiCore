
'''import random
usernames = ["Zzz24", "user1", "user2", "mr_smith123", "neo456"]

print(type(usernames)) #<class 'list'>
print(len(usernames)) #shows list length
print(usernames[0]) #prints first username in list
print(len(usernames[-1])) #shows length of last username

##############
#random.shuffle(usernames) #shuffles order of usernames
#print(usernames) #will print the above shuffled list

####SETS####
set1 = {"apple", "cherry"}
set2 = {"banana", "cherry"}

print(set1.difference(set2)) #will confirm what is in set 2 that is not set 1
print(set1.union(set2)) #will get everything in all sets (apple, cherry, banana)
print(set1.intersection(set2)) #will get everything which is only in both sets (cherry)
print(set1.symmetric_difference(set2)) #will get items which are only in one set (banana, apple)

set1.add("fig") #add new item to set
print(set1)

#set1.remove("fig") #remove item from set but will give an error if it does not exist
#print(set1)

#set1.discard("fig") #will remove but will not give an error if it does not exist

'''
###########

phrase1 = "Clean Couch"
phrase2 = "Giant Table"


#will check if the letters of both words in each phrase are the same
if phrase1[0] and phrase1[6] == phrase2[0] and phrase2[6]:
    #if the same
    print("the first letters of both words in each phrase are the same")
    print("First letters of phrase 1: ", phrase1[0], phrase1[6],"," , "First letters of phrase 2: ", phrase2[0], phrase2[6])
else:
    #if not the same
    print("the first letters of both words in each phrase are not the same")
    print("First letters of phrase 1: ", phrase1[0], phrase1[6], "," ,"First letters of phrase 2: ", phrase2[0], phrase2[6])

my_string1 = "This is a short phrase"
my_string2 = "This is actually a significantly longer phrase than the previous one"

#will print string in reverse
print(my_string1[::-1]) 
print(my_string2[::-1])