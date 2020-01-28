class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.can_move = True
        self.can_grow = True

    def say_hello(self):
        print("\nMy name is {}".format(self.name))

class Bird(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.has_wings = True
        self.has_feathers = True
        self.can_fly = True

    def say_tweet(self):
        print("\nTweet Tweet Tweet!".format(self.name))


def q1():
    print("Question 00")
    # What kind of data structure is a turtle?
    your_answer = ""
    print(your_answer)


def q2():
    print("Question 01")
    # What are three examples of turtle attributes?
    # What are three examples of turtle methods?
    your_answer = ""
    print(your_answer)


def q3():
    print("Question 02")
    # When you print out a instance of a class, you get the ugly class-instance 23f1s23g421 nonsense.
    # In the reading, you read about a way to create a class method that gives you control over what prints
    # out. What is the name of the special method? Create a method for the Animal class above that, when
    # you print the class instance as is done below, prints out all the attributes of that class.

    jon = Animal("jon")
    print(jon)


def q4():
    print("Question 03 is worth 01 points")
    # add a function called clean_lyrics to last week's analyze lyrics program, that removes capital letters
    # and punctuation.
    your_answer = ""
    print(your_answer)


def q5():
    print("Question 05 is worth 05 points")

    """Write a separate program called zombies.py, that:
        creates a class "Human" and a class "Zombie that inherits from class turtle. 
        
        each human's init function should:
            - make human's shape a human image (a 50x50 pixel '.gif' file
            - put pen up
            - move human to a random location
            - make a "speed" attribute set to 50
            
        each zombie's init function should:
            - make zombie's shape a zombie image (a 50x50 pixel '.gif' file
            - put pen up
            - move zombie to a random location
            - make a "speed" attribute set to 75
    
        create a method for zombie called "chase", where the zombie
            - turns in the direction of the nearest human
            - moves in that direction up to zombie.speed units to catch the human
        
        create a method for the zombie called "attack", which is called by "chase" if zombie gets within 25 units of 
        the human. this function should:
            - kill the human turtle
            - replace it with a zombie turtle
            - add the new zombie to the zombie list
            - remove the human from the human list
        
        create a method for the human function called "run_away", that
            - picks a direction to run away (you can decide how the human chooses what direction)
            - move up to human.speed units in that direction
            
        in main function
            -create a human_list with H human instances (a variable that you change)
            -create a zombie_list with Z zombie instances (a variable that you can change
        
        create a loop that runs for NUM_TURNS times (or until all humans are dead), on each turn:
            - cycles through each zombie, calls their chase function, and if appropriate, calls their attack function
            - cycles through each human, and calls their run function
    
        
        

    """

def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()

main()