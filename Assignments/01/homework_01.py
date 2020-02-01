"""Homework 1
"""
'''
    1. what is the difference between a list and a tuple? What is a situation you might want to use a tuple instead
    of a list? (1 POINTS)
'''
a1 = "The key difference between a list and a tuple is that while a list is mutable, a tuple is immutable, meaning that we can modify a list, but not a tuple. We should use a tuple if we want to make sure that no change occurs. For example, someone's unchangeable information such as birthdays should be stored as a tuple to prevent accidental changes."
print(a1 + "\n\n")

'''
    2. the for loop lab described two ways of writing for loops. How were they different? What are the advantages
    of each way of doing it? (1 POINTS)
'''
a2 = "In python, there is a for in loop and an iterative for loop. A for in loop allows direct access to the elements, while an iterative for loop uses an index to loop through the list. If we do not need the index (ie we don't need to care about order of retrieval), or are just grabbing the values from one list, a for in loop is advantageous because we do not have to keep track of the indices. However, if we need the index (ie grabbing the 3rd element first) or are grabbing values from multiple lists, a for loop is advantageous because we can manipulate the order using the indices."
print(a2 + "\n\n")

'''
    3. what do "break" and "continue" do in loops? (1 POINTS)
'''
a3 = "Break statement will terminate the loop right away. The continue statement forces the loop to go back to the start of the loop."
print(a3 + "\n\n")

'''
    3. what is a list "slice"? How do you slice a list, and what is the result? (1 POINTS)
'''
a4 = "A slice is a new list made using the contents of the original list. It can be the whole list, but is usually a partial segment of the original list. To slice, we use the bracket notation (Ex: my_list[1:3]). The result is a new list with values pertaining to the index. In the example provided, it would create a list containing element at index 1 and 2 (3 is excluded)."
print(a4 + "\n\n")


'''
5. there are a bunch of useful things you can do with lists. write code that prints out the result after doing the 
following things to the lists below: 
of the lists below: (5 POINTS)
    a) sort them
    b) get their sizes
    c) concatenate them
    d) get the count of a particular item in a list
    e) remove the duplicates from a list
'''
list_a = [1, 2, 3, 4, 5, 6]
list_b = ["dog", "cat", "lion", "tiger", "rat", "mouse", "rat", "mouse"]

print("answer to 5a")
list_a.sort()
list_b.sort()
print(list_a)
print(list_b)
print("\n")

print("answer to 5b")
print(len(list_a))
print(len(list_b))
print("\n")

print("answer to 5c")
concat_list = list_a + list_b;
print(concat_list)
print("\n")

print("answer to 5d")
concat_list_no_dup = []

for item in concat_list:
  if item not in concat_list_no_dup:
    concat_list_no_dup.append(item)

for thing in concat_list_no_dup:
  print("Count of " + str(thing) + " : " + str(concat_list.count(thing)))

print("\n")

print("answer to 5e")
print(concat_list_no_dup)
print("\n\n")


'''
5. A string can be treated like a list. Write code that that uses the input function to take in a string, and
save it to a variable. Then write a for loop that prints out each letter in the string, one by one. (2 POINTS)
'''
print("answer to question 5")

input_string = input("Type in a string!: ")
for character in input_string:
  print(character)

print("\n\n")

'''
6. You can make a list out of anything, even other lists. Write code that takes in input from the keyboard, and adds
each word to a list. If the list is three items long, add that list as an element to a "master_list". For example, 
if the words "one" through "nine" were typed at the keyboard, the resulting "master_list" should be:
master_list = [["one", "two", "three"], ["four", "five", "six"], ["seven", "eight", "nine"]]
(3 POINTS)
'''

# your code to #6 goes here
master_list = []
temp_list = []

print("Type in as many words as you want! When you are done, type 'done' to generate your new list!!")
count = 0
thing = input("Word #" + str(count + 1) + " : ")
count += 1

while thing != 'done':
  temp_list.append(thing)
  count += 1

  if (len(temp_list) >= 3):
    master_list.append(temp_list)
    temp_list = []

  thing = input("Word #" + str(count) + " : ")

if (not (len(temp_list) == 0)):
  while len(temp_list) < 3:
    temp_list.append('')

  master_list.append(temp_list)

print(master_list)
print("\n\n")

'''
7. you can use the split() function on a string. The result is a list, as shown below. write code that:
    - creates a second list called "type_list" that has all duplicates from first list removed
    - print out the type_lst
    - has a for loop that iterates over each item in "type_list", prints out that word, and prints out how many times it 
      occurs in "token_list", the result should look something like:
      i: 2
      am: 2
      the: 3
      egg: 2
      man: 1
      ...
(3 POINTS)
'''
input_string = "i am the egg man. they are the egg men. i am the walrus. goo goo g'joob."
token_list = input_string.split(" ")
print(token_list)

type_list = []
for item in token_list:
  if item not in type_list:
    type_list.append(item)

print(type_list)

for word in type_list:
  print(word + ": " + str(token_list.count(word)))

print("\n\n")

'''
8. Correctly complete the code for lab_01_05_big5e.py. Paste the code here.
(4 POINTS)
'''

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
for i in range(0, len(question_list)):
  question = question_list[i]
  answer = int(input(question))

  if i % 2 == 1:
    answer *= -1

  answer_list.append(answer)
  final_score += answer

print("Your total extroversion score is: " + str(final_score))

# End of File.