class tunnel:
    def __init__(self, description, danger, name):
        self.description = description
        self.danger = danger
        self.name = name
goblinTunnel = tunnel("A goblin jumps", 5, "goblin")
trollTunnel = tunnel("A troll lumbers", 8, "troll")
manticoreTunnel = tunnel("A manticore leaps", 10, "manticore")
dragonTunnel = tunnel("A small dragon scurries", 12, "small dragon")
adultTunnel = tunnel("A roar and blast of heat great you as a full grown dragon emerges", 15, "adult dragon")
descList = [goblinTunnel.description, trollTunnel.description, manticoreTunnel.description, dragonTunnel.description, adultTunnel.description]
dangerList = [goblinTunnel.danger, trollTunnel.danger, manticoreTunnel.danger, dragonTunnel.danger, adultTunnel.danger]
nameList = [goblinTunnel.name, trollTunnel.name, manticoreTunnel.name, dragonTunnel.name, adultTunnel.name]
class tunnel:
    def __init__(self, description):
        self.description = description
crates = tunnel("from behind a tall pile of crates stacked on the side of the room.")
chasm = tunnel("from inside a wide chasm spanning most of the room.")
pillar = tunnel("around a massive set of stone pillars supporting a high cave roof.")
window = tunnel("into the light being cast down from tall windows carved into the roof of the cave.")
stal = tunnel("out from an area dense with stalagmite formations, creating a great hiding place.")
objList = [crates.description, chasm.description, pillar.description, window.description, stal.description]