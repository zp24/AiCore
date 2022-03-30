import random

class RPS:
    options = []
    def print_options(self):
        # Print the options:
        self.options = ['rock', 'paper', 'scissors']
        #self.options = []
        #print('(1) Rock\n(2) Paper\n(3) Scissors')
        print(self.options)
    
    def get_human_choice(self):
        # Let the user choose
        human_choice = self.options[int(input('Enter the number of your choice: ')) - 1]
        # Print the user's choice
        #print(f'You chose {human_choice}')
        return human_choice

    def get_computer_choice(self):
    # Make the computer choose one option amongst the options list
        self.computer_choice = random.choice(options)
        # print the computer's choice
        #print(f'The computer chose {computer_choice}')
    
    def print_choices(self,human_choice, computer_choice):
        print(f'You chose {human_choice}')
        print(f'The computer chose {computer_choice}')

    def print_result(self,human_choice, computer_choice):
        # Print the results
        if human_choice == 'rock':
            if computer_choice == 'paper':
                print('Sorry, paper beat rock')
            elif computer_choice == 'scissors':
                print('Yes, rock beat scissors!')
            else:
                print('Draw!')
        elif human_choice == 'paper':
            if computer_choice == 'scissors':
                print('Sorry, scissors beat paper')
            elif computer_choice == 'rock':
                print('Yes, paper beat rock!')
            else:
                print('Draw!')
        elif human_choice == 'scissors':
            if computer_choice == 'rock':
                print('Sorry, rock beat scissors')
            elif computer_choice == 'paper':
                print('Yes, scissors beat paper!')
            else:
                print('Draw!')
    def print_win_lose(self,human_choice, computer_choice, human_beats, human_loses_to):
        if computer_choice == human_loses_to:
            print(f'Sorry, {computer_choice} beats {human_choice}')
        elif computer_choice == human_beats:
            print(f'Yes, {human_choice} beats {computer_choice}!')

rps = RPS()

rps.options = ['rOck', 'paper', 'scissors']

rps.print_options()
human_choice = rps.get_human_choice
#computer_choice = rps.get_computer_choice
#rps.print_choices(human_choice, computer_choice)
#rps.print_result(human_choice, computer_choice)