class Hero: #template
#class variabel
jumlah = 0
def __init__(self, inputName, InputHealth, inputPower, inputArmor):
    # instance variabel
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor
    Hero.jumlah +=1
    print("Membuat Hero Dengan nama " + inputName)

hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000, 100, 0)
print(Hero.jumlah)