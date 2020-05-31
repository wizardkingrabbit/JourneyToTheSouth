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
define greta = Character("Greta Scottson")
define gates = Character("Mr. Gates")
define lb = Character("Little Boy")
define oop = Character("Owner of Plantation")

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
    you "I didn't kill them. And as wrong as my business is, we've never killed anyone before. The last thing I knew was that I was the last person left behind."
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
            mark "Like hell I can't, Did you forget who's the boss here?"
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
    you "Never. We always did business without any casualties. We aren't killers. But on the off chance that something really did happen, Mount's just doing his job to protect me and the gang."
    you "And why do you use violence? Why do you go so far as to cross the line and kill someone? Just for the hell of it?"
    mark "Hey, I don't need some kid to be judging me. I killed my parents after enduring all the beatings they've given me. Ever since then, fighting is all I know."
    you "That's not a reason, Big Mark. I'm sorry that happened to you, but why throw that anger onto Mount?"
    you "I know you're a smart man. Hell, you practically rule over this prison. Mount wasn't the one who did anything to you, so why do you keep insisting?"
    mark "Fighting to the death fills the hole in my chest. Through that abusement, I found my greatest passion."
    mark "You wouldn't understand. If you were abused, you would have end up as obsessed with violence as I am."
    menu:
        "Kill Big Mark":
            you "Sigh, this is going nowhere. All I'm hearing the the same reason over and over again."
            you "I've had enough of your bullshit."
            jump sf_markdead
        "Is that so?":
            "You pull up your shirt and reveal a scar next to your waist."
            you "You see this shit? My own, damn mother sold my kidney just to get some drugs. I really wanted to do what you did, but I couldn't. And It wasn't because I was weak. It was because she was the only family I had back then."
    you "I've endured as much abusement as you had, maybe twice as much, but in the end I didn't want to become the kind of monster that they were turning me into."
    mark "Shit. Sorry to hear that little fella..."
    mark "But so what? Why should that matter? Why should I give up my source of entertainment? My passion? I just want to fight. I enjoy the fight."
    you "Who's going to be left to fight when everybody is dead? You're going to end up being the last person alive and alone."
    you "Don't you get it? Everytime you do this shit, you lose something. A piece of yourself."
    you "Do you even remember the first time you did anything with your parents?"
    mark "...No. I can't remember."
    you "That's right, Mark. This was the life you gave away. You lost a family. Most importantly, you lost your true self."
    mark "And so what if I killed them. What does this have to do with my fight with Mount?"
    you "Because your parents changed you. That is their purpose, can't you see? They are the ones that are turning you into a shitty person."
    mark "So...so they succeeded? Am I one?"
    you "It depends. I don't think you are. But if you're still insisting on having the duel with Mount, then you might be making the wrong life decision."
    mark "I already killed my family. It's already too late for me."
    you "Idiot, you're not even close to being late. It's never too late to stop. Now, you have the chance to step out of this trap and be a new person after your sentences, or continue to be a slave of the two dead people for the rest of your life."
    "Big Mark falls to the ground, weeping and defeated."
    you "Mount, I think we're done here."
    "You stride through the crowd, with Mount following right behind you."
    "The two of you exit the prison without a single casualty."
    mount "Damn, buddy, I didn't know you had such a tragic past."
    menu:
        "It was the truth":
            you "I usually don't like talking about it, but you're the first person to hear my story, Mount."
            "You can feel your bond with Mount become as strong as it was back then."
        "It was a lie":
            you "Because I don't. I actually got that scar from fighting other drug dealers while I was rising to the top."
            "Mount bursts into laugher."
            mount "Now thats the %(playerName)s I know. Anyways, thanks for helping me out boss. I'll definitely return the favor."
    "With laughs and tears, the white Ford car heads away out for the next recruit to pick up."
    jump transfer2

label sf_markdead:
    $ GoodTalks -= 1
    "You put a bloody hole between Mark's eyes. In that moment, everyone was shocked, including Mount. The next thing you remember was everybody clawing towards you to tear you apart. But Mount was there to protect you. He was on your side."
    "With some scratches and bruises, the two of you managed to get out of prison before anyone can catch you."
    "You and Mount jumped into the car and booked it."
    jump transfer2

label transfer2:
    "After getting away from San Francisco, you finally get the chance to talk to Mount."
    you "Hey, Mount. I've been meaning to ask, but what happened to everybody back then? Why did you and everybody leave me?"
    "Mount doesn't say anything for a moment. You glance over and notice that he's clutching his hands tightly."
    mount "...it was my fault, boss. I was the one who killed those policemen. You know, that was actually my first time getting my hands dirty."
    mount "I'm a experienced sniper and fighter, yet the worse thing I did was shoot to threaten. That was all. This time, it was different. Everybody didn't know what to do, so we all ran..."
    #Entering Mount's flashback
    buenos "Mount...mount! Check if the other one is breathing!"
    "After shooting two policemen, Mount dropped his gun. He was shaking."
    "Buenos was the only one who had the courage to go up to them. Because of our countless, successful operations, this was really the first time dealing with a dead body."
    mount "H-how?"
    buenos "Put a finger under his nose, or just check his pulse! Hurry, we don't have much time left!"
    mount "He's not breathing, Buenos..."
    buenos "Shit. Agh, damnit! Where the hell did these guys come from?"
    "Buenos tries to think for a moment. Everything was going haywire at this point."
    buenos "Mount, we need to get everybody we can, and get out of here. That's the best option we could do right now."
    mount "W-what about the boss? We can't just leave him back there!"
    buenos "I'm sure he''ll understand why we need to go. It's now or never, Mount."
    mount "But I have to save my bos-"
    buenos "You can't do anything to save anyone right now!" with hpunch
    "Buenos grabs Mount, as well as the other members, and escapes. By the end of the raid, you were the only one there."
    #End of flashback
    menu:
        "I understand, Mount":
            you "If you guys hadn't left, this would have been the end for all of us. Buenos made the most reasonable choice."
            you "This was all my fault. I should have made sure this operation was completely safe,"
            you "Everybody got hurt because of me. I didn't want anyone to die that day."
            mount "%(playerName)s, It's not your fault. Even if it is, we're not going to blame you. We all carry the sin of leaving you. We regret that forever, so stop beating yourself up."
        "How could you, Buenos":
            $ GoodTalks -= 1
            you "I thought I could trust you guys. I sure as hell didn't expect everybody to leave their own leader."
            you "This is all his fault. If we had everybody guarding each post, then we all would have been able to escape."
            "All you can do is slam on the car horn. Mount waits patiently until blew off your steam."
            you "It doesn't matter anymore. The past is in the past now."
            mount "I'm sorry, boss. Everything we did was shit."
        you "Sigh. Anyways, let's just get going. Our next stop is Sacramento. Buenos, we're coming to get you."
    jump Sacramento

 # Chapter 3 (Jason Iino) <- das me :>
label Sacramento:
    define baites = Character("Charles Baites")
    define alfred = Character("Alfred")
    define guard = Character("Guard")
    define s_guard = Character("Security Guard")

    #I'll clean up dialogue/actually write dialogue later, just laying out framework
    #"Approach jail, which consists of tall buildings"
    #Greeted by Rebublican mayor Charles Baites, is a large civilized cobra"
    #"Tells you got a call from the governor about your quest"
    #"Expresses distrust for governor, but notes doesn't necessarily have ill will towards you"

    #"Offers to give you Buenos in exchange for the drug"
    #"Talks about how civil unrest has been high in Sacremento as of late"
    #"He believes that the drug could help to calm his citizens if they could analyze and reproduce it"
    #"Basically make him look desperate and be a tragic villain who doesn't want
    #to do the things he does, but feels he needs to for the greater good"

    "You drive up to Sacramento's county prison, Buenos' current holding place"
    mount "I don't know what he was brought in for exactly"
    mount "We all lost contact with eachother after splitting up"
    you "I heard this prison is run by Sacramento's Republican mayor"
    you "So we'll probably have to go through him to get to Buenos"
    "You pull up to the parking lot, shaded by the prison towering before you"

    "As you walk up to the entrance, you show the guard your papers from the governor"
    "He looks at them confused, then reluctantly lets you in"
    "As you make your way through the courtyard, a large snake the size of a man slithers out the front door"
    "He's wearing a sleeveless white business suit..."
    "...well, sleveless in the sense there are no arm holes, it just wraps around his body"
    "Following closely to his side is a tall, slender man in a pitch black suit"

    mount "Geez, what are you supposed to be?"
    "The man turns towards the large snake and pronounces a series of hisses to him"
    "The snake returns in kind, before the man turns back to you and Mount"
    alfred "\"Hello gentlemen, my name is Charles Baites, and this man in the black suit here is my translator Alfred\""

    menu:
        "Wait, YOU'RE the mayor of Sacremento?":
            "The snake gives a quick nod"
            baites "*quick hiss*"
            alfred "\"Yes that correct, I was elected into office almost a year ago\""
            jump sac_entrance

        "Nice suit":
            "The snake gives a quick grin, showing off his large fangs"
            baites "*upbeat hiss*"
            alfred "\"Thanks, you don't look too bad yorselves\""
            jump sac_entrance


    label sac_entrance:
        baites "*series of hisses*"
        alfred "\"Anyway, I've heard why you're here\""
        alfred "\"You've come for one of our prisoners on request of the governor no?\""
        you "That is correct, his name is Buenos"
        "You hand the paperwork to Baites, who grabs it with his tail"
        baites "*slow, spaced hisses*"
        alfred "\"I see... I see...\""
        alfred "\"Well, it seems like everything is in order\""
        alfred "\"However..\""
        alfred "\"Me and the governor aren't exactly on the gratest of terms\""
        alfred "\"Let's just say he doesn't ahve the greatest amount of influence here\""
        alfred "\Although... this does seem gravely important to you...\""

        baites "..."
        baites "*sinister hiss*"
        alfred "\"How about I make you a deal\""
        alfred "\"Word on the street is that your on mission to get some great, magical drug south of the border\""
        alfred "\"Now, there's been a lot of unrest around these parts as of late\""
        alfred "\"Protests, riots, people aren't the happiness around here at the moment\""
        alfred "\"Someone could do a lot of good with a magical item such as that drug\""
        alfred "\"I think you see where I'm going with this\""
        alfred "\"Promise that you'll deliver the drug to me instead of the governor, and we'll let your friend go\""
        alfred "\"Now doesn't that sound great?\""

        menu:
            "Accept offer":
                jump sac_accept

            "Decline offer":
                jump sac_decline


    label sac_accept:
        "Baites gives a wide grin showing off his sharp fangs"
        baites "*upbeat hisses*"
        alfred "\"Excelent, I'll see that your friend is released safely\""
        "Baites slithers away back into the prison, Alfred tailing behind him"

        "After a few minutes of waiting, you see Buenos walking put of the prison"
        buenos "Man I cannot believe what is happening. You made a deal with this devil?"
        you "Whether you come with me or stay here, keep complaining and get killed."
        "Buenos relunctantly follows you and get into the car. However, when you start the engine, you hear Mount whispering from the back seat."
        mount "Boss..."
        "You look back and see the mysterious man holding two guns, one pointing at Mount, one pointing at you."
        you "Okay, should I be nervous now?"
        mm "I think you should. Prove to me that you did not betray me."
        menu:
            "It was a lie. I only work for someone who can give me freedom and secure my family.":
                mm "I don't like liars, and I don't need one working for me."

            "I had to do that or I woul've died.":
                mm "Buenos, is that the case?"
                buenos "Sorry boss, but I am tired working with you now."
                mm "Well, well, well"
        "The mysterious man pulls the trigger, the last thing you hear is the sound of a firing gun."
        jump gameEnd


    label sac_decline:
        "Baites grin shifts to a look of disappointment"
        baites "*low, quick hiss*"
        alfred "\"That's a shame\""
        alfred "\"Well it seems you two have no business here, please be on your way\""
        "Baites rears back his tail, before swinging it in a wide arc at you and Mount"
        "It knocks the two of you clean out of the front gate, you see Baites slithering away"

        you "Well that was a bust"
        mount "You're telling me, urgh my aching back"
        you "You okay? That looks bad"
        mount "Yeah I'll be fine"
        "Mount slowly rises, clutching his back with his right arm"
        mount "But what are we going to do? It doesn't seem they're going to willingly give Buenos up"



        menu:
            "Try to sneak in and extract Buenos":
                jump sac_sneak

            "Try to bargain with guards":
                jump sac_bargain


    label sac_sneak:
        you "Maybe we can try to sneak in and get Buenos out"
        mount "You really think two people can sneak into a prison without ta plan?"
        you "It seems security is light today, probably to ensure that Baite's visit goes smoothly"
        mount "..."
        mount "Now that you mention it they do seem to be light on personnel"
        mount "How about I cause a distraction and you sneak around the back"
        you "Sounds good, what are you going to do?"
        mount "I'll think of something, just get into position and wait for something excessive"
        "You make your way around the courtyard gate near a laoding bay"
        "You look through the chainlink fence to see Mount moving towards the courtyard entrance"
        "He steps up to the guard in the booth, looking like he's about to strike up a conversation"
        "Suddenly, he begins throwing up into the booth all over the guard"
        "The gaurds around the entrance begin moving towards him"
        "Seizing the chance, you knock the lock off the door with the butt of your gun, and make your way inside"

        jump sac_buenos


    label sac_bargain:
        you "Lets try talking to the guards again, maybe they'll be more lenient with us"
        mount "Likely, old scales over there looks like he's harboring quite the grudge"

        "You make your way to the entrance again, the guard in the booth raising an eyebrow in suspicion"
        guard "I thought the mayor told you two to get out?"

        menu:
            "Emphasize the importance of the governor":
                jump sac_bargain2

            "Threaten with gun":
                jump sac_threaten


    label sac_bargain2:
        you "You see, we are on official business from the state governor"
        you "Crossing someone with that high authority may not be the wisest decision"
        guard "..."
        guard "..."
        "He seems to be mulling it over"
        guard "Let me see those papers again"
        "You hand them the governors paper's once more"
        guard "..."
        guard "Fine you can go on in"
        guard "But only you, not the big guy, don't want a chance of you two stiring up any trouble"
        mount "You know what, that's fair"
        mount "Good luck in there %(playerName)s, give my regards to Buenos, I'll guard the car"
        guard "Okay, get on in, but don't run into Baites while you're in there, I don't want to get on his bad size"
        "you make your way through the courtyard and into the prison"
        jump sac_buenos


    label sac_threaten:
        "You brandish your gun, pointing it towards the guard in the booth"
        "The guards eyes go wide in fear, as he instictivly puts his hands in the air"
        menu:
            "Shoot the guard":
                "Before he can react, you shoot the guard in the chest with your silenced pistol"
                "You scan around to see if anyone noticed"
                "You see Mount obstructing the view between you and the rest of the complex"
                "He gives you a nod"
                mount "Well that was abrupt"
                you "You mind guarding this mess until I get back?"
                mount "Sure thing %(playerName)s, good luck in there, give my regards to Buenos"
                $ GoodTalks -= 1
                jump sac_buenos

            "Tell him to let you in":
                jump sac_bad_shoot

            "Demand him to have Buenos brought out":
                jump sac_bad_shoot

    label sac_bad_shoot:
        "Before you can get a word in, the guard capitalizes on your brief pause to hit a button above the booth window"
        "He then dives down into the booth, as it's shutters slam shut over the window"
        "You hear alarms blaring, and the sound of heavy boots rushing towars you"
        "You turn to see guards rushing out of the front door of the prison"
        "Before you can react, they shoot you down with their handguns"
        "Your vision begins to go dark as blood spills from your body"
        "..."
        "..."
        jump gameEnd


    label sac_buenos:
        "The halls inside the prison are dimly lit and seem to go on forever"
        "There doesn't seem to be many people here"
        you "Baites presence must demand a lot of security"
        "You find one of the holding rooms, cells lining the many floors"
        "You scan a clipboard listing all the inmates names for Buenos"
        "You find his cell number, it appears to be in this room"
        "You approach the cell"
        "You see a man slumped over on the prison bed, not noticing your presence"

        menu:
            "Knock on the bars":
                jump sac_alert1

            "Call his name":
                jump sac_alert2


    label sac_alert1:
        "You knock on the bars to get Buenos' attention"
        "He slowly turns his head towards you, making little effort to get up"
        "His eyes then slowly come up, causing his face to light up, as he finally realizes who it is visiting him"
        jump sac_alert_done


    label sac_alert2:
        "You call Buenos' name to get his attention"
        "His eyes widen, as he immediately darts up out of his hunched posture, hearing a familiar voice after so long"
        jump sac_alert_done


    label sac_alert_done:
        buenos "%(playerName)s, is that really you?"
        "He approaches the bars, a wide smile covering his previosly sulken face as he snacs you head to toe"
        buenos "It is! But-but how? You got a lifetime sentence."

        "You explain to Buenos everything that's happened over the past few days"
        "The mysterious man, your family, the mission..."
        "...and why you've come to see him"
        "Suddenly, the joy drains from Buenos' face, being replaced by a look of dejection once more"
        "He slowly walks away from the bars, and falls into the same hunched state on the bed as when you first entered"

        buenos "I see..."
        buenos "..."
        buenos "..."
        buenos "%(playerName)s, maybe you should just leave"

        menu:
            "But why?":
                buenos "I've made some mistakes over the past few years"
                jump sac_story

            "What happened?":
                buenos "Things have not been great ever since we parted ways"
                jump sac_story


    label sac_story:
        buenos "When you got arrested, Mount, Tsing, and I went our seperate ways"
        buenos "Leaving you was hard, I could never shake the feeling the feeling maybe it
        would've ended diffeently if we would've stayed to help you"
        buenos "After we split up, I tried to get more work, something to distract me from losing you"
        buenos "I ended up joining a gang the next town over, they needed a translator to help with negotiations"
        buenos "They seemed well, they offered people protection from the more dangerous gangs in town in exchange for payment"
        buenos "However, things started to seem a little off after a while"
        buenos "People who were unwilling or unable to pay seemed to be immediate targets of gang harrassment"
        buenos "It was all so obvious, but I continuosly denied it to myself"
        buenos "I wanted so desperately to do something good, that I let blatant wrong doing happen
        in order to justify to my self that I was a good person after leaving you all those years ago"
        buenos "Eventually the whole operation went down, and most of us got arrested"
        buenos "I wasn't even upset, just relieved that the gang was eventually stopped"
        buenos "..."
        buenos "I really want to help you %(playerName)s, I really do. But my judgement just isn't
        there to be put in situations where peoples lives are on the line"

        $ sac_family = False

        menu:
            "You won't have to make that decision":
                buenos "Then why do you have a gun with you?"
                buenos "Your on a mission from a mysterious man who released you from jail to smuggle a drug from Mexico"
                buenos "That is no the kind of job where people lives aren't at risk"
                jump sac_silence1


            "That isn't the Buenos I know":
                buenos "Then why did you get arrested"
                buenos "Why did it come to us having to kill people"
                buenos "I may not have killed that man, but we can't pretend that the blood isn't also on my hands"
                jump sac_silence1


            "Please, my daughter is in danger":
                $ sac_family = True
                buenos "I'm really sorry for your situation %(playerName)s, I really am"
                buenos "But I just can't go back to that life"
                jump sac_silence1


    label sac_silence1:
        menu:
            "I promise it won't come to that again":
                buenos "..."
                jump sac_silence2

            "My family needs help":
                if (sac_family == False):
                    buenos "I'm really sorry for your situation %(playerName)s, I really am"
                    buenos "But I just can't go back to that life"
                    jump sac_silence2
                else:
                    buenos "..."
                    jump sac_silence2


    label sac_silence2:
        menu:
            "You've never been like this before":
                buenos "..."
                jump sac_silence3

            "Please, we need you":
                buenos "..."
                jump sac_silence3


    label sac_silence3:
        menu:
            "Buenos...":
                buenos "..."
                jump sac_silence4

            "We can't do this without you":
                buenos "..."
                jump sac_silence4


    label sac_silence4:
        menu:
            "Please...":
                jump sac_silence_done

            "We miss you...":
                jump sac_silence_done


    label sac_silence_done:
        buenos "%(playerName)s, maybe you should just go"

        menu:
            "Leave":
                "You leave the jail cell"
                jump sac_boss

            "Stay":
                buenos "Please don't make me call the guards"
                jump sac_stay1


    label sac_stay1:
        menu:
            "Leave":
                "You leave the jail cell"
                jump sac_boss

            "Stay":
                buenos "%(playerName)s"
                jump sac_stay2

    label sac_stay2:
        menu:
            "Leave":
                "You leave the jail cell"
                jump sac_boss

            "Stay":
                buenos "Please..."
                jump sac_stay3

    label sac_stay3:
        menu:
            "Leave":
                "You leave the jail cell"
                jump sac_boss

            "Stay":
                buenos "..."
                buenos "I'm sorry"
                "Buenos lets out a blood curtling scream"
                "Suddenly, you hear the sound of heavy boots making there way towards the cell"
                "You turn just in time for a guard to pull out his pistol and shoot you in the center of your chest"
                jump gameEnd


    label sac_boss:
        "You make your out of the prison courtyard, the harsh sun beating down on you"
        you "Buenos seems set on staying, maybe we could..."
        "*quick aggressive hiss*" # Maybe play a snake hissing sound
        you "ARRRGHH"
        "A sharp pain flares up in your arm"
        "You turn to see Baites sinking his teeth into you"
        "You struggle in an attempt to break free, the pain becoming almost ubearable"
        "Baites releases you from his grasp, causing you to colapse to your knees"
        "As the pain courses through you, you notice Alfred appearing from behind the large snake towering over you"

        baites "*slow hiss*"
        alfred "\"My apologies good sir, I really wish it didn't have to come to this\""
        alfred "\"You've just been injected with a lethal dose of venom, you will not last more than 10 minutes\""
        alfred "\"I have a dose of antivenom right here, please come to your senses and accept my offer\""

        "You notice a syringe of yelloew liquid holstered in a pocket on Baites' body"
        "You can already feel your legs going numb"

        menu:
            "Accept the offer":
                jump gameEnd

            "Decline the offer":
                jump sac_boss2


    label sac_boss2:
        "You shake your head no despite the pain it causes"
        "There must be another way out of this"

        baites "*reluctant hiss*"
        alfred "\"Fine, be stubborn\""
        alfred "\"You'll perish where you stand\""

        $ sac_turns = 0 # Turn count
        $ sac_cry = False # If you call for help or not

        label sac_boss_loop1:
            $ sac_turns += 1

            if (sac_turns >= 4):
                jump sac_boss3

            # Intro before menu
            if (sac_turns == 1):
                "Baites is slithering around you slowly"

            elif (sac_turns == 2):
                "Your vision is getting foggy"

            elif (sac_turns == 3):
                if (sac_cry == True):
                    "Mount isn't moving"
                else:
                    "Baites eyes you closely"
            # End of intro
            menu:
                "Shoot Baites":
                    jump sac_kill

                "Cry for help":
                    if (sac_cry == False):
                        $ sac_cry = True
                        "You let out a loud scream for help"
                        "..."
                        "Suddenly, you hear the sound of heavy footsteps rushing frm behind you"
                        mount "Don't worry %(playerName)s, I'm coming!" #Make this text better
                        "Mount rushes towards Baites, at a speed you didn't know was possible for a man of his size"
                        "But Baites dodges to the side, wrapping Mount with his tail, before slamming him into the pavement knocking him out cold"
                        jump sac_boss_loop1

                    else:
                        "You let out a loud scream for help"
                        "..."
                        "But nobody came"
                        jump sac_boss_loop1

                "Reason with Baites":
                    "You call out to Baites to tell him that he doesn't have to do this"
                    "But he can't understand a word you're saying"
                    "And Alfred doesn't seem keen on helping"
                    jump sac_boss_loop1


    label sac_boss3:
        buenos "Get away from them!"
        "Through the pain you can vaguely make out Buenos, staring down Baites as he rushes to your side"
        baites "*abrubt hiss*"
        alfred "\"What, what are you doing out here\""
        "Buenos lets out a series of hiss like sounds towards Baites, before turning to you with a smirk"
        buenos "I heard the guards talking about what you were doing, struggling to get through to Baites"
        buenos "I'm sorry I gave you the cold shoulder earlier, but it took me time to realize that you're right"
        buenos "Me sitting around moping all day isn't going to fix what I did"
        buenos "You're giving me another chance to make up for the past few years, and by hell if I'm going to let that oppurtunity pass up"
        buenos "You want to end this peacfully, then let's do it, I'll help you get through to him, just tell me what to say"

        $ sac_turns = 0 # How many turns until you perish
        $ sac_stress = 2 # variable of how many times you must make the right decision with Baites
        # goes down if you make a good decision that gets through to baites, win if it hits 0

        # baites confronts you at the gate, starts stressing, as he feels he's letting down his constituients
        # must choose one depending on what hes saying to calm him down so he can give you anti venom
        # must make so many right decisions in a few turns before you die
        # guranteed to get one on 4th turn, and not get one on the first, so basically have to say the right thing once in 2 decisions

        baites "*aggressive hisses*"
        buenos "\"Stop this nonsense, accept my offer and promise me you'll deliver the drug to me\""

        menu:
            "You don't have to do this":
                "Buenos translated what you said to Baites"
                "..."
                "He seems unfazed"
                jump sac_boss_a1

            "There has to be another way":
                "Buenos translated what you said to Baites"
                "..."
                "He seems unfazed"
                jump sac_boss_a1

            "Shoot Baites":
                jump sac_kill2


        label sac_boss_a1:
            "The feeling in your legs has gone away"
            baites "*slow hisses*"
            buenos "\"I'm sorry, I have a duty to my constituents\""
            buenos "\"The've suffered long enough\""

            menu:
                "You really do care about them":
                    "..."
                    baites "*quik hisses*"
                    buenos "\"Yes I do, and you're standing in my way of helping them\""
                    jump sac_boss_a2

                "You feel responsible for them don't you":
                    "..."
                    baites "*spaced out hisses*"
                    buenos "\"Of course, they elected me in, it's my duty to tend to their needs\""
                    $ sac_stress -= 1
                    jump sac_boss_a2

                "Shoot Baites":
                    jump sac_kill2


        label sac_boss_a2:
            menu:
                "I understand what you're going through":
                    "You explain you're experiences as a gang leader..."
                    "Having to provide for a group of people who relied on you for food and money..."
                    "The stress of how maybe one day you won't be able to help them"
                    "..."
                    "Baites' harsh glare softened a little"
                    $ sac_stress -= 1
                    jump sac_boss_a3

                "You're doing a great job governing them":
                    "You tell Baites that he's doing a great job"
                    "..."
                    baites "*aggressive hisses*"
                    buenos "\"How could you possibly know that\""
                    buenos "\"You've been in jail for 10 years and you just arrived in this town\""
                    buenos "\"Spare me your sympathy\""
                    jump sac_boss_a3

                "Shoot Baites":
                    jump sac_kill2


        label sac_boss_a3:
            "Your vision is starting to blur"
            baites "*sudden hisses*"
            buenos "\"Distress has been on the rise of late\""
            buenos "\"Riots, angry letters, protests...\""
            buenos "\"I can't just sit back and let that all happen\""

            menu:
                "You can't please all your citizens":
                    "You tell Baites that it's impossible to please everyone"
                    "That there's always going to be people who will be unhappy with a decision"
                    "..."
                    "Baites' head begins to droop downward"
                    $ sac_stress -= 1
                    jump sac_boss_end

                "They're not representative of everyone":
                    "You tell Baites that vocal minorites do exist sometimes"
                    "That while people may be upset over a decision he makes, it doen't necssarily mean it was the wrong one"
                    "..."
                    "Baites' head begins to droop downward"
                    $ sac_stress -= 1
                    jump sac_boss_end

                "Shoot Baites":
                    jump sac_kill2



        label sac_boss_end:
            if (sac_stress <= 0):
                jump sac_boss_win

            "Baite's form begins to go muddy"
            "You turn to Buenos, you can barely make out the features of his face"
            "Your vision begins to black out"
            "..."
            "..."
            "The venom finally cauht up to you"
            "You blacked out"
            jump gameEnd


        label sac_boss_win:
            $ GoodTalks += 1
            baites "*slow spaced hisses*"
            buenos "\"It's hard you know\""
            buenos "\"The stress of having to worry about satisfying hundred of people with different needs\""
            buenos "\"The doubt that comes with every decision you make, did a law you pass end up hurting more people in the long run...\""

            menu:
                "All you can give is your best":
                    "..."
                    jump sac_boss_win2

                "I'm sorry, dealing with all of that must be hard":
                    "..."
                    jump sac_boss_win2

        label sac_boss_win2:
            "Baite's form begins to go muddy"
            "You turn to Buenos, you can barely make out the features of his face"
            "Your vision begins to black out"
            "..."
            "..."
            "...%(playerName)s..."
            buenos "%(playerName)s"
            buenos "Wake up!"
            #scene fade back in

            baites "*calm hisses*"
            buenos "\"I've injected you with the antivenom, the pain should go away within the hour\""
            buenos "\"I'm sorry for causing you so much trouble\""
            buenos "\"I only meant to threaten you with the poison, I did not intend for it to come that close\""
            buenos "\"I... haven't exactly been in the best state of mind as of late\""
            buenos "\"Tension has been high recently, I so desperately wanted an easy out to all my problems\""
            buenos "\"It's been stressing me out beyond belief\""
            buenos "\"But you've helped me realize that I'm just going to have to persevere through it\""
            buenos "\"I don't know why you're going on this journey, but it seems very important to you if you're willing to go through all that for it\""
            buenos "\"I'll let you take your friend, he's a good man, and I wish you both the best of luck on your journey\""

            menu:
                "Thank you":
                    jump sac_leave
                "Good luck in office":
                    jump sac_leave


    label sac_leave:
        "Baites shoots a big grin and nod your way, before slithering off back inside the prison"
        jump SanDiego



    label sac_kill:
        "Despite the pain, you reach for your pistol"
        "Even though the venom is slowing your movements, you manage to draw and shoot your pistol before Baites can react"
        "You hit him right between the eyes"
        "Baites collapses to the ground, blood pooling around his head on the hot asphault"
        "Alfred flees at the sight of his boss' corpse lying lifeless on the stone"
        "Suddenly, Buenos comes out the front door of the prison, looking both horrified and confused"
        "He runs over to Baites, then to you, injecting you with the antivenom"

        buenos "I heard the guards talking about hat you were doing"
        buenos"I came to help, but it looks like you handled it"
        buenos "I'm sorry I gave you the cold shoulder earlier, but it took me time to realize that you're right"
        buenos "Me sitting around moping all day isn't going to fix what I did"
        buenos "You're giving me another chance to make up for the past few years, and by hell if I'm going to let that oppurtunity pass up"
        buenos "I know that was hard for you, but it seems you didn't have any other choice"
        buenos "But come on, we have to go, I hear guards coming"
        jump sac_kill_end


    label sac_kill2:
        "Despite the pain, you reach for your pistol"
        "Noticing your plan, Buenos picks up a sharp rock off the ground and begins to circle around Baites"
        buenos "*aggressive hisses*"
        "Baites, seeing Buenos as the bigger threat, starts to turn around to face him"
        "The venom is making your arms heavy"
        "You can barely muster the strength to raise the pistol"
        "You pull the trigger..."
        "And hit Baites in the back of the head"

        baites "*abrupt hiss*"
        "Baites collapses to the ground, blood pooling around his head on the hot asphault"
        "Alfred flees at the sight of his boss' corpse lying lifeless on the stone"
        "Buenos runs over to Baites, then to you, injecting you with the antivenom"
        "Your vision begins to clear up, the pain begins to fade"
        buenos "I know that was hard for you"
        buenos "I didn't like doing it myself, but I couldn't just leave you again"
        buenos "But come on, we have to go, I hear guards coming"
        jump sac_kill_end


    label sac_kill_end:
        if (sac_cry == True):
            "You hear the sound of alarms blaring"
            "Buenos helps you up, before going to Mount to wake him"
            "The three of you make your way to Ford, before driving off"

        else:
            "You hear the sound of alarms blaring"
            "Buenos puts your arm around his shoulder so that you can stand"
            "The two of you stumble back to the Ford to meet up with Mount, who seems a combination of shocked, confused and happy"
            "Buenos helps you in, before telling Mount to floor it"
            "The three of you make your way off, away from the prison"

        $ GoodTalks -= 1
        jump SanDiego


    #You should never go here
    menu:
        "Talk to trouble":
            $ GoodTalks += 1
            jump SanDiego
        "Kill the trouble":
            jump SanDiego



# Chapter 4 (Michael Kahn)
label SanDiego:
   define sd_warden = Character("SD Prison Warden")
   define sd_guard = Character("SD Prison guard")
   $ sd_silent_count = 0
   $ sd_stealth = False

   "After a long drive from Sacramento, you finally come into sight of the San Diego prison"
   "You approach the prison, planning to get Tsing and get going as quickly as your group can"
   "Its been a long enough journey already, and the faster its over the better"
   "As you get closer, you start feel like something is off, and your crew seems to feel the same way"
   buenos "Somethings not right."
   mount "So i'm not the only one thinking that, there seems to be a lot more activity than there should be at this time"
   "You get close enough now that you can make out the prison and easily see the heightened security"
   mount "It looks like the prison is on lockdown. Did someone try to escape while we were on our way here?"
   you "Not sure, but something is definetly going on"
   "You wonder in a way if maybe they were expecting your arrival, but theres no way that could be possible, right?"
   "You realize you have to quickly decide how you are going to handle this unexpected turn of events"
   menu:
       "Park near the entrance":
           "You head towards the entrance, deciding to ignore the warning signs"
           jump sd_route_direct
       "Park in the shadows":
           "Taking the warning signs into consideration, you head to park in the shadows"
           jump sd_route_careful

   label sd_route_direct:
       "You arrive near the entrance and find an empty parking spot."
       "As you and your crew get out of the car you hear sudden shouting in your direction"
       "Looking towards the sound, you realize you are being surround by the prison security"
       sd_guard "Get on the ground now! Surrender peacefully and noone needs to get hurt!"
       menu:
           "Surrender":
               "You and your team lay down as the security forces make a quick approach"
               "Before you know it you are blindfolded, and being dragged away somewhere"
               label sd_route_warden:
               "After some time of being forcefully moved, you are thrown down onto and quickly feel the cold embrace of a cement floor"
               "A door slams and you are soon left in complete silence"
               "After what seems like a lifetime, you hear some commotion coming from nearby"
               "You hear the door to the room you are in open and footsteps as a figure approaches you"
               "Your blindfold is torn off you and you look up to see a middle-aged women standing before you. She does not look happy"
               sd_warden "So you are my fathers pet that he sent to satiate his addiction"
               sd_warden "Did you really think I would let you just come in here and complete your mission"
               "The women sighs as she can see the visual confusion on your face, as you have no clue who she is or how she knows about your mission"
               sd_warden "It seems you don't realize the situation you are in. I am the warden of this prison, and I also just so happen to be the daughter of the man who controls you"
               sd_warden "However, I have no intention of letting him get his way, he has caused enough problems for me, he only seeks to ruin everything. You will not be helping him."
               menu:
                   "Stay silent":
                       sd_warden "It seems you think that staying silent will help you in some way, but don't worry, regardless of what you say or do, it is hopeless for you"
                   "Ask what she she means by mission":
                       sd_warden "Do not try to play games with me, I know who you are and why you are here. You won't be seeing your friend Tsing anytime soon"
                       "Tsing is in trouble! Things just got a lot more complicated"
               sd_warden "Now then, you can either be a good boy and give me the information or I want, or I can force it out of you"
               sd_warden "Where is my father sending you?"
               "It seems the warden does not know everything about the mission"
               label sd_route_direct_warden:
               menu:
                   "Tell the warden the truth":
                       "You decide that telling the warden the truth would be your best bet of getting out of here"
                       "As you explain about the mysterious man and the mission to go to Mexico, the warden gets angier and angier looking, but yet she does not interrupt you."
                       "You finish with your tale leading up to the point you arrived at this prison"
                       sd_warden "That damned man, has he not ruined enough already. He just can never have enough, he will not stop until everything is truly destroyed"
                       sd_warden "At least now I know where he is getting his supply from, maybe I can finally put an end to this"
                       sd_warden "As for you, you will be going nowhere, there is no way I will permit you to help that man ruin anything else"
                       "This is not going well, your chances of getting out of here are getting slimmer and slimmer, and you have not even found Tsing yet"
                       label sd_route_direct_convo:
                       menu:
                           "Stay silent":
                               "You remain silent. The warden continues with her outburst seemingly forgetting your presence"
                           "Try to get more information out of her":
                               you "What are you talking about? What has your father done to deserve such animosity?"
                               sd_warden "What has he done!? The better question would be what has he not done"
                               sd_warden "He tore our family apart, his addiction has hurt everyone around him, those who care about him have been tossed aside like nothing more than trash"
                               sd_warden "He has become a monster, a man I can no longer truly call my father. And I will do anything to stop him from continuing down this path."
                               jump sd_route_direct_convo
                           "Try to convince her to let you go":
                               "In a last attempt at getting out of here with Tsing, you make up a plan to try and convince the warden to let you go"
                               "Maybe if you convince her that you are going to Mexico with intents to sabotage, she would let you go as that would be seen as helping her"
                               you "I have no intents of helping that man either, I want him taken down just as much as you"
                               sd_warden "Oh really, and you expect me to believe that?"
                               menu:
                                   "Tell her you plan to kill her father":
                                       sd_warden "Is that what you think I want. That I want him dead? How dare you even so much as suggest the though. I will save him not kill him."
                                       "The warden storms off leaving you alone in the cell, where you contemplate your life choices. You remain locked up and fail your mission"
                                       return
                                   "Tell her you plan to destroy the plantation":
                                       "This seems to have peeked her interest as she turns to eye you weirdly"
                                       sd_warden "Destroy it you say? That would definetely hurt him, in more ways than one. That could work..."
                                       "The warden beings to mumble to herself, you can't hear what she is saying, but it seems the idea of destroying the plantation has really struck something"
                                       "After some time, the warden finally turns toward you"
                                       sd_warden "Do you really plan to destroy the plantation"
                                       "She stares at you, as if looking into your soul."
                                       you "Of course, even I can see how bad that man is, I would love to see him pay for what he has done"
                                       sd_warden "Hmm, seems you may be telling the truth ... I don't know why I am doing this, but this is the first time in a while an oppurtunity like this appeared."
                                       "The warden approaches you and undoes your binds"
                                       sd_warden "Do not make me regret this, I am an enemy you do not want to have"
                                       "Before you have a chance to respond, you are being pushed out by a couple of guards. And before you know it, you are back at the entrance of the prison."
                                       "Moments later your companions appear out front as well, including Tsing."
                                       $ GoodTalks += 1
                                       jump sd_end
                                   "Tell her you plan to take the drugs for yourself":
                                       sd_warden "And what will they help with? delay the inveviatble? Your a fool if you think I will help you with your own addiction!"
                                       "The warden storms off leaving you alone in the cell, where you contemplate your life choices. You remain locked up and fail your mission"
                                       return
                           "Attack her while she is distracted":
                               "While the warden is distracted by her rage, you move to get up from the cold floor"
                               "The warden is looking the other way, this is your chance. You get up and charge at the warden"
                               "As you get close she turns to the noise of you moving just in time as you tackle her"
                               "You slam her to the ground with all the force you can muster, but just as quickly as you got her down the door opened and multiple guards came rushing in"
                               "The guards pull you off her and slam you to the ground away from her. Another guard helps the warden up from the ground"
                               sd_warden "You fool, did you really think you could get away by attacking me, you are surrounded and under constant surveilence."
                               sd _warden "And now you will spend the rest of your days here. You will never complete your mission."
                               "The guards beat you down and leave with the warden, close the door loudly. You have failed your mission and have been imprisioned once again"
                               return
                   "remain silent":
                       if sd_silent_count == 0:
                           sd_warden "So you choose to hold your tounge, trust me you really do not want to piss me off more than I already am"
                           $ sd_silent_count += 1
                           jump sd_route_direct_warden
                       elif sd_silent_count == 1:
                           sd_warden "Still wish to piss me off, very well. If you don't start talking, your friends are going to suffer for it"
                           "You can tell the warden is starting to get really irritated"
                           $ sd_silent_count += 1
                           jump sd_route_direct_warden
                       elif sd_silent_count == 2:
                           sd_warden "You insolent fool, this is your last chance!"
                           "The warden is viusally pissed and you know that staying silent any longer is not going to end well"
                           $ sd_silent_count += 1
                           jump sd_route_direct_warden
                       elif sd_silent_count == 3:
                           "The warden slams you against the ground. You gasp as the wind is knocked out of you."
                           sd_warden "You really think this is a game you fool. Seems you really need to be taught a lesson. Final chance or you and your companions are done!"
                           $ sd_silent_count += 1
                           jump sd_route_direct_warden
                       else:
                           sd_warden "Very well, you only have yourself to blame for this. I gave you plenty of chances to come clean and you have decided that being stubborn was your best choice."
                           "The warden leaves you and slams the door to the room you are in. You hold out some hope that this is only temporary and you will soon be on your way again."
                           "But as time went on you lost hope of any chance of escape. You never would see the light of day again. You have failed your mission"
                           return

           "Make a run for cover":
               "You make a break for cover behind your nearby car, your crew following suit."
               "As you and your team crouch down behind the car and wait for the inpending barrage of bullets, you hear the guards shouting once more"
               sd_guard "Surrender now or we will open fire! This is your last warning!"
               "Do you try to fight your way out of this or try to get in the car and take off running"
               menu:
                   "Fight your way out":
                       "You give your crew members a look and they nod in ackowledgement"
                       "All of you came to realization that there is not much chance of getting out of there"
                       "You draw your pistol and leave the cover of your car"
                       jump sd_route_openfire
                   "Attempt to flee":
                       "Deciding that escape was your best option now, you make your way into your car from the passenger side"
                       "Buenos and Mount dive into the back seat as you slam on the gas, aiming to get out of there quickly as possible"
                       "You manage to escape and find a place to lay low for a bit, but now getting Tsing out is going to be even harder than before"
                       "A bit later on, you prepare to get Tsing out with a more careful approach"
                       jump sd_route_careful
           "Open fire":
               "You decide that the only possible choice in this situation is to open fire on the approaching security"
               "You draw your pistol and bring it up to fire"
               label sd_route_openfire:
                   "Before you even have time to get a shot off, you hear the sound a high caliber rifle going off"
                   "You fall to the ground, and as the light fades around you, you quickly realize how stupid a choice deciding to fight your way out was"
                   return

   label sd_route_careful:
       "With the prison on high alert, the only way Tsing is getting out anytime soon is through breaking him out"
       "As you look around the outside of the prison, you find your point of entry, a delivery bay."
       "Suprisingly, there are not many guards around, you guess they focused most of their attention elsewhere."
       "Entering the delivery bay, you find a doorway leading into the prison that has a few guards protecting it, you also spot a service room off to the side"
       menu:
           "Blitz the entrance and force your way through":
               "You get yourself and the team into position, with Mount taking point"
               "With one last deep breath, you give the signal to charge. Mount takes off and takes down the first two guards with ease"
               "You and Beunos take down the other guard. With all the guards down, you make your way into the prison"
           "Sneak into the service room":
               "You sneak into the service room off to the side, making sure none of the guards noticed you or your crew."
               "Once all of you are inside, you look around and take stock of your options"
               "Luck would seem to be on your side this night as there were some mainainence uniforms hung up on a rack neaby. You found your ticket inside"
               "You and the crew quickly changed into the uniforms and walked back outside towards the entrance to the prison, confidence would be key here"
               "Approaching the guards, you quicken your step to get past them as quick as possible, but one of the guards steps in front of you"
               sd_guard "Hey, what are doing out here? The prison is in lockdown."
               menu:
                   "Shrug off the guard":
                       "You simply shrug at the guard as you and your crew move towards the doors."
                       sd_guard "Ugh, you maintainence guys are just as rude as ever. I'm not paid enough to deal with this."
                   "Make up a lie":
                       you "There was an urgent request for a maintainence crew over in the east wing for some undisclosed matter. We were just told to get in as fast as possible"
                       sd_guard "Leave it to management to leave us in the dark, especially with everything being so hectic right now, hurry along, I just want to go home"
               $ sd_stealth = True
               "Somehow, this worked and you made it past the guards and into prison, now the real challenge begins"
       "Once in the prison, your realize that you don't actually know where Tsing is. Your first step is to find where they are holding him prisoner."
       "Ahead of you are two paths to choose from. To your left is the path to the offices of the prison, and ahead of you is a path leading to the center of the prison."
       "The offices are likely to have prisoner information, so the first step is heading in there."
       if sd_stealth == False:
           "So far no one has noticed the guards that were taken down in the delivery area, but time is of the essence"
       "You rush down the hallway and enter the offices, your best bet is likely a higher up adminstrator. You scan the various office rooms trying to find one which can possible get you the information you need"
       "And there it is, the warden's office, that has to have the information needed. Only issue is the door is locked"
       "Mount comes up behind you and pushes you to the side. He slams foot in the door a few tims and eventually breaks it open"
       you "I guess that is one way to get in there ..."
       "Mount simply shrugs and steps to the side to let you inside"
       "Once inside you set about searching the various files until you can find anything on Tsing."
       "After some time, you finally find a document stating that Tsing was transfered into the high risk section of the prison, the most secure part. Although at this point saying its the most secure isn't really saying much"
       "You quickly share this information with the crew and head back towards the hallway you came from. Quickest way to the high security section is through the center of the prison"
       "Once back at the hallway you quickly turn down the other way and head towards the center of the prison"
       if sd_stealth == False:
           jump sd_route_loud
       else:
           jump sd_route_stealth

   label sd_route_loud:
       "As you head down the hallway, the alarm sounds. They clearly found the guards back at the delivery bay. Things are going to get hectic from here on out, especially the longer it takes"
       "You quickly rush down the hallway, your crew close behind you, as you make your way through the various hallways and rooms, dodging the guards that are now running around trying to find the cause of the alarm"
       "With how fast you were moving, it didn't take long to reach the high risk area. Thankfully it seems since you set the alarm off in the other part of the prison, there was less security around here"
       "You quickly start checking through the cells hoping ot spot Tsing. After some time you come across one of the last cells and spot the very man you have been looking for"
       you "Hello Tsing, it's been quite some time hasn't it"
       "Tsing looks up at you, visibly confused at your sudden appearence before him"
       tsing "Either I have gone truly crazy, or is it really you?"
       you "Of course it is really me. I need your help and I am getting you out of here"
       tsing "Good luck with that, this place is locked down tight, only way your getting me out of this cell is through the security office for this section of the prison"
       you "Well then, seems I know where I am going next"
       "You give Tsing a quick nod and head off towards the security office"
       tsing "Good luck you crazy fool"
       "The security office was not very hard to find thanks to the various signs posted around. Chances are the guards inside were going to be on high alert. So be ready for a fight"
       "As you approach the door, its pretty clear that your best chance is to charge in and try to get the drop on the people inside. You quickly relay this to your team and they nod in agreement"
       "You charge the door and quickly enter the room with your gun drawn"
       "But they were ready for you, and before you know it you are being held at gun point by a group of guards. This is not going to end well"
       "Before the guards though, stands a women. She clearly isnt a guard based on what she is wearing, but she has an air of authority about her"
       jump sd_route_confront
   label sd_route_stealth:
       "You head down the hallway, easily getting past everyone. Seems you fit right in as the maintainence crew."
       "Quickly making your way through the prison, while still trying to avoid anyone finding out your identity, you reach the high risk section"
       "The first step here is to actually find Tsing and confirm the information you found is correct"
       "After some searching, you find Tsing in a cell towards the rear of the section"
       "As you approach the cell, Tsing looks up at you"
       tsing "Well this is not what I was expecting to see tonight. You the reason the prison is so tight on security right now?"
       you "No clue if I am the reason, but I am here to get you out. I need your help with a mission."
       tsing "Well good luck with that, only way I am getting out is if you can get to the security office and unlock my cell from there. But that place is highly guarded."
       you "Well, we will see what we can do, we at least have the element of suprise so far. Everyone seems to think we are actually a part of the maintainence crew"
       "After your brief conversation with your old companion, you now know your next destination, the security office."
       "Making your way back out of the high risk section, you find a hallway leading to he security office for this part of the prison. In there would be your only chance of breaking Tsing out"
       "As you approach the entrance to the security office, you peak into a small window into the office. Inside you spot a few guards and middle-aged women in a suit. She must be some admistrator or something"
       "You need to get in and access the security controls, so the guards are going to have be dealt with"
       menu:
           "Barge in and force the guards to surrender":
               "You slam the doors to the security office open and rush in. But as you go to shout at them to surrender, they are already up and ready to defend against you"
               jump sd_route_confront
           "Sneak in and subdue the guards":
               "You quietly open the door, making as little sound as possible. With door open, you sneak into the room, the guards still unaware of your presence"
               "As quickly as possible, you and the team charge at the guards and subdue them quickly. Seems stealth was the right option"
               "With the people in the room subdued, its time to get Tsing out. You look around the room at the various control panels and find one showing controls to open cells. Easy enough"
               "With Tsing's cell door open, its time to grab him and get out of there quickly"
               "You quickly reach Tsing's now open cell and throw him a spare uniform you had grabbed earlier"
               tsing "I am amazed any of this is actually working, to think I may be out of here in just a few moments"
               you "Well if you want things to continue working, hurry up and put that uniform on"
               "Tsing quickly changed into the uniform, and the four of you head back out to the way you came in from"
               "Quickly making your may down the various hallways, hoping to remember the way out, you end up back in the original hallway you entered from"
               "Just a little more and you and the rest of your crew will be out of this prison and on the road to Mexico"
               tsing "Lets get going, I am quite tired of being in this place"
               "You nod in agreement, and walk out into the delivery bay, and further on back towards your car"
               $ GoodTalks += 1
               jump sd_end

   label sd_route_confront:
       sd_warden "Did you really think you could just come in here and get away with no issue! You are going nowhere, surrender now!"
       "You look around the room and notice a few armed guards along with the women. You may be able to fight your way out as it seems she expects you to surrender, but is it worth the risk?"
       menu:
           "Open fire":
               "There is no going back now, you quickly raise your weapon and open fire, your crew following suit. The women clearly wasnt expecting you to do something so crazy and her and the gaurds didnt even have a chance to properly react."
               "Killing was not your first choice, but at this point you do not really have time to think about it."
               "While your crew goes and checks to make sure the threat is no more, you go about looking for a way to unlock Tsing's cell"
               "After some looking around, you find a control panel for cell control, exactly what you needed. With some quick button presses you get confirmation that Tsing's cell was opened. It is time to get out of here"
               "You and the crew quickly leave the security office before anyone realizes what happened in there and make your way back to Tsing"
               "After a short trip you arrive at Tsing's cell, Tsing is already up and ready to go when you get there"
               tsing "Well you somehow did it, let us get out of here, quickly"
               you "Was not pleasent, but we have more important things to deal with right now, lets go"
               "You and the crew quickly make your way back to the way you came in from. You rush through the hallways and out into the delivery bay. Freedom at last"
               "You head to the car and get ready to continue with the mission"
               $ GoodTalks -= 1
               jump sd_end
           "Surrender":
               "You realize that your chances of getting out of here are basically nothing at this point. You throw down your weapon and raise your hands in the air"
               "The guards quickly come up to you and bind you and your crew, then blindfold you. Before you know it your being shoved off to somewhere else in the prison"
               $ GoodTalks += 1
               jump sd_route_warden
   label sd_end:
       "You take off from the prison, not looking back as you speed down the road. Everyone in the car is quiet, Tsing eventually breaks the awkward silence"
       tsing "So you went to all this effort to get me out, mind explaing what I am actually being taken along for?"
       you "We are heading to Mexico, toa plantation down there specifically, picking up a package"
       tsing "Thats it? Sounds like getting me to come along sounds a bit excessive."
       you "The person we are working for isn't your average man, he's danagerous and we have no clue what we are actually getting into"
       tsing "Sounds pleasent, I am curious how you came across this mission, since last I knew you were still in prison, for life"
       you "I was, until recently that is, the offer came to me in prison and got me out, not exactly willingly, but I did not really have much choice in the matter"
       tsing "And I am guessing your not going expand on that, are you?"
       you "No, but I have no intention of going back to prison, or letting any of you go back either, we are getting this mission done then going free"
       tsing "Well, sounds like this going to be fun ... lets get this done with"
       you "You read my mind, the faster we are done, the faster we can all get away from this whole mess"
       "The silence in the car returns, as you contrinue to drive down the card, getting close to ending this all"
       jump border


# Chapter 5 (Ian Maynard)

define protestor = Character("Protestor")

label border:
    "Riding down the 5 the air starts to get warmer. You see the border just over the horizon"
    you "Finally"
    buenos "What was that?"
    you "I see the border... and..."
    "Squinting your eyes as you get off the highway, you see a large crowd near the entrance to the underground passage"
    you "Oh give me a fuckin break..."
    "You and the team park the car and get out to approach the crowd. They appear to be protesting something. Imagine having that kind of time"
    "You seem to spot their leader, a tall nordic looking woman"
    you "Excuse me, what exactly is goin on here?"
    protestor "We are protesting the absolutely ABSURD notion that Techro needs any more office buildings in this part of town. They already have 3 on this street alone!"
    protestor "To make matters worse, they plan on making this bigger and ,as a result, more environmentally hazardous than their previous offices"
    protestor "We refuse to stand by as these corparate douchebags try and ruin our planet!"
    you "Peace, love, and all that. Can me and my friends just squeeze past those barricades?"
    protestor "Not happening. We dont know who you are or WHO you work for!"
    "The woman eyes the men in suits around 20 feet away. They are glued to their cell phones"

    menu:
        "Convince Greta and the group to leave":
            you "Wait aren't you that lady from the news? Greta Scottson right? Funny seeing you here given whats happening in LA just a couple hours away"
            greta "What the hell are you going on about!? Whats in Los Angeles?"
            you "Oh you didnt hear? Extron is building a new pipeline right through the heart of Los Angeles under a lower class neighborhood!"
            greta "Oh yeah which one then smart guy?"
            "You remember in your days of hustling that you once delivered to a real shady neighborhood in LA once. You are able to name an adress almost immediately"
            "Greta is shocked"
            greta "Wow I had no idea! We should head there right away!"
            "Greta signals to the rest of the protesters who scramble to their cars, your team travels through the passage amongst the chaos..."
            $ GoodTalks += 1
            jump Mexico
        "Help the Greta with the suits":
            you "What if we tried to talk to these so called Douchebags for you?"
            protestor "Be our guest! Talk to the main douche. Gates."
            "The protestor laughs and goes back to chanting with the crowd"
            "You and the team approach the group of suits."
            you "Excuse me, are you in charge here?"
            "The man pays you no attention, and continues staring at his phone"
            you "Ok then, hey Mount I think this guy wants to talk to you"
            "Mr. Mount nods and starts to move toward him"
            "Two bodyguards come out from behind the man in the suit and block his path"
            gates "Can I help you gentlemen?"
            jump confront_gates
        "Shoot Greta and run for the Passage":
            you "Alright screw it, we are so close I dont have time for this"
            "You pull out your gun and shoot the woman, amongst the chaos your team travels through the passage"
            "Buenos glares at you but says nothing"
            $ GoodTalks -= 1
            jump Mexico

label confront_gates:
    # talk to gates, dude is an absolute nut job. the idea of extraterrestrial life is not crazy but this dude absolutely is
    menu:
        "Ask gates what the project is about":
            you "What do you guys want a fourth office building for on this street?"
            gates "Oh this is no mere office building you feeble-minded fool"
            "Feeble-minded? Who says that"
            you "Ok then what is it Shakespeare?"
            gates "This building shall be a BEACON"
            gates "A shining beacon of progress that will finally allow humanity to join the society amongst the stars"
            mount "This dude talkin' about aliens?"
            "Ok we are dealing with a nut job. Great."
            jump confront_gates
        "Ask gates to cancel the project":
            you "Listen dude, you dont need a fourth office building in this area. Your company doesnt even have that many employees! Just cancel the project man."
            gates "Oh you are just one of the protestors, move along"
            "Gates goes back to his phone and pays you no mind"
            jump confront_gates
        "Kill Gates":
            "You reach for your weapon..."
            "But the left bodyguard is faster than you. He draws his weapon and shoots you square in the chest"
            jump gameEnd
        "Return to the Protestors":
            "You begin to realise it is useless to try and talk to this guy and walk back toward the protestors"
            jump backToGreta
label backToGreta:
        menu:
            "Convince Greta and the group to leave":
                you "Wait aren't you that lady from the news? Greta Scottson right? Funny seeing you here given whats happening in LA just a couple hours away"
                greta "What the hell are you going on about!? Whats in Los Angeles?"
                you "Oh you didnt hear? Extron is building a new pipeline right through the heart of Los Angeles under a lower class neighborhood!"
                greta "Oh yeah which one then smart guy?"
                "You remember in your days of hustling that you once delivered to a real shady neighborhood in LA once. You are able to name an address almost immediately"
                "Greta is shocked"
                greta "Wow I had no idea! We should head there right away!"
                "Greta signals to the rest of the other protesters who scramble to their cars, your team travels through the passage amongst the chaos..."
                $ GoodTalks += 1
                jump Mexico
            "Shoot Greta and run for the Passage":
                you "Alright screw it, we are so close I dont have time for this"
                "You pull out your gun and shoot the woman, amongst the chaos your team travels through the passage"
                "Buenos glares at you but says nothing"
                $ GoodTalks -= 1
                jump Mexico

# Chapter 6 (haonan lin)
label Mexico:
    "After all kinds of hardships, you and your teammates finally arrived at the destination of this trip"
    "Everyone is excited and feels that victory is so closed"
    "However, things are not easy as they seem. Outside the plantation, there is a huge wall"
    "The only entrance to the plantation has many security guards at the door"
    "You and your teammates can try to enter from the main entrance or try to find another way into the plantation"
    menu:
        "Try to enter from the main entrance":
            "Riding down the street to the entrance of the plantation, the guards stop you"
            guard"What are you doing here? Strangers are not welcome here"
            you "We are here to see your boss. We are here for your boss to ask for some thing"
            guard"What's that?"
            "But you don’t want to tell the guard the purpose of this trip"
            you "You don't have to know what it is. It is better for you"
            guard"If you don't say it, you can fuck off"
            "You are so angry because the guards perverted you impatiently."
            buenos"It's not a big deal. Let me tell you. We are looking for a special king of drug. I hear this special drug is only available here"
            guard"Drug? Are you kidding me? We don't have that here. Get out of here"
            "You notice the guard starting to pull out his gun. You look at their gear and decide it's best to slip away first and try to find another way to get into the plantation"
        "Find a way into the plantation":
            pass
    "After some searching, you discover a secret cave that may lead to the plantation"
    "You and your teammate decide to give it a try no matter what is end at the cave"
    "The dark tunnel seemed to have no end, and the atmosphere became very oppressive"
    buenos"Shall we do it another way? There may be no way out"
    you "Hang in there a little longer and victory is ahead. I think the exit is just ahead"
    "Suddenly you smell the fresh air and everyone gets excited"
    "Finally, you climbed out of a hidden manhole cover"
    "You start searching for this plantation"
    lb"Who are you? What are you doing here?"
    "Your whereabouts were caught by a little boy. Seeing whereabouts are about to be exposed, and the mission is about to fail. Buenos rush up and try to cover the little boy's mouth"
    lb"Are you here to save us? We have been here for a long time"
    "The boy's voice suddenly fell, and the boy looked at us carefully and hopefully"
    you"What are you doing here at such a young age?"
    "The boy's words and deeds startled you. You decided to ask some information from little boy"
    lb"We are all here to work for the master. If we do not meet the requirements of the master, we will get punishment by him"
    you"Master? Why you call him master? Are there many children like you?"
    lb"The owner of this plantation let us call him master. If we don’t do this, we will be punished"
    lb"Also, master will find many children without parents to come here and work for him. We have nothing to rely on but to work for him"
    lb"Can you help us?"
    you"If you can take me to see your master, I will help you. I will try to convince him. If it doesn't work, I will think of another way"
    "You decide to let the little boy take you to see the owner of this plantation first. The rest is just perfunctory words"
    lb"That's very kind of you. The master believes me the most, and I will take you there"
    "Led by the little boy, you finally meet the owner of the plantation"
    oop"See who is coming? My best friends. I have waited so long, and you finally came"
    you"Do you know who we are? We just arrived here"
    you"Not even your guard knows who we are. He also stopped us from coming in. We have to work hard to get here"
    oop"They are just performing their duties. Please understand their difficulties. I'll give them a little punishment afterwards"
    oop"Your boss has told me your purpose. And they don’t deserve to know too much. Can I see the hand writing of your boss."
    "You hand the handwriting to the owner. The owner tell his men to give you the drug"
    "You look at the small red pills in the transparent jar in your hand and start to think what is the magic of these pills. Why can it let so many people struggle to get it"
    you"What use are these pills? What secrets do they have?"
    oop"They are just ordinary pills. It won’t have any effect if you eat it, or if you want to try it"
    you"If it is ordinary, why do we spend so much effort to get it. Don't treat us like fools"
    oop"OK. OK. Then let me put it another way. It allows you to get something and lose something. For example, power?"
    "You poured a pill on your hand. Looking at this blood-red pill, you are deciding whether to give it a try"
    menu:
        "eat it":
            jump gameEnd
        "Put it back in the jar":
            pass
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
    "You choose to attack the plantation owner, and all your friend choose to help you."
    "You rescue the children and ask your team to bring these kids to US while you take the underground railway alone."
    "when you see the governor, he tells you that all kids are treated as illegal immigrants and sent back to Mexico."
    "He asks you to give him the drug and the pistol. You lose your pistol in the underground railway, so for this branch, you can only obey him."
    "He told you that you can go back to your home and you are free now."
    "When you go back to your home, you see your wife and daughter waiting for you come back."
    "After all those, you finally can enjoy the free time with you family."
    return

label ending2:
    "With the fire of the plantation,you see more and more people come to surround your teams."
    buenos "you are killing too many people,I’m done with you"
    "But they still need some time to be here. You want to kill Buenos, because Buenos know every bold in your hand and you cannot accept betray"
    tsing "we must leave right now! They are almost here."
    menu:
        "Kill Buenos, then leave":
            "You killed Buenos, but you are surround by enemies. Because you burn the plantation,You were caught back and tortured to death."
            jump gameEnd
        "Leave right now":
            you "Let’s go"
            "During your retreat, the enemy caught up with you. After a gun fight, Tsing and Mount were shot by the enemy. Fortunately, you flew back to the US with the drug."

    "When you came out of the airport, the governor ’s people found you and took you to the governor."
    "Governor ask you to give him the drug and the pistol. But you see governor do not bring a gun, you are thinking to kill the governor and sell the drug"

    menu:
        "Shoot Governor":
            you "Go fuck yourself!"
            "You pull out your gun and prepare to target the governor."
            "Before you shoot governor, his bodyguards kill you immediately"
            "You are so close to you freedom and your family, but finally you choose the wrong step and fall in blood."
            return
        "Give him the drug and the pistol.":
            "The governor nodded and asked the bodyguard to send you home."
            "After a few days, the governor sent some money and informed you that your files had been cleaned up."
            "Finally, you can enjoy your life with your family"
            return

label ending3:
    "You choose to convince the plantation owner, but he still refuse."
    "But he give you some money to make you leave."
    "Your still want to convince the owner, but you see him is angry."
    menu:
        "Continue convince him":
            "Plantation owner took out a gun and shoot you and your team"
            "You and your team try to fight back, but owner's bodyguards arrive soon. And kill all of your team."
            return
        "Accept the money and leave":
            you"Let's go, I'm going to ask the state governor to take care of this."
            buenos"Shut up, this plantation is protected by the governor. We gonna leave you after arriving home"
            "You and your team flew back to the US with the drug."
    "When you and your team came out of the airport, your team leave you."
    "The governor ’s people found you and took you to the governor."
    "Governor ask you to give him the drug and the pistol. But you see governor is alone and do not bring a gun, you are thinking to kill the governor and sell the drug"
    menu:
        "Shoot Governor":
            you "Go fuck yourself!"
            "You pull out your gun and prepare to target the governor."
            "Before you shoot governor, his bodyguards kill you immediately"
            "You are so close to you freedom and your family, but finally you choose the wrong step and fall in blood."
            return
        "Give him the drug and the pistol.":
            "The governor nodded and asked the bodyguard to send you home."
            "After a few days, the governor sent some money and informed you that your files had been cleaned up."
            "Finally, you can enjoy your life with your family"
            return


label ending4:
    "Because you kill too many people, the plantation owner do not trust you."
    "He think you are a joker, and told you leave right now."
    "However, you need to close the plantation or destroy it."
    "But plantation owner have lots of bodyguards."
    menu:
        "Kill the plantation owner":
            "You took out a gun and killed Owner, but then his bodyguard arrived and killed all of you"
            jump gameEnd
        "Leave the plantation":
            "You and your team go back to US with drugs"
    "When you came out of the airport, the governor ’s person found you and took you to the governor."
    "Governor ask you to give him the drug and the pistol."
    "He appreciates that you kill many troublemakers along your journey, so he offers you to stay and work for him."
    menu:
        "Refuse the work":
            "Governor said you kill too many people, and know too much thing about me"
            "He told his bodyguards to kill you"
            return
        "Accept the job":
            "You accept the job."
            "However, because you work for governor, you cannot see your family forever."
            return

label gameEnd:
    "You were so close to your freedom and your family, but now you fall in your own blood. Hope you have a better luck next time."
    return

label test:
    "Use jump to jump between scenes"
