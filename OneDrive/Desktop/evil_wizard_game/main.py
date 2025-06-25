# main.py
import random

class Character:
def __init__(self, name, health, max_health, attack_range):
self.name = name
self.health = health
self.max_health = max_health
self.attack_range = attack_range

def is_alive(self):
return self.health > 0

def attack(self):
damage = random.randint(*self.attack_range)
print(f"{self.name} attacks for {damage} damage!")
return damage

def heal(self):
heal_amount = random.randint(10, 20)
self.health = min(self.health + heal_amount, self.max_health)
print(f"{self.name} heals for {heal_amount}. Current health: {self.health}")

def take_damage(self, amount):
self.health -= amount
print(f"{self.name} takes {amount} damage! Remaining health: {self.health}")

def show_stats(self):
print(f"{self.name} - HP: {self.health}/{self.max_health}")


class Warrior(Character):
def __init__(self, name):
super().__init__(name, 100, 100, (15, 25))

def special1(self, target):
print(f"{self.name} uses Power Strike!")
target.take_damage(35)

def special2(self):
print(f"{self.name} uses Battle Roar! (Boosts next attack)")


class Mage(Character):
def __init__(self, name):
super().__init__(name, 80, 80, (20, 30))

def special1(self, target):
print(f"{self.name} casts Fireball!")
target.take_damage(40)

def special2(self):
print(f"{self.name} casts Mana Shield! (Reduces next damage)")


class Archer(Character):
def __init__(self, name):
super().__init__(name, 90, 90, (10, 20))

def special1(self, target):
print(f"{self.name} uses Quick Shot!")
for _ in range(2):
target.take_damage(random.randint(10, 15))

def special2(self):
print(f"{self.name} uses Evade! (Avoids next attack)")


class Paladin(Character):
def __init__(self, name):
super().__init__(name, 110, 110, (10, 18))

def special1(self, target):
print(f"{self.name} uses Holy Strike!")
target.take_damage(25)

def special2(self):
print(f"{self.name} uses Divine Shield! (Blocks next hit)")


class EvilWizard(Character):
def __init__(self):
super().__init__("Evil Wizard", 150, 150, (10, 25))

def regenerate(self):
heal_amount = random.randint(5, 15)
self.health = min(self.health + heal_amount, self.max_health)
print(f"{self.name} regenerates {heal_amount} health! Now at {self.health}.")


def battle(player, enemy):
while player.is_alive() and enemy.is_alive():
print("\n--- Your Turn ---")
print("1. Attack\n2. Heal\n3. Use Ability 1\n4. Use Ability 2\n5. View Stats")
choice = input("Choose an action: ")

if choice == "1":
damage = player.attack()
enemy.take_damage(damage)
elif choice == "2":
player.heal()
elif choice == "3":
player.special1(enemy)
elif choice == "4":
player.special2()
elif choice == "5":
player.show_stats()
enemy.show_stats()
continue
else:
print("Invalid choice.")
continue

if not enemy.is_alive():
print("\n🎉 Victory! You defeated the Evil Wizard!")
break

print("\n--- Evil Wizard's Turn ---")
enemy.regenerate()
damage = enemy.attack()
player.take_damage(damage)

if not player.is_alive():
print("\n💀 Defeat! The Evil Wizard has won.")
break


if __name__ == "__main__":
print("Choose your hero:\n1. Warrior\n2. Mage\n3. Archer\n4. Paladin")
choice = input("Enter your choice: ")
name = input("Enter your hero's name: ")

if choice == "1":
hero = Warrior(name)
elif choice == "2":
hero = Mage(name)
elif choice == "3":
hero = Archer(name)
elif choice == "4":
hero = Paladin(name)
else:
print("Invalid choice. Defaulting to Warrior.")
hero = Warrior(name)

wizard = EvilWizard()
battle(hero, wizard)
