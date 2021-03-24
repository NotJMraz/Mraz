# coding=utf-8
from sys import exit

print "Hey, wake up, you need to get out of here. Tell me your name."
name = raw_input("> ")
print "%s, I will make you out of here, trust me." % name

knapsack = []

def dead(why):
    print why
    exit(0)

def center_room():
    print "Here have 4 rooms, which do you wanna get in?"

    choice = raw_input("> ")

    if "north" in choice:
        north_room()
    elif "east" in choice:
        east_room()
    elif "south" in choice:
        south_room()
    elif "west" in choice:
        west_room()
    else:
        print "Just tell me which room"

def north_room():
    global knapsack
    if "sword" in knapsack:
        print "You split the flame with your sword and go through it."
        print "You enter the boss room."
        boss_room()

    elif "stick" and "clothes" in knapsack:
        print "Do you wanna make a torch?"

        choice = raw_input("> ")

        if "yes" in choice:
            print "You got a torch."
            knapsack.append("torch")
        else:
            north_room()

    else:
        print "There has a flame wall, we can not go through it, what can wo do?"
        print "back or rush into the flame?"

    choice = raw_input("> ")

    if "back" in choice:
        center_room()
    elif "rush" in choice:
        dead("You burning!")
    else:
        print "Well, just back or rush into it, OK?"
        north_room()

def west_room():
    global knapsack
    print "There have some wooden stick and clothes, what you goona do?"

    choice = raw_input("> ")

    while True:
        if "stick" in choice:
            print "You got a wooden stick. What you gonna do?"
            knapsack.append("stick")
            choice = raw_input("> ")
            if "clothes" in choice:
                print "You got some clothes. What you gonna do?"
                knapsack.append("clothes")
                print knapsack
            else:
                knapsack = ["stick"]
                continue
        elif "back" in choice:
            center_room()
        else:
            print "Do you wanna take stick or clothes?"
            west_room()

def south_room():
    global knapsack
    print "Here have a dead man, do you wanna search?"

    choice = raw_input("> ")

    if "yes" in choice:
        print "You get some coins. What do you gonna do?"
        knapsack.append("coins")

        choice = raw_input("> ")

        if "back" in choice:
            center_room()
        else:
            dead("The dead man stand up and eat your brian.")
    else:
        dead("The dead man stand up and eat your brian.")

def east_room():
    global knapsack
    print "You see a business man stay here. What do you gonna do?"
    choice = raw_input("> ")

    if "buy" in choice:
        print "You get a sword."
        knapsack.append("sword")
        east_room()
    elif "back" in choice:
        center_room()
    else:
        east_room()

def boss_room():
    global knapsack
    if "key" in knapsack:
        print "Do you wanna go outside?"

        choice = raw_input("> ")

        if "yes" in choice:
            print "You finally out of here, congratulation!"
            exit(0)
        else:
            dead("So you gonna live here with me? Right? The Aside killed you.")
            exit(0)
    else:
        print "what do you gonna do?"

        choice = raw_input("> ")

        if "fight" in choice:
            print "You fight with the boss and you win."
            print "You got a key."
        else:
            dead("The boss kill you and eat your legs.")
            exit(0)

        knapsack.append("key")

        print "Here have two rooms, select one room: Gold room or Exit?"

        choice = raw_input("> ")

        if "gold" in choice:
                gold_room()
        else:
            print "You finally out of here, congratulation!"
            exit(0)

def gold_room():
    global knapsack
    print "Here is the golden room, do you wanna get some gold?"

    choice = raw_input("> ")

    if "yes" in choice:
        print "You get some gold."
        print "You need to go, %s" % name
        knapsack.append("gold")
        boss_room()
    else:
        boss_room()

center_room()
