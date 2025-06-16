import random
from datetime import datetime
def play():
    r = random.randint(1,10)
    print("Choose a level:E for Easy,M for medium, H for hard")
    level= input("enter your level").upper()
    if (level=="E"):
        count=5
    elif(level=="M"):
        count=3
    elif(level=="H"):
        count=1
    else:
        count=3
        print("no proper level.default level is medium")
    
    gusses=[]

    while count!=0:
        try:
            n = int(input("enter a number from 1 to 10:"))
            gusses.append(n)
        except ValueError:
            print("please enter a valid number")
            continue
        if (n>10 or n<1):
            print("please enter number between 1 and 10")
            continue
        if (r==n):
            ans="won"
            print("correct")
            Save= input("do you want to save it(Y/N)").upper()
            if(Save=="Y"):
               save(ans,r,gusses)
                
            break
        else:
            ans="lost"
            print("wrong")
            print("you have",count-1,"left")
            if (count==1):
                print("you lost.the correct number was:",r)
                Save= input("do you want to save it(Y/N)").upper()
                if(Save=="Y"):
                    save(ans,r,gusses)
        count-=1   


def save(ans,r,guesses):
    with open("results.txt","a") as f:
        f.write(f"Result: {ans}\n")
        f.write(f"correct: {r}\n")
        f.write(f"Timestamp: {datetime}\n")
        f.write(f"Gusses: {guesses}\n")


        
while True:
    play()
    again=input("do you want to play game again(Y/N)").upper()
    if again=="Y":
        play()
    else:
        print("thanks for playing.")
        break
