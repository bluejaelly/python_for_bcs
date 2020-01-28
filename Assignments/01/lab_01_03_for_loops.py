x = 1

for i in range(10):
    y = x ** 2
    print(i, x, y)

food_list = ['pizza', 'sandwich', 'apple', 'ice cream', 'salad']
score_list = [1, 3, 4, 5, 2]

num_foods = len(food_list)
combined_list = []
for i in range(num_foods):
    new_pair = [score_list[i], food_list[i]]
    combined_list.append(new_pair)
    combined_list.sort()
print(combined_list)


for word in food_list:
    for letter in word:
        print(letter)
    print()

# what will the following code do
# for food in food_list:
#     print(food)

# The code above will each element of the food_list in order they are in the list.

#
# what will the following code do
# num_foods = len(food_list)
# for i in range(num_foods):
#     print(food_list[i], score_list[i])

# First, num_foods takes the value of length of food_list. Then, i will be from 0 (inclusive) to length of food list (exclusive). We print two things at a time, food_list's element at index i and score_list's element at index i.

# what will the following code do
# combined_list = []
# for i in range(num_foods):
#     new_pair = [score_list[i], food_list[i]]
#     combined_list.append(new_pair)
#     combined_list.sort()
# print(combined_list)

# For every element at index i in score_list and food_list, we make a new list containing those two things. Then we put that list into a list called combined_list, and each time, sort them. The sort is done based on the first value of the list, so in this case, by the scores.

# what will the following code do
# for word in food_list:
#     for letter in word:
#         print(letter)
#     print()

# It will first print a letter at a time of the word at index i. Then after the inner for loop, it will print a empty space and continue onto the next whole word available.

# End of File.