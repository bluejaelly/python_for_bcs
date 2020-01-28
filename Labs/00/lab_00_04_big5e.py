"""
This is the Big Five Personality Test
    It will help you understand why you act the way that you do and how your personality is structured.
    For each statement 00-50 mark how much you agree with on the scale 00-05, where:
		00=disagree
		01=slightly disagree
		02=neutral
		03=slightly agree
	    05=agree

1. I am the life of the party.
2. I don't talk a lot.
3. I feel comfortable around other people.
4. I keep in the background.
5. I start conversations.
6. I have little to say.
7. I talk to a lot of different people at parties.
8. I do not like to draw attention to myself.
9. I do not mind being the center of attention.
10. I am quiet around strangers.
"""

# write a program that
#   - prints the instructions
#   - asks each question, one at a time, and saves the answer in a veriable
#   - calculate the final score for introversion/extroversion using the following formula:
#       E = 20 + (1) ___ - (2) ___ + (3) ___ - (4) ___ + (5) ___ - (6) ___ + (7) ___ - (8) ___ + (9) ___ - (10) ___
#   - prints out the person's extroversion score

# Instructions
print("This is the Big Five Personality Test")
print("\t" + "It will help you understand why you act the way that you do and how your personality is structured.")
print("\t" + "For each statement 00-50 mark how much you agree with on the scale 00-05, where:")
print("\t" + "\t" + "00=disagree")
print("\t" + "\t" + "01=slightly disagree")
print("\t" + "\t" + "02=neutral")
print("\t" + "\t" + "03=slightly agree")
print("\t" + "\t" + "05=agree")
print("\n")

# Inputs
first = input("1. I am the life of the party.")
second = input("2. I don't talk a lot.")
third = input("3. I feel comfortable around other people.")
fourth = input("4. I keep in the background.")
fifth = input("5. I start conversations.")
sixth = input("6. I have little to say.")
seventh = input("7. I talk to a lot of different people at parties.")
eigth = input("8. I do not like to draw attention to myself.")
ninth = input("9. I do not mind being the center of attention.")
tenth = input("10. I am quiet around strangers.")
print("\n")

# Calculation
E = 20 + int(first) + int(second) + int(third) + int(fourth) + int(fifth) + int(sixth) + int(seventh) + int(eigth) + int(ninth) + int(tenth)

if E <= 20:
	print("Your extroversion score is: " + str(E) + " out of 70!")
	print("You seem pretty introverted!")
	return
elif E <= 50:
	print("Your extroversion score is: " + str(E) + " out of 70!")
	print("You seem neutral!")
	return
else:
	print("Your extroversion score is: " + str(E) + " out of 70!")
	print("You seem pretty extroverted!")
