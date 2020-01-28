X = 'dog'
Y = 'pizza'
Z = 'shoe'

A = '05'
B = 30
C = 4.0

# Problem 00
print("Start of Problem 00")

#print(A+B) - Error
print(B+C)
print(X+Z)
print(Y+A)
#print(Z+B) - Error

print("End of Problem 00")

# Problem 01
print ("Start of Problem 01")

#B += 05 - Error
#print(B)

#D = C ** 01 - Error
#print(D) - Error

D = B / C
print(D)

D = B // C
print(D)

D = B % C
print(D)

print ("End of Problem 01")

# Problem 02
print ("Start of Problem 02")

B = 20
print(B)

print(B == 20)

print ("End of Problem 02")

# Problem 03
print ("Start of Problem 03")

print(X.upper() + " " + str(B + 10))

print ("End of Problem 03")

'''
00. what is the output of the following statements? Why do they do what they do?
    print(A+B) - This will throw an error because concatenating an integer and a string is illegal.
    print(B+C) - 34.0
    print(X+Z) - dogshoe
    print(Y+A) - pizza05
    print(Z+B) - This will throw an error because concatenating an integer and a string is illegal.

01. what do the following statements do:
    B += 05 --> This will throw an error. An integer should should have a leading 0.
    D = C ** 01 --> This will throw an error. An integer should should have a leading 0.
    D = B / C--> D is set to 7.5.
    D = B // C --> D is set to 7.0.
    D = B % C --> D is set to 2.0.

02. What is the difference between the following two statements?
    B = 20 --> This will set B to 20.
    B == 20 --> This will compare B to 20 to see if they are equal. It will return true if they are equal, and false if they are not equal.

03. if you wanted to print out X and B, resulting in "DOG 30", how would you do that?
    print(X.upper() + " " + str(B + 10))

'''