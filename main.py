from clothing import *
from handle_input import *

# Room functions

def morning():
    print "You made it! Nice!\n"
    print "You fall into bed and pass out.\n"
    print "...\n"
    print "...\n"
    print "It's morning and your mum comes in to wake you up.\n"
    if pyjamas: # if there is something in pyjamas list, True
        print "'Good morning sweetie, breakfast is ready.'\n"
        print "You made it to your room & into your pyjamas without being caught.\n"
        print "You win!\n"
        exit(0)
    else:
        why = "'Why are you asleep in your clothes? Did you get drunk last night?\n"
        grounded(why)


def squeak():
    print "As you walk along the hallway towards your room, the floorboards make a loud squeak.\n"
    print "You're right outside your mum's room!\n"
    room_flair = "Run for it, or freeze?\n"

    choice2 = handle_choice(False, room_flair)

    invalid = True

    while invalid:
        choice2 = choice2.title()
        if "Run" in choice2:
            print "Your mum stirs, but doesn't see anyone in the hall so falls back to sleep.\n"
            morning()
            invalid = False
        elif "Freeze" in choice2:
                print "You freeze and hold your breath. Your mum stirs and sees you.\n"
                why = "'Why are you home so late? Are you drunk?!'\n"
                grounded(why)
                invalid = False
        else:
            print "That's not a valid input.\n"
            choice2 = raw_input(room_flair)

def hallway_cont():
    print "You continue along the hallway and up the stairs.\n"
    print "Your bedroom is just down the hall, but you'll have to walk past mum's bedroom to get there.\n"
    print "She's a light sleeper, and her door is open.\n"
    print "If you sleep in the guest room, you won't have to walk past mum's room.\n"
    room_flair = "Go left to your bedroom, or right and crash in the guest room?\n"

    choice2 = handle_choice(False, room_flair)

    invalid = True

    while invalid:
        choice2 = choice2.title()
        if "Left" in choice2:
            squeak()
            invalid = False
        elif "Right" in choice2:
                print "You sneak into the guest room and fall into the bed, exhausted.\n"
                print "...\n"
                print "AAAAAAHHHHH!\n"
                print "Oh no, Aunt Judy is staying over, and she does not seem pleased that you just climbed into bed with her!\n"
                why = "The whole house wakes up from all the yelling.\n"
                grounded(why)
                invalid = False
        else:
            print "That's not a valid input.\n"
            choice2 = raw_input(room_flair)

def awake():
    print "You run past the room as fast as you can, trying to tip-toe as you go.\n"
    print "It doesn't work, you accidentally wake up your dad!\n"
    print "Dad: 'Where have you been? Why are you home so late?'\n"
    room_flair = "Tell the truth, or lie?\n"

    choice2 = handle_choice(False, room_flair)

    invalid = True

    while invalid:
        choice2 = choice2.title()
        if "Lie" in choice2:
            print "He falls for your lies and goes back to the couch.\n"
            hallway_cont()
            invalid = False
        elif "Truth" in choice2:
                why = "Dad: You're too young to be out late drinking!\n"
                grounded(why)
                invalid = False
        else:
            print "That's not a valid input.\n"
            choice2 = raw_input(room_flair)

def hallway():
    print "You walk through the front door and can see the light pouring into the hallway from the living room.\n"
    print "The TV is on high volume and you can hear your dad snoring from the couch.\n"
    print "The snoring stops and your dad stirs, calling out in his confused slumber.\n"
    print "'Is someone there?'\n"
    room_flair = "Run past the room and hope he stays asleep, or freeze?\n"

    choice2 = handle_choice(False, room_flair)

    invalid = True

    while invalid:
        choice2 = choice2.title()
        if "Run" in choice2:
            awake()
            invalid = False
        elif "Freeze" in choice2:
                print "You freeze, holding your breath...\n"
                print "...\n"
                print "Phew, he fell back to sleep.\n"
                hallway_cont()
                invalid = False
        else:
            print "That's not a valid input.\n"
            choice2 = raw_input(room_flair)

def backgarden():
    print "You walk around the side of the house and head towards the backdoor.\n"
    print "Just as you reach for the handle, your dog comes bouncing out of her kennel, excited to see you.\n"
    print "She starts excitedly barking, hounding you for attention.\n"
    print "You look around and notice some sticks on the ground, and you pull an old dog treat from your pocket.\n"
    room_flair = "Throw the stick, throw the treat, or ignore the dog and run inside?\n"

    choice2 = handle_choice(False, room_flair)
    invalid = True

    while invalid:
        choice2 = choice2.title()
        if "Stick" in choice2 or "Run" in choice2 or "Ignore" in choice2:
            print "The dog carries on barking loudly.\n"
            print "You see a light turn on in an upstairs bedroom.\n"
            print "Your dad comes storming out to meet you.\n"
            why = "Dad: 'What are you doing back here? It's the middle of the night, are you just getting home?\n"
            grounded(why)
            invalid = False
        elif "Treat" in choice2:
                print "The dog stops barking and runs after the treat.\n"
                print "You open the door and run in while the dog is distracted.\n"
                hallway_cont()
                invalid = False
        else:
            print "That's not a valid input.\n"
            choice2 = raw_input(room_flair)

# game entry/exit functions

def grounded(why):
    print why, "You're grounded!"
    exit(0)

def start():
    print "It's 2am and you're only just arriving home.\n"
    print "You're 16, and you've been at a party.\n"
    print "You're very drunk, and if your parents catch you you'll be grounded... forever.\n"
    print "Your goal is to make it out of your clothes, into your pyjamas and up to your bedroom without getting busted.\n"
    print "To take off clothes, type 'Remove [item name]'\n"
    print "To put on pyjamas, type 'Put on pyjamas'\n"
    print "You only get 1 chance per room to take off or put on clothes, so don't forget to do it!\n"
    print "To give you a headstart, you pull off your shirt on the way up the front steps.\r"
    print "..."
    print "As you approach the house, you notice a light on in the front room.\n"
    room_flair = "Go through the front door, or go round the back?\n"

    choice2 = handle_choice(False, room_flair)
    invalid = True

    while invalid:
        choice2 = choice2.title()
        if "Front" in choice2:
            hallway()
            invalid = False
        elif "Back" in choice2:
                backgarden()
                invalid = False
        else:
            print "That's not a valid input."
            choice2 = raw_input(room_flair)

# main
start()
