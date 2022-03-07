import random
import string

def remove_alphabet(): #function to remove letters of the alphabet from set upon user input
    string.ascii_letters
    x = string.ascii_lowercase
    print (string.ascii_lowercase)

    
    while 0 < len(x) <=26:
     test1 = input("pick a letter: ").lower()
     if test1 in x:
        y = x.replace(test1, "")
        x = y
        print(x)
        continue
     else:
         print("letter removed, try again")
         continue
    if len(x) == 0:
        print("all letters removed")

#remove_alphabet() #to run function

def add_alphabet(): #function to add letters of the alphabet to set upon user input
    alphabet_set = set()

    while len(alphabet_set) < len(string.ascii_lowercase):
        test2 = input("add a letter: ")
        if test2 not in alphabet_set: #only adds input if not in set already
            alphabet_set.add(test2)
            print(sorted(alphabet_set)) #sorts out letters in alphabetical order
        else:
            print("try again") #will tell user that the letter is already in the set
    if len(alphabet_set) == len(string.ascii_lowercase): #will run once all 26 letters of the alphabet are added to the set
        print("all letters added")

#add_alphabet() #to run function
'''lives = 5
words = ["hello", "goodbye"]

x = random.choice(words)
print(x)

guessed_letters = set()

while 0 < lives <= 5:
 test = input("select a letter: ").lower()
 for idx, character in enumerate(x):
    if test in character:
        #if character in x:
         #   "*"[id] = character
        print(test)
        guessed_letters.add(test)
        y = guessed_letters
        print(y)
        continue
    else:
         print("_")

if lives == 0:
    print("game over")
    '''
'''
words = ["hello", "jam", "yellow", "bat", "guess"]

choose_word = random.choice(words)
print(choose_word)
display = choose_word
#replace each letter of word with .
for i in range(len(display)):
    display = display[0:i]+ "." + display[i+1:]


#print("word: ", choose_word)
#print("".join(current_display))
print("".join(display))

guess_word = ""
used_letters = []

lives = 5
while lives >= 0 : #keep guessing until length of guess matches chosen word
    print(f"lives: {lives}")
    user_input = input("guess a letter of the word: ")
    #for i in range(len(choose_word)):
     #if choose_word[i] == user_input:
        #guess_word.add(user_input)
        #guess_word += user_input
        #used_letters.append(user_input)
        #print("used letters", used_letters)
      #  display = display[0:i] + user_input + display[i+1:]
        #print("_", end="")
        #print(guess_word, "\n", end=" ")
        #print("".join(display))
    for i in range(len(choose_word)):
     if user_input == choose_word[i] and choose_word[i] == user_input:
      display = display[0:i] + user_input + display[i+1:]
      print("Guess: ", "".join(display))
      #y = choose_word.replace(user_input, "")
      #x = y
      #print(x)
    if user_input not in choose_word:
         lives -=1
         print(f"lives remaining: {lives}")
         continue
    else:
        print("try again", "\n")
        lives -=1
        print(f"lives remaining: {lives}")
        #used_letters.extend(user_input)
        #print("used letters", used_letters)
        continue
     
    #else user_input not in choose_word[i]:
     #   lives -=1
      #  print(f"lives remaining: {lives}")
if display == choose_word: #game ends once length of guess_word matches chosen word
    print(f"well done, you have guessed the word: {choose_word}")  
if lives == 0:
    print("game over")'''

#Fix an AssertionError
x = 0
try:
    answer = 1/x
except ZeroDivisionError:
    answer = "undefined"
print(f"answer is {answer}")

date1 = "24 February 1999"
date2 = "29 December 1993"

print(date1 < date2)

num_sides = -1
#try:
#           x =  num_sides > 0
#except AssertionError:
#           x = "needs a number of sides"
#print(x)

assert num_sides > 0, "incorrect"