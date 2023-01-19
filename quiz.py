'''
-----TODO-----
Make ask function better to accept different answers

'''
import random, time, os, sys
def t(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)
    print('')

def ask(q,a): #q: question, a: correct answer
    if input(q) == a:
        t("Congrats! You got it correct")
    else:
        t("You suck! You got it wrong")

