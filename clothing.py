# splits input into list ('remove hat' to ['remove', 'hat'])
# pops off the last word in the list and returns it

def remove_word(sentence):
    removing = str.split(sentence)
    return removing.pop()

# check if clothes list is empty
# check if choice is a valid option, then execute

def naked(edited_choice):
    if not clothes:
        print "Can't remove any more clothes, you're naked."
    else:
        if edited_choice in clothes:
            clothes.remove(edited_choice)
            print "Removed %s" % edited_choice
        else:
            print "But you're not wearing any %s" % edited_choice

# checks if pyjamas list has variables
# checks if clothes list is empty
# puts pyjamas in list if input is correct and above are both true

def add_clothes(choice):
    edited_choice = remove_word(choice)
    if pyjamas:
        print "Can't put on pyjamas again, you're already wearing them."
        return edited_choice
    else:
        pass

    if not clothes:
        if edited_choice == "pyjamas" or edited_choice == "Pyjamas":
            pyjamas.append(choice)
            print "Put on pyjamas."
        else:
            print "Can't put on %s, can only put on pyjamas." % edited_choice
    else:
        print "You can't put your pyjamas on, you're still wearing your clothes."


# changes 'remove item' to 'item'
# prevents removing certain items before others
# otherwise, runs naked() to remove item or warn of invalid input

def remove_clothes(choice):
    edited_choice = remove_word(choice)
    if edited_choice == 'socks' and 'shoes' in clothes:
        print "You can't take off your socks before your shoes!"
    else:
        naked(edited_choice)

# Clothing lists (at game start)
clothes = ['trousers', 'socks', 'shoes']
pyjamas = []
