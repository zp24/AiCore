import random
import string

words = ["hello", "cat", "water", "dog", "random", 
"cherry", "tortoise", "rabbit", "chocolate", "lentils", "juice"]

alphabet = set(string.ascii_lowercase)

class Hangman():

    def __init__(self, lives, guess_word):
        self.lives = lives
        lives = 10 #starting number of lives
        self.guess_word = guess_word

        self.word_letters = set(guess_word) #letters in the word
        self.used = set() #list of letters player has used

    def welcome(self):
        return "Welcome to Hangman!" #message to print when code is run

    #get player guess
    def get_user_input(self):

        user_input = input("Select a letter: ").lower()
        return user_input
        

    #play game
    def play(self):
        
        while len(self.word_letters) > 0: #keep playing until all letters are guessed   
         
         #show list of used letters
         print("Used letters: ", " ".join(self.used))
         
         #keep track of player's progress
         self.word_list = [letter if letter in self.used else "_" for letter in guess_word]
         print("Word: ", " ".join(self.word_list))

         user_input = self.get_user_input() #call user input function and assign to variable - needs to be in while loop for game to work properly

         for i in range(len(guess_word)):
            
          if user_input in alphabet and guess_word[i] == user_input:
            #self.used.add(user_input) #add letter to used list           
            if user_input in self.word_letters:
                    self.word_letters.remove(user_input) #remove letter from word 
         if user_input not in guess_word:
                self.lives -=1 #deduct 1 life for an incorrect letter
                print(f"\n{user_input} is not in the word. Lives remaining: {self.lives}") #tells player letter is not in word and lives remaining
                if self.lives == 0:
                    print(f"\nGame over. The word was {guess_word}") #game ends when 0 lives remain
                    break
         self.used.add(user_input) #add letter to used list - works properly here
         
        if len(self.word_letters) == 0: #game ends when all letters have been removed/guessed correctly
           print("\nWord: ", guess_word) 
           print("Well done, you guessed correctly!")
                

if __name__ == '__main__':
    guess_word = random.choice(words) #call word list
    #print(guess_word) #print word to guess
    #print(len(guess_word)) #print length of word to guess
    hangman = Hangman(10, guess_word) #call class - lives and word to guess specified
    print(hangman.welcome()) #print opening message
    hangman.play() #call function to play game