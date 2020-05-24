# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# test
define GEthresh = 3
define GoodTalks = 0
define GoodEnding = True
define BurnPlantation = True

define you = Character("you")
define daughter = Character("Anny")
define unk = Character("???")
define officer = Character("Officer")
define mm = Character("Mysterious Man")
define mount = Character("Mount")
define tsing = Character("Tsing")
define buenos = Character("Buenos")

# The game starts here.

#Chapter 1 (Jingtian Li)
label start:
    "Just where am I?"
    "You realize that this is a dream, and you don't want it to end."
    "Because here you see your little daughter, Anna. She is looking at you too, smiling."
    "She looks beautiful with her long, curly hair."
    $ playerName = renpy.input("You hear her calling your name: ")
    "Her voice is so sweet."
    "And then you see your wife, doing household chores. You want to speak with her, but you just can't bring your mouth to open."
    "Suddenly you hear your own voice shouting, 'I have to do this!’" with vpunch
    "'I do all I can to support this family!’ How tragic, your wife and daughter are frightened by your voice and you can't even stop it."
    "You hear another voice thrusting into your dream, ‘Hey bastard, wake up.' This voice is from reality."
    unk "Somebody wants to see you."
    menu:
        "Wake up":
            "Sigh. You'd have to wake up eventually. You open your eyes and see the patrolling officer standing outside your prison cell."
            officer "I don't want to have to go in there, fella. Let's go."
            "He dangles a pair of handcuffs in the air, and you put your back against the bars to let him put it on."
        "Stay asleep":
            "'Just one more moment,' you whisper, but your daughter’s face is already fading."
            "Whipping out his baton, the man unlocks a door and walks toward you. He starts beating you out of your humble abode."
            "Anna finally disappears in your dream and you wake up without much of a choice."
            "Fully awake, you remember where you are and quickly apologize to the patrolling officer."
            officer "Where do you think this is, asshole? It's a fucking prison, not a luxury hotel. Get your ass up."
            "He handcuffs your hands while you were still recovering from that one-sided beatdown."
    scene bg room
    "The officer takes you through the cell block and into a very fancy dining room."
    show eileen happy
    "Sitting at the end of the table, you see a man in a suit. His face is covered with a mask."
    mm "‘Ah, if it isn't %(playerName)s. I know you. Please, sit’, he speaks casually."
    menu:
        "Remain silent":
            pass
        "Who the hell are you?":
            mm "Do you think I'd really tell you if I was wearing this mask?. You will know who I am in the future anyway."
    mm "Four years ago, you were the leader of the White Fog Gang in Los Angeles, and you controlled over 80 percent of drug dealing business in Los Angeles. If not for killing two policemen, you would not have been here for this long."
    you "I didn't kill those policemen. As wrong as my business is, we don't kill with intent. The last thing I knew was that I was the last person left behind."
    mm "Is that really the case? Well, that doesn’t matter. It’s not important to me at all." 
    mm "Anyways, how much longer are you staying in this dump? Oh right, lifetime, correct? It is such a sad story you'll never see your daughter in person. Did you know that she's be going to middle school this fall?"
    you "What the hell did you do to her!" with hpunch
    mm "Nothing at all, relax!. I just wanted to remind you of your family."
    mm "And maybe offer you an opportunity of seeing your daughter wearing her middle school uniform."
    "You hear him giggling. A part of you knows where this is going, but you let him continue."
    mm "I was sent by someone with high authority, someone so powerful that I was suprised myself by the request. Let's assume that this person just is as powerful as the current state governor."
    mm "He wants a special kind of drug that can only be produced in Mexico. US law forbids this drug, but he needs it. Rather than getting his hands dirty, he wants to hire a professional in that field."
    mm "Luckily there's one person in front of me that fulfills the requirements! We came here to offer you a chance to get your life back. We just need you to go to Mexico and get that drug for him."
    mm "In return, we'll take you off the grid. That means complete freedom in California and essentially a new life. After that, you can do whatever the hell you want."
    "The mysterious man hands you a note with address and name of a plantation. Even after all the drug smuggling you've done over these years, this plantation is one that you've never heard of."
    menu:
        "This mission is practically impossible.":
            pass
        "I cannot do it alone.":
            pass
    mm "Of course not! You won't be fighting alone. See this paper? We will allow you to recruit three prisoners from any prison in California. Let this be an opportunity to meet with your old companions and work together with them again!"
    "Maybe I can found out what really happened back then..."
    menu:
        "Why do you trust me?":
            mm "You have the experience. And you have family. I know you aren't a killer, or am I wrong? Right now, you are the best choice for us."
        "Why should I trust you?":
            mm "You are always free to decline my offer! That is, if you want to stay in this prison, and NEVER reunite with your family."
    "The mysterious man brings you out of the prison. You see a white Ford car parked in front of the prison gate."
    mm "That car is for you. We left a fake ID in the passenger seat. You're still convicted prisoner until this mission is complete, so try to stay low. And remember, we'll be keeping an eye on you."
    mm "Oh, and I almost forgot! Thing is also for you. Try not use this, will you?"
    "He throws you a pistol. You catch it and can immediately tell that it is loaded."
    menu:
        "Shoot Him":
            "You raise the gun and point it at this mysterious man. However, before you pull the trigger, you had no time to react to a bullet that instantly pierced your head."
            mm "Sigh, how stupid."
            jump gameEnd
        "Get on your way":
            "You stare at the mysterious man but you decide not to shoot him. He watches you geting into the car with a creepy smile on his face. Revving up the Ford, you step on the gas. A few seconds later, he disappears in the rearview mirror."
            jump transfer

            
 # Chapter 2 (Johnny Ngo) (Transfer->San Francisco)          
            
label transfer:
    "Driving on the California freeway, your mind is all over the place."
    "What the hell just happened?"
    "One moment you were a prisoner with lifetime imprisonment, and now you're an escapee on a mission to be freed from conviction."
    "Your thoughts take you back to the past, back when you were managing the drug business four years ago."
    "It all started with you and three of your most trustful friends, ruling the dark side of Los Angeles."
    "Mr. Mount was your best fighter and also an amazing sniper. He protected you from countless dangers and made sure their clients knew what they were dealing with. This is a man that you would surely want on your team."
    "Mr. Tsing was both your dedicated engineer and navigator. He previously worked for the US government and has investigated numerous US-Mexican tunnels that were built for drug smuggling. Finding a safe path to Mexico with him would be a piece of cake."
    "Mr. Buenos is from Catalonia, and he was your translator. Altough you had other gang members who can also speak Spanish, Buenos stood out for some reason. He was always there when you needed him the most."
    "Who should we pick up first?"
menu:
    "Mr. Mount, the bodyguard and fighter":
        jump SanFrancisco
    "Mr. Tsing, the technicial and navigator":
       jump Sacramento
    "Mr. Buenos, the translator":
        jump SanDiego
        
label SanFrancisco:
    "You park the car in front of the prison of San Francisco. All you can see in front of you is the gray, towering wall and a massive closed gate"
    menu:
        "Shoot at the sky":
            "Within seconds after you soon, policemen swarm outside and surround you. You want to show them the paper from state governor. However, all they can see is the gun in your hands, and so they decide to shoot you."
            jump gameEnd
        "Knock on the door":
            "The gate is opened. You see a thin, short jail guard looking at you behind the gate."
    you "Hello sir, I am sent by the state governor. He issued an executive order to move a prisoner here to another place. *hand him the paper from the mysterious man*"
    ""
    ""
    ""
    ""
    menu:
        "Talk to trouble":
            $ GoodTalks += 1
            jump Sacramento
        "Kill the trouble":
            jump Sacramento

            
 # Chapter 3 (Jason Iino)
label Sacramento:
    menu:
        "Talk to trouble":
            $ GoodTalks += 1
            jump SanDiego
        "Kill the trouble":
            jump SanDiego
            

 # Chapter 4 (Michael Kahn)
label SanDiego:
    menu:
        "Talk to trouble":
            $ GoodTalks += 1
            jump border
        "Kill the trouble":
            jump border

            
# Chapter 5 (Fredlin?)
label border:
    menu:
        "Talk to trouble":
            $ GoodTalks += 1
            jump Mexico
        "Kill the trouble":
            jump Mexico

            
# Chapter 6 (Ian Maynard)
label Mexico:
    menu:
        "Burn the plantation":
            if GoodTalks > GEthresh:
                jump ending1
            else:
                jump ending2
        "Leave the plantation":
            if GoodTalks > GEthresh:
                jump ending3
            else:
                jump ending4

# Endings (Guozheng Yang)              
label ending1:
    "ending 1"
    "Burn the plantation, do a lot of good talk"
    return

label ending2:
    "ending 2"
    "Burn the plantation, do no good talk"
    return

label ending3:
    "ending 3"
    "Leave the plantation, do a lot of good talk"
    return

label ending4:
    "ending 4"
    "Leave the plantation, do no good talk"
    return

label gameEnd:
    "You were so close to your freedom and your family, but now you fall in your own blood. Hope you have a better luck next time."
    return

label test:
    "Use jump to jump between scenes"