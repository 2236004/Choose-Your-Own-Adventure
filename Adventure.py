from textwrap import fill as raptext
import textwrap


tryagain = "y"
while tryagain.lower() == "y":

    print(raptext("Welcome! I'm thrilled to share an exciting story with you. But before we dive in, I'd like to ask you a few questions. After typing your answers, remember to press the enter key to proceed. Let's embark on this journey together!"))

    while True:
        try:
            name = input("What is your character's name?:  ")
        except ValueError:
            print("I don't understand")
            continue
        if name.isdigit():
            print ("That is a number")
            continue
        if name and not friend.isdigit():
            break
        else: 
            print("Answer cannot be blank!")
            continue
     
    while True:
        try:
            friend = input("What the name of your best freind?:  ")
        except ValueError:
            print("I don't understand.")
            continue
        if friend.isdigit():
            print ("That is a number")
            continue
        if friend and not friend.isdigit():
            break
        else: 
            print("Answer cannot be blank!")
            continue
    
    while True:
        try:
            years = int(input("Choose a number from 1 to 100:  "))
        except ValueError:
            print("You must enter a number greater then 0")
            continue
        if years >= 1: 
            break
        print ("You must enter a number greater then 0")
        continue
    
    while True:
        try:
            rules = input("Do you follow the rules or break them? yes or no:  ").lower()
        except ValueError:
            print("I don't understand.")
            continue
        if rules == "yes" or rules == "no":
            break
        else:
            print("Please answer with 'yes' or 'no'!")
            continue
    
    print(raptext(f"{name} Wakes in the dimly lit confines of a high-security prison, there existed a world of shadows and secrets. The air was heavy with the weight of despair, and the clanking of metal against metal echoed through the narrow corridors, a constant reminder of captivity. Amidst the bleakness, there was one inmate whose spirit refused to be broken. His name was {friend}, a man whose past was shrouded in mystery, his present confined within the unforgiving walls of the prison. Marcus had been incarcerated for a crime he didn't commit. He was a victim of circumstance, a pawn in a game of power and corruption. But despite his innocence, he had accepted his fate with stoic resignation, determined to survive the ordeal with dignity intact."))
        
        

    

    tryagain = input("GAME OVER, do you wish to try again? Enter y/n:").lower()
