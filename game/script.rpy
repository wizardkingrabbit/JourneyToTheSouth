# The script of the game goes in this file.

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
define mark = Character("Big Mark")
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
            mm "Do you think I'd really tell you if I was wearing this mask? You will know who I am in the future anyway."
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
        "I can't do it alone":
            pass
    mm "Of course not! You won't be fighting alone. See this fancy paper? We will allow you to recruit three prisoners from any prison in California. Let this be an opportunity to meet with your old companions and work together with them again!"
    "A sudden thought comes across your mind: maybe I can found out what really happened back then..."
    menu:
        "Why trust me?":
            mm "You have the experience. And you have family. I know you aren't a killer, or am I wrong? Right now, you are the best choice for us."
        "Why should I trust you?":
            mm "You are always free to decline my offer! That is, if you want to stay in this prison, lose your daughter, and never reunite with your family."
    "The mysterious man brings you out of the prison. You see a white Ford car parked in front of the prison gate."
    mm "That car is for you. There's also a fake ID and a credit card in the back seat. You're still convicted prisoner until this mission is complete, so try to stay low. And remember, we'll be keeping an eye on you as well as your beloved daughter."
    mm "Oh, and I almost forgot! This thing is also for you. Try not use this, will you?"
    "He throws you a pistol with a silencer on it. You catch it and can immediately tell that it is loaded."
    menu:
        "Shoot him":
            "You raise the gun and point it at this mysterious man. However, before you pull the trigger, you had no time to react to a bullet that instantly pierced your head."
            mm "Sigh, how stupid."
            jump gameEnd
        "Get on your way":
            "You stare at the mysterious man but you decide not to shoot him. He watches you geting into the car with a creepy smile on his face. Revving up the Ford, you step on the gas. A few seconds later, he disappears from the rearview mirror."
            jump transfer


 # Chapter 2 (Johnny Ngo & Jingtian Li) (Transfer->San Francisco->Transfer2)

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
    "Yep, this guy is definitely dirty. At least some good may come out of this."
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
        "Go back to the car":
            "You tell them you have money in car and then see a wretched smile climbing up his face. A few minutes later, you return with a credit card in your hand."
        "Threaten him verbally":
            jump sf_3
        "Threaten him with your gun":
            jump sf_4
    officer "Damn idiot, you think we do credit card transactions for this type of business? Either you bring me cash or you get the hell out of my office."
    "Seems like you have to try another way, and walking away isn't going to be an option."
    if (sf_threat):
        jump sf_4
    else:
        jump sf_1a

label sf_3:
    $ sf_threat = True
    you "You damn motherfucker. Either you help me, or I will twist your head off right here, right now."
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
    "The chief makes an annoucement over the intercom for someone to escort you to Mr. Mount for the transfer."
    if (sf_headlock):
        "You release him from your headlock and push him into the corner of the room. He's quivering in fear."
    else:
        "You drive the chief into the corner of his office. He's shaking in fear of your gun."
    officer "P-please, you can lock me in here and take my phone. I'm begging you, don't kill me!"
    menu:
        "Kill him":
            $ GoodTalks -= 1
            "You point your gun towards the chief and shoot. He's dead."
            jump sf_5a
        "Tie him up":
            "You use whatever you could find in his office to restrain his arms and legs. You also gag his mouth with his own sock."
            you "These restraints might not hold, maybe I should have some extra insurance..."
    menu:
        "Leave him in the office":
            "You leave the room, making sure the door was locked from the inside. Before you left, the chief seemed relieved that nothing happened to him."
            jump sf_5b
        "Shoot his leg":
            $ GoodTalks -= 1
            "As another layer of precaution, you shoot his leg. This way, you know he won't be going anywhere. The chief immediately loses consciousness from the shock."
            jump sf_5a

label sf_5a:
    "Despite the noise reduction from the silencer, the prison guard from earlier knocks from outside the office."
    "You quickly open the door and pull him in, making sure he sees the gun pointed at him."
    you "Now, I don't want you to end up like your chief over there, so it'd be best to follow my orders."
    "The guard definitely looks frightened. That's a good sign for you at least. You know he won't be causing any trouble as long as you got your eye on him."
    jump sf_5b

label sf_5b:
    "He escorts you to the northern cell block, presumably where Mr. Mount is. As you're passing by, you can hear the hysterical noises from the inmates."
    "You spot Mount in a cell slightly bigger than most. His gaze locks onto yours and you can see a mixture of both relief and happiness in his eyes."
    mount "Boss...is that you?"
    you "Long no see, buddy. I got some questions for you, but let's get you out of here first. Hey guard, open this cell up."
    mount "Ah, no need boss. This cell isn't locked."
    you "Huh?"
    "Mount stands up from his bed and casually slides open the door himself."
    mount "This isn't just any cell block. A prisoner by the name of Big Mark controls this entire section, and he's even got policemen working for him. Hell, I bet he's got a leash on the chief officer."
    mount "He created this bribing system as well as a hierarchy here. The strong reaps the most rewards. Delicious food, drugs, phones, you name it."
    "You look at the prison guard. Seeing how weak he is, he'd really be an easy pushover."
    officer "Hey, don't look at me like that, if you knew who Big Mark was, you'd be pummeled to bits."
    you "Mount, its already been four years. Isn't it time to leave? What happened to us?"
    mount "You know I'm a fighter, boss. This place is my heaven now, and you were in jail. Plus, even if I wanted to leave, Big Mark is the only person standing in my way."
    "A burst of laughter comes out from behind. You turn around and see a guy who's even bigger than Mr. Mount. He's also accompanied with other prisoners."
    you "Ah, you must be Big Mark."
    mark "And I thought you were a government envoy. Now it seems like there's nothing to be afraid of."
    you "The hell you talking about? I am a government envoy."
    mark "You think I am idiot? In all my years I've never heard a prisoner call a government official his boss."
    you "That's none of your business. Mount, let's go."
    "Big Mark blocks you from the exit."
    mark "If you really were sent by the government, then show me some proof. I doubt you are anyways. You're just a retard who doesn't even know how to bluff."
    menu:
        "Kill Mark":
            $ GoodTalks -= 1
            jump sf_markdead
        "Show your paper":
            "Big Mark yanks the paper out of your hands. This guy is dangerous."
            mark "I must say, this signature does look legitimate. But then I dont quite trust you won't report any of this to the higher powers. In the end, I can't let you leave this building."
    you "Hey look man, I'm not trying to start anything here, and I sure as hell won't tell a soul."
    "Mount comes stands beside me with his vouch. The prisoners next to Big Mark seems to awknowledge Mount's approval."
    "Big Mark thinks about it.."
    mark "Let make a deal then. "
    you "And what is this deal?"
    mark "I want a fistfight with that big fella right next to you. If he beats me, you're free to go. If not, well, you'll find out later."
    "Mount pulls on your shoulder and whispers to you."
    mount "This guy's a nut job. He's been itching to fight me for the past four years, and I've been talking my way out of it ever since. To be frank, I really don't think I could handle him. At the same time, I dont even want to imagine what will happen if he wins."
    you "So, Mark, all it takes is one fight to let us go? Is that why you kept Mount in here? Isn't that a bit childish?"
    mark "That's only part of the reason. I keep everyone here and make sure there's no snitching going on towards this corrupted prison. But besides that, I just want to see what this man can do to me."
    "The prisoners start to slowly surround you. Your chances of escaping peacefully are getting lower."
    mount "Boss, what should we do here?"
    menu:
        "Kill Mark":
            jump sf_markdead
        "Accept the duel on Mount's behalf":
            you "We'll take you up on your offer."
            mark "Haha! That's what we're talking about!"
            "Mount pulls me over again. For a veteran fighter, he seems to be shaking a little."
            mount "I don't think this is the solution, boss. This guy is more vicious than you think he is."
        "Talk your way out of this":
            jump sf_6

    you "I have plan. He's not going to be able to beat you, and I need you to trust me on that."
    you "Believe in yourself. You're only thinking you can't beat him because you're not believing. Give yourself some more confidence."
    "Big Mark and other prisoners lead you to the main hall of the prison. The prison guard comes foward to act as the referee."
    "The duel begins without a moment of preperation. Mount's expression still lacks determination."
    "Big Mark charges in, delivering heavy punches to Mount without him being able to retaliate."
    menu:
        "Kill Big Mark":
            jump sf_markdead
        "Support Mount":
            you "Mount, listen to me. He only got you by surprise. Focus. You're not my bodyguard for nothing."
            "Mount stabilizes his breath. He then successfully dodges a few hits from Big Mark second barrage. After finding an opening, Mount launches his counter attack, breaking through Big Mark's defense."
            "Both of them land hits on each other, but Mount suffered more damage due to the weight difference."
    menu:
        "Kill Big Mark":
            jump sf_markdead
        "Support Mount":
            you "C'mon Mount! Don't let those punches anywhere near you buddy. He has no idea what's coming to him!"
            "Mark's aggresive assault becomes harsher and harsher. Finally, a successful blow past Mount's defense dropped him to the ground. But Mark doesn't stop here. He starts delivering punishing kicks onto Mount."
            guard "Hey! You can't do that!"
            mark "Like hell I can't, Did you forget who's the boss here?."
            "Big Mark pushes the thin guard with ease and continues his one-sided beatdown."
    menu:
        "Kill Big Mark":
            $ GoodTalks -= 1
            "You pull out your pistol and try to aim at Big Mark. Unfortunately, the crowd became too aggresive at this point made your shot miss its mark."
            "Seeing you miss, the prisoners overwhelm you by force. You are eventually killed by Big Mark."
        "Stop the beatdown":
            "The raging crowd tossed you back and forth from getting to the middle of the fight. After what seemed like an eternity, you managed to push your way through."
            "The only thing you can see is Mount's lifeless body."
            you "You...you bastard!" with hpunch
            mark "Oops, It looks like I accidentally killed your little friend. Sorry kiddo, I sometimes get carried away when fighting. Now since this toy has finally run out of use, I guess you're next."
            "All you can do is hold onto Mount's body and mourn for him. Big Mark personally takes you to where Mount is."
    jump gameEnd

label sf_6:
    you "Violence not always the right thing to do, Mark. Believe me."
    mark "Who the hell are you to be saying that. Just look at your buddy Mount. I know he used to kill anyone that got in your way, am I wrong?"
    you "It was his job to do what he needs to do to protect me and my gang. And why do you use violence? Just for the hell of it?"
    mark "Hey, I don't need some kid to be judging me. I killed my parents after all the beatings they've given me. Ever since then, fighting is all I know."
    you "That's not a reason, Big Mark. I'm sorry that happened to you, but why throw that anger onto Mount? He hasn't done anything to you."
    mark "You wouldn't understand. If you were abused, you would have end up as obsessed with violence as I am."
    menu:
        "Kill Big Mark":
            you "I've had enough of your bullshit."
            jump sf_markdead
        "Is that so?":
            "You pull up your shirt and reveal a scar next to your waist."
            you "You see this shit? My own, damn mother sold my kidney just to get some drugs. I really wanted to do what you did, but I couldn't. And It wasn't because I was weak. It was because she was the only family I had back then."
    mark "Shit. Sorry to hear that little fella."
    mark "But so what? Why should that matter? Why should I give up this fighting obsession? I just want to fight. I enjoy the fight."
    you "Because everytime you do, you lose something. You are losing your true self. Do you even remember the first time you did anything with your parents?"
    mark "...No. I can't remember."
    you "That's right, Mark. This was the life you gave away. You lost a family."
    mark "And so what if I killed them. What does this have to do with my fight with Mount?"
    you "Because your parents changed you. That is their purpose, can't you see? They are the ones that are turning you into a shitty person."
    mark "So...so they succeeded? Am I one?"
    you "It depends. I don't think you are. But if you're still insisting on having the duel with Mount, then you might be making the wrong life decision."
    mark "I already killed my family. It's already too late for me."
    you "Idiot, you're not even close to being late. It's never too late to stop. Now, you have the chance to step out of this trap and be a new person after your sentences, or continue to be a slave of the two dead people for the rest of your life."
    "Big Mark falls to the ground, weeping and defeated."
    you "Mount, I think we're done here."
    "You stride through the crowd, with Mount following right behind you."
    "The two of you exit the prison without much damage."
    mount "Damn, buddy, I didn't know you had such a tragic past."
    menu:
        "It was the truth":
            you "I usually don't like talking about it, but you're the first person to hear my story, Mount."
            "You can feel your bond with Mount become as strong as it was back then."
        "It was a lie":
            you "Because I don't. I actually got that scar from fighting other drug dealers while I was rising to the top."
            "Mount bursts into laugher."
            mount "Now thats the %(playerName)s I know. Anyways, thanks for helping me out boss. I'll definitely return the favor."
    "With laughs and tears, the white Ford car heads towards the next destination: Sacramento."
    jump transfer2

label sf_markdead:
    $ GoodTalks -= 1
    "You put a bloody hole between Mark's eyes. In that moment, everyone was shocked, including Mount. The next thing you remember was everybody clawing towards you to tear you apart. But Mount was there to protect you. He was on your side."
    "With some scratches and bruises, the two of you managed to get out of prison before anyone can catch you."
    "You and Mount jumped into the car and booked it."
    jump transfer2

label transfer2:
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
        "Accept offer":
            jump sac_accept

        "Decline offer":
            jump sac_decline

        #"Shoot":
            #do something


    label sac_accept:
        "Governor kills you"
        jump gameEnd

    label sac_decline:
        "Baites seems dissapointed, and tells you to be on you way, swatting you out the gate with his tail"

    menu:
        "Try to sneak in and extract Buenos":
            jump sac_sneak

        "Try to bargain with guards":
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
