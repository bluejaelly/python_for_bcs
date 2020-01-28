# describe in a comment what each commented line does
# comment out the lines that generate errors, but make sure you still describe why they dont work

number_list = []

object_list = ['dog', 'cat', 'shoe', 'sock']

print(object_list)

object_list.insert(2, 'tree')

print(object_list)

print("Popping fourth element: " + object_list.pop(3))

print(object_list)

object_list.remove('dog')

print("Removing dog from list")
print(object_list)

object_list.sort(reverse=True)
print(object_list)

print(number_list)
print(object_list)

print(object_list[0])
# print(number_list[0]) - ERROR

number_list.append(5)
number_list.append(6)
print(number_list)

object_list.append('car')
print(object_list)

if 'shirt' in object_list:
    print('shirt is in the list')
else:
    print('no shirt in the list')

object_list[2] = 'shirt'
print(object_list)

if 'shirt' in object_list:
    print('shirt is in the list')
else:
    print('no shirt in the list')

num_items = len(object_list)
print("there are {} items in object list".format(num_items))

'''
    Questions:
    
    00. if i wanted to insert 'tree' into the 3rd position in the object list, so that it does NOT replace any items,
        how do I do that?

        object_list.insert(2, 'tree')

    01. what is the difference between list.pop() and list.remove()
	
		remove() removes the first matching value, while pop removes the element at an index. pop() also returns the popped value, while remove does not.

    02. print out the object list, sorted in reverse alphabetical order

    	object_list.sort(reverse=True)

'''

# End of File.