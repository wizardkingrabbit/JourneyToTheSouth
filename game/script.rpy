# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# test
$ GEthresh = 3
$ GoodTalks = 0
$ GoodEnding = True
$ BurnPlantation = True

define you = Character("you")
define daughter = Character("Anny")
define unk = Character("Unknown")
define jailer = Character("jailer")
define MM = Character("Mysterious Man")

# The game starts here.

label start:
    "You know this is a dream, but you wish not to wake up."
    "Because here you see your little daughter. She is looking at you too, smiling"
    "Look how cute she is with her long curly hair. She calls your name. her voice is so sweet."
    $ playerName = renpy.input("You hear her calling your name: ")
    "And then you see your wife. She is doing chores. You want to speak with her, but you just cannot open your mouth."
    "‘I have to do this’, suddenly you hear your own voice shouting, ‘and I do all I can to support this family’. How tragic, your wife and daughter are frightened by your voice and you cannot even stop it." with vpunch
    "You hear another voice thrusting into your dream, ‘wake up, bastard. This voice is from reality."
    unk "Somebody wants to see you."
    menu:
        "wake up":
            "You do not have choice, you have to wake up. And you see a jailer standing outside your prison cell"
        "do not wake up":
            "just one more moment you whisper, but your daughter’s face is fading"
            "The man unlocks a door and walk toward you. Then he starts beating you"
            unk "where do you think you are asshole? It's fucking prison, not a hotel. Get your ass up"
            "Your daughter finally disappears in your dream and you wake up without a choice"
    scene bg room
    show eileen happy
    "In the meeting room, you see a man with suit and a joker mask. ‘%(playerName)s, I know you’, he speaks peacefully."
    menu:
        "Remain silence":
            pass
        "Who are you then?":
            MM "This is a trivial question. And you will know in future anyway."
    MM "Four years ago, you were the leader of the ‘white fog gang’ in Los Angeles, and you controlled over 80 percent of illegal drug dealing in Los Angeles. If it was not that you and your hound dogs killed two polices, no one would decide to arrest you."
    menu:
        "Explain yourself out":
            you"It was just an accident, and it is not even caused by me."
            MM "Is that the case? I guess even you don’t know if you are lying. But it doesn’t matter. It’s not important to me at all."
        "Remain silence":
            pass
    MM "Anyway, you need to stay in this prison for fifteen years. Hm, eleven more years to go, right? It is such a sad story you cannot see your daughter again for a long long time. Do you know that she should be going to middle school this autumn?"
    you "What happens to her!" with hpunch
    MM "Nothing, just to remind you of your family."
    MM "And maybe offer you an opportunity of seeing your daughter wearing middle school uniform."
    "You hear him giggling. But you just cannot reject the offer."
    you "What is your offer then?"
    MM "I was sent by someone who was very, very powerful. For now let us just assume that this person is the current state governor. He is powerful enough to get you out of the prison and give you eternal freedom in California, but not powerful enough to publicly break the US laws."
    MM "He wants a very special kind of drug that only being produced in Mexico. US laws forbidden this drug, but he needs it. We do not want to get our own hands dirty, luckily there is you. So, we want you to go to Mexico and get that drug for him."
    "The mysterious man hands you a note with address and name of a plantation. You did not know this plantation even you have done drug smuggling for so many years."
    menu:
        "This mission is simply impossible":
            pass
        "I cannot do it alone":
            pass
    MM "Of course you will not be fighting alone. See this paper? It allows you to recruit three prisoners from any prison in California. You can use this to meet with your old companions and work together with them again."
    menu:
        "Why do you trust me":
            MM "You have potential. And you have family. You are the best choice for us."
        "Why should I trust you":
            MM "You do not need to. If you want to stay in this prison, and NEVER reunite with your family."
    "the mysterious man brings you out of the jail. You see a nice Ford car parking in front of the prison gate."
    MM "It’s for you. The fake ID is in the trunk. But try to stay low and keep this mission secret. Now you are free to go."
    MM "Oh, and I almost forget! This thing is also for you. Try not use this, will you?"
    "He throws you a pistol. You catch it and find it loaded."
    menu:
        "Shoot Him":
            "You raise the gun and point it at this mysterious man. However, before you pull the trigger, he takes out his gun lightning fast and shoots you in your heart."
            MM "How stupid. How pity."
            jump gameEnd
        "Get on Your way":
            "You stare at the mysterious man but you decide not to shoot him. He watches you geting into the car with a creepy smile on his face. You move your gaze away from his face and step on the gas. A few seconds later, he disappears in the rearview."
            jump SanFrancisco

label SanFrancisco:
    "Driving on the California freeway, the old days comes back to you mind again."

label gameEnd:
    "You were so close to your freedom and your family, but now you fall in your own blood. Hope you have a better luck next time."
    return

label test:
    "Use jump to jump between scenes"