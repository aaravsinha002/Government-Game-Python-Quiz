'''
-----TODO-----
Make ask function better to accept different answers
End screen
'''
import pygame
pygame.init()

WHITE=(255,255,255)
GREEN=(0,255,0)

import random, time, os, sys
def t(t): #typewriter effect
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.005)
    print('')

def ask(q,a,at=None): 
    clear = lambda: os.system('cls')
    clear()
    t(q)
    r=input("")
    if r == a.lower() or r == at.lower():
        t("Congrats! You got it correct")
    else:
        t("You got it wrong")

'''
syntax of ask()
ask(q, a, t)
q: question
a: answer from the user in lowercase
t: optional parameter
'''
#hello
def end():
    #make end screen when all questions are correct
    #maybe use gui pop up and show art or an image
    t("Congrats! You finished the entire quiz")
    
    import pygame  
  
    pygame.init()  
    screen = pygame.display.set_mode((500,500))  
    done = False  
    pygame.display.set_mode('Congrats!You finished the Quiz!)
    
    font = pygame.font.SysFont(Arial,24)
    txt=font.render('Game over: Your score was : '+str(score),True,GREEN)
    

    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True
        screen.fill(WHITE)
        screen.blit(txt, (20, 20))
                            
        pygame.display.flip()  
    
    
    
    
#start
t("Welcome to the government quiz made by Aarav, Sebastian, and Ian!")
t("This python program will ask you questions related to the government unit.")
t("Topics are Bill of Rights, government terms, tax, Texas public education and much more!")
tmp=input("Press enter to continue > ")
#start questions here

ask("Which amendment guarantees the freedom of speech, press, religion, and right to assembly? ", "1", "1st")
ask("Which amendment guarantees the right to bear arms (weapons)?", "2", "2nd")
ask("Which amendment prevents soldiers to quarter on any private property without the owner's consent, even during war?", "3", "3rd")
ask("Which amendment prevents governmental officials from seizing or searching private property and items without a probable reason?", "4", "4th")
