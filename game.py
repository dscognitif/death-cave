import random, time


gamePlay = True


def displayIntro():
    print("You are in a land in which Chuck Norris resides") 
    print("He hides in the darkness ready to pounce")
    print("Sometimes he is friendly and will provide you with assistance to further your journey")
    print("Other times he will destroy you like he destroyed your mother.")
    print("You are at a crossroads, there are two pathways) 
    print("You have to choose a pathway ...") 
    print()


def displayCaveEntrance():
    print("You walk towards the pathway...")
    time.sleep(2)
    print("It is  ")
    time.sleep(2)
    print("You see Chuck Norris walking towards you.....") 
    time.sleep(2)
    print("And Then he.... !!!")
    time.sleep(2)
    
    

while gamePlay:
    goodCave = random.randint(1, 2)

    displayIntro()
    print("Which pathway would you like to go into? (1 or 2)")
    playerChosenCave = int(input())
    if playerChosenCave == goodCave:
        displayCaveEntrance()
        print("You have been blessed with Chuck Norris wisdom:)")
        time.sleep(1)
        print("Congratulations! you have won, you may continue on your journey:")
    else:
        displayCaveEntrance()
        print("He gives you a wink.")
        time.sleep(1)
        print("You are perplexed")
        time.sleep(3)
        print("He approaches you") 
        time.sleep(2)
        print("You are nervous as he is coming closer at you ...")
        time.sleep(2)
        print("You then see him unzipping his pants ......")
        time.sleep(2)
        print("He then proceeds to anal rape the shiznit out of you")
        time.sleep(1)
        print("You die a happy man:(")

    print()
    print("Do you want to play again? (yes or no)")
    playAgain = str(input()).lower()

    if playAgain in ['yes', 'y']:
          gamePlay = True
    else:
          gamePlay = False




exit(0)