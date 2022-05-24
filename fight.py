import random
import chance
import tunnelType
import lifes
import asciiPics
def fightingFunc():
    chance.success = random.randint(1, 20) + lifes.armament
        #combat
    baddy = random.randint(0, 4)
    print(tunnelType.descList[baddy], tunnelType.objList[random.randint(0, 4)])
    if baddy == 4:
        print(asciiPics.dragon.pic)
    combatChoice = 0
    while combatChoice == 0:
        combatChoice = input("Do you want to attack or run? ")
        if combatChoice != "attack" and combatChoice != "run":
            combatChoice = 0
    if combatChoice == "attack":
        if chance.success >= tunnelType.dangerList[baddy]:
            lifes.gold = random.randint(1,4)*tunnelType.dangerList[baddy]
            print("You successfully killed the", tunnelType.nameList[baddy], "and got", lifes.gold, "gold!")
            lifes.kills = lifes.kills+1
        else:
            lifes.lives = lifes.lives-1
            if lifes.lives > 0:
                print("You managed to escape, but lost a life! You have", lifes.lives, "lives remaining")
            elif lifes.lives == 0:
                print("You managed to escape, but lost a life! You have", lifes.lives, "life remaining")
            else:
                print("You were killed by the", tunnelType.nameList[baddy], "!")
    else:
        if chance.success >= 5:
            print("You bolt across the room and escape!")
        else:
            lifes.lives = lifes.lives - 1
            if lifes.lives > 0:
                print("You managed to escape, but took a hit as you ran! You have", lifes.lives, "lifes.lives remaining!")
            elif lifes.lives == 0:
                print("You managed to escape, but took a hit as you ran! You have", lifes.lives, "life remaining!")
            else:
                print("You were killed by the", tunnelType.nameList[baddy], "as you tried to escape it!")
    lifes.goldEarned=lifes.goldEarned+lifes.gold