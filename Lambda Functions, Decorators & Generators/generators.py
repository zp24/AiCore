from random import randint, random, randrange

'''def gen_test():
    print("hello")
    yield 1
    print("it's me")
    yield 2
    print("can you hear me?")
    yield 3
    print("I'm in California dreaming of the life we used to lead")
    yield 4
    print("When we were younger")
    yield 5
    print("I'm not sure if the last line was correct, but I don't know the rest of the song")
    yield 6
    print("..Skips to chorus...")
    yield 7
    print("Hello from the other side")
    yield 8
    print("I must've called a thousand times")
    yield 9
    print("To tell you I'm sorry, for all the things that I've done")
    

gen = gen_test()

#call generator
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
'''
'''
def gen1():
    while True:
     for n in range(1,55):
        yield n

gen_new = gen1()

next(gen_new)
'''
def numGenForever():
    while True:
        for i in range(1,13):
           yield i
y = numGenForever()
next(y)

def gen_test():
    print('Starting the generator')
    yield 1
    print('Second time calling the generator')
    yield 2
    print('Third time calling the generator')
    yield 3
    print('Fourth time. After this, I will die if you call me again')
    yield 4
    print('Why do you hate me?')

gen = gen_test()
#call generator
#next(gen)
#next(gen)
#next(gen)
#next(gen)
#next(gen)

#can call generator in a for loop
#for i in gen:
 #   print (i)

def inf_gen():
    i = 0
    while True:   
        yield i
        i += 1

gen1 = inf_gen()

next(gen1)


random_num = [num for num in range(1, 100)]
print(random()) #prints random float numbers when run
print(randint(1, 100)) #prints random int numbers between 1 and 100

for n in range(1,50):
    n = n **2
    print(n)

print("Random number", randrange(1,100)) #prints a random number between 1 and 100

print("Random integer between 1 and 50:", randint(1,50)) #prints random integer between 1 and 50


def gen_gen():
 greetings = ["hello", "welcome", "ahoy"]

 for x in greetings:
    yield x 
    #for x in x:
     #   if x % 4 ==0:
      #   yield x

gengen = gen_gen()

next(gengen)