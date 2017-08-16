from clothing import *

# removed always called with False
# so function can only be accessed once per room
# prevents all clothes being removed in one room
# returns original choice with capitalisation

def handle_choice(removed, room_flair):
    choice = raw_input(room_flair)
    if  not removed and  "remove" in choice or "Remove" in choice:
        remove_clothes(choice)
        choice = handle_choice(True, room_flair)
    elif removed and "remove" in choice or "Remove" in choice:
        print "You've already tried to remove or put on an item this turn. Can't remove again."
        choice = handle_choice(True, room_flair)
    elif not removed and "pyjamas" in choice or "Pyjamas" in choice:
        add_clothes(choice)
        choice = handle_choice(True, room_flair)
    elif removed and "pyjamas" in choice or "Pyjamas" in choice:
        print "You've already removed or put on an item in this room."
        choice = handle_choice(True, room_flair)
    else:
        pass
    return choice

