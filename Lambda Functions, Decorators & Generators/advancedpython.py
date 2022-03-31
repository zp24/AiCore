import pandas as pd #give pandas alias of pd
from pandas import DataFrame #import DataFrame class from pandas

word_list = [] #empty list

def simple_func():
    user_input = input("enter a word: ")
    user_input = word_list.append(user_input) #add input to list
    
    #print length of list
    print("length of list: ", len(word_list))
    char_wordlist = [len(word) for word in word_list]
     
    for word in word_list:
     #print each word
      print("one word in the list is: ", word)
     #print length of each word
      print("length of word is:", len(word))

        
    #show number of characters in each word in list
    print("length of each word in list:", char_wordlist) 
    #total sum of all characters in list
    print("sum of all the characters in the list:", sum(char_wordlist)) 
    
    
i = 0
while i < 5:        
        simple_func()  
        i +=1  #add item to list 5 times
        
if i == 5:
    print(word_list)
 
    


