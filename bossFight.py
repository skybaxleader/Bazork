import random
import lifes
bossDeath = 0
class bossEnemy:
    def __init__(self, name, descriptionBoss, weapon, danger, bossReward):
        self.name = name
        self.descriptionBoss = descriptionBoss
        self.weapon = weapon
        self.danger = danger
        self.bossReward = bossReward
Klarg = bossEnemy("Klarg", "a giant bugbear", "a gleaming war ax.", 15, 5)
Strahd = bossEnemy("Strahd", "a cunning vampire", "sharp fangs and long clawlike nails.", 17, 7)
Acererak = bossEnemy("Acererak", "a cold and glowering demi-lich", "tendrils of black energy radiating from him.", 20, 10)
bossName = [Klarg.name, Strahd.name, Acererak.name]
bossDesc = [Klarg.descriptionBoss, Strahd.descriptionBoss, Acererak.descriptionBoss]
bossWeapon = [Klarg.weapon, Strahd.weapon, Acererak.weapon]
bossDanger = [Klarg.danger, Strahd.danger, Acererak.danger]
bossMultiplier = [Klarg.bossReward, Strahd.bossReward, Acererak.bossReward]

combatChoice = 0
bossChoice = random.randint(0, 2)
print("You stumble into a grand tunnel. As you look around in wonder at the size of it, you see",
      bossDesc[bossChoice], "with", bossWeapon[bossChoice], "'My name is",
      bossName[bossChoice], "' he says, 'and I am the one who is going to kill you.'")
for i in range(5):
    while combatChoice == 0:
        combatChoice = 0
        combatChoice = input("Do you want to attack or run? ")
        if combatChoice != "attack" and combatChoice != "run":
            combatChoice = 0
    success = random. randint(1,20)
    if combatChoice == "attack":
        if success >= bossDanger[bossChoice]:
            bossGold = bossMultiplier[bossChoice] * bossDanger[bossChoice]
            print("You successfully killed", bossName[bossChoice], "and found", bossGold, "gold in his pouch!")
            lifes.kills = lifes.kills + 1
            bossDeath=1
            break
        else:
            lifes.lives = lifes.lives - 1
            if lifes.lives > 1:
                print("You take a hit and lost a life! You have", lifes.lives, "lives remaining")
            elif lifes.lives == 1:
                print("You take a huge blow and only have 1 life remaining")
            else:
                print("You were killed by", bossName[bossChoice], "!")
                break
    else:
        if success >= 5 and lifes.lives == 1:
            print("You bolt across the room and escape", bossName[bossChoice],
                  "'s grasp! You slam the door and lock it from the outside. You're safe... for now.")
            break
        elif lifes.lives == 1 and success <= 5:
            print("As you attempted to escape,", bossName[bossChoice],
                  " lunges at you and makes a killing blow!")
            break
        else:
            print(bossName[bossChoice], "blocks your exit.")
if bossDeath == 0:
    print(bossName[bossChoice]), "looks at you in terror, realizing how hard it is to kill you. He turns around and runs out the exit to the tunnels."
    combatChoice = 0