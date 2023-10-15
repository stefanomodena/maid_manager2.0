init python:

    import random


    # # MAIDS **********************************************************************************************************


    class Maid:
            def __init__(self, name, status, level, xp, hired, affection):
                self.name = name
                self.status = status
                self.level = level
                self.xp = xp
                self.hired = hired
                self.affection = affection




    makotoMaid = Maid("Makoto", True, 1, 0, True, 0)
    rebeccaMaid = Maid("Rebecca", True, 1, 0, False, 0)
    marcyMaid = Maid("Marcy", True, 1, 0, False, 0)
    emilyMaid = Maid("Emily", True, 1, 0, False, 0)

    def levelingup(maid):
        global didLevel
        if maid.xp >= maid.level * 10:
            didLevel = True
            maid.level += 1
            maid.xp = 0
            return didLevel
        else:
            didLevel = False
            return didLevel

    # # CUSTOMERS ******************************************************************************************************

    # # Define lists of first and last names to use for generating random names
    first_names_male = ['Bob', 'Charlie', 'David', 'Frank']
    first_names_female = ['Alice', 'Emily', "Karen", "Susan"]
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']



    class Customer:
        def __init__(self, name, age, gender, requests):
            self.name = name
            self.age = age
            self.gender = gender
            self.requests = requests

    # # Create a list to hold the customer instances
    customers = []

    # # Generate 10 random customers

    for i in range(10):
    #   # Generate a random gender using a 50/50 chance
        gender = 'male' if random.randint(0, 1) == 0 else 'female'

        if gender == "male":
            first_name = random.choice(first_names_male)
            last_name = random.choice(last_names)
        else:
            first_name = random.choice(first_names_female)
            last_name = random.choice(last_names)

        name = f"{first_name} {last_name}"

    #   # Generate a random age between 18 and 99
        age = random.randint(18, 99)



    #   # Generate a random list of requests (could be empty)
        requests = []

        num_requests = random.randint(0, 3)

        for j in range(num_requests):
            requests.append(f"Request {j+1}")

    #   # Create a new Customer instance with the random values
        customer = Customer(name, age, gender, requests)

    #   # Add the customer to the list
        customers.append(customer)


    # # TASKS **********************************************************************************************************

    class Task:
        def __init__(self, name, difficulty, base_payment):
            self.name = name
            self.difficulty = difficulty
            self.base_payment = base_payment

    tasks = []

    # # Create task instances for various tasks
    vacuuming = Task('Vacuuming', 3, 50)
    dusting = Task('Dusting', 2, 30)
    washing_dishes = Task('Washing Dishes', 2, 20)
    babysitting = Task('Babysitting', 4, 60)
    gardening = Task('Gardening', 5, 70)
    welcoming_guests = Task('Welcoming Guests', 5, 80)

    # # Add the tasks to the list
    tasks.extend([
    vacuuming, dusting, washing_dishes, babysitting, gardening, welcoming_guests
    ])



    # # REPUTATION *****************************************************************************************************

    reputation = 0


    # # UPGRADES *******************************************************************************************************

    upgrade1 = False
    upgrade2 = False
    upgrade3 = False
    upgrade4 = False




    # # VARIABLES ******************************************************************************************************

    # MAINTENANCE

    maintenanceCost = 50

    money = 0

    debt = 1000000

    current_day = 0

    supplies_stock = 0

    stamina_max = 10

    stamina = 10

    datePartner = ""

    alternateMakoto = False

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unkown = Character("???")
define m = Character("Makoto")
define pov = Character("[povname]")
define r = Character("Rebecca")
define ma = Character("Marcy")

# Character images

image MakotoNeutral:
    "Makoto.png"

image MakotoDate:
    "MakotoDate.png"

image RebeccaNeutral:
    "Rebecca.png"

image MarcyNeutral:
    "Marcy.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene main:
        zoom 2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"

    "[povname] had never imagined that he would one day find himself the owner of a company. Let alone a Maid company."
    "He had inherited his grandmother's business, but upon arriving at the company's headquarters..."
    "He was shocked to find it in disarray."
    "The grand, well-maintained building had lost its luster, and the business seemed to be crumbling."

    "As he stepped through the entrance, he was greeted by a gentle, purple-haired girl with a warm smile."

    show MakotoNeutral

    m "Welcome! I'm Makoto, and you must be my new master!"

    pov "Master?"

    m "Yes! That's how a proper maid should greet her employer."

    pov "I see. Anyway, I'm [povname]. Can you tell me more about the company?"

    scene office:
        zoom 2

    show MakotoNeutral

    "Makoto led [povname] to a cozy sitting area in the office and gestured for him to sit."
    "She then took a seat across from him and began to explain the situation."

    m "Well, [povname], I must admit that the company is not in the best shape right now."

    m "We're in debt, and there's only one maid left."

    pov "I'm sorry to hear that, I'm assuming that you're the last maid."

    m "Yes."

    pov "What happened to the others?"

    m "Many of them left when times got tough."
    m "They were worried about job security, and our reputation took a hit."
    m "It's been hard trying to manage everything on my own."

    pov "Makoto, I'm determined to turn things around for this company."
    pov "I may not know much about the maid business, but I'm willing to learn."
    pov "Will you help me rebuild the company?"

    m "Of course, [povname]! I've been waiting for someone like you to come and help us."
    m "With your guidance and my experience, I believe we can bring this company back to its former glory."

    pov "Then it's settled! We'll work together to make this company thrive again, and I'll learn what it takes to be a proper master in the process."

    jump mapTutorial

label mapTutorial:

    show MakotoNeutral

    m "So, this is where we live."
    m "This is our company, this is the market, this is the tavern, the plaza, the construction company, the luxury store, the mayor's mansion and the forest."
    m "We can find anything we want on those places or meet the right people like customers and other maids."

    pov "It's quite a small, tight-knit community, it seems."

    m "Yes, [povname]. It's a wonderful town, and the people here have been kind. We can build a strong reputation and clientele if we're careful."

    pov "What should be our first step then? You mentioned the plaza and the message board."

    m "Yes, the plaza is a great place to start. There's a board there where people can post various services or messages."
    m " It's a fantastic way to find gigs that can help us make money before we focus on renovating the company."

    pov "Alright, let's head to the plaza then. We can see what opportunities are available, and I can get a better sense of the town and its residents."

    m "Great choice, [povname]! I'll be with you every step of the way."

    "With Makoto's guidance and the newfound determination to rebuild the company, [povname] and his loyal maid set off to the plaza, ready to take on their first challenges and breathe new life into the struggling business."

    jump plazaTutorial

label plazaTutorial:

    scene plaza:
        zoom 2

    show MakotoNeutral

    "[povname] and Makoto approach the message board where the citizens place ads selling products, offering services or looking for professionals."

    m "We can always come here to look for new jobs."

    pov "Do you see any we can do it?"

    m "Let's see..."

    m "..."

    m "Here! This customer needs his house cleaned! An easy job we can do for some money."

    pov "Let me help you!"

    m "No! I'm the maid, [povname]. Just make sure I have a place to live, my needs are met, and I have supplies."

    pov "I still feel bad for you doing the manual work. I want to be involved, Makoto."

    m "You're very gentle, [povname]. But it's my duty to handle the cleaning."
    m "You have your own responsibilities, like managing the company and making sure everything runs smoothly."

    pov "Alright, Makoto. I'll trust your judgment. But please don't hesitate to let me know if you need anything, or if there's a way I can assist you"

    jump officeTutorial

label officeTutorial:

    scene office:
        zoom 2

    show MakotoNeutral

    pov "We didn't made much money."

    m "Yeah, we don't have the same reputation as before, but as our reputation rises we will get better jobs."

    pov "You're right. Building our reputation takes time, and we need to start somewhere."

    m "We also need to buy supplies before taking on any more jobs. Each job consumes one unit of supplies, and we have daily maintenance costs to cover."

    pov "How much it costs to keep business afloat?"

    m "It costs [maintenanceCost]."

    pov "Per day?!"

    m "Per day."

    pov "That's going to be tough, but we can do it."
    pov "So, let's go to the market tomorrow to buy supplies. We don't want to overexert ourselves."

    m "Thank you for understanding, [povname]. Each maid has her stamina, and I'm a bit rusty, so I can only do one job per day. I need to train to take on more work."

    pov "Of course, Makoto. We'll take it one step at a time and work together to make this company a success."

    hide MakotoNeutral

    "The next day..."

    jump marketTutorial

label marketTutorial:

    scene market:
        zoom 2

    show RebeccaNeutral

    pov "Hi! I need some cleaning supplies"

    unkown "Sure, I can help you with that."

    pov "What's your name?"

    r "I'm Rebecca! You're new in town, right?"

    pov "Yeah! I'm [povname]. I'm new here, and I'm the new owner of the maid company."

    r "Oh, that's exciting! It's nice to meet you, [povname]. If you ever need anything or have any questions about the town, feel free to ask."
    r "The people here are friendly, and we're always happy to welcome newcomers."

    "Added 5 boxes of supplies to inventory"

    $ supplies_stock += 5

    pov "Thank you, Rebecca. I'll keep that in mind. It's been a pleasure meeting you."

    r "Likewise, [povname]! I hope to see you again soon."

    pov "Before I go, I see that you're very happy working here, but would you like to work for me?"

    r "Well, I can't leave my stable job right now. If you raise your company's reputation, I can consider it."

    pov "Fair enough, Rebecca. I'll do my best to build our company's reputation, and maybe in the future, we can discuss the possibility of you joining our team."

    r "I'll be watching, [povname]. Good luck with your business, and don't hesitate to ask if you need anything."

    jump mainTutorialUpgrade

label mainTutorialUpgrade:

    scene main:
        zoom 2

    show MakotoNeutral

    pov "I got 5 units of supplies, enough for the next few days,"

    m  "Great! Those will help. But now, I think it's time to show you how to upgrade our company."

    pov  "Upgrade?"

    m "Yes, we need to upgrade the company headquarters to receive more maids, make more profit, and unlock a wider range of job opportunities."

    pov "How can we do that?"

    m "You can talk with Marcy. She's really good with construction and renovations. She can help us improve our headquarters and expand our business."

    pov "Alright, I'll seek out Marcy and discuss the upgrades with her. It sounds like a promising step in our journey to success."

    jump workshopTutorial

label workshopTutorial:

    scene workshop:
        zoom 2

    show MarcyNeutral

    "[povname] located Marcy, who, as Makoto had suggested, was known for her construction and renovation skills."
    "She was busy working on her workshop. As [povname] approached her, he greeted her with a friendly smile."

    pov "Hi, Marcy! I've heard you're an expert in construction and renovations."

    ma "Hi! That would be me."
    ma "And before you ask: Yes, the ears are real so is the tail."

    pov "I was wandering where the tail was attached, that answers it."
    pov "We're looking to upgrade our company headquarters to expand our business. Can you help us with that?"

    ma "Of course, I'd be delighted to help. Upgrading the company headquarters is a great idea."
    ma "It will make it more appealing to potential maids and clients."

    pov "That's exactly what we're aiming for. What do you need from us to get started?"

    ma "First, we'll need to discuss what kind of upgrades you have in mind. Then, we'll create a plan and estimate the costs."
    ma "How about we start with a bigger storage room? So you can store more supplies and make less trips to the market."

    pov "I don't mind going more to the market and seeing Rebecca, but I think that's a great start."

    jump mainTutorialUpgrade2

label mainTutorialUpgrade2:

    init:
        transform flip:
            xzoom -1.0

    scene main:
        zoom 2

    show MakotoNeutral

    m "Hey, Marcy!"

    show MarcyNeutral at flip


    ma "Hey, Makoto!"

    m "So, you're here to help us renovate?"

    ma "Yeah, we're thinking about enlarging your storage room. It will allow you to store more supplies, making your operations more efficient."

    pov "Let's proceed with the storage room upgrade."

    m "That sounds like a fantastic idea. It will save us time and energy and make the workspace more organized."

    hide MarcyNeutral with dissolve

    hide MakotoNeutral with dissolve

    scene black

    "Some time later..."

    scene main:
        zoom 2

    show MarcyNeutral at flip

    ma "There you have it! A new and improved storage room!"

    pov "That was fast! I'm impressed!"

    show MakotoNeutral

    m "Marcy is very efficient. We're lucky to have her helping us."

    ma "You guys flatter me, keep going."

    pov "Now the bad part, how much do we owe you?"

    ma "We can treat this as a demonstration. So you can know how I work. Next upgrades we can discuss prices."

    pov "Thanks, Marcy. We'll need a lot of help renovating the company, and your expertise will be invaluable in making our business a success."

    ma "You're always welcome at my workshop to talk about work or other things... *wink*"

    hide MarcyNeutral with dissolve

    "Marcy leaves and [povname] blushes while Makoto giggles."

    pov "What now?"

    m "I think you have all the tools you need to fix the company. Now you just need to keep it runing."

    pov "I'll do my best!"

    m "I know, and I'm here for you."

    scene black

    "The next day..."

    jump mainMenu



# # END OF TUTORIAL ****************************************************************************************************

# # MAIN MENU **********************************************************************************************************

label mainMenu:

    scene main:
        zoom 2

    show screen day_money_counter


    menu:


        m "What do you want to do now?"

        "Look for jobs":

            jump tasksMenu

        "Map":

            jump map

        "Go to office.":

            jump office
#
#         "Hire new maids":
#
#             jump hireMaids
#
#         "Maid School":
#
#             jump MaidSchool
#
#         "Bank":
#
#             jump bank

        "rest for the day":

            jump endday

        "quit the game":

            jump quit

# # MAIN ENDDAY ********************************************************************************************************

label endday:

    scene endday:
        zoom 2

    python:
        makotoMaid.status = True
        rebeccaMaid.status = True
        marcyMaid.status = True



        current_day += 1

        stamina = stamina_max



        money -= maintenanceCost



    "The day ends and you and the maids rest.\n$[maintenanceCost] was deducted to cover expenses. You now have: $[money]"



    jump mainMenu



# # TASKS **************************************************************************************************************

label tasksMenu:
    python:
        index = random.randint(0, len(tasks)-1)
        taskName = tasks[index].name

    menu:
        m "Let's see what is available!"

        "[taskName]":
            jump taskDescription

        "Go back":
            jump managermenu

label taskDescription:
    python:
        customerIndex = random.randint(0, len(customers)-1)
        customerIndex = int(customerIndex)

        customerHiring = customers[customerIndex].name


    hide MaidNeutral with dissolve

    menu:
        m "[customerHiring] needs us to do [taskName]. Lets see who is available"

        "Makoto" if makotoMaid.status == True and supplies_stock > 0:
            $ supplies_stock -= 1
            show MakotoNeutral with dissolve
            $ chosen_maid = makotoMaid
            $ makotoMaid.status = False
            jump taskResolution

        "Rebecca" if rebeccaMaid.status == True and rebeccaMaid.hired == True and supplies_stock > 0:
            $ supplies_stock -= 1
            show RebeccaNeutral with dissolve
            $ chosen_maid = rebeccaMaid
            $ rebeccaMaid.status = False
            jump taskResolution

        "Marcy" if marcyMaid.status == True and marcyMaid.hired == True and supplies_stock > 0:
            $ supplies_stock -= 1
            show MarcyNeutral with dissolve
            $ chosen_maid = marcyMaid
            $ marcyMaid.status = False
            jump taskResolution

        "You don't have enough supplies!" if supplies_stock <= 0:
            jump mainMenu

        "Go back":
            jump mainMenu



label taskResolution:
    python:

        taskPayment = tasks[index].base_payment
        taskPayment = taskPayment + (taskPayment * (chosen_maid.level / 10))
        if upgrade1 == True:
            taskPayment = taskPayment * 2
        money += taskPayment
        exp = tasks[index].difficulty
        chosen_maid.xp += exp
        if upgrade2 == True:
            reputation += (tasks[index].difficulty * 2)
        else:
            reputation += tasks[index].difficulty
        levelingup(chosen_maid)
        if didLevel:
            levelUpText = f"{chosen_maid.name} has leveled up!"
        ResolutionText = f"Great! {chosen_maid.name} was successful! We got payed ${taskPayment} and she got exp. Now we have ${money}"


    if didLevel:
        m "[ResolutionText], [levelUpText]"
    else:
        m "[ResolutionText]"



    jump mainMenu

# # MAP ****************************************************************************************************************

label map:

    scene board:
        zoom 2


    menu:

        "workshop":

            jump workshop

        "Market":

            jump market

        "Go back":

            jump mainMenu

# # MARKET *************************************************************************************************************
label market:

    scene market:
        zoom 2

    show RebeccaNeutral

    if rebeccaMaid.hired == False:
        r "Hi, [povname]! Want to buy some supplies or hire me?"
    else:
        r "Hello, Master! How can I help?"

    menu:

        "Buy supplies ($10)":

            menu:
                "Buy one box of supplies ($10)":
                    if money >= 10:
                        $ money -= 10
                        $ supplies_stock += 1
                        "you boughht some supplies now you have [supplies_stock] boxes."
                        jump market
                    else:
                        "you don't have enough money!"
                        jump market
                "Buy five boxes of supplies ($50)":
                    if money >= 50:
                        $ money -= 50
                        $ supplies_stock += 5
                        "you boughht some supplies now you have [supplies_stock] boxes."
                        jump market
                    else:
                        "you don't have enough money!"
                        jump market
                "Buy ten boxes of supplies ($100)":
                    if money >= 100:
                        $ money -= 100
                        $ supplies_stock += 10
                        "you boughht some supplies now you have [supplies_stock] boxes."
                        jump market
                    else:
                        "you don't have enough money!"
                        jump market

        "Hire Rebecca." if rebeccaMaid.hired == False:
            if reputation >= 10:
                r "Now I can join your company!"
                $ rebeccaMaid.hired = True
                jump market
            else:
                r "If your company grows more I can consider."
                jump market

        "Go on date." if rebeccaMaid.hired == True and reputation >= 30:
            pov "I want to take you on a date."

            m "A-a date, master?"

            pov "Yes! Would you like that?"

            m "I feel honored!"
            menu:
                m "Where are you taking me?"

                "To the park! ($20 5 stamina)":
                    if money >= 20 and stamina >= 5:
                        $ money -= 20
                        $ stamina -= 5
                        $ datePartner = rebeccaMaid.name
                        jump datePark
                    else:
                        ma "I think we should postpone our date, Master."
                        jump office


                "I've to postpone our date.":
                    m "Sorry to hear that, looking foward to it."
                    jump office


        "Go back":
            jump mainMenu


# # WORKSHOP ***********************************************************************************************************

# 1 Upgrade MORE MONEY
# 2 Upgrade MORE REPUTATION
# 3 Upgrade MORE RELATIONSHIP
# 4 Upgrade NEW WORKSHOP

label workshop:

    scene workshop:
        zoom 2

    show MarcyNeutral

    if marcyMaid.hired == False:
        ma "Hi, [povname]! What do you need built?"
    else:
        ma "Hey there, Master! I'm here to help you with anything you want."

    menu:

        ma "What you want built today?"

        "1 Upgrade MORE MONEY" if upgrade1 == False:
            if money >= 100:
                ma "This upgrade will help you make more money!"
                $ upgrade1 = True
                jump workshop
            else:
                ma "Sorry, but we're going to need more money for that"
                jump workshop

        "2 Upgrade MORE REPUTATION" if upgrade2 == False:
            if money >= 100:
                ma "This upgrade will help you bring more customers!"
                $ upgrade2 = True
                jump workshop
            else:
                ma "Sorry, but we're going to need more money for that"
                jump workshop

        "3 Upgrade AFFECTION" if upgrade3 == False:
            if money >= 100:
                ma "With this new workshop you'll raise affection faster."
                $ upgrade3 = True
                jump workshop
            else:
                ma "Sorry, but we're going to need more money for that"
                jump workshop

        "4 Upgrade NEW WORKSHOP" if upgrade1 == True and upgrade2 == True and upgrade3 == True and upgrade4 == False:
            if money >= 100:
                ma "With this new workshop I can automate things and have enough time to work with you!"
                $ marcyMaid.hired = True
                $ upgrade4 = True
                jump workshop
            else:
                ma "Sorry, but we're going to need more money for that"
                jump workshop

        "No upgrades available" if upgrade1 == True and upgrade2 == True and upgrade4 == True:
            ma "Everything is as good as it gets, Master. But who knows in the future what we can build?"
            jump workshop

        "Go back":
            jump mainMenu

# # OFFICE *************************************************************************************************************

label office:

    scene office:
        zoom 2

    show MakotoNeutral

    m "Hello, master!"

    menu:

        m "How can I help you, master?"

        "I just want to chat.":
            if stamina >= 5:
                $ stamina -= 5
                if upgrade3 == True:
                    $ makotoMaid.affection += 2
                else:
                    $ makotoMaid.affection += 1
                $ makotoAffection = makotoMaid.affection
                "You and Makoto spend some time chatting. Her affection towards you is: [makotoAffection]."
                jump office
            else:
                m "I think you could use some rest, Master."
                jump office

        "Go on a date" if makotoMaid.affection >= 10:

            pov "I want to take you on a date."

            m "A-a date, master?"

            pov "Yes! Would you like that?"

            m "I feel honored!"
            menu:
                m "Where are you taking me?"

                "To the park! ($20 5 stamina)":
                    if money >= 20 and stamina >= 5:
                        $ money -= 20
                        $ stamina -= 5
                        $ datePartner = makotoMaid.name
                        jump datePark
                    else:
                        ma "I think we should postpone our date, Master."
                        jump office


                "I've to postpone our date.":
                    m "Sorry to hear that, looking foward to it."
                    jump office




        "Nevermind, I've changed my mind.":
            jump mainMenu


# # DATE AT THE PARK****************************************************************************************************

label datePark:

    scene park:
        zoom 2

    if datePartner == "Makoto":
        show MakotoDate
        m "Thanks for bringing me, Master!"
        hide MakotoDate
        scene black
        "Some time later..."
        scene park:
            zoom 2
        "You and [datePartner] spend a great time together!"
        $ makotoMaid.affection += 5
        "[datePartner] affection +5."
        show MakotoDate
        m "I had lots of fun, Master."
        pov "Me too, [datePartner]."
        m "I hope I'm not being too foward, but I'm looking foward to our next date."
        pov "Me too."
        hide MakotoDate
        jump mainMenu
    elif datePartner == "Rebecca":
        show RebeccaNeutral
        r "Thanks for bringing me, Master!"
        hide RebeccaNeutral
        scene black
        "Some time later..."
        scene park:
            zoom 2
        "You and [datePartner] spend a great time together!"
        $ makotoMaid.affection += 5
        "[datePartner] affection +5."
        show RebeccaNeutral
        r "I had lots of fun, Master."
        pov "Me too, [datePartner]."
        r "I hope I'm not being too foward, but I'm looking foward to our next date."
        pov "Me too."
        hide RebeccaNeutral
        jump mainMenu
    elif datePartner == "Marcy":
        show MarcyNeutral
        ma "Thanks for bringing me, Master!"
        hide MarcyNeutral
        scene black
        "Some time later..."
        scene park:
            zoom 2
        "You and [datePartner] spend a great time together!"
        $ makotoMaid.affection += 5
        "[datePartner] affection +5."
        show MarcyNeutral
        ma "I had lots of fun, Master."
        pov "Me too, [datePartner]."
        ma "I hope I'm not being too foward, but I'm looking foward to our next date."
        pov "Me too."
        hide MarcyNeutral
        jump mainMenu







label quit:

    m "You've created a new Ren'Py game."

    m "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
