# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# test

define you = Character("you")
define daughter = Character("Anny")
define unk = Character("Unknown")
define jailer = Character("jailer")

# The game starts here.

label start:
    daughter "Daddy!"
    "Look at this little cutie. She is my daughter."
    "And this beautiful woman is my wife. Together we live in this little shack."
    "not a very good place to live in I know. But I'll do anything to support my family."
    unk "Hey! You there, wake up!"
    scene bg room with vpunch
    show eileen happy
    jailer "Somebody wants to see you. Get to the meeting room quickly."
    menu:
        "Go to the meeting room":
            jump meeting

label meeting:
    "You see a man in black suit. He wares a joker mask"