# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#the range to select the secret number from
num_range = range(0, 100)

message = "Number of remaining guesses is "

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    #secret number
    global secret_number
    secret_number = random.choice(num_range)
    #calculates the number of remaining guesses
    global number_of_guesses
    number_of_guesses = int(math.ceil(math.log((max(num_range) - min(num_range) + 1), 2)))
    #Number of remaining guesses message
    global message
    message = "Number of remaining guesses is " + str(number_of_guesses)
    print ""
    if num_range == range(0, 100):
        print "New game. Range is from 0 to 100"
        print message
        print ""
        return
    else:
        print "New game. Range is from 0 to 1000"
        print message
        print ""
        return
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new ga
    global num_range
    num_range = range(0, 100)
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = range(0, 1000)
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here
    global number_of_guesses
    global message
    guess = int(guess)
    print "Guess was " + str(guess)
    
    #check for number of guesses left
    if (number_of_guesses > 1):
        number_of_guesses -= 1
        message = "Number of remaining guesses is " + str(number_of_guesses)
        print message
        
        #check if guess is correct
        if (guess > secret_number):
            print "Lower"
            print ""
            return
        elif (guess < secret_number):
            print "Higher"
            print ""
            return
        else:
            print "Correct"
            print ""
            new_game()
            
    #if no more remaining guesses, start new game
    else:
        number_of_guesses = 0
        message = "Number of remaining guesses is " + str(number_of_guesses)
        print message
        print "You lose!"
        new_game()
        

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)
frame.add_input("Enter your guess", input_guess, 100)
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)


# register event handlers for control elements and start frame


# call new_game 
new_game()

frame.start()
# always remember to check your completed program against the grading rubric
