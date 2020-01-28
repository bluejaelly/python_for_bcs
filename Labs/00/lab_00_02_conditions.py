X = 1
Y = 2
Z = 10

A = '00'
B = '01'
C = '10'
D = 'dog'

if C == D:
    print("Same")
else:
    print("Different")

if C > D:
    print(C)
else:
    print(D)

'''
    change the above code to compare:
        Y & Z - Y and Z are different, and Z is printed because Z is larger than Y.
        X & Z - X and Z are different, and Z is printed because Z is larger than X.
        A & B - A and B are different, and B is printed because B is "larger" than A. Larger means alphabetically/numerically behind.
        A & C - A and C are different, and C is printed because C is "larger" than A. Larger means alphabetically/numerically behind.
        B & C - B and C are different, and C is printed because C is "larger" than B. Larger means alphabetically/numerically behind.
        C & D - C and D are different, and D is printed because D is "larger" than C. Larger means alphabetically/numerically behind. Alphabets are behind numerical strings.
        Z & C - Z and C are different. The second if-else statement throws an error because > operator is not supported in comparison between a string and an int.
'''

# what will this "AND" code do? - AND makes sure that both conditions are considered in the if statement. If and only if both are true, the condition inside the if statement will be true, meaning even if one of the statements is false, the condition as a whole becomes false.
if (X > Z) and (int(A) == X):
    print("Success")
else:
    print("Fail")

# what about this "OR" code? - OR will stop when finding a condition that is true. This means that as long as one of the conditions are true, the condition as a whole becomes true. If both are false, the condition as a whole becomes false.
if (X > Z) or (int(A) == X):
    print("Success")
else:
    print("Fail")

# is this is the same as the AND code or the OR code? - This is the same as the AND code.
if X > Z:
    print("Success")
else:
    if int(A) == X:
        print("Success")
    else:
        print("Fail")
# how would you change it to make it behave like the other one   
# in other words, if the code above is like the AND code, change it to behave like the OR code
# but continuing to use two separate if statements instead of one combined one - Use an elif statement (see below):

    #if X > Z:
        #print("Success")
    #else:
        #if int(A) == X:
            #print("Success")
        #else:
            #print("Fail")
