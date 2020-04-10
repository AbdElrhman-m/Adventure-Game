# importing libraries
import time as t
import random


def print_pause(message, delay=0):
    # printes a message with delay
    # default delay = 2
    print(message)
    t.sleep(delay)


def print_pause_messages(message_list, delay=0):
    ####
    # looping through a list
    # and printing each massages with a delay
    ####
    for message in message_list:
        print_pause(message, delay)


def intro(monster, weapon):

    # printing the intro messages

    message_list = ["You find yourself standing in an "
                    "open field, filled with grass and yellow wildflowers.",
                    f"Rumor has it that a {monster} is somewhere around here,"
                    " and has been terrifying the nearby village.",
                    "In front of you is a house.",
                    "To your right is a dark cave.",
                    f"In your hand you hold your trusty"
                    f" (but not very effective) {weapon}\n"]
    print_pause_messages(message_list)


def validate(x, choices_number=2):
    ####
    # validate the numeric  user input
    ####
    return x in range(1, choices_number+1)


def take_action(monster, weapon, has_magic_sward):
    ####
    # reflect the action taken by the user
    ####
    reflection_lst = [["You do your best...",
                      "but your dagger is no match for the gorgon.",
                       "You have been defeated!,",
                       "GAMEOVER!"],
                      [f"As the {monster} moves to attack, "
                      "you unsheath your new sword.",
                       f"The sword of Ogoroth shines brightly in your hand"
                       " as you brace yourself for the attack.",
                       f"But the {monster} takes one look at your "
                       "shiny new toy and runs away!",
                       f"You have rid the town of the {monster}."
                       " You are victorious!\n"]]

    try:
        action = int(input("Would you like to (1) fight or (2) run away?"))
    except ValueError:
        print_pause("Try again!")
        take_action(monster, weapon, has_magic_sward)
    if validate(action, choices_number=2):
        if action == 1:
            if has_magic_sward[:1]:
                print_pause_messages(reflection_lst[1])
            else:
                print_pause_messages(reflection_lst[0])
        elif action == 2:
            field(monster, weapon, has_magic_sward)
    else:
        print_pause("Try again!")
        take_action(monster, weapon, has_magic_sward)


def house(monster, weapon, has_magic_sward):
    ####
    # Things that happen to the player in the house
    ####
    house_events = ["You approach the door of the house.",
                    f"You are about to knock when the door opens"
                    f" and out steps a {monster}.",
                    f"Eep! This is the {monster}'s house!",
                    f"The {monster} attacks you!",
                    f"You feel a bit under-prepared for this,"
                    f" what with only having a tiny {weapon}."]
    print_pause_messages(house_events)
    take_action(monster, weapon, has_magic_sward)


def cave(monster, weapon, has_magic_sward):
    ####
    # Things that happen to the player in the cave
    ####
    message_list = ["You peer cautiously into the cave.",
                    "It turns out to be only a very small cave.",
                    "Your eye catches a glint of metal behind a rock.",
                    f"You have found the magical {weapon} of Ogoroth!",
                    f"You discard your silly old {monster} "
                    f"and take the {weapon} with you.",
                    "You walk back out to the field."]
    list_if_visited = ["You peer cautiously into the cave.",
                       "You've been here before, and"
                       " gotten all the good stuff. "
                       "It's just an empty cave now.",
                       "You walk back out to the field."]
    if has_magic_sward[:1]:
        print_pause_messages(list_if_visited)
    else:
        print_pause_messages(message_list)
        has_magic_sward.append(True)


def field(monster, weapon, has_magic_sward):
    ####
    # Things that happen to the player in the field
    ####
    print_pause("You run back into the field. Luckily,"
                " you don't seem to have been followed.")
    where_to_go(monster, weapon, has_magic_sward)


def play_again(monster, weapon, has_magic_sward):
    ####
    # start the game again
    ####
    choice = input("Would you like to play again? (y/n)").lower()
    if choice in ['y', "n", "yes", "no"]:
        if choice in ['y', 'yes']:
            print_pause("Excellent! Restarting the game ...")
            play_now()
        elif choice in ['n', 'no']:
            print_pause("Thanks for playing! See you next time.")
    else:
        print_pause("Try again!")
        play_again(monster, weapon, has_magic_sward)


def where_to_go(monster, weapon, has_magic_sward):
    ####
    # chooseing where player wants to go
    ####
    choice_list = ["Enter 1 to knock on the door of""the house.",
                   "Enter 2 to peer into the cave."]
    print_pause_messages(choice_list)
    print_pause("What would you like to do?")
    try:
        respond = int(input("(Please enter 1 or 2.)\n"))
    except ValueError:
        print_pause("Try again!")
        where_to_go(monster, weapon, has_magic_sward)
    if validate(respond, len(choice_list)):
        print_pause(
            choice_list[respond-1][choice_list[respond-1].find("o ")+2:])
        if respond == 1:
            house(monster, weapon, has_magic_sward)
            play_again(monster, weapon, has_magic_sward)
        elif respond == 2:
            cave(monster, weapon, has_magic_sward)
            where_to_go(monster, weapon, has_magic_sward)
    else:
        print_pause("Try again!")
        where_to_go(monster, weapon, has_magic_sward)


def set_varriables():
    monster_list = ["Cannibals", "lion", "tiger", "wolf", "wolfman", "vampire"]
    weapon_list = ["sword", "knife", "Shotgun", "pistol", "Machine gun"]
    monster = random.choice(monster_list)
    weapon = random.choice(weapon_list)
    return monster, weapon


def play_now():
    ####
    # start the game
    ####
    has_magic_sward = []
    monster, weapon = set_varriables()
    intro(monster, weapon)
    where_to_go(monster, weapon, has_magic_sward)


if __name__ == '__main__':
    play_now()
