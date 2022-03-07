import random

def start_game():
        #starting number of lives 
        lives = 11

        #create an empty list to store the used letters
        used = []

        #words for computer to select for player to guess
        word_select = ["hello", "cat", "chocolate", "water", "dog", "random", "cherry", "tortoise", "rabbit"]

        #select random word from list
        computer_choice = random.choice(word_select)

        display = computer_choice
        for i in range (len(display)):
            #replace each letter with a '_'
            display = display[0:i] + "_" + display[i+1:]

        #print word as dashes at start of game - space between each dash
        print (" ".join(display))

        #player can keep guessing until there are 0 lives remaining
        while display != computer_choice:
         guess_letter = input("Guess the word by selecting a letter: ").lower() #return input in lowercase

         #Add letter to the list of used letters
         used.extend(guess_letter)

         for i in range(len(computer_choice)):
            if computer_choice[i] == guess_letter: #add correct guess to word
                display = display[0:i] + guess_letter + display[i+1:]
                print("Used letters: ") #print letters used so far
                print(used)

         if guess_letter not in computer_choice: 
                lives -= 1 #lose 1 life for every incorrect letter
                print(f"The letter {guess_letter} is not in the word.") #tells player letter is not in word
                print(f"Try again, lives remaining: {lives}") #tells player how many lives are remaining
                print("Used letters: ")
                print(used)
                if lives == 0:
                        print(f"0 lives remaining. Game over. The word was {computer_choice}")
                        break
                continue

         #Print the string with guessed letters (with spaces in between) after each succesful guess)
         print("Current word:", " ".join(display))

        #game ends once all letters have been guessed correctly 
        if display == computer_choice:
            print("Well done, you guessed right!")

    

if __name__ == '__main__':
    start_game()