steps = "?" #to be printed
n = 5

## square pattern ##
print("\nsquare pattern")
#outer loop holds row numbers
for i in range(n):
    #inner loop holds column numbers
    for j in range(n):
        print(steps, end=" ")
    print()

## increasing triangle pattern ##
print("\nincreasing triangle pattern")
for i in range(n):
    #inner loop holds column numbers
    for j in range(i+1): #set inner loop to i+1 to increase number of steps in each row by 1
        print(steps, end=" ")
    print()

## decreasing triangle pattern ##
print("\ndecreasing triangle pattern")
for i in range(n):
    #inner loop holds column numbers
    for j in range(i, n): #set inner loop start range as i 
        print(steps, end=" ")
    print()

## increasing and decreasing triangle pattern without nested for loops ##
print("\n increase and decrease without nested for loops")
for n in range(n+1):
    print(steps * n)

for n in range(n,0,-1):
    print(steps * n)