from datetime import datetime
import dateutil.parser as parser

class Person():

    #friends = [] #applies to all instances - any friends added will be added to each person
    def __init__(self, name, date_of_birth, friends = None): 
        #instance variables
        self.name = name #set name attribute to name passed in initialisation function
        self.date_of_birth = date_of_birth
        #self.friends = friends or [] #initialise as list here
        self.friends = friends
        friends = [] #applies to its respective instance - any friends added will be added to the specific person
        
    def get_name(self):
        return self.name
    
    def get_date_of_birth(self):
        return self.date_of_birth

    def get_friends(self):
        return self.friends
        
    def __str__(self): #show details in a list, with labels
        self.listToStr = ", ".join([str(friend) for friend in self.friends]) #convert list to string
        # ',' used to separate each item in list
        return f"This is {self.name}, born on {self.date_of_birth}, and has {len(self.friends)} friends"
    
    def add_friends(self, friend): #add to list of friends
        self.friends.append(friend)
    
    def __add__(self,other): #add attributes together to be shown in one list
        return self.name + " " + other.name, self.date_of_birth + " " + other.date_of_birth, self.friends + " " + other.friends
    
    def __lt__ (self,other): #compares dates of birth only
        self.date = parser.parse(self.date_of_birth) #converts date to of birth to ISO format
        other.date = parser.parse(other.date_of_birth)
        return self.date < other.date
        

###########################################################
if __name__ == '__main__':
    person = Person("Zoya", "24 February 1994", ["Sarah", "Mary", "Freya"])
    date_of_birth = datetime.strptime(person.date_of_birth, '%d %B %Y')
    person2 = Person("Bob", "29 December 1993", ["Tim", "Alex", "Gary"])
    #print(person2)
    
    person.add_friends("Nate") #add friend to list

    #prints according to attributes and number of arguments passed
    #print("Print details as is:", person.name, person.date_of_birth, person.friends) 

    #print(person.info)
    #print("Adding attributes together: ", person.name + person.date_of_birth + str(person.friends))
    print(person) #prints as string
    print(person2)
   
    print("Comparing date of birth", person.date_of_birth < person2.date_of_birth)
    print(person < person2) #will still compare date of birth only - no need to specify the attribute again as seen above


'''
Assertion is a programming concept used while writing a code where the user declares a condition to be true 
using assert statement prior to running the module. If the condition is True, the control simply moves to the 
next line of code. 
In case if it is False the program stops running and returns AssertionError Exception. 
'''   
# AssertionError with error_message.
'''name = "Dave"
assert name in person.friends, "Invalid Operation - friend not in friend list" 
#friend not in friend list
#message after the ',' is the error message which will appear if there is an Assertion Error
print(name)'''

y = "Bob"
try:
    x = y is person
except AssertionError:
    x = f"{y} is not {person}"
print("Checking this is working:", x)
