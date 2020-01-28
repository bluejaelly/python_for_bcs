"""in this homework, type all your answers as string variables that get printed out, so that your TA can run the
    program and see all of your answers.
"""

'''
    00. what are the difference between variables, statements, and expressions in python? (3 POINTS)
'''
# type your answer here
a0 = "Variables are used to store information to be used by the program. Their values can change. A statement on the other hand is a syntactic combination that represents some action to be carried out by the program. A statement is usually a standalone unit of execution, meaning that no values are returned. An expression is a combination of constants, variables, operators, and functions to be interpreted by the compiler. Unlike a statement, an expression returns the new value."
print(a0 + "\n\n")
'''
    01. what is the difference between a string, an integer, and a float variable in python?
        what is a situation where if you thought something was a float, and instead it was an int, you might get in 
        trouble? What is a situation where if you thought somethinng was a int, and instead it was a string, you
        might get in trouble? (3 POINTS)
'''
# type your answer here
a1 = "String, or a string literal, consists of series of characters. They are used to represent English characters, words, phrases, sentences, and more. Strings are surrounded by either single or double quotations. On the other hand, an integer represents whole numbers and their negative equivalents, as well as zero. Unlike an integer, a float can represent decimal points. More specifically known as floating point numbers, a float can represent decimal point numbers. There really is no issue with assuming that something is a float and it turns out to be an int. This issue only existed in Python 2 where integer to integer division did not give the exact answer including the decimals. On the other hand, if you thought something was an int and it turned out to be a string, you may run into many issues. For example, mathematical expressions would throw an error. Concatenating a string to an int or the other way around will throw an error."
print(a1 + "\n\n")

'''
    02. what is the difference between an operator and an operand? What is the difference between the following kind
    of operators (3 POINTS):
    - Arithmetic Operators
    - Comparison (Relational) Operators
    - Assignment Operators
    - Logical Operators
    - Identity Operators
'''
# type your answer here
a2 = "An operator is a symbol that represents some action to be performed by the compiler. For example, + is an operator that concatenates or adds. Operands are the things that are acted on and manipulated by the operators. For example, in 1 + 1, the 1's are the operands, and the + is the operator. An arthmetic operator, such as +, -, /, and *, is an operator that performs mathematical caculation on two operands. A Comparison operator, such as >, >=, <, <=, and ==, allows comparison between two values. The result of the comparison is either true or false. An assignment operator, such as =, is used to set or re-set a new value to a variable. Logical operators, such as not, and and or, are used to control the flow of the program. They mostly involve boolean manipulation. Identity operators, such as is and is not, are used to determine class or type membership of a value. For example, (type(5) is int) will return true."
print(a2 + "\n\n")

''' 
    03. Describe the difference behavior between the two following lines of code (1 POINT):
      if not (x > 02) or (y > 02):
      if not ((x > 02) or (y > 02)):  
'''
# type your answer here

a3 = "The two problems differ in what is being affected by the not keyword. In the first line of code, the not keyword is affecting (x > 02), meaning that the if statement is true if x is not greater than 02 or y is greather than 02. In the second line of code, the not keyword is affecting ((x > 02) or (y > 02)), meaning that the if statement is true if ((x > 02) or (y > 02)) is false. "
print(a3 + "\n\n")

''' 
    05. Write a program that asks for a temperature in celcius and converts it to farenheit, and prints it out. 
    (3 POINTS)
'''
# type your answer here

celsius = input("Type in a temperature in Celsius: ")
fahrenheit = (float(celsius) * (9/5)) + 32
print(celsius + " degrees celsius in fahrenheit is: " + str(fahrenheit))
print("\n\n")

''' 
   06. write a program that asks you to type in the score of five exams, one at a time, and calculates and
        prints the mean score, the highest score, the lowest score, and the average score dropping the lowest score. 
        The output should look this this: (7 POINTS)
        
        Mean Score: 89.5343
        Lowest Score: 70
        Highest Score: 100
        Mean After Dropping Lowest: 92.412
'''
# type your answer here

print("Hello! Please type in 5 exam scores")
score1 = input("Exam score 1: ")
score2 = input("Exam score 2: ")
score3 = input("Exam score 3: ")
score4 = input("Exam score 4: ")
score5 = input("Exam score 5: ")
print("Mean Score: " + str((float(score1) + float(score2) + float(score3) + float(score4) + float(score5)) / 5))
minScore = min(float(score1), float(score2), float(score3), float(score4), float(score5))
print("Lowest Score: " + str(minScore))
print("Highest Score: " + str(max(float(score1), float(score2), float(score3), float(score4), float(score5))))
print("Mean After Dropping Lowest: " + str((float(score1) + float(score2) + float(score3) + float(score4) + float(score5) - minScore) / 4))

print("\n\n")
print("Done!")

# End of file