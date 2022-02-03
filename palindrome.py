#palindrome - a word which reads the same backward or forward

#x = "pop"
x = "deed"
#x = "blueberry"
#x = "cheese"
y = x[::-1] #[::-1] reverses string

if x == y:
    print(f"{y} is a palindrome of {x}")
else:
    print(f"{y} is not a palindrome of {x}")