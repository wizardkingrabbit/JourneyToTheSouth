# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#art
image bg Prison_Gate_C = LiveTile("Prison_Gate_C.png")
image bg Prison_Gate_B = LiveTile("Prison_Gate_B.png")
image bg Prison_Gate_A = LiveTile("Prison_Gate_A.png")
image bg Border = LiveTile("Border.png")
image bg Border_Office = LiveTile("Border_Office.png")
image bg Border_Protest = LiveTile("Border_Protest_B.png")
image bg Cityhall = LiveTile("Cityhall.png")
image bg Dream = LiveTile("Dream.png")
image bg Freeway = LiveTile("Freeway.png")
image bg Gates_Office = LiveTile("Gates_Office_B.png")
image bg In_Car = LiveTile("In_Car.png")
image bg Openspace = LiveTile("Openspace.png")
image bg Out_Car = LiveTile("Out_Car.png")
image bg Plantation_Gate = LiveTile("Plantation_Gate.png")
image bg Plantation_Inside = LiveTile("Plantation_Inside.png")
image bg Plantation_Farmland = LiveTile("Plantation_Farmland.png")
image bg Prison_Cell_A = LiveTile("Prison_Cell_A.png")
image bg Prison_Hall = LiveTile("Prison_Hall.png")
image bg Prison_Office = LiveTile("Prison_Office.png")
image bg Underground_Railroad = LiveTile("Underground_Railroad.png")

image baitesp = LiveTile("baites.png")
image big_markp = LiveTile("big_mark.png")
image buenosp = LiveTile("buenos.png")
image buenos_prisonp = LiveTile("buenos_prison.png")
image gretap = LiveTile("greta.png")
image guardAp = LiveTile("guard1.png")
image guardBp = LiveTile("guard2.png")
image guardCp = LiveTile("guard3.png")
image little_boyp = LiveTile("little_boy.png")
image little_girlp = LiveTile("little_girl.png")
image mountp = LiveTile("mount.png")
image mount_prisonp = LiveTile("mount_prison.png")
image mr_britp = LiveTile("mr_brit.png")
image mysterious_manp = LiveTile("mysterious_man.png")
image mysteryp = LiveTile("mystery.png")
image policep = LiveTile("police.png")
image protesterp = LiveTile("protester.png")
image recpetionistp = LiveTile("recpetionist.png")
image tsingp = LiveTile("tsing.png")
image tsing_prisonp = LiveTile("tsing_prison.png")


# Endings
define GEthresh = 3
define GoodTalks = 0
define GoodEnding = True
define BurnPlantation = True

# some flags use within a Chapter
define sf_bribe = False
define sf_threat = False
define sf_headlock = False
define daughter_die = False
define sd_gun = False
define sd_disguise = False
define sd_silent = 0
define sd_asked = False

define you = Character("you")
define sgboss = Character("State Governor")
define uspa = Character("US Police A")
define uspb = Character("US Police B")
define mark = Character("Big Mark")
define daughter = Character("Anny")
define unk = Character("???")
define guard = Character("Prison Guard")
image guard1p = LiveTile("guard1.png")
image guard2p = LiveTile("guard2.png")
image guard3p = LiveTile("guard3.png")
define pguard = Character("Guard")
define officer = Character("Chief Officer")
define mm = Character("Mysterious Man")
define mount = Character("Mount")
define tsing = Character("Tsing")
define buenos = Character("Buenos")
define greta = Character("Greta Scottson")
define gates = Character("Mr. Gates")
define lb = Character("Little Boy")
define oop = Character("Mr. Brit")
define sd_warden = Character("Warden")
define sd_guard = Character("Guard")
define sd_receptionist = Character("Receptionist")
define baites = Character("Charles Baites")
define alfred = Character("Alfred")
define guard = Character("Guard")
define s_guard = Character("Security Guard")
define protestor = Character("Protestor")

# The game starts here.

#Chapter 1 (Jingtian Li)
label start:
    "Just where am I?"
    "You realize that this is a dream, and you don't want it to end."
    scene bg Dream with dissolve
    show little_girl at right
    "Because here you see your little daughter, Anna. She is looking at you too, smiling."
    "She looks beautiful with her long, curly hair."
    $ playerName = renpy.input("You hear her calling your name: ")
    "Her voice is so sweet."
    "You see your wife in the background, doing household chores. You want to speak with her, but you just can't bring your mouth to open."
    "Suddenly you hear your own voice shouting, 'I have to do this!'" with vpunch
    "'I do all I can to support this family!’ How tragic, your wife and daughter are frightened by your voice and you can't even stop it."
    scene bg Prison_Cell_A with dissolve
    hide little_girl
    "You hear another voice, a voice from reality, thrusting into your dream, ‘Hey bastard, wake up.'"
    show police at left
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
    scene bg Prison_Office with dissolve
    show mysterious_man at left
    "The officer takes you through the cell block and into a very fancy dining room."
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
    scene bg Out_Car with dissolve
    show mysterious_man
    "The mysterious man brings you out of the prison. You see a white Ford car parked in front of the prison gate."
    mm "That car is for you. There's also a fake ID, change of clothes, and a credit card in the back seat."
    mm "You're still convicted prisoner until this mission is complete, so try to stay low. And remember, we'll be keeping an eye on you as well as your beloved daughter."
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
    scene bg Freeway with dissolve
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
    scene bg Prison_Gate_A with dissolve
    "After parking the car in front of the San Francisco prison, all you can see in front of you is the gray, towering wall and a massive closed gate."
    "You tuck the gun behind your back and walk towards the gate."
    menu:
        "Shoot at the sky":
            "Within seconds after you shoot, policemen swarm outside and surround you. You want to show them the paper from state governor. However, all they can see is the gun in your hands, and so they decide to shoot you."
            jump gameEnd
        "Knock on the door":
            "A voice calls above you. You see a thin, short jail guard looking at you at the top of the gate."
    show guard1 at left
    you "Good evening sir, I am sent by the state governor. He issued an executive order to move a prisoner here to another place. I've got the papers with me."
    "The prison guard eyes you suspiciously for only a second before lowering his guard."
    "Years of working in the shady business has refined your improvisation skills indeed."
    guard "I see. Our chief officer will need to see the paperwork. I'll take you over to him."
    scene bg Prison_Office with dissolve
    show guard1 at left
    show guard2 at right
    "The guard opens the gate and brings you to the chief's office. You see the chief sitting on his chair enjoying a cup of black coffee."
    guard "This guy says he's here to conduct a prisoner transfer."
    officer "Sigh, this better be important. I'll take it from here."
    hide guard1
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
    scene bg Prison_Hall with dissolve
    "He escorts you to the northern cell block, presumably where Mr. Mount is. As you're passing by, you can hear the hysterical noises from the inmates."
    "You spot Mount in a cell slightly bigger than most. His gaze locks onto yours and you can see a mixture of both relief and happiness in his eyes."
    hide gaurd2
    scene bg Prison_Cell_A with dissolve
    show mount_prison at left
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
    show big_mark at right
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
    scene bg Openspace with dissolve
    show mount_prison at left
    show big_mark at right
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
    hide big_mark
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
    scene bg Openspace with dissolve
    show mount_prison at left
    show big_mark at right
    $ GoodTalks -= 1
    "You put a bloody hole between Mark's eyes. In that moment, everyone was shocked, including Mount. The next thing you remember was everybody clawing towards you to tear you apart. But Mount was there to protect you. He was on your side."
    hide big_mark
    "With some scratches and bruises, the two of you managed to get out of prison before anyone can catch you."
    "You and Mount jumped into the car and booked it."
    jump transfer2

label transfer2:
    scene freeway with dissolve
    show mount at right
    "After getting away from San Francisco, you finally get the chance to talk to Mount."
    you "Hey, Mount. I've been meaning to ask, but what happened to everybody back then? Why did you and everybody leave me?"
    "Mount doesn't say anything for a moment. You glance over and notice that he's clutching his hands tightly."
    mount "...it was my fault, boss. I was the one who killed those policemen. You know, that was actually my first time getting my hands dirty."
    mount "I'm a experienced sniper and fighter, yet the worse thing I did was shoot to threaten. That was all. This time, it was different. Everybody didn't know what to do, so we all ran..."
    #Entering Mount's flashback
    scene bg Openspace with dissolve
    show buenos at right
    show mount at left
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
    hide buenos
    #End of flashback
    scene bg Freeway with dissolve
    "You think about Mount's reason (as well as everybody else) for leaving you."
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

    scene bg Prison_Gate_B with dissolve

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



#Chapter 4(Michael Kahn)
label SanDiego:
    scene bg Prison_Gate_B
    "After some time driving, the San Diego prison finally comes into view. This is final stop for getting your crew together"
    "You still wonder how Tsing ended up here, but at this point that's not really important. That can come later"
    "You drive up to the guard house that blocks the entrance to the prison. Two guards stationed there step out to greet you"
    show guard1 at right
    sd_guard "Hello sir, what might be your business here today?"
    you "I am here on business, I have some paperwork I need to show the warden"
    "You take out the paperwork you were given earlier and show it to the guard, the guard looks it over quickly and then goes back the guard booth"
    "You can see the guard making a phone call and have a brief conversation before coming back to you"
    sd_guard "Seems like everything is order, head on in"
    "You take the paperwork back, and drive into the prison as the gate opens. Seems like this should be fairly straightforward"
    scene bg Out_Car
    "You pull out your gun and put in the glove box. There was no way you were getting that inside."
    you "You both stay here in the car, I will go in and get Tsing"
    show mount at right
    mount "No, we are going in with you, if things do go wrong, which they likely will, it would be better if we stuck together"
    show buenos at left
    buenos "I agree, we would just be sitting ducks out here otherwise, we would be much more help inside"
    you "Very well, but I will do allt he talking if it comes to it"
    "Both of your crew members nod in agreement as you all exit the car and head inside"
    scene bg Prison_Office
    "You approach the receptionist in the lobby and show her the paperwork to get Tsing out"
    show receptionist at right
    sd_receptionist "We have be waiting for you, please head down that hallway to the right, there is a room at the end you will wait in as we process everything"
    "You nod in agreement and to where the receptionist mentioned"
    hide receptionist
    "As you walk down the hallway, you start to feel uneasy, something feels off with all of this, but there is not much you can do about it at this point. You reach room that was mentioned and head inside"
    "Well, seems that uneasy feeling was correct, as you enter the room you are met by a quite a few guards and in front of them a women in business attire. She clearly is in charge right now."
    show warden at center
    sd_warden "Welcome to my prison, I am the warden here, may I know who I am speaking to?"
    menu:
        "Tell her your name":
            sd_warden "Hmm, I see."
            "The warden seems lost in thought for a moment"
        "Remain silent":
            sd_warden "Choosing to hold your tongue I see, I can appreciate that"
    sd_warden "No matter, now then, tell me why you have an executive order from my father to get this Mr. Tsing out of prison"
    you "I am simply here under orders to get Tsing out, I was not given any other information than that"
    "The warden eyes you suspicously, clearly not buying the blantant lie you just gave"
    sd_warden "I'd advise against lying to me. Especially when your so bad at it."
    sd_warden "This all seems quite odd, and until I get further confirmation that this paperwork is legit, I have decided to transfer this Mr. Tsing to solitary. To ensure he stays out of reach"
    "The warden gives you an eerie smile, she clearly does not want to let Tsing go for some reason, and has to decided to make a lot of trouble for you"
    sd_warden "Now then, what to do with you in the time being ... "
    "The warden stares at you as she thinks for moment, then she grins as she seems to have to come to an idea"
    sd_warden "If you would be so kinda as to surrender, I believe you have information I want and I would rather we converse elsewhere"
    "Things have quickly turned for the worse, and the warden clearly knows something about your mission, just to what extent you do not know"
    "However, you do not have much choice in the matter right now, you are unarmed and surrounded by armed guards. Even if you did make a break for it, chances are one or more of you was not going ot make it"
    "You throw up your arms, your companions following suit, as the guard quickly move in to subdue you. Zip-tying your hands behind your back. Your then quickly ushered down another hallway"
    show bg Prison_Hall
    "As you are forced down the hallway, you keep thinking about some way of getting out of this situation. As you get lost in your thoughts, the warden speaks up from in front of you"
    show warden at center
    sd_warden "You know, when I saw that order come in for a prison release, I was quite suprised, I wasn't expecting to have to be dealing with my father's antics today"
    sd_warden "He just does not know when to stop causing problems. But do not worry, I will make sure that he doesn't get what he wants this time."
    "As she says this, her tones quickly changes from one of authority to one of a person who has been deeply hurt"
    sd_warden "You will tell me what you know, one way or another, and if you don't, then well, do not expect to ever get out of here again"
    "The warden snickers to herself as she says this. She clearly has some issue with her father, the one who is behind this whole mission your on anyways. But there has to be some way out of this"
    "After some time of walking in silence, you finally spot a possible oppurtunity to break free. Coming from the other direction is a janitor with his equipment cart. You could pontentially use this and cause a distraction and break off down a nearby hallway"
    menu:
        "Stay with the guards":
            jump sd_route_stay
        "Make a break for it":
            jump sd_route_distract

    label sd_route_stay:
        "It is clearly to risky to attempt such a feat. You are better of waiting this out and hoping a better oppurtunity comes, hopefully soon"
        "After being pushed through the prison for a while, you come to a split in the hallways. You are pushed down one hallway, while your crew is pushed down the other."
        "Things are getting worse and worse, especially now with you being seperated from you crew. You have no clue how you are going to get out of this now"
        scene bg Prison_Cell_A
        "Before long, you come up to a secure door which is opened as you reach it, inside is a bare room with a concrete floor. You are tossed inside and left alone"
        "The guards and the warden leave you be in the room for some time, you do not know exactly how long"
        "Finally you hear the door open, and the warden walks in, with a face that shows shes clearly pleased with how you have been treated so far"
        show warden at center
        sd_warden "So I hope you have been enjoying your stay in my prison so far"
        "She snickers as she says this to you, she clearly loves to torment people"
        sd_warden "Now then, onto business. I want to know what you are doing for my father and what this Mr. Tsing has to do with it"
        you "Your father?"
        sd_warden "Of course, the governor. The one who signed the orders to get Tsing out, and the one who is responsible for you"
        you "And what does that has to do with me, I have the proper paperwork and everything"
        sd_warden "True, the paperwork is legit, but it is clear my father is up to something once again, and I have no intention of allowing him to have his way"
        sd_warden "Stopping you here will hurt him. I don't know exactly what he has planned with you and this Mr. Tsing. But I will not let him"
        sd_warden "As for what I intend to do with you, that depends on how helpful you intend to be. I can make your life quite miserable. You would be wise to tell me what I want to know"
        you "What is it exactly that you want to know?"
        sd_warden "We can start with what your actual goal is coming here to release Tsing for. Its clear he has some use to my father and I want to know what"
        "The warden is clearly going to do whatever it takes to get the information out of you. You could simply tell her the truth, but considering the hostility she shows towards her father that might not be a good idea"
        "Lying is also a possible choice, she does not know any of the specifics of what is going on so that leaves a good place to start."
        label sd_route_questions:
            menu:
                "Ask her why she is doing this" if sd_asked == False:
                    $ sd_asked = True
                    you "So why go to all this trouble to hinder me, all the paperwork I have is legit"
                    sd_warden "It has nothing to do with it being legit, it has to do with you working for my father. That is where the issue lies"
                    you "Whatever problem you have with your father is not my problem, I am simply here with orders to get Tsing out"
                    sd_warden "Yes, and I am sure the reason you are getting him out is to help my father"
                    you "Why are you so against your father, that you would go this far to cause more trouble for everyone"
                    sd_warden "Of course you wouldn't know, that man has caused so many problems for our family. I refuse to help him further make problems"
                    sd_warden "He has torn us apart and made us his enemies, his own family. He chose is addiction and corruption over us. I will make him pay for that"
                    sd_warden "Hindering you is simply one of those ways to hinder that man. I would say it's nothing personal, but it is very personal"
                    sd_warden "So tell me, what did he ask you to do?"
                    jump sd_route_questions
                "Tell the truth":
                    you "I was tasked with heading to Mexico to retrieve some drug from a plantation down there. I was not given much information more than that"
                    you "I will have you know however, that I am not doing this exactly willingly"
                    sd_warden "Your reasons for taking this task matter little to me, but now it makes sense. He is looking to satisfy is addiction to that damn drug once more."
                    sd_warden "That drug is the reason for all this, the root all these problems, and yet he continues to make things worse. He just does not know when to stop."
                    sd_warden "He has already taken so much from me and the rest of the family. I will not let you help him. You and your friends are not going to going anywhere anytime soon"
                    you "Even if you stop me, I am sure he will just find someone else to take the job"
                    sd_warden "Sadly, I cannot disagree with that, but this will still set him back, and that is at least something. Even the little hits can still hurt him"
                    "It's pretty clear the warden and her father are not on great terms, and she fully intends to make sure you do not leave this place. Maybe there is some way to convince her to let you go"
                    sd_warden "Anyways, you will spending a while here, I suggest you get conformatable"
                    you "This does not have to go down this way. I hate that man just as much as you right now. But he has me where it hurts right now."
                    you "However, maybe we can work together, and both get something we want"
                    "This seems to have peaked the wardens interest as she motions for the guards to stop."
                    sd_warden "Speak, and you better not be lying to me. My father is not the only one with the power to make certain things happen around here"
                    "You nod slowly at the warden, taking her threat to heart. After your dealings with the mysterious man, you do not doubt her claim."
                    you "The plantation he is sending me to, I could destroy it. Shut down the operations there. I am sure with my crews help we could achieve that"
                    you "Removing that plantation will definitely hurt your father, more so than preventing my crew and I from continuing with the mission"
                    you "And it lets me get a chance to get back at him as well, its a win win for both of us"
                    sd_warden "Hmm, that is quite the tempting offer, but once you leave here I still have no way of making sure you stay to your word"
                    you "True, and I have nothing to give as insurance, but this is still the type of oppurtunity you have been waiting for. I know that much"
                    you "This is a gamble for both of us, but I believe the odds are in our favor. You would be wise to take advantage of this"
                    you "In the end, if I fail, noone will know of what we transpired to do here. Your name won't ever be mentioned"
                    sd_warden "That is true, this is the first chance I have had in a while to truly strike back at that man"
                    sd_warden "I believe we may just have found some common ground. However, I will remind you once more, do not double cross me. You will regret it"
                    "The warden is not understating that threat, she clearly means to take you down if you betray her. But she at least seems to have come to agree with your plan, you actually just might get out of here with Tsing after all."
                    you "So it sounds like we have a deal, if you just get me Tsing, my crew and I can get out of here and stop causing any more problems for you"
                    jump sd_route_convinced
                "Tell a lie":
                    "The warden still does not know what your mission actually is at this point. Maybe there is still a chance to convince her without revealing anything about the actual task"
                    "The question then is, what can you convince her with that could get you and your crew out of here"
                    "After thinking to yourself in the few moments you had, you realize that she probably doesn't know about the mysterious man, this could work to your advantage"
                    you "A mysterious man came to me in the prison I was being held at. He gave me a deal I could not refuse"
                    you "I do not have many details, as the information the man gave me was minimal at best, but one thing I know is that what I am being asked to do is not to help your father"
                    you "If anything, what I was asked to do would help take down your father"
                    "The warden looks at you skeptically, she does not look like she is really buying the lie"
                    sd_warden "So you expect me to believe that you came here with an executive order signed by my father, the very man your supposedly tasked with helping take down"
                    you "Once again, the details I know are minimal, I was simply told to come get Tsing out of prison as he is a part of the mysterious mans plan"
                    you "How the mysterious man got the paperwork is beyond what I know and allowed to know"
                    you "I am just lowly henchman, nothing more"
                    "The warden still has the same skeptical look as before, but you can tell she is starting to relax a bit, the lie just might be working"
                    sd_warden "I still do not find any of this to be believable, for one I find it hard to believe you actually know as little as you do"
                    sd_warden "You are clearly a decently smart man, you cannot realistically expect me to believe that this is all you have been told"
                    "You are so close to getting her to believe you, you know it. But you still need something to push her over the edge, anything at this point"
                    you "I may have overheard a thing or two, but I do not know if I should share anything. You never know who is listening"
                    "The warden gives you a smile, looks like she may finally have bought it"
                    sd_warden "Oh really, so you do actually know something, I knew it. Don't worry any said in these walls stays in these walls, I am sure of that"
                    "You give her a skeptical look of your own, but bow your head a bit and speak quietely, hoping to truly sell the lie"
                    you "I overheard the man who gave me my orders talking to another person, I do not know who, but they mentioned something about a plantation in Mexico and some drug it produces"
                    you "I think they were talking about ways to sabotage it, I am not entirely sure though as I had to be careful to not be found out"
                    sd_warden "Hmm, I have heard about one of my fathers suppliers being in Mexico, that at least checks out"
                    sd_warden "And if this man is truly trying to sabotage this plantation to get at my father, I would be stupid not help. Anything to hurt my father benefits me."
                    "The warden goes silent for a while, clearly lost in her own thoughts. After some time she finally looks up"
                    sd_warden "This is an oppurtunity I will not see often, so I am going to choose to believe you. But, let me warn you now, if you are lying to me and are planning to help my father, I will know1"
                    sd_warden "If you think the people you work for are powerful, then you should understand what I am capable of. I will not tolerate being betrayed, so you better be telling the truth"
                    "you give the warden a quick nod, making sure to show you acknowledged her threat, which you doubt she is understating at all"
                    you "Of course, I am not so foolish as to lie and end up an enemy of someone like you"
                    sd_warden "Good, seems we have an understanding then"
                    jump sd_route_convinced
                "Stay Silent":
                    if sd_silent == 0:
                        $ sd_silent += 1
                        sd_warden "Choosing to hold your tongue I see. You do understand your powerless here. Your better off telling me what I want to know now. It will make both of our lives easier"
                        sd_warden "Once again, I ask you what your purpose is here and why are you getting Mr. Tsing out of prison?"
                        jump sd_route_questions
                    elif sd_silent == 1:
                        $ sd_silent += 1
                        sd_warden "Still trying to play hard I see. You know your not the only one your screwing over by staying silent. Your companions probably won't be happy to know that their predictament is entirely your fault"
                        sd_warden "If you care at all about them, you should start talking. I can cause lots of trouble for you if you don't start talking"
                        jump sd_route_questions
                    elif sd_silent == 2:
                        $ sd_silent += 1
                        sd_warden "This is my last warning. Continue to hold your tongue and you will truly never see the light of day again. I will make sure you and your friends rot in here"
                        sd_warden "All you have to do is tell what you are here for, it is that simple. Your an idiot if you cannot understand that."
                        sd_warden "Last chance, speak, or you will live in hell for the rest of your life"
                        jump sd_route_questions
                    else:
                        sd_warden "Oh well, I tried to work with you. Maybe we could of even worked something out, but no, you just had to hold your tongue. Whether I get that information or not, I still win dthis fight"
                        sd_warden "I hope you enjoy it here, you are going to be here a while. At least you get to stay with your friends, isn't that nice. Although I would not be happy if I were them"
                        sd_warden "You are the reason they are getting locked up after all"
                        "With one last laugh in your direction, the warden walked out of the room, slamming the door behind her. You have failed your mission and get stuck in prison once again."
                        "Game Over"
                        return

    label sd_route_distract:
        scene bg Prison_Hall
        "There is no way your going back into a cell, and there is no way you are going to fail this mission, not with what is at stake"
        "As you get close to the janitor, he moves to the side to allow the guards past. As he does this though, you dash for it and push the cart directly at the guards in front of you. Blocking them off for a moment"
        "Buenos and Mount quickly realized what you are doing and bashed the guards next to them over, give the three of you a chance. You make a brek for it down the side hallway and into another section of the prison"
        "You can hear the warden shouting at the guards to chase after you, and soon after you hear the prison alarm go off. Well this has gotten complicated, you think to yourself"
        "The first step though now was to find somewhere to recoup with your companions and make a plan. Also to get the zipties off your hands."
        "You make a quick turn down another hallway and run past a maintainence closet to your side. Bingo, just the place you needed. You quickly motion to your crew and move inside before anyone can see you enter."
        "Once inside, it was pretty easy to find something to cut off the zip ties. Now for the hard part, getting out of here, and you still needed to find Tsing somehow"
        "You did not have many options. Trying to just get to Tsing directly was impossible now with the prison on high alert. AS you thought to yourself, your companions spoke up"
        show mount at right
        show buenos at left
        mount "Well this is a mess, but we need to get moving. Our best bet is to find some disguises and sneak are way through"
        buenos "That might work, but she knows where we are going to go, we need a distraction. We could split up and try to get her to spread the security out. Causing it overall to be weaker"
        "Both plans could work, but which one is better. There is not much time to think, you must decide quickly"
        menu:
            "Find disguises and sneak through":
                jump sd_route_disguise
            "Split up and have your companions cause distractions":
                jump sd_route_split

    label sd_route_disguise:
        $ sd_disguise = True
        "Deciding that being a bit stealthy was your best bet at getting to Tsing, you set out to find some disguises"
        mount "We should try to see if we can find some guard uniforms lying around, or take some forcefully. No one would really question us then"
        buenos "That is easier said than done, where are we going to find those"
        you "Mount is probably right, and we probably are better trying to get the drop on some guards and taking their uniforms"
        buenos "It is risky, but I guess we do not have much in the way of choices right now. Let's get this done with quickly"
        mount "Agreed, we can lure a few guards by having one of us distract them. And then the other two can attack from behind"
        "You all nod in agreement"
        you "Sounds good, buenos do you mind running distraction?"
        buenos "Of course you suggest me, fine I'll do it."
        "Buenos sighs as he moves to the door to peak outside"
        buenos "The coast is clear right now, I will try to get some guards attention and lead them back this way. When I run by again you get them from behind"
        you "Sounds good, good luck"
        "With one last peak outside, Buenos quickly ran out into the hallway and down towards one end"
        "Mount of you wait in silence for some time, with the only sound being the prison alarm still ringing. Quite a few minutes later you here the stamping of running feet coming your direction"
        you "Sounds like it might be buenos coming back"
        "Mount gives you a nod and peaks out into the hallway. Sure enough buenos is running full speed down the hallway, with three guards in tow. Perfect"
        "As the guards run past the room your in, you quickly break out of the room and with Mount beside you, you charge down the hallway following the guards"
        you "Hey guards, over here!"
        "You shout at the guards as you get close to them, cause them to turn just in time to get tackled as you crash into them"
        "Mount easily knocks the guard closest to him out and quickly moved onto the third guard. By the time you disable the guard you attacked, Mount had already taken care of the other guard"
        "With the three guards taken care of, you each grab one and quickly drag them back into the mainainence room. Quickly changing into their uniforms as quickly as possible. Time is of the essence."
        "As you finish changing you notice the guards were all armed with pistols."
        menu:
            "Take the guns":
                $ sd_gun = True
            "Leave the guns":
                $ sd_gun = False
        "With your crew now disguised, its time to make your way to solitary where they are holding Tsing. You need to find some way of releasing him and getting him out"
        "Setting out from the mainainence room, you make your way back towards where you orginally arrived, you needed to find a map or something so you can make your way to solitary"
        "It seems the disguises are working at least, as no one has stopped you so far, so that at least takes some pressure off. But time is still limited and the longer you take the worse it is going to get"
        "Eventually, after walking around taking various paths you eventually find a sign stating the direction toward solitary, took long enough"
        "Heading down the hallway, you enter solitary, hoping that the security isn't too much here, and hold out hope that you can still get Tsing out"
        "Moving forward you reach to the entrance to the solitary block, no turning back now"
        "Entering solitary, it's fairly obvious they were definitely expecting you, as the heightened security is quite noticable. You realize quickly that getting Tsing out was going to be complicated"
        "There were just too many guards in the way"
        mount "We could potentially lead some of these guards away. Since they do not recognize us, Buenos and I can try to set some false tip offs to some of these guards and try to lead them out"
        buenos "Should be easy enough, since they all look they would rather be elsewhere right now"
        you "Get to it then, we are running out of time"
        "Mount and Buenos walk off towards different sections and start to converse with some of the guards. While they start their distractions, you begin to make your way to the main section, where the prisoners are actually located"
        "As you reach your destination, you notice your companions walking off with some of the guards, seems whatever they said worked, and their disguises seemed to be holding up"
        "You continue onward, time to do your part"
        jump sd_route_confront
    label sd_route_split:
        you "Security is probably going to be tight around solitary since that is where she is likely expecting us to go. We need to get their attention away from there"
        you "You two need to run distraction and I will head over to solitary and get Tsing. Do whatever you can to draw attention and then work your way back here"
        you "Once I get Tsing, I will get back here and we will get out of here and hopefully be on the road again"
        buenos "Sounds good, I will see if I can cause some trouble with the other inmates, maybe cause a riot or something"
        mount "I will try to set some falseleads to lead them around, maybe knock out a few guards here and there"
        you "Very well, good luck, let's get this done"
        "Your crew give you a nod of agreement, and the three of you head out of the room and set off in different directions. You take off towards where you hope solitary is and only can hope that the distractions are enough"
        hide buenos
        hide mount
        "As you are making your way down a hallway you come accross a group of three guards on high alert. As far as you can tell this is the only path towards solitary."
        "You could try and find another way around, but that could lead to more possibilities of running into guards. Or you can wait and hope that your companions distractions may get these guards out of the way."
        "As you contemplate which route you want to take, bya  stroke of luck, it seems your companions have come through. Over the loudspeaker you can hear requests for extra assistance being needed on the other side of the prison"
        "The guards in your way stop their conversation as they hear the announcement. Two of them sigh and bid the other farewell as they rush off, presumably to head towards the distraction"
        "This just leaves the one guard blocking your path, taking down one guard instead of three is much easier. You creep as close as you can to the guard without being spotted, and prepare to charge"
        "Best bet here is to be quick and take down the guard directly, so you set off running and before the guard as any time to react, you tackle him down, knocking him unconscious"
        you "Well that went well"
        "As you get up from the guard, you notice the firearm he has holstered by his side"
        menu:
            "Take the gun":
                $ sd_gun = True
            "Leave the gun":
                $ sd_gun = False
        "Moving forward you reach to the entrance to the solitary block, no turning back now"
        "Entering solitary, security was a lot less than expected, seems the distractions caused by Mount and Buenos worked well"
        "Making your way past the few guards that were presence, you approach the main section of solitary, where the prisoners are located"
        you "Well, just got to hope there are no more suprises after this"
        "You sigh to yourself, and enter the next area"
        jump sd_route_confront

    label sd_route_confront:
        scene bg Prison_Cell_A
        "Upon entering the solitary area, you are almost not suprised that waiting before you stood the Warden"
        show warden at center
        sd_warden "How nice of you to join me, although it seems you have lost your friends in process"
        "She smiles at you, two guards move forward, one on each side of here"
        sd_warden "You really made it easy for us, coming right here. Moving Tsing made good bait. And I am sure we will find your friends soon enough"
        "You stare at the warden, contemplating what your next plan of action might be"
        if sd_gun == True:
            "You still have the firearm you picked up earlier. Could come in use. They probably do not expect you to be armed right now, and can probably get the drop on them"
            "But is it really worth it to kill them, that could easily backfire in many ways"
        else:
            "You are unarmed and outnumbered, probably best to go along with whatever the warden has planned right now. She clearly wants to talk as she did not have you taken down right away"
        "The warden looks at you, seems shes waiting for you to say something, or at least do something. One wrong step here and it could be your last"
        menu:
            "Ask her what she wants":
                you "So why go to all this trouble to hinder me, all the paperwork I have is legit"
                sd_warden "It has nothing to do with it being legit, it has to do with you working for my father. That is where the issue lies"
                you "Whatever problem you have with your father is not my problem, I am simply here with orders to get Tsing out"
                sd_warden "Yes, and I am sure the reason you are getting him out is to help my father"
                you "Why are you so against your father, that you would go this far to cause more trouble for everyone"
                sd_warden "Of course you wouldn't know, that man has caused so many problems for our family. I refuse to help him further make problems"
                sd_warden "So tell me, what did he ask you to do?"
                menu:
                    "Tell the truth":
                        you "I was tasked with heading to Mexico to retrieve some drug from a plantation down there. I was not given much information more than that"
                        you "I will have you know however, that I am not doing this exactly willingly"
                        sd_warden "Your reasons for taking this task matter little to me, but now it makes sense. He is looking to satisfy is addiction to that damn drug once more."
                        sd_warden "That drug is the reason for all this, the root all these problems, and yet he continues to make things worse. He just does not know when to stop."
                        sd_warden "He has already taken so much from me and the rest of the family. I will not let you help him. You and your friends are not going to going anywhere anytime soon"
                        you "Even if you stop me, I am sure he will just find someone else to take the job"
                        sd_warden "Sadly, I cannot disagree with that, but this will still set him back, and that is at least something. Even the little hits can still hurt him"
                        "It's pretty clear the warden and her father are not on great terms, and she fully intends to make sure you do not leave this place. Maybe there is some way to convince her to let you go"
                        sd_warden "Now then, now that I know specifically what is going on, it would be nice if you simply surrendered peacefully. Gaurds take him down."
                        "The warden motions for the guards to move in and take you down. You need to do something or else everything you have done so far has been for nothing."
                        menu:
                            "Try to reason with the warden":
                                you "This does not have to go down this way. I hate that man just as much as you right now. But he has me where it hurts right now."
                                you "However, maybe we can work together, and both get something we want"
                                "This seems to have peaked the wardens interest as she motions for the guards to stop."
                                sd_warden "Speak, and you better not be lying to me. My father is not the only one with the power to make certain things happen around here"
                                "You nod slowly at the warden, taking her threat to heart. After your dealings with the mysterious man, you do not doubt her claim."
                                you "The plantation he is sending me to, I could destroy it. Shut down the operations there. I am sure with my crews help we could achieve that"
                                you "Removing that plantation will definitely hurt your father, more so than preventing my crew and I from continuing with the mission"
                                you "And it lets me get a chance to get back at him as well, its a win win for both of us"
                                sd_warden "Hmm, that is quite the tempting offer, but once you leave here I still have no way of making sure you stay to your word"
                                you "True, and I have nothing to give as insurance, but this is still the type of oppurtunity you have been waiting for. I know that much"
                                you "This is a gamble for both of us, but I believe the odds are in our favor. You would be wise to take advantage of this"
                                you "In the end, if I fail, noone will know of what we transpired to do here. Your name won't ever be mentioned"
                                sd_warden "That is true, this is the first chance I have had in a while to truly strike back at that man"
                                sd_warden "I believe we may just have found some common ground. However, I will remind you once more, do not double cross me. You will regret it"
                                "The warden is not understating that threat, she clearly means to take you down if you betray her. But she at least seems to have come to agree with your plan, you actually just might get out of here with Tsing after all."
                                you "So it sounds like we have a deal, if you just get me Tsing, my crew and I can get out of here and stop causing any more problems for you"
                                jump sd_route_convinced
                            "Surrender":
                                "There is no talking your way out of this now. Your not armed either, so the chances of fighting your way out are basically nothing. All you can do is go along with her now"
                                "You throw your hands in the air and surrender to the approaching guards"                                    "Nothing left to do now but wait and hope something goes right in the future, but that is unlikely to happen. Seems like this whole insane task was truly impossible."
                                "Game Over, you surrendered to the warden and remained in capitivty."
                                return
                            "Draw your weapon" if sd_gun == True:
                                jump sd_route_shoot
                    "Tell a lie":
                        "The warden still does not know what your mission actually is at this point. Maybe there is still a chance to convince her without revealing anything about the actual task"
                        "The question then is, what can you convince her with that could get you and your crew out of here"
                        "After thinking to yourself int he few moments you had, you realize that she probably doesn't know about the mysterious man, this could work to your advantage"
                        you "A mysterious man came to me in the prison I was being held at. He gave me a deal I could not refuse"
                        you "I do not have many details, as the information the man gave me was minimal at best, but one thing I know is that what I am being asked to do is not to help your father"
                        you "If anything, what I was asked to do would help take down your father"
                        "The warden looks at you skeptically, she does not look like she is really buying the lie"
                        sd_warden "So you expect me to believe that you came here with an executive order signed by my father, the very man your supposedly tasked with helping take down"
                        you "Once again, the details I know are minimal, I was simply told to come get Tsing out of prison as he is a part of the mysterious mans plan"
                        you "How the mysterious man got the paperwork is beyond what I know and allowed to know"
                        you "I am just lowly henchman, nothing more"
                        "The warden still has the same skeptical look as before, but you can tell she is starting to relax a bit, the lie just might be working"
                        sd_warden "I still do not find any of this to be believable, for one I find it hard to believe you actually know as little as you do"
                        sd_warden "You are clearly a decently smart man, you cannot realistically expect me to believe that this is all you have been told"
                        "You are so close to getting her to believe you, you know it. But you still need something to push her over the edge, anything at this point"
                        you "I may have overheard a thing or two, but I do not know if I should share anything. You never know who is listening"
                        "The warden gives you a smile, looks like she may finally have bought it"
                        sd_warden "Oh really, so you do actually know something, I knew it. Don't worry any said in these walls stays in these walls, I am sure of that"
                        "You give her a skeptical look of your own, but bow your head a bit and speak quietely, hoping to truly sell the lie"
                        you "I overheard the man who gave me my orders talking to another person, I do not know who, but they mentioned something about a plantation in Mexico and some drug it produces"
                        you "I think they were talking about ways to sabotage it, I am not entirely sure though as I had to be careful to not be found out"
                        sd_warden "Hmm, I have heard about one of my fathers suppliers being in Mexico, that at least checks out"
                        sd_warden "And if this man is truly trying to sabotage this plantation to get at my father, I would be stupid not help. Anything to hurt my father benefits me."
                        "The warden goes silent for a while, clearly lost in her own thoughts. After some time she finally looks up"
                        sd_warden "This is an oppurtunity I will not see often, so I am going to choose to believe you. But, let me warn you now, if you are lying to me and are planning to help my father, I will know1"
                        sd_warden "If you think the people you work for are powerful, then you should understand what I am capable of. I will not tolerate being betrayed, so you better be telling the truth"
                        "you give the warden a quick nod, making sure to show you acknowledged her threat, which you doubt she is understating at all"
                        you "Of course, I am not so foolish as to lie and end up an enemy of someone like you"
                        sd_warden "Good, seems we have an understanding then"
                        jump sd_route_convinced
                    "Draw your weapon" if sd_gun == True:
                        jump sd_route_shoot
            "Draw your weapon" if sd_gun == True:
                jump sd_route_shoot

    label sd_route_convinced:
        $ GoodTalks += 1
        sd_warden "Gaurds escort this man out of my prison, and get his friends out as well. I am tired of their presence here. I will have Mr. Tsing delivered to you outside shortly."
        sd_warden "Do not make me regret this"
        "The guards quickly approach you and start pushing out towards the exit. Seems like something is finally going right in this damn place."
        "You are escorted quickly back out the way you came in and before you know it, you are standing out front of the prison, Mount and Buenos appearing beside you shortly after"
        scene bg Out_Car
        show mount at right
        show buenos at left
        mount "So, is everything good? I was not expecting to be escorted out of the prison of all things"
        buenos "Well Tsing is not here, so did you simply work a way for us out, or are we still getting Tsing?"
        you "Tsing should be out shortly, if the warden is true to her word. I had to come to a deal with her, but I think it will work out for the better for both sides in the end"
        mount "Hmm, that sounds sketchy, but then again all of this is sketchy, I guess its better to possibly have an ally right now"
        buenos "Indeed, especially when dealing with all these people that hold so much power"
        "You nod in agreement, and wait in silence for some time"
        "Finally, you notice a small commotion coming from the direction of the prison, and shortly after Tsing is walking towards you, now a free man"
        "Tsing approaches your group, eyeing you with a look of confusion, he clearly does not know what is happening still and why he is suddenly free"
        you "Welcome Tsing, to the outside once more"
        show tsing at center
        tsing "Yes, it is indeed nice to not be behind bars right now, but the question still stands, why have I been suddenly released, and why are you here waiting for me"
        tsing "Last I heard, you were still locked up tight"
        you "A lot has happened, but right now I have been given the chance to be free if I take care of a task for a very powerful person"
        you "But I cannot do it alone. As you can see I already got Mount and Buenos to join, you are the last piece needed to make this whole thing possible"
        "Tsing gives each of your companions a quick nod of aknowlegdement, getting a nod in return from each of them"
        you "I am sure you have a lot more questions, but we really best be going, I can tell you more details once were on the road"
        tsing "Very well, does not seem like I have much choice in the matter, let us get moving, I would rather not have to see this place again"
        "With that, you and the crew get back into the car and leave the prison. Thankful for that mess being over, but weary about what is to come"
        jump border

    label sd_route_shoot:
        $ GoodTalks -= 1
        $ daughter_die = True
        "You have had enough of this. You quickly reach down and draw your weapon you picked up earlier and aim it towards the warden."
        hide warden
        "Its over in an instant, and before you lie three bodies. Their blood is on your hands now, but thinking aobu that can come later. You still have your mission to complete"
        "Now that threat was out of the way, and no one seems to have noticed the small gun fight, it was time to get Tsing and get out"
        "Hopefully the warden was at least telling the truth about Tsing being in solitary"
        "Walking down the hallway of solitary cells, you peak into the small window into each cell. You get worried as you still havn't found Tsing after checking almost all the cells"
        "However, as you reach the final cell and peak inside, you recognize him immediatelly. Your old companion, Tsing. He did not look happy to be in solitary confinement"
        "Now that you found Tsing, getting him out would be the next step. There has to be some way to open the door. Looking around, you find the entrance to the security office. That has to be where you can open the door from."
        "Entering the security office, a single guard is stationed inside currently. You quickly approach the guard before he has time to react and knock him out with the gun."
        "Scouring the various controls and screens, you find a section for door controls. Quickly finding Tsing's door in the list, you press the button, and can hear confirmation of the door opening."
        "Time to get out of here. You quickly head back out to Tsing's cell and find him looking confused at the now open doorway. When you step into his sight, his look of confusion grows even more"
        show tsing at center
        tsing "So you're the reason all this trouble is happening. I was wondering what I did to get suddenly thrown in solitary for no good reason."
        "Tsing sighs. He was not happy to see you clearly"
        tsing "You better have a damn good reason to be going through all this trouble to get to me. And who did you piss off to make them punish me as well?"
        you "I need your help to get to Mexico. I was given a task that I could not refuse, and I cannot complete it alone. I have already got Mount and Buenos to join me"
        you "Your the last piece before we can finally get this mission done with. I know it is not exactly what you want, but this is also a way out of prison for you as well"
        you "Would have been cleaner if the Warden didn't decide to cause some extra trouble, but what's done is done. Are you with me?"
        tsing "You expect me to just up and join you like that. You are leaving out a lot of details. What is this mission, who are you working for?"
        you "I do not have time to go into much detail right now. It is only matter of time before anyone notices what has happened."
        you "But that clearly is not enough for you. All I can say right now is that the person who I am working for is a very powerful man"
        you "and ... he has my daughter. It is not a mission I can turn down, and it is definitely not a mission I can fail. Are you in?"
        "Tsing sighs once more, he has a defeated look on his face"
        tsing "You really are not giving me much choice here, are you?"
        tsing "Then again, it seems you do not have much choice yourself. Very well, seems like I will be joining you"
        you "Good, I will make up for it later. Right now lets get out of here"
        you "Mount and Buenos helped make some distractions and will be meeting us back towards the entrance, so let us get moving"
        tsing "What's your plan to get me out, you can't just simply walk me out can you?"
        if sd_disguise:
            you "Well, that might actually just work. This disguise has worked for me so far. I can probably pass off as transfering you pretty easily. The guards here are pretty easy to fool"
            tsing "It's risky, but I guess its the quickest and safest way right now"
            "Getting up, Tsing heads over to and places his hands in front of you"
            tsing "Your going to have to cuff me if we want this to work"
            scene Prison_Hall
            "You nod your head, and put Tsing in cuffs, and head out towards the exit"
            "Thankfully, not many guards were around, so you quickly were able to move Tsing out of solitary and into the maze of the prison"
            "Trying to remember the way your came, you quickly moved down each hallway, avoid guards where you could. Those you could not avoid, you made sure to show you were moving Tsing, the prisoner"
            "After many minutes of traveling, you finally arrive at the maintainence room from the beginning, hoping that the rest of your crew is waiting inside"
            "Taking a deep breath you open the door, and luck seems to be on your side right now, as both Mount and Buenos are standing inside. Neither look happy for having to wait so long"
            show mount at right
            show tsing at center
            show buenos at left
            mount "You took your damn time"
            buenos "We were beginning to think you screwed up and we were going to have to leave you ... again"
            you "Ran into some trouble, but it has been dealth with. Let's get out of here quickly"
            tsing "Nice to see you two as well"
            mount "Sorry for the lack of pleasentries, we are not exactly in a great situation right now"
            tsing "fair enough, lets get going, these cuffs are quite uncomfortable to wear"
            "With one last nod of agreement by everyone, you set out towards the entrance"
            "Seems like no one is really focusing on this part the prison right now, so getting to the reception area was quite easy"
            "Quickly walking through the reception area and out to the parking area, the reception looked up confused to see three guards walking out with a prisoner"
            scene Prison_Office
            show receptionist
            sd_receptionist "Hey what are you guys doing, I did not hear anything about a prisoner release?"
            you "Direct orders from the warden. If you want to know more ask her. We were just old to bring this man outside"
            "The receptionist does not look happy when you say that, but grabs the phone and goes to make a phone call. while she is distracted doing that, you walk outside and head towards the car"
            hide receptionist
            "Quickly undoing Tsing's cuffs, you all get into the car and drive off, thankful to be free of that prison, and back on the path to finishing this crazy mission"
            jump border
        else:
            you "Well, we do not have time to come up with anything complicated, but right now most of the guards attention is elsewhere in the prison"
            you "I say we just make a break for it, I think I remember the route back to the regroup area"
            tsing "You are going to get me killed ... but let's go. We really do not have any other option do we"
            "Both of you head quickly out towards the exit of solitary, breaking into a sprint once you get to the maze of hallways that is the prison"
            "Quickly darting down different hallways, trying to avoid guards, you make your way back to the maintainence room"
            "Of the few guards you do come across, most either do not really notice you, or are too slow to react as you run by"
            "Eventually, you reach the maintainence room, hoping your other companions have faired well and are waiting for you inside"
            "Taking a deep breath you open the door, and luck seems to be on your side right now, as both Mount and Buenos are standing inside. Neither look happy for having to wait so long"
            show mount at right
            show buenos at left
            mount "You took your damn time"
            buenos "We were beginning to think you screwed up and we were going to have to leave you ... again"
            you "Ran into some trouble, but it has been dealth with. Let's get out of here quickly"
            tsing "Nice to see you two as well"
            mount "Sorry for the lack of pleasentries, we are not exactly in a great situation right now"
            "With one last nod of agreement by everyone, you set out towards the entrance"
            "Seems like no one is really focusing on this part the prison right now, so getting to the reception area was quite easy"
            "Quickly walking through the reception area and out to the parking area, the reception looked up confused to see the four of you walking out"
            show receptionist
            sd_receptionist "Hey what are you guys doing, what the hell is going on right!"
            hide receptionist
            "You ignore the receptionist and make your way quickly towards your car, hopping in as fast as you can and driving off."
            "Finally free of the prison, and hoping no one is following you, you finally relax a bit. It would only be a matter of time before the next trouble occurs"
            jump border

# Chapter 5 (Ian Maynard)

label border:
    scene bg Freeway with dissolve
    "Riding down the 5 the air starts to get warmer. You see the border just over the horizon"
    you "Finally"
    buenos "What was that?"
    you "I see the border... and..."
    "Squinting your eyes as you get off the highway, you see a large crowd near the entrance to the underground passage"
    you "Oh give me a fuckin break..."
    scene bg Border_Protest with dissolve
    "You and the team park the car and get out to approach the crowd. They appear to be protesting something. Imagine having that kind of time"
    "You seem to spot their leader, a tall nordic looking woman"
    show gretap
    you "Excuse me, what exactly is goin on here?"
    protestor "We are protesting the absolutely ABSURD notion that Techro needs any more office buildings in this part of town. They already have 3 on this street alone!"
    protestor "To make matters worse, they plan on making this bigger and ,as a result, more environmentally hazardous than their previous offices"
    protestor "We refuse to stand by as these corparate douchebags try and ruin our planet!"
    you "Peace, love, and all that. Can me and my friends just squeeze past those barricades?"
    protestor "Not happening. We dont know who you are or WHO you work for!"
    "The woman eyes the men in suits around 20 feet away. One is glued to their smartphone"

    menu:
        "Convince the protestor and the group to leave":
            you "Wait aren't you that lady from the news? Greta Scottson right? Funny seeing you here given whats happening in LA just a couple hours away"
            greta "What the hell are you going on about!? Whats in Los Angeles?"
            you "Oh you didnt hear? Extron is building a new pipeline right through the heart of Los Angeles under a lower class neighborhood!"
            greta "Oh yeah which one then smart guy?"
            "You remember in your days of hustling that you once delivered to a real shady neighborhood in LA once. You are able to name an adress almost immediately"
            "Greta is shocked"
            greta "Well I haven't seen anything on my news app, how do I know you are telling the truth? For all I know that could be your address!"
            "You quickly remember a protest occured in that neighborhood after a cop drove into a cyclist about 6 months ago. You scramble onto your phone"
            you "Here, see?"
            "you hold up a shady news article with a date that only shows the year. Of course the title is just clickbait enough it doesn't mention what the protest is about."
            greta "Wow I had no idea! We should head there right away!"
            "Greta signals to the rest of the protesters who scramble to their cars, your team travels through the passage amongst the chaos..."
            mount "That was way to easy"
            you "Protestor's have good hearts and their head is in the right place, but usually they are pretty easy to trick. I wonder how long it will take them to realise I sent them to a McDonalds parking lot"
            "The whole team laughs"
            $ GoodTalks += 1
            jump Mexico
        "Help the protestor with the suits":
            you "What if we tried to talk to these so called douchebags for you?"
            protestor "Be our guest! Talk to the main douche. Gates. The one on his phone"
            "The protestor giggles at the thought of you trying to help and goes back to chanting with the crowd"
            "You and the team approach the group of suits."
            scene bg Gates_Office with dissolve
            show
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
            you "How are you going to make this building a umm, Beacon was it?"
            gates "A massive satellite dish array? Duh..."
            you "Oh you mean like the ones scientists have set up all over the world? What makes yours so special?"
            "Gates pauses for a moment, as if somehow he has never been asked that question"
            gates "These are TECHRO satellites... You wouldn't understand even if I had the time to explain it to you..."
            "Gates pays no attention to you and begins to make a phone call"
            jump confront_gates2
        "Ask gates to cancel the project":
            you "Listen dude, you dont need a fourth office building in this area. Your company doesnt even have that many employees! Just cancel the project man."
            gates "Oh you are just one of the protestors, move along"
            you "Protestor? No dude I'm just a man on a mission"
            gates "A mission to piss me off? Why would I throw months of planning and millions of dollars in the trash because some random dude came up to me and told me to cancel? And people think I'm the crazy one? HA!"
            you "I mean you said it not me"
            "Gates gives you a piercing glare and goes back to his phone"
            you "What if you postponed it like a day for me. I just need to get past these protestors man"
            "Gates pays no attention to you and begins to make a phone call"
            jump confront_gates3
        "Kill Gates":
            "You reach for your weapon..."
            "But the left bodyguard is faster than you. He draws his weapon and shoots you square in the chest"
            jump gameEnd
        "Return to the Protestors":
            "You begin to realise it is useless to try and talk to this guy and walk back toward the protestors"
            jump backToGreta

label confront_gates2:
    menu:
        "Ask gates to cancel the project":
            you "Listen dude, you dont need a fourth office building in this area. Your company doesnt even have that many employees! Just cancel the project man"
            gates "Oh you are just one of the protestors, move along"
            you "Protestor? No dude I'm just a man on a mission"
            "Gates angrily hangs up his phone"
            gates "A mission to piss me off? Why would I throw months of planning and millions of dollars in the trash because some random dude came up to me and told me to cancel? And people think I'm the crazy one? HA!"
            you "I mean you said it not me"
            "Gates gives you a piercing glare and goes back to his phone"
            you "What if you postponed it like a day for me. I just need to get past these protestors man"
            "Gates pays no attention to you"
            jump confront_gates4
        "Kill Gates":
            "You reach for your weapon..."
            "But the left bodyguard is faster than you. He draws his weapon and shoots you square in the chest"
            jump gameEnd
        "Return to the Protestors":
            "You begin to realise it is useless to try and talk to this guy and walk back toward the protestors"
            jump backToGreta

label confront_gates3:
    menu:
        "Ask gates what the project is about":
            you "What do you guys want a fourth office building for on this street?"
            gates "Oh this is no mere office building you feeble-minded fool"
            "Feeble-minded? Who says that"
            you "Ok then what is it Shakespeare?"
            "Gates mumbles to the person on the phone"
            gates "Ok I don't have a lot of time but to sum it up, this building is going to be a BEACON"
            gates "A shining beacon of progress that will finally allow humanity to join the society amongst the stars"
            mount "This dude talkin' about aliens?"
            "Ok we are dealing with a nut job. Great."
            you "How are you going to make this building a umm, Beacon was it?"
            gates "A massive satellite dish array? Duh..."
            you "Oh you mean like the ones scientists have set up all over the world? What makes yours so special?"
            "Gates pauses for a moment, as if somehow he has never been asked that question"
            gates "These are TECHRO satellites... You wouldn't understand even if I had the time to explain it to you..."
            "Gates buries his head back into his smartphone and pays no attention to you"
            jump confront_gates4
        "Kill Gates":
            "You reach for your weapon..."
            "But the left bodyguard is faster than you. He draws his weapon and shoots you square in the chest"
            jump gameEnd
        "Return to the Protestors":
            "You begin to realise it is useless to try and talk to this guy and walk back toward the protestors"
            jump backToGreta
label confront_gates4:
    menu:
        "Kill Gates":
            "You reach for your weapon..."
            "But the left bodyguard is faster than you. He draws his weapon and shoots you square in the chest"
            jump gameEnd
        "Return to the Protestors":
            "You begin to realise it is useless to try and talk to this guy and walk back toward the protestors"
            jump backToGreta
label backToGreta:
    scene bg Border_Protest with dissolve
    show gretap
    menu:
        "Convince Greta and the group to leave":
            you "Wait aren't you that lady from the news? Greta Scottson right? Funny seeing you here given whats happening in LA just a couple hours away"
            greta "What the hell are you going on about!? Whats in Los Angeles?"
            you "Oh you didnt hear? Extron is building a new pipeline right through the heart of Los Angeles under a lower class neighborhood!"
            greta "Oh yeah which one then smart guy?"
            "You remember in your days of hustling that you once delivered to a real shady neighborhood in LA once. You are able to name an adress almost immediately"
            "Greta is shocked"
            greta "Well I haven't seen anything on my news app, how do I know you are telling the truth? For all I know that could be your address!"
            "You quickly remember a protest occured in that neighborhood after a cop drove into a cyclist about 6 months ago. You scramble onto your phone"
            you "Here, see?"
            "you hold up a shady news article thats date only shows the year. Of course the title is just clickbait enough it doesnt mention what the protest is about."
            greta "Wow I had no idea! We should head there right away!"
            "Greta signals to the rest of the protesters who scramble to their cars, your team travels through the passage amongst the chaos..."
            $ GoodTalks += 1
            jump Mexico
        "Shoot Greta and run for the Passage":
            you "Alright screw it, we are so close I dont have time for this"
            "You pull out your gun and shoot the woman, amongst the chaos your team travels through the passage"
            "Buenos glares at you but says nothing"
            $ GoodTalks -= 1
            jump Mexico

# Chapter 6 (Jingtian Li & haonan lin)
label Mexico:
    scene bg freeway
    show mount
    "After all kinds of hardships, you and your teammates finally arrived at the destination of this trip"
    mount "Everyone, I am so excited and feels that victory is so closed"
    scene bg Plantation_Gate
    "However, things are not easy as they seem. Outside your destination, there is a huge wall"
    "The only entrance has many security guards at the door"
    "You and your teammates can try to enter from the main entrance or try to find another way into the plantation"
    menu:
        "Try to enter from the main entrance":
            "Riding down the street to the entrance of the plantation, the guards stop you"
            pguard"What are you doing here? Strangers are not welcome here"
            you "We are here to see your boss. We are here for your boss to ask for some thing"
            pguard"What's that?"
            "But you don’t want to tell the guard the purpose of this trip"
            you "You don't have to know what it is. It is better for you"
            pguard"If you don't say it, you can fuck off"
            "You are so angry because the guards perverted you impatiently."
            buenos"It's not a big deal. Let me tell you. We are looking for a special king of drug. I hear this special drug is only available here"
            pguard"Drug? Are you kidding me? We don't have that here. Get out of here"
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
    scene bg Plantation_Inside
    show little_boy
    "You start searching for this plantation"
    lb"Who are you? What are you doing here?"
    "Your whereabouts were caught by a little boy. Buenos rush up and try to cover the little boy's mouth"
    lb"You must go to our master. Please."
    "The boy's voice suddenly fell. You see fear in his eyes."
    you"What are you doing here at such a young age?"
    lb"You should not ask... I should not tell. Please just go to our master. I am going back to work."
    mount"Sounds like child labor to me. What do you say boss?"
    menu:
        "Hey, kids. What is your job?":
            lb "No, sir I have no job..."
            you"I see..."
            menu:
                "Tell me the truth or I can use this gun to blow your 12-year-old brain off":
                    lb "what, please do not. I... I will tell you. I grow stuff for Mr. Brit. He is the owner of this place."
                    you "stuff. You mean ingredients for drug?"
                    lb "I do not know sir. Please, just let me go."
                    you "Fine, but tell me where is Mr. Brit."
                    lb "He is patroling around the farm land. You should be able to see him when you get nearer. He usually rides his white horse."
                    "You let the child go and lead your crew to the farm land. A man with round top hat and gold-frame glasses is riding on a white horse, using the leather in his hands to whip workers in the field. Some of those workers look just as young as the little boy you just met."
                    jump mexico_2
                "Fine. you can go.":
                    "You let the kid go, and wander around this place. A moment later, a few guards rush to you, too fast that you are unable to find a place to hide yourself."
                    tsing"that damn kid..."
                    buenos"#SOME SPANISH THAT YOU CANNOT UNDERSTAND#"
                    pguard"#Angry in Spanish#"
                    "They start to beat you."
                    mount"Buenos, what the hell did you tell them"
                    buenos"Nothing, they beat us for no reason."
                    "They stop after a few minutes. Then, this group of man seems unsure about how to deal with you. they talk in Spanish for minutes. Suddenly, Buenos starts to speak again."
                    buenos"#SOME SPANISH THAT YOU CANNOT UNDERSTAND#"
                    pguard"#SOME SPANISH THAT YOU CANNOT UNDERSTAND#"
                    buenos"#SOME SPANISH THAT YOU CANNOT UNDERSTAND#"
                    pguard"#SOME SPANISH THAT YOU CANNOT UNDERSTAND#"
                    buenos"Good news, %(playerName)s, they are going to take us to their boss, Mr. Brit."
                    jump mexico_2
        "Kill this kid":
            hide little_boy
            $ GoodTalks -= 1
            tsing "WTF, what are you doing"
            you "letting this kid running around would cause trouble."
            "You and your crew stealth around for a few more minutes. Finally, you see a man in decent clothes with round top hat and gold-frame glasses, riding on a white horse around a big chunck of farm land."
            tsing "that could be the owner of this place."
            mount "people working in the fields seem to obey him."
            buenos "I can hear some security guys calling him Mr. Brit."

label mexico_2:
    scene bg Plantation_Farmland
    show mr_brit
    show buenos at right
    "Mr. Brit seems to be interested when he sees you. But he does not get down from his horse."
    oop"#Spanish#"
    buenos"He knows we are not locals, and he wants to know why we are here."
    you"#hand him the paper given by the mysterious man# we are here for a mission."
    oop"#Spanish, with brighter voice#"
    buenos"he says 'so you are my friend then. Sorry if my men did not treat you that well'."
    you"Even your guards do not know who we are. He stopped us from coming in. We have to work hard to get here"
    oop"#Spanish#"
    buenos"He apologize. They are just performing their duties."
    oop"#Spanish#"
    buenos"He wants to talk about your mission."
    you"Yes, please give me the drug."
    oop"#Spanish, with angry voice# #put on a pair of white gloves, also throw you a pair of white gloves#"
    buenos"Boss, relax. he thinks you are being rude. he asks you to put on the white gloves."
    "Brit hands you a big jar of red pills. unlike this dirty plantation, the pills and the jar seem extremely clean. You cannot even find a fingerprint on the glass."
    you"How can I know I got the real thing."
    oop"#with awkward English# Come on, I have no reason to play trick with you. you wanna know if its real? Fine, eat it then you will know."
    "You stare at him, thinking."
    menu:
        "I cannot trust a guy who uses child labor":
            "you feel a sudden dizziness. Your family again appear in front of you. You reach your hands to your wife and hold her gently. Then you fall down."
            jump gameEnd
        "I will trust you. But never expect I will trust you on other things ever again.":
            jump mexico_3
        "What is the effect of this drug.":
            oop "Really? You ask the effect of drug? You are a retard, aren't you. If you are not sent by the state governor, I would cut through your fucking throat right now."
            you "I just want to know what I got through this long journey. This mustn't be simply an ordinary drug."
            oop "I do not hear bullshit from pussy. Fuck off from my plantation. You will never be welcomed here from now."
            jump mexico_3

label mexico_3:
    scene bg Plantation_Farmland
    show Mount
    show tsing at right
    show buenos at left
    "The face of Brit is furious. His guards also look irritated."
    mount "we should go"
    buenos "He's right, %(playerName)s"
    "At the moment you are about to turn around, you see the little boy again. he is hiding behind Brit, he stares at you desperately. You cannot help asking this questions."
    you "Are you using child labor?"
    oop "I think I just said you should go."
    "Brit follows your glance and sees that little boy too. He yells at the boy in Spanish. Three of his guards rush to the boy, put him down on ground and start to beat him."
    if GoodTalks > GEthresh:
        mount "#whisper# Boss, we need to do something."
        buenos "#whisper# Asshole"
        tsing "..."
    else:
        "You feel heartache. Even though you have killed so many people, you still feel sad seeing this happening in front of you."
    oop "One last change, leave, or you will be like that little boy."
    menu:
        "No, this is beyond my acceptance.":
            if GoodTalks > GEthresh:
                jump ending1
            else:
                jump ending2
        "Leave.":
            if GoodTalks > GEthresh:
                jump ending3
            else:
                jump ending4

# Endings (Jingtian Li & Guozheng Yang)
label ending1:
    scene bg Plantation_Farmland
    show Mount
    show tsing at right
    show buenos at left
    "You swiftly put out your gun and shoot Brit. He falls down. It is not a deadly shot, but still shocking enough. Before Brit makes any order, Mount rushes to one of his guard, knocked him out and throws his gun to Tsing."
    "Tsing also reacts quickly, he uses the gun to kill two other guards standing next to Brit. But Tsing also gets one shot on the right arm."
    tsing "Buenos, pick up the gun!"
    "Buenos stands there still while Brit is trying hard to creep to the corpse of his dead guard for guns. You shoot at Brit, but no hit."
    you "Buenos, wake up!"
    "Buenos finally reacts to this situation. He sprints toward the guns on ground, kills Brit and a few other enemies."
    "More guards come to the battlefield but you four work together and kill them all. Standing among the dead corpses, those child labors gather to you. Their eyes are still filled with fear and tead."
    buenos"we should bring them back to America."
    mount "I agree boss. you should bring those kids through border. We shall take the drug back by underground railway."
    you "sounds like a nice plan to me."
    scene bg Border_Office
    "You and the kids reach the US-Mexico border."
    show police at right
    show guard3 at left
    you "Police officers, they are refugees from Mexico. I just rescued them from a plantation in Mexico."
    uspa "Who are you? How can you prove they are refugees instead of illegal immigrants."
    uspb "Oh I thought those two are the same things."
    uspa "Haha, nice one."
    "You move your hand to the gun in your pocket, but finally, you decide to give them your fake ID. That is the only thing you can offer now."
    uspb "Wait... are you?"
    "You see the police searching for something in the drawer. Later, he finds a photo of you."
    uspa "Shit, he is the guy."
    "they knock you off with a electric gun. You fall down without a chance of defending yourself. When you wake up, you find yourself in a big office room. the state governor stands in front of you, aside with the mysterious man."
    scene bg Prison_Office
    show mystery
    show mysterious_man at left
    sgboss "welcome home boy. you have done an excelent job. You friends already gave me what I want. But I still want to thank you in person, and remind you that this is a secret between us. Now you are free to leave."
    you "where are my friends, where are those kids?"
    sgboss "#chuckle# I do not know where your friends are. I gave them freedom as well."
    sgboss "As for those kids, they are illegal immigrants. So I guess they are back home now."
    you "you asshole..."
    "once again you reach your hand to your pocket for gun, but you find it gone."
    sgboss "What are you waiting for, get back to your family, and good luck to rest of your life."
    hide mystery
    if daughter_die:
        "Before you leave the building, the mysterious man stops you. After he makes sure there is no one around, he drags you to a corner."
        you "What the hell"
        mm "I just wanna say, nice work killing my dear sister."
        you "What does that mean. are your looking for a revenge?"
        mm "...No."
        mm "Actually I think I should say thank you."
        you "Thank me for what? I have had enough of you and your father. could you let me leave now?"
        mm "#stare at you# OK... you can leave now."
    scene Cityhall
    "You head out of building and find yourself at the city hall of Los Angeles. People around you look at you like you are an alien. But whatever, you can return to your family now."
    return

label ending2:
    scene bg Plantation_Farmland
    show Mount
    show tsing at right
    show buenos at left
    "You swiftly put out your gun and shoot Brit. He falls down. It is not a deadly shot, but still shocking enough. Before Brit makes any order, Mount rushes to one of his guard, knocked him out and throws his gun to Tsing."
    "Tsing also reacts quickly, he uses the gun to kill two other guards standing next to Brit. But Tsing also gets one shot on the right arm."
    mount "Buenos, pick up the gun!"
    "Buenos stands there still while Brit is trying hard to creep to the corpse of his dead guard for guns. You shoot at Brit, but no hit."
    you "Buenos, wake up!"
    "Buenos finally reacts to this situation. He sprints toward the guns on ground. He points the gun at Brit, but at this moment, he hesitates."
    buenos "We have killed so many people, boss. It is not what you have promised to me. I cannot take anymore."
    tsing "It is not time for that shit, Buenos."
    buenos "Maybe it's not. But you really should stop killing."
    "Buenos drops the gun, turns around and walks away."
    "But he does not notice Brit picks up the gun and aim it at Mount."
    you "Mount, GET DOWN!"
    "It is too late, Brit puts a bullet in Mount's head. Next shot, Brit kills Buenos. Sadness overwhelms you and other guards start to gather around you."
    tsing "Boss, we must leave right now!"
    hide buenos
    hide mount
    menu:
        "Run, Tsing, Run!":
            "Although both of you are fast, Tsing still sustains a fatal shot. He dies in the plantation. But you escape with the drug."
        "Tsing, you go ahead, I will follow behind you.":
            "You reload your gun and try to protect Tsing while retreating. You never want to lose one more friend."
            "However, there are too many of them. Short after, both of you are shot."
            jump gameEnd
    hide tsing
    scene bg Underground_Railroad
    "Tear covers your face as you travel through the underground railway. When you finally get back to US, there is really nothing left in your brain but tremendous sadness."
    scene bg Out_Car
    "You find a paper note in the car. There is an address on it. You set it as the destination then follow the GPS system like a robot."
    scene bg Cityhall
    "You arrive at the city hall of Los Angeles. You park the car at the parking lot. It is around 10:30, so not a lot of people around."
    "Just before you get out of your seat, the back doors and the vice driving door are opened. three men enter the car. One of them is the mysterious man. He is sitting in the back."
    scene bg In_Car
    show mystery
    show mysterious_man at right
    "Another man in the back seat starts to speak."
    sgboss"Hello, my friend %(playerName)s, welcome back. I am the state governor. Now you can give me the drug."
    "You peek at the man seating next to you. He seems to be the bodyguard of the state governor."
    you "It is under your seat. If you may excuse me, I shall leave now."
    sgboss"No, no, no. Not so fast. I think we have a few other things to talk about."
    "He takes one pill and puts it in his mouth Then you hear some strange voices from him."
    sgboss"You killed my daughter but that is OK, I don't like her anyway. But you injured my friend. That is not cool, man. That is not cool."
    sgboss"But You know what, I am nice enough so I decide to let you go now. Just... just give my bodyguard your gun then leave."
    menu:
        "I will do this for my friends":
            "You pull out your gun and prepare to target the governor."
            "But before you shoot governor, his bodyguards kill you immediately"
            "You are so close to you freedom and your family, but finally you choose the wrong step and fall in blood."
            return
        "Give him the gun":
            hide mystery
            if daughter_die:
                "The governor nods and asks the bodyguard to stay in the car before you arrive home. He then gets off the car. But the mysterious man does not follow."
                mm "Jack, I'll do that. You may leave now."
                "The bodyguard nods, then gets off as well."
                mm "Finally, it's just you and me. Do not start the engine, I do not wish to go to your home. I just want to talk with you for a sec. Then I'll get off."
                you "..."
                mm "I just wanna say, nice work killing my dear sister."
                you "..."
                mm "I guess I should say thank you Huh?"
                you "..."
                mm "#stare at you# OK... you can leave now."
                scene bg Dream
                "After a few days, the governor sends some money and informs you that your files have been cleaned up."
                "Finally, you can enjoy your life with your family"
                return
            else:
                scene bg Dream
                "The governor nods and asks the bodyguard to stay in the car before you arrive home."
                "After a few days, the governor sends some money and informs you that your files have been cleaned up."
                "Finally, you can enjoy your life with your family"
                return

label ending3:
    scene bg Plantation_Farmland
    show Mount
    show tsing at right
    show buenos at left
    "You wish you can convince him to give up child labor, but finally, you give up because you see the anger in Brit's eyes. You leave the plantation."
    mount "No boss, we should not leave like this. Where is your courage that you expressed through this journey. Has it all gone?"
    "Buenos and Tsing remain in silence, but you can tell from their faces that they are not happy either."
    mount "#turn around# Brit, what you have done in this plantation is inhuman. and you should stop right now."
    oop"Haha, is this a joke? Am I supposed to be laughing? Does world has changed so much that even drug smugglers nowadays can teach others how to be a proper human?"
    mount "Yes we are smugglers but we have buttom line."
    oop "Very funny. I have to say though I hate your boss, I like you, dude. Here, take this money and be my guy."
    menu:
        "Remain in silence":
            mount "No. Never. You are a disgusting person."
            "Mount rushes to Brit and punches his face before you could stop him. Though astonished, Tsing and Buenos react quickly and join the battle with Mount."
            oop"OK, this is getting interesting. Kill them, my guards!"
            "Though you have a gun, but that cannot compare with several fully armed guys. You are your friends get defeated within a minute."
            jump gameEnd
        "That is enough, Mount. We should leave":
            pass
    "The whole team remains in silence as traveling through the underground railway."
    scene bg Underground_Railroad
    show Mount
    show tsing at right
    show buenos at left
    menu:
        "Well, maybe I can make the state governor take care of that":
            tsing "Are you kidding us? You know it is not going to happen"
            mount "Boss, you really let me down this time."
            you "At least the state governor can put some pressure on him. You... you know, customer is the king."
            buenos "Can you just shut up?"
            you "Oh you are letting me shut up now. Then why didn't you speak up back in the plantation."
            buenos "Because I heard somebody talking about the state governor at the moment."
            you "Really nice, so what is the matter?"
            buenos "This guy who we are working for, the state governor knows what is happening there. And he still chooses to this plantation because he just wants his fucking drug."
            buenos "I cannot believe we are working for such cold-blood, hypocitical, and evil person."
            "You do not know if Buenos is refering to you or the state governor. But you decide not to ask and remain silence in the rest of the trip."
        "Remain in silence":
            pass
    scene bg In_Car
    "As soon as you get back to US, all of them three leave you without a word. You look at their backs through tears; there is really nothing left in your brain but tremendous sadness."
    "You find a paper note in the car. There is an address on it. You set it as the destination then follow the GPS system like a robot."
    scene bg Cityhall
    "You arrive at the city hall of Los Angeles. You park the car at the parking lot. It is around 10:30, so not a lot of people around."
    scene bg In_Car
    show mystery
    show mysterious_man
    "Just before you get out of your seat, the back doors and the vice driving door are opened. three men enter the car. One of them is the mysterious man. He is sitting in the back."
    "Another man in the back seat starts to speak."
    sgboss"Hello, my friend %(playerName)s, welcome back. I am the state governor. Now you can give me the drug."
    "You peek at the man seating next to you. He seems to be the bodyguard of the state governor."
    you "It is under your seat. If you may excuse me, I shall leave now."
    sgboss"No, no, no. Not so fast. I think we have a few other things to talk about."
    "He takes one pill and puts it in his mouth Then you hear some strange voices from him."
    sgboss"I heard one of your friend interests Brit a lot. I can pay a big money to... you know, sort of, buy his labor."
    you "He left me already."
    sgboss"OK, that's a shame. Just... just give my bodyguard your gun then leave."
    menu:
        "I will do this for my friends":
            "You pull out your gun and prepare to target the governor."
            "But before you shoot governor, his bodyguards kill you immediately"
            "You are so close to you freedom and your family, but finally you choose the wrong step and fall in blood."
            return
        "Give him the gun":
            hide mystery
            if daughter_die:
                "The governor nods and asks the bodyguard to stay in the car before you arrive home. He then gets off the car. But the mysterious man does not follow."
                mm "Jack, I'll do that. You may leave now."
                "The bodyguard nods, then gets off as well."
                mm "Finally, it's just you and me. Do not start the engine, I do not wish to go to your home. I just want to talk with you for a sec. Then I'll get off."
                you "..."
                mm "I just wanna say, nice work killing my dear sister."
                you "..."
                mm "I guess I should say thank you Huh?"
                you "..."
                mm "#stare at you# OK... you can leave now."
                scene bg Dream
                "After a few days, the governor sends some money and informs you that your files have been cleaned up."
                "Finally, you can enjoy your life with your family"
                return
            else:
                scene bg Dream
                "The governor nods and asks the bodyguard to stay in the car before you arrive home."
                "After a few days, the governor sends some money and informs you that your files have been cleaned up."
                "Finally, you can enjoy your life with your family"
                return


label ending4:
    scene bg Underground_Railroad
    show Mount
    show tsing at right
    show buenos at left
    "You leave the plantation, get back to US by the underground railway. Find a note in the car with an address on it. Your drive to there, it is the city hall of Los Angeles."
    scene bg Cityhall
    show receptionist
    "The front desk lead you and your crew to the top office. You see three men in the room. One of them is the mysterious man. The man sitting in the middle starts to speak."
    hide receptionist
    show mystery
    show mysterious_man at right
    sgboss"Hi, I am the state governor. First thing first, where is my drug"
    "Tsing hands the jar of drug to the state governor. He takes one pill and puts it in his mouth Then you start to hear some strange voices from him."
    sgboss"Yes, yes, it feels so right!"
    you"So can we leave? I already feel sick of your mission."
    sgboss"No, no, no. Not so fast. I think we have a few other things to talk about."
    sgboss"I appreciate that you killed many troublemakers along your journey, so I offers you, all of you to stay and work for me."
    menu:
        "Refuse to stay":
            sgboss"Fine, one last thing before you leave, give me back your gun."
            menu:
                "Shoot him":
                    "You pull out your gun and prepare to target the governor."
                    "But before you shoot governor, his bodyguards kill you immediately"
                    "You are so close to you freedom and your family, but finally you choose the wrong step and fall in blood."
                    return
                "Give him the gun":
                    scene bg In_Car
                    "Finally the journey is over. Driving in the LA downtown, you and your friends decide first to have something to eat."
                    show tsing
                    Tsing "%(playerName)s, watch out!" with vpunch
                    "A big truck bumps into your car at the cross road. That is the last thing you know."
                    jump gameEnd
        "Accept the job":
            you "As long as you have money, whatever you say, boss."
            "You three friends are unsure of this decision at beginning, but when they see a case of cash, they all start to laugh like you do."
            "The job is busy and exciting. You never have a chance to go back to your family since you accepted the job. But who cares? You get money! And you can kill people with your friend. There can be no happier life than this in this world."
            return

label gameEnd:
    scene bg Openspace
    "You were so close to your freedom and your family, but now you fall in your own blood. Hope you have a better luck next time."
    return

label test:
    "Use jump to jump between scenes"
