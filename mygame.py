# coding=utf-8
from random import randint
from sys import exit

bag = []

class Scene(object):

    def enter(self):
        print "OK, fine"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print "You died."
        exit(1)

class Center_room(Scene):

    name = raw_input("Welcome to my world traveller. Please tell me your name\n>>>")
    print "Ok, %s I have to tell you something, you are not gonna escape." % name
    print "Yes, It means you now belongs to me, I'll touture you to death."
    print "Struggle for your life and try to run. I'll stare at you."

    def enter(self):

        print "Here have four doors, which one should I go?"
        print ">>>1. North door"
        print ">>>2. West door"
        print ">>>3. South door"
        print ">>>4. East door"

        action = raw_input("> ")

        if action == "1":
            return 'north_room'
        elif "2" in action:
            return 'west_room'
        elif action == "3":
            return 'south_room'
        elif action == "4":
            return 'east_room'
        else:
            print "You should choose one door enter."
            return 'center_room'

class West_room(Scene):

    def enter(self):

        global bag

        if "stick" and "clothes" in bag:
            print "Here have nothing to find."
            return 'center_room'
        else:
            print "You entered the west room.In front of you is a bunch of stick."
            print "Some clothes are messy on the right side."
            print "What do you wanna do?"
            print ">>>1. Take stick."
            print ">>>2. Take clothes."
            print ">>>3. Go back."

            choice = raw_input("> ")

            if choice == "1":
                print "Taken"
                bag.append("stick")
                return 'west_room'

            elif choice == "2":
                print "Taken"
                bag.append("clothes")
                return 'west_room'

            elif choice == "3":
                return 'center_room'

            else:
                print "You have to learn how to print a number."
                return 'west_room'

class South_room(Scene):

    def enter(self):

        global bag

        if "torch" in bag:
            print "Do you wanna burn the dead guy?"
            print ">>>1. Burn it."
            print ">>>2. Go back."

            choice = raw_input("> ")

            if choice == "1":
                print "The dead guy is burning and you find some coins till the fire gone."
                bag.append("coins")
                return 'center_room'
            elif choice == "2":
                return 'center_room'
            else:
                print "Silly boy, print 1 or 2."
                return 'south_room'
        else:
            print "You entered the south room.In front of you is a dead man."
            print "What do you gonna do?"
            print ">>>1. Search it."
            print ">>>2. Go back."

            choice = raw_input("> ")

            if choice == "1":
                print "You find some coins but the dead man stand up and eat your brain."
                return 'death'
            elif choice == "2":
                return 'center_room'
            else:
                print "Choose someting!"
                return 'south_room'

class East_room(Scene):

    def enter(self):

        global bag

        print "A merchant here, what you wanna do?"

        if "coins" in bag:
            print ">>>1. Buy something."
            print ">>>2. Go back."
        else:
            print "You don't have money, I won't trade with you."
            print "Go back."
            return 'center_room'

        choice = raw_input("> ")

        if "1" or "buy" in choice:
            print "You buy a sword."
            bag.append("sword")
            return 'center_room'
        else:
            return 'center_room'

class North_room(Scene):

    def enter(self):

        global bag

        if "sword" in bag:
            print "You split the flame and enter the boss room."
            return 'boss_room'
        elif "stick" and "clothes" in bag:
            print "Do you wanna make a torch?"

            choice = raw_input("> ")

            if choice == "yes":
                print "You have made a torch."
                bag.append("torch")
                return 'center_room'
            elif "back" in choice:
                return 'center_room'
            else:
                return 'death'
        else:
            print "We can not rush into the flame."
            print "We should go back."

            choice = raw_input("> ")

            if choice == "back":
                return 'center_room'
            else:
                return 'death'

class Boss_room(Scene):

    global bag

    def enter(self):
        print "Hahahahah, I'll been wait for you so long, come and fight with me!"
        print "Ahhhhhh!"
        print "I'll kill you then get out of here!"
        print ">>>1. With sword."
        print ">>>2. With torch."

        choice = raw_input("> ")

        if choice == "1":
            print "The boss strike your sword off and kill you."
            return 'death'
        else:
            print "You throw the torch and fire boss's clothes by accident."
            print "The boss was burn to death."
            print "You win!"
            print "You got a key."
            bag.append("key")
            print "You open the gold room with your key."
            return 'gold_room'

class Gold_room(Scene):

    def enter(self):
        print "Countless gold coins here, how much do you get?"

        choice = int(raw_input("> "))

        if choice <= 100:
            print "You got %d coins." % choice
            return 'exit'
        else:
            print "You're a greedy man, you can't get out of here."
            return 'death'

class Exit(Scene):

    def enter(self):
        print "You survived!Congratulation!"
        return 'finished'

class Map(object):

    scenes = {
    'center_room': Center_room(),
    'west_room': West_room(),
    'north_room': North_room(),
    'south_room': South_room(),
    'east_room': East_room(),
    'boss_room': Boss_room(),
    'gold_room': Gold_room(),
    'death': Death(),
    'finished': Exit(),
    'exit': Exit()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('center_room')
a_game = Engine(a_map)
a_game.play()
