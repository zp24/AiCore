#nested for loops to check for prime numbers - can only be divisible by itself and 1

for i in range(10, 51): #specify range 
        #j = numbers between 2 and i from above range
        for j in range(2, i): #2 is the first prime number 
            if i%j==0: #if i is divisible by all numbers, it is not a prime number
                #e.g. 2 only has 1 and itself as its multiples, whereas 50 has 1,2,5,10 and 25 
                print(i, "is not a prime number")
                break #this is needed otherwise all numbers are labelled as both prime and not prime
        else:
                print(i, "is a prime number")