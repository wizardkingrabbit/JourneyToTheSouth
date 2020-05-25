﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Endings
define GEthresh = 3
define GoodTalks = 0
define GoodEnding = True
define BurnPlantation = True

# some flags use within a Chapter
define sf_bribe = False
define sf_threat = False
define sf_headlock = False

define you = Character("you")
define mark = Character("big Mark")
define daughter = Character("Anny")
define unk = Character("???")
define guard = Character("Prison Guard")
define officer = Character("Chief Officer")
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
    "You see your wife in the background, doing household chores. You want to speak with her, but you just can't bring your mouth to open."
    "Suddenly you hear your own voice shouting, 'I have to do this!'" with vpunch
    "'I do all I can to support this family!’ How tragic, your wife and daughter are frightened by your voice and you can't even stop it."
    "You hear another voice, a voice from reality, thrusting into your dream, ‘Hey bastard, wake up.'"
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
    mm "Nothing at all, relax! I just wanted to remind you of your family."
    mm "And maybe offer you an opportunity of seeing your daughter wearing her middle school uniform."
    "You hear him chuckle. A part of you already knows where this is going, but you let him continue."
    mm "I was sent by someone with high authority, someone so powerful that I was suprised myself by the request. Let's assume that this person just is as powerful as the current state governor."
    mm "He wants a special kind of drug that can only be produced in Mexico. US law forbids this drug, but he needs it. Rather than getting his hands dirty, he wants to hire a professional in that field."
    mm "Luckily there's one person in front of me that fulfills the requirements! We came here to offer you a chance to get your life back. We just need you to go to Mexico and get that drug for him."
    mm "In return, we'll take you off the grid. That means complete freedom in California and essentially a new life. After that, you can do whatever the hell you want."
    "The mysterious man hands you a note with address and name of a plantation. Even after all the drug smuggling you've done over these years, this plantation is one that you've never heard of."
    menu:
        "This mission is practically impossible":
            pass
        "I cannot do it alone":
            pass
    mm "Of course not! You won't be fighting alone. See this paper? We will allow you to recruit three prisoners from any prison in California. Let this be an opportunity to meet with your old companions and work together with them again!"
    "A sudden thought comes across your mind: maybe I can found out what really happened back then..."
    menu:
        "Why trust me?":
            mm "You have the experience. And you have family. I know you aren't a killer, or am I wrong? Right now, you are the best choice for us."
        "Why should I trust you?":
            mm "You are always free to decline my offer! That is, if you want to stay in this prison, and NEVER reunite with your family."
    "The mysterious man brings you out of the prison. You see a white Ford car parked in front of the prison gate."
    mm "That car is for you. There's also a fake ID and a credit card in the back seat. You're still convicted prisoner until this mission is complete, so try to stay low. And remember, we'll be keeping an eye on you as well as your beloved daughter."
    mm "Oh, and I almost forgot! Thing is also for you. Try not use this, will you?"
    "He throws you a pistol. You catch it and can immediately tell that it is loaded."
    menu:
        "Shoot him":
            "You raise the gun and point it at this mysterious man. However, before you pull the trigger, you had no time to react to a bullet that instantly pierced your head."
            mm "Sigh, how stupid."
            jump gameEnd
        "Get on your way":
            "You stare at the mysterious man but you decide not to shoot him. He watches you geting into the car with a creepy smile on his face. Revving up the Ford, you step on the gas. A few seconds later, he disappears from the rearview mirror."
            jump transfer

            
 # Chapter 2 (Jingtian Li & Johnny Ngo) (Transfer->San Francisco)          
 
label transfer:
    "Driving on the California freeway, your mind is all over the place."
    "What the hell just happened?"
    "One moment you were a prisoner with lifetime imprisonment, and now you're an escapee on a mission to be freed from conviction."
    you "Shit, I'll have to be careful with what I do from now on."
    "Any wrong move will put both you and Anna in danger."
    "Your thoughts take you back to the past, back when you were managing the drug business four years ago."
    "It all started with you and three of your most trustful friends, ruling the dark side of Los Angeles."
    "Mr. Mount was your best fighter and also an amazing sniper. He protected you from countless dangers and made sure their clients knew what they were dealing with. This is a man that you would surely want on your team."
    "Mr. Tsing was both your dedicated engineer and navigator. He previously worked for the US government and has investigated numerous US-Mexican tunnels that were built for drug smuggling. Finding a safe path to Mexico with him would be a piece of cake."
    "Mr. Buenos is from Catalonia, and he was your translator. Although you had other gang members who can also speak Spanish, Buenos stood out for some reason. He was always there when you needed him the most."
    "You look at the paper and notice that all three of your trusted partners are prisoners at different locations."
    you "I guess everybody is in prison nowadays."
    "You choose to drive to the closest person: Mr. Mount, holed up at a prison located in San Francisco."
    jump SanFrancisco
        
label SanFrancisco:
    "After parking the car in front of the San Francisco prison, all you can see in front of you is the gray, towering wall and a massive closed gate."
    "You tuck the gun behind your back and walk towards the gate."
    menu:
        "Shoot at the sky":
            "Within seconds after you shoot, policemen swarm outside and surround you. You want to show them the paper from state governor. However, all they can see is the gun in your hands, and so they decide to shoot you."
            jump gameEnd
        "Knock on the door":
            "A voice calls above you. You see a thin, short jail guard looking at you at the top of the gate."
    you "Good evening sir, I am sent by the state governor. He issued an executive order to move a prisoner here to another place. I've got the papers with me."
    "The prison guard eyes you suspiciously for only a second before lowering his guard."
    "Years of working in the shady business has refined your improvisation skills indeed."
    guard "I see. Our chief officer will need to see the paperwork. I'll take you over to him."
    "The guard opens the gate and brings you to the chief's office. You see the chief sitting on his chair enjoying a cup of black coffee."
    guard "This guy says he's here to conduct a prisoner transfer."
    officer "Sigh, this better be important. I'll take it from here."
    "You take out the paper that the mysterious man gave you and hand it over to the chief officer."
    officer "Hm. Usually we need to do some investigations on these kind of requests. That means it would take a few weeks to verify and get back to you. But..."
    "The officer makes sure no one is watching and makes a gesture that you know all too well."
    "This guy is definitely dirty. At least some good may come out of this."
    jump sf_1

label sf_1:
    menu:
        "Bribe him":
            jump sf_2
        "Threaten him verbally":
            jump sf_3
        "Threaten him with your gun":
            jump sf_4

label sf_1a:
    menu:
        "Threaten him verbally":
            jump sf_3
        "Threaten him with your gun":
            jump sf_4

label sf_1b:
    menu:
        "Bribe him":
            jump sf_2
        "Overpower him":
            $ sf_headlock = True
            "Despite the years of being holed up in prison, you've been maintaining your physique whenever possible."
            "You quickly rush right behind the chief and put him into a headlock before he can even react."
            you "One last chance, or I'll be pointlessly talking to a dead body."
            jump sf_5
        "Threaten him with your gun":
            jump sf_4
            
label sf_1c:
    menu:
        "Overpower him":
            $ sf_headlock = True
            "Despite the years of being holed up in prison, you've been maintaining your physique whenever possible."
            "You quickly rush right behind the chief and put him into a headlock before he can even react."
            jump sf_5
        "Threaten him with your gun":
            jump sf_4
            
label sf_2:
    $ sf_bribe = True
    "You habitually reach inside your pocket for a wallet, but then you remember that the only money you have is the credit card back in the car."
    menu:
        "Go back to car":
            "You tell them you have money in car and then see a wretched smile climbing up his face. A few minutes later, you return with a credit card in your hand."
        "Threat him verbally":
            jump sf_3
        "Threat him with your gun":
            jump sf_4
    officer "Damn idiot, you think we do credit card transactions for this type of business? Either you bring me cash or you get the hell out of my office."
    "Seems like you have to try another way, and walking away isn't going to be an option."
    if (sf_threat):
        jump sf_4
    else:
        jump sf_1a

label sf_3:
    $ sf_threat = True
    you "You better help me right now motherfucker, or I will twist your head off right here, right now."
    officer "Ha! I'd like to see you try. Enough bluffing. I suggest you wait for, I don't know, a week or two untill we find out if this document really came from the state governor."
    "You're running out of options."
    if (sf_bribe):
        jump sf_1c
    else:
        jump sf_1b

label sf_4:
    "You end up pulling out the gun and pointing it towards the chief. His face turns pale. Hell, he's even peeing himself."
    you "One last chance, or I'll be pointlessly talking to a dead body."
    jump sf_5
    
label sf_5:
    officer "Shit! Okay, okay. Just tell me who's the prisoner you're trying to get out of here."
    you "Mr. Mount."
    officer "Alright, easy there man. Let me make the call."
    "The chief makes an annoucement over the intercom to escort you to Mr. Mount for the transfer."
    if (sf_headlock):
        "You release him from your headlock and push him into the corner of the room. He's quivering in fear."
    else:
        "You drive the chief into the corner of his office. He's shaking in fear of your gun."
    menu:
        "Kill him":
            $ GoodTalks -= 1
            "Jail officer looks frightened. That is a good sign. He will always obey you as long as you have your gun in your hands"
        "How can I make sure you would not run around and call cops":
            officer "this office can be locked from outside and no one except me usually comes here. you just need to take away his phone and leave him alone."
    menu:
        "Sounds good to me":
            "you follow the officer's suggestion. The officer seems to calm down a little bit. after a few minutes, you arrive at the prison area. prisoners here all start to laugh when they see the officer"
        "I actually have a better idea (shoot his legs)":
            $ GoodTalks -= 1
            "that is surely a good plan. the guard loses consciousness immediately. Jail officer looks frightened, but he still leads you to the prison area. prisoners here all start to laugh when they see the officer"
    "You see Mount in a really big cell. He sees you at the same moment. the grief on his face suddenly disappears"
    you "Yoooooo, long long no see. #fist bump# Let me release you from this cell"
    mount "No need boss. The door is not locked"
    you "what?"
    mount "This officer is bribed by one of the prisoner. #walk out of the cell# We call him big Mark. Mark forced this officer not to lock our door and provide him good food, drugs, smart phones and internet. then he used these resources to bribe prisoners here. Oh by the way, please do not think that I got bribed by him. I decided to quit drug since I was here"
    "You peek at the officer. he shrugs, with a bitter smile"
    officer "I thought about refusing him, but he offered too much."
    you "then why do you still stay here for 4 years. sounds like you can just leave"
    "A burst of laughter comes to you from behind. You see a guy who's even stronger than Mr. Mount standing there. And many other prisoners also walk out of their cells. Obviously, that strong man is big Mark"
    mark "I thought you were really a government envoy. Now it seems there is nothing we need to be afraid of"
    you "I am a government envoy"
    mark "You think I am idiot? I never saw a prisoner call a goverment guy boss"
    you "Whatever. we are leaving"
    mark "If you are a government guy, I shall let you leave. But so unlucky, you are a retard who don't even know how to lie about it."
    menu:
        "Kill Mark":
            $ GoodTalks -= 1
            "You put a bloody hole between Mark's eyes. everyone is shocked, even Mount. The next moment, almost every prisoner rushes to you and tries to tear you apart. But you have Mount to protect you. Finally you and Mount jumped into the car. those thugs can never touch you again."
            jump Sacramento
        "Show your paper":
            mark "This signature is from state governor, incredible. But since you already know the secret of this prison, I still cannot let you leave."
    you "Don't push me to kill you, sir. I can promise you I shall not tell the secret of this prison to anyone. You just need to let us leave peacefully"
    "Mark seems to parse for a while"
    mark "Fine. You leave me no choice. I have to let you go. But before you leave, I want you to pay some prices"
    you "What's the price"
    mark "I want a duel with Mount"
    you "WTF"
    "You feel Mount pulling your sleeve"
    mount "#whisper# This man is crazy. he wants to have a duel with me since I got here. I really do not think I can defeat this guy and I cannot know what would happen if I get defeated"
    you "So, Mark, you kept my friend here for 4 years merely to have a fight with him? Don't you think that is childish?"
    mark "That is only part of the reason. I kept everyone who should be here, so that government would not know I corrupted this prison. But besides that, I do like having duel with other strong budies"
    mark "So, Mount, would you accept the duel or not"
    mount "#pulling your sleeve# #whisper# No. we should think another way out"
    menu:
        "Kill Mark":
            $ GoodTalks -= 1
            "You put a bloody hole on Mark's chest. everyone is shocked, even Mount. The next moment, almost every prisoner rushes to you and tries to tear you apart. But you have Mount to protect you. Finally you and Mount jumped into the car. those thugs can never touch you again."
            jump Sacramento
        "Accept the duel for Mount":
            mount "Are you trying to kill me. this is not the solution. I cannot beat him. Are you deaf or something."
        "Violence is always not a correct thing to do, Mark":
            jump sf_6
    menu:
        "I have plan.":
            you "You are not going to be beaten. Trust me."
        "Believe in yourself":
            you "You cannot defeat him simply because you do not believe you can. But you can do that. believe in yourself. Just do it"
    "Mark and other prisoners lead you to the main hall of the prison. the chief officer is made to be the judge of this duel"
    "The battle begins. Mount seems lack determination. Mark punches Mount heavily while Mount gives no effective strike back"
    menu:
        "Kill Mark":
            $ GoodTalks -= 1
            "You put a bloody hole on Mark's chest. everyone is shocked, even Mount. The next moment, almost every prisoner rushes to you and tries to tear you apart. But you have Mount to protect you. Finally you and Mount jumped into the car. those thugs can never touch you again"
            jump Sacramento
        "Cheer for Mount":
            "Mount stabilizes his breath. Then he successfully dodges a few hits from Mark. However, when Mount launches the counter attack, his defence is broken through. Both of them hit each other, but Mount suffers harder"
    menu:
        "Kill Mark":
            $ GoodTalks -= 1
            "You put a bloody hole on Mark's chest. everyone is shocked, even Mount. The next moment, almost every prisoner rushes to you and tries to tear you apart. But you have Mount to protect you. Finally you and Mount jumped into the car. those thugs can never touch you again"
            jump Sacramento
        "Cheer for Mount":
            "Mark's attack becomes harsher and harsher. Finally, Mount fell to ground. But Mark does not stop. He kicks and stomps on Mount"
    menu:
        "Kill Mark":
            $ GoodTalks -= 1
            "You are so sad that you miss your first shot. Then prisoners overwhelm you. You are killed by big Mark"
        "Do Nothing":
            mark "Oops, It looks like I accidently killed your little friend. Trust me I really wish I did not do this but I just get carried away sometimes when fighting. Now since leting you out possibly lead no good result. I now decide to kill you here"
    jump gameEnd

label sf_6:
    mark "What are you talking about. I know Mount used to kill people for living yet he is still you companion"
    you "He is doing that because he needs to protect himself and others. Why do you use violence? To satisfy your pervert mind?"
    mark "Hey, do not judge me. I was abused by my parents when I was young. One day I had it enough and killed them with my bare hands. Since then I like to fight"
    you "This is not even explanatory. Normal people would feel disgusting after doing such things"
    mark "Because I got their inheritance after I killed them. Even after I killed them I still get to keep their money"
    you "But you can get your parents' inheritance anyway. Everyone will die someday. It is still wrong to use violence, especially to kill people"
    mark "But you are not the one who was abused. If... if you were abused before, you would be obsessed with violence too"
    menu:
        "Enough of your bullshit":
            $ GoodTalks -= 1
            "You put a bloody hole on Mark's chest. everyone is shocked, even Mount. The next moment, almost every prisoner rushes to you and tries to tear you apart. But you have Mount to protect you. Finally you and Mount jumped into the car. those thugs can never touch you again."
            jump Sacramento
        "Oh really?":
            you "#show the scar on your waist# see this? My mother once sold my kidney for drug when I was a kid. Do you think that is not enough to be called abusement?"
    mark "fuck. Sorry I do not know you have such tragic past"
    you "Now you know, so get out of my face and let us leave"
    mark "but hey, why should that matter? why should I find a reason for being obsessed with violence? I just want to fight. I will not let you leave without a fight anyway"
    you "because you are losing your true self. Think about it, when you abused by your parents for the first time, have you ever thought about killing them?"
    mark "... No, I cannot really remember"
    you "The answer is no. You though about how to make them forgive you, Mark. Every kid who gets abused by parents think that way at beginning."
    mark "OK if you are right, why the hell did I kill them at last"
    you "Because they changed you. That is their purpose don't you see? They want you to be a shitty person like them"
    mark "So... so they succeeded?"
    you "No. But if today you insist to have the duel with Mount, they will succeed"
    mark "But I already killed them. Isn't that the sign that they transformed me successfully."
    you "that is only half way to their goal, idiot. That is a trap. They lured you to kill them so you can be more degenerated in prison. Now it is your chance to step out of this trap and be a new person after your sentences. Or you can continue to be slave of two dead people in the rest of your life"
    "Big Mark sits on ground with tear on his face"
    you "Now can we leave?"
    mark "Yes, yes. Sure, leave me alone"
    "You stride through the crowd, with Mount following behind you"
    mount "#whisper# damn, pal, I did not even know you had such sad past"
    you "#whisper# because I do not. I got that scar when I fought other drug dealers when I was in community college"
    "When you got into the car, Mount finally bursts out his laugh. You also can no longer hold back your laughter"
    mount "Oh man, look at him sitting there crying. Boss, you really help me solve a real big trouble"
    "With laughters and tears, the car is rolling to your next destination"
    jump Sacramento

 # Chapter 3 (Jason Iino) <- das me :>
label Sacramento:
    define baites = Character("Charles Baites")

    #I'll clean up dialogue/actually write dialogue later, just laying out framework
    "Approach jail, which consists of tall buildings"
    "Greeted by Rebublican mayor Charles Baites, is a large civilized cobra"
    "Tells you got a call from the governor about your quest"
    "Expresses distrust for governor, but notes doesn't necessarily have ill will towards you"

    "Offers to give you Buenos in exchange for the drug"
    "Talks about how civil unrest has been high in Sacremento as of late"
    "He believes that the drug could help to calm his citizens if they could analyze and reproduce it"
    "Basically make him look desperate and be a tragic villain who doesn't want
    to do the things he does, but feels he needs to for the greater good"

    menu:
        "Accept offer"
            jump sac_accept
        "Decline offer"
            jump sac_decline
        "Shoot"
            #do something


    label sac_accept:
        "Governor kills you"
        jump gameEnd

    label sac_decline:
        "Baites seems dissapointed, and tells you to be on you way, swatting you out the gate with his tail"

    menu:
        "Try to sneak in and extract Buenos"
        jump sac_sneak

        "Try to bargain with guards"
        jump sac_bargain


    label sac_sneak:
        #set of decisions that involve not raising an alarm variable, making decisions to not get caught
        $ alarm = 0
        $ max_alarm = 4

        jump sac_boss


    label sac_bargain:
        #try to bargain with guards, might just cut this and do sneak, or make it so
        #that you if you suceed you do the sneak section with a higher max alarm (turns a blind eye)
        jump sac_boss


    label sac_boss:
        #baites confronts you at the gate, starts stressing, as he feels he's letting down his constituients
        #bites and poisons you in an attempt to stop you
        #must make a series of decisions to reason with baites (calm, encourage, reason, ect.)
        #must choose one depending on what hes saying to calm him down so he can give you anti venom
        #must make so many right decisions in a few turns before you die

        $ turns = 0 #How many turns until you perish
        $ stress = 6 #variable of how many times you must make the right decision with Baites


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
