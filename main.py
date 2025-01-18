import os
import time

from character import Hero, Goblin, Dragon


def battle(hero, enemy):
    print(f"\nBattle Start: {hero.name} vs {enemy.name}")
    while hero.isAlive() and enemy.isAlive():

        print("\nChoose an action:")
        print("1. Attack")
        print("2. Special Attack")
        print("3. Heal")
        print(f"\n")

        choice = input("> ")
        if choice == "1":
            hero.attack(enemy)
            hero.health_bar.draw()
            enemy.health_bar.draw()
        elif choice == "2":
            hero.special_attack(enemy)
            hero.health_bar.draw()
            enemy.health_bar.draw()
        elif choice == "3":
            hero.heal()
            hero.health_bar.draw()
            enemy.health_bar.draw()
        else:
            print("Invalid choice!")

        if enemy.isAlive():
            print(f"\n")
            time.sleep(2)
            enemy.attack(hero)
            hero.health_bar.draw()
            enemy.health_bar.draw()

    if hero.isAlive():
        print(f"\n{hero.name} defeated {enemy.name}!")
    else:
        print(f"\n{hero.name} was defeated by {enemy.name}...")

def main():
    print("Welcome to Heroes of OOP!")
    name = input("Enter your hero's name: ")
    hero = Hero(name, 100, 100, 15, 30)

    enemies = [Goblin(), Dragon()]
    for enemy in enemies:
        if hero.isAlive():
            battle(hero, enemy)
        else:
            break

    if hero.isAlive():
        print("\nCongratulations! You have defeated all enemies!")
    else:
        print("\nGame Over. Better luck next time!")

if __name__ == "__main__":
    main()
