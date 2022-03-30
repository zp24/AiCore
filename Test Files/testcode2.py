	
import unittest
import random

#create a list of hangman words
wordList = ["cat","dog","mouse"]

#choose a word from the list at random
wordChosen = random.choice(wordList)

#create an empty list to store the used letters
used = []

#create a variable to store and display the player's guesses  
display = wordChosen
for i in range (len(display)):
  #replace each letter with a '_'
  display = display[0:i] + "_" + display[i+1:]
  
#put a space between each dash
print (" ".join(display))

#counter stops the game once all letters have been guessed correctly
attempts = 0
lives = 5

#keep asking the player untill all letters are guessed
while display != wordChosen:
  guess = input("Please enter a letter: ")
  #guess = guess.lower()
  #Add the players guess to the list of used letters
  used.extend(guess)
  attempts +=1
  print ("Attempts: ")
  print (attempts)
  
  #Search through the letters in answer
  for i in range(len(wordChosen)):
    if wordChosen[i] == guess:
      display = display[0:i] + guess + display[i+1:]
      print("Used letters: ")
      print(used)

  if guess not in wordChosen:
      lives -= 1
      print("try again", f"lives remaining: {lives}")
      print("Used letters: ")
      print(used)
      print ("Attempts: ")
      print(attempts)
      if lives == 0:
            print("game over")
            break
      continue
  

  #print("Used letters: ")
  #print(used)
      
  #Print the string with guessed letters (with spaces in between))
  print(" ".join(display))
  #attempts +=1
if display == wordChosen:
    print("Well done, you guessed right!")

unittest.main()