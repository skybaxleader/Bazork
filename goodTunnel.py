class safeTunnel:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
stoneTunnel = safeTunnel("You enter a tunnel with rough stone walls and a small stack of boxes.", 3)
armorTunnel = safeTunnel("You enter a massive tunnel with stacks of broken armor. You find a set of armor your size.", 0)
armorTunnel2 = safeTunnel("You find better armor that fits you. You've never felt safer", 0)
weaponTunnel = safeTunnel("You find a sharper sword made out of strong steel", 0)
weaponTunnel2 = safeTunnel("You find a blade that calls out to you, as if it's meant to be in your hand", 0)
crampedTunnel = safeTunnel("You slowly travel through cramped tunnel that at times requires you to crawl to get through it. You're thankful that you aren't too clausterphobic, but still...", 0)
restTunnel = safeTunnel("You enter a tunnel that smells vaguely of smoke. You find the remains of an old camp. You decide to rest and regain your strength.", 1)
wetTunnel = safeTunnel("You wade through a tunnel with water flowing across the floor. It's not enough to carry you away, but now your feet are wet and your shoes are making squishy noises.", 1)
drinkTunnel = safeTunnel("Enter a mysterious tunnel with runes written along the walls. You find a table and a bottle that says DRINK ME.", 0)
throneTunnel = safeTunnel("You find a giant tunnel with a throne in the middle of it. After poking around near it, you activate a secret compartment with a diamond in it",10)
safeDesc = [stoneTunnel.description, armorTunnel.description, armorTunnel2.description, weaponTunnel.description, weaponTunnel2.description, crampedTunnel.description, restTunnel.description, wetTunnel.description, drinkTunnel.description, throneTunnel.description]
goldList = [stoneTunnel.amount, armorTunnel.amount, armorTunnel2.amount, weaponTunnel.amount, weaponTunnel2.amount, crampedTunnel.amount, restTunnel.amount, wetTunnel.amount, drinkTunnel.amount, throneTunnel.amount]