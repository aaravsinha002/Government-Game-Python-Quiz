'''
-----TODO-----
Make ask function better to accept different answers
End screen
'''
import random, time, os, sys
def t(t): #typewriter effect
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.005)
    print('')

def ask(q,a,at=None): 
    t(q)
    r=input("")
    if r == a.lower() or r == at.lower():
        t("Congrats! You got it correct")
    else:
        t("You suck! You got it wrong")

'''
syntax of ask()
ask(q, a, t)
q: question
a: answer from the user in lowercase
t: optional parameter
'''

def end():
    #make end screen when all questions are correct
    #maybe use gui pop up and show art or an image
    t("Congrats! You finished the entire quiz")
    
    
    
    
#start
t("Welcome to the government quiz made by Aarav, Sebastian, and Ian!")
t("This python program will ask you questions related to the government unit.")
t("Topics are Bill of Rights, government terms, tax, Texas public education and much more!")
tmp=input("Press enter to continue > ")
#start questions here

ask("Which amendment guarantees the freedom of speech, press, religion, and right to assembly? ", "1", "1st")
    
