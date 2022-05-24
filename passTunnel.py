import lifes
import goodTunnel
import random
def passFunc():
    tunnelLuck = random.randint(0, 9)
    print(goodTunnel.safeDesc[tunnelLuck])
    lifes.gold = goodTunnel.goldList[tunnelLuck]
    if tunnelLuck == 7:
        lifes.wetFeet = 2
    if tunnelLuck == 9:
        print("It's worth", lifes.gold, "gold!")
    elif tunnelLuck == 0 or tunnelLuck == 7:
        print("You found", lifes.gold, "gold in the tunnel.")
    elif 4 >= tunnelLuck >= 1:
        lifes.armament = lifes.armament + 1
    elif tunnelLuck == 6:
        lifes.lives = lifes.lives + 1
        print("You recover 1 life. You now have", lifes.lives, "remaining and find", lifes.gold,
              "gold at the old camp.")
    elif tunnelLuck == 7:
        lifes.wetFeet = 2
    elif tunnelLuck == 8:
        drinkChoice = 0
        while drinkChoice == 0:
            drinkChoice = input("Do you want to drink it or leave it? ")
            if drinkChoice == "drink" or drinkChoice == "drink it":
                drinkType = random.randint(1, 10)
                if drinkType == 1:
                    lifes.lives = lifes.lives - 1
                    if lifes.lives > 0:
                        print("The drink burns in your stomach after you drink it and you feel weak! You have",
                              lifes.lives, "lives remaining! Maybe don't drink random drinks in caves...")
                    elif lifes.lives == 0:
                        print("The drink burns in your stomach after you drink it and you feel weak! You have",
                              lifes.lives, "life remaining! Maybe don't drink random drinks in caves...")
                    else:
                        print(
                            "As you drink, you begin to feel weak and fall over. The poison was too much for you. Maybe don't drink random drinks in caves...")
                elif 9 >= drinkType >= 2:
                    lifes.lives = lifes.lives + 1
                    print(
                        "As you drink the drink, you feel warmth spread across your body. You recover 1 life. You now have",
                        lifes.lives, "lives left!")
                else:
                    print(
                        "As you drink, a light starts glowing brighter and brighter. When your eyes adjust, you see that you were teleported to the surface!")
                    break
            elif drinkChoice == "leave it" or drinkChoice == "leave":
                print("You leave the drink and continue wandering the maze of tunnels.")
            else:
                drinkChoice = 0
    lifes.goldEarned=lifes.goldEarned+lifes.gold