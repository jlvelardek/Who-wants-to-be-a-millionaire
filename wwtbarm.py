from time import sleep 
import sys
import string
import random

# friend_phone_nmbr = input("Enter this person\'s phone number: ")

#Global Variables
bal=0
calls=1
audience=1

#Strings
welcomefriend = "You have listed your friend %s for the \"call a friend option\""

#Balances
balancestring = "Your balance is: %s razorbucks"
calls_left = "You have " + str(calls)+ " call(s) left"
audience_q = "You have " +str(audience) + " ask the audience left"

#Strings
choices = "Press a, b,c or d and enter to input your answer,\nYou can also type: call a friend, if you wish to use your call\nYou can also type: \'take the money\' if you want to take the money home\n"
takemoneystring = "Congratulations, you have made %s razorbucks playing this game, have fun!"
friend_responds ="%s: Hello...?"
anchor_responds = "Hello %s, your friend %s needs some help answering the following question: \n"
current_question =""
randomanswergen = str(random.choice("abcd"))
friend_final = "\\%s: hmmm... I think the answer is " + randomanswergen




def typer1(x,y):
    for char in x:
        sleep(y)
        sys.stdout.write(char)
        sys.stdout.flush()


def inp():
    global answer_1
    answer_1 = str(input())  

def gameover():
    print(" G A M E     O V E R")
    sys.exit()

def balplus():
    global bal
    if bal == 0:
        bal += 1000
    else:
        bal *= 4

def balminus():
    global bal
    bal = 0

def answeris():
    sleep(2)
    print('... And the answer is...\n')
    sleep(2)
    print('...')
    print('...')

def printbalances():
    print(balancestring % (bal))
    print(calls_left)
    print(audience_q)

def correct_(x):
    global answer_1
    if answer_1 == x:
        answeris()
        print(x.upper()+"!")
        sleep(2) 
        print("You got it man, You win. Never Yield!")
        balplus()
        printbalances()
        pass
    elif answer_1 == "take the money":
        print(takemoneystring % (bal))
        gameover()
    #Virtual friend gives you a random answer
    elif answer_1 == "call a friend":
        global calls
        if calls > 0:
            calls = 0
            print(welcomefriend % (friend_name))
            print("... Ringing ...")
            sleep(3)
            print("... Ringing ...")
            sleep(2)
            print(friend_responds % (friend_name))
            sleep(3)
            print(anchor_responds % (friend_name, participant_name))
            print(friend_final)
            

            

        else:
            print("You already used your call")


    else:
        answeris()
        print(x.upper()+"!")
        sleep(2)
        print("Oh no... incorrect answer, it looks like you have lost all of your money")
        balminus()
        print(balancestring % (bal))
        sys.exit()  

#Program begins

#Welcome Greeting, check balance, friend info

participant_name = input("Enter your name here: ")
print("You are allowed to consult a friend or family member for a question you might not know during the game")
friend_name = input("Enter your friend/familymember\'s name: ")
print(welcomefriend % (friend_name))

print(calls_left)
print('''... Insert Dramatic Music \n
...Drum Roll... \n''')
welcome1=("Hello "+ str(participant_name)+ " and welcome to \"Who wants to be a University of Arkansas Razorbucks Millionaire\n")
typer1(welcome1, 0.02)
print(balancestring % (bal))
sleep(3)

#Question1
current_question ="Here is Question1: What is the mascott from the University of Arkansas? "
print(current_question)
print("a) The T-Rex b) Chihuahua c) Alligator d) The razorback\n")
print(choices)

inp()
correct_('d')

#Question2
current_question="Here is Question 2: How does the crowd call the hogs?"
print(current_question)
print("a) Rawr b) Woof Woof! c) Woo Pig Sooie! d) Meow!\n")
print(choices)
inp()
correct_('c')

#Question3
current_question ="Who is our biggest Rival?"
print(current_question)
print("a) LSU b) NWACC c) A&M d) Bama\n")
print(choices)
inp()
correct_('a')








