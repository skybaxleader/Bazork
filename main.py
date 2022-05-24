def script():
    import random
    import time
    import passTunnel
    import asciiPics
    import lifes
    import fight
    print("You wake up lost underground in a maze of tunnels. You have a bronze sword in your hand and torn leather armor. You light a torch with your flint and steel and try to get your bearings.")
    #starting stats
    lifes.armament = 0
    for i in range(random.randint(10,20)):
        if lifes.lives == 0:
            break
        #choosing a tunnel
        if lifes.wetFeet > 0:
            print("*squish* *squish* You walk up to where two tunnels intersect.")
            lifes.wetFeet = lifes.wetFeet - 1
        else:
            print("You walk up to where two tunnels intersect.")
        tunnelChoice = 0
        while tunnelChoice == 0:
            tunnelChoice = (input("Choose tunnel 1 or tunnel 2: "))
            if tunnelChoice == "1":
                tunnelChoice = 1
            elif tunnelChoice == "2":
                tunnelChoice = 2
            else:
                tunnelChoice = 0
        dangerTunnel = random.randint(1,2)
#combat
        if dangerTunnel == tunnelChoice:
            fight.fightingFunc()
    #non-dangerous tunnels
        else:
            passTunnel.passFunc()
        tunnelChoice=0
    #boss fight
    import bossFight
#finish
    lifes.goldEarned = lifes.goldEarned + bossFight.bossGold
    if lifes.lives >= 1:
        print("You escaped to the surface! You managed to collect", lifes.goldEarned,"gold and killed", lifes.kills, "enemies on your journey! Congratulations adventurer!")
        print(asciiPics.castle.pic)
    else:
        print("You could not escape the long maze of tunnels! You managed to collect", lifes.goldEarned, "gold and killed", lifes.kills, "enemies on your journey!")
    time.sleep(5)
    restart=0
    while restart == 0:
        restart=input("Would you like to play again? (yes or no) ")
        if restart == "yes":
            print("\n\n\n\n\n\n\n\n\n\n")
            lifes.lives = 5
            script()
        elif restart == "no":
            print("Thanks for playing!")
        else:
            restart = 0
script()