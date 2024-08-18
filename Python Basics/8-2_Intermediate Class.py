# class MageClass:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print("The mage class was creaed.")
#         print(f"Remaining health is {self.health}")
#         print(f"Remaining mana is {self.mana}")

#     def __len__(self):
#         return self.mana
    
#     def attack(self, target):
#         target.health -= 10
    
# class MonsterClass:
#     health = 40

# mage = MageClass(100, 200)
# print(len(mage))

# monster = MonsterClass()
# print(monster.health)
# mage.attack(monster)
# print(monster.health)


# Inheritance
# class WarriorClass:         # bad approach
#     def __init__(self, health):
#         self.health = health

#     def attack(self):
#         print("Attack!")

# class BarbarianClass:
#     def __init__(self, health):
#         self.health = health

#     def attack(self):
#         print("Attack!")

# warrior = WarriorClass(50)
# barbarian = BarbarianClass(100)
# warrior.attack()
# barbarian.attack()

# class HumanClass:
#     def __init__(self,health):
#         self.health = health

#     def attack(self):
#         print("Attack!")

# class WarriorClass(HumanClass):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense

# class BarbarianClass(HumanClass):
#     def __init__(self, health, damage):
#         super().__init__(health)
#         self.damage = damage

# warrior = WarriorClass(50, 8.5)
# barbarian = BarbarianClass(100, 5.5)
# warrior.attack()
# barbarian.attack()
# print(warrior.health)


class HumanClass:
    def __init__(self,health, damage):
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f"Monsters HP is {self.health}"

    def attack(self):
        print("Attack!")
        print(f'Damge amount {self.damage}')

class WarriorClass(HumanClass):
    def __init__(self, health, damage):
        super().__init__(health, damage)

class BarbarianClass(HumanClass):
    def __init__(self, health, damage):
        super().__init__(health, damage)

warrior = WarriorClass(50, 8.5)
barbarian = BarbarianClass(100, 5.5)
warrior.attack()
barbarian.attack()
print(warrior)
# print(warrior.health)