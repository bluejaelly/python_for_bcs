"""This is the Big Five Personality Test
    It will help you understand why you act the way that you do and how your personality is structured.
    For each statement 00-50 mark how much you agree with on the scale 00-05, where:
		1=disagree
		2=slightly disagree
		3=neutral
		4=slightly agree
	    5=agree

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

# Last week, you wrote a program where each question was stored in a different variable.
# This week, write a program that
#       - stores the questions in a question_list.
#       - prints the instructions
#       - has a for loop that iterates over the list, each time through the loop
#           - asks the question
#           - saves the response to an answer_list
#           - also updates their final_score
#       - once the loop is done, the program should print out their final extroversion score

# Instructions
question_list = ['I am the life of the party.', 'I don\'t talk a lot.', 'I feel comfortable around other people.',
				 'I keep in the background.', 'I start conversations.', 'I have little to say.',
				 'I talk to a lot of different people at parties.', 'I do not like to draw attention to myself.',
				 'I do not mind being the center of attention.', 'I am quiet around strangers.']

print("This is the Big Five Personality Test")
print("\t" + "It will help you understand why you act the way that you do and how your personality is structured.")
print("\t" + "For each statement 00-50 mark how much you agree with on the scale 00-05, where:")
print("\t" + "\t" + "1=disagree")
print("\t" + "\t" + "2=slightly disagree")
print("\t" + "\t" + "3=neutral")
print("\t" + "\t" + "4=slightly agree")
print("\t" + "\t" + "5=agree")
print("\n")

answer_list = []
final_score = 0
for question in question_list:
	answer = int(input(question))
	answer_list.append(answer)
	final_score += answer


if final_score <= 15:
	print("Your extroversion score is: " + str(final_score) + " out of 50!")
	print("You seem pretty introverted!")
elif final_score <= 40:
	print("Your extroversion score is: " + str(final_score) + " out of 50!")
	print("You seem neutral!")
else:
	print("Your extroversion score is: " + str(final_score) + " out of 50!")
	print("You seem pretty extroverted!")

# End of File.