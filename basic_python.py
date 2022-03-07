#assign string to variable and print
long_word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
print (long_word)

#len() counts number of letters in string
print ("number of letters: ", len(long_word)) #45


#index first letter of above string
first_c = long_word[0] #first letter will be given an assignment of 0
#print first letter only
print("First letter: ", first_c)

#index last letter of above string
#because first letter is assigned 0, final letter will be one less (44)
last_c = long_word[44] 

print("Last letter: ", last_c)

#add last and first letters together
sum = 's' + 'p'
print("last + first letter = ", sum)


#####################################################
#basic operations
a = 42
b = 25

sum_new = a + b
print (sum_new)

difference = a - b
print(difference)

product = a * b
print (product)

#a = 4.2
division = a/b 
print (division) #when a = 4.2, answer is now 0.168

#type() is used for debugging purposes & to determine type of text extracted
print(type(sum_new)) #prints <class 'int'>

print(type(long_word)) #prints <class 'str'>

##########

sum1 = 0.75 + 1044 #can add an int and float together
print(sum1) #1044.75

sum2 = 2000 - 955.25
print(sum2) #1044.75

c = 27%3 #% is the modulo operator
print (c) #if there is no remainder, modulo operator will return 0
#here, the answer is 0 because 27 can be divided by 3 equally and is a multiple of 3

d = 1 + 2 * 3 - 4 / 6 * (6+7) * 8 ** 9 #-1163220302.3333333
print(d)

e = 24/4

#floor division - divides and rounds number down to nearest integer
f = 24//5

g = 24/5

print(e)
print(f)
print(g)
