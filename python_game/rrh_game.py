import time

chantarelle = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣶⣦⣤⣴⣶⣶⣶⣶⣤⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢤⡀⠉⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠦⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⠘⢶⣦⡄⢠⣤⣤⠄⢠⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠘⢷⡌⢻⣷⠸⣿⡟⢰⡟⠀⠀⠀⠀⠀⠀
⠀⠰⠾⢿⣿⣿⣿⣿⡿⠿⠛⠋⠁⠀⠀⠀⢻⣆⢻⣦⣿⠁⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠐⠠⣄⠀⢀⣀⣤⠀⣾⠀⠀⠀⠀⠀⠀⢻⣮⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠳⡌⢿⣿⣴⡇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
"""

magic = """
                   _..._                
                 ,' (_) `.                 
               .'   .-.   `.               
              ,'_) :   : .-.\             
             .;-.   `-' (   )\            
             (   )    _  `-'  ;           
              `-;_   (_)   ,-'              
                 `'------'                
         _..-"-.._ |    |                   
_..-`:.:'          |    |'''''"-----.._       
                  /     |              `''
_______\|/__________\\;_\\//___\|/________
"""
porcini = """
           ____
       _.-'    `"`--._
   ,".."..  .     ,   ''-.
 ,......  `      ..______.]
/_..__..----""        __.'
`-._       /""| _..-''
    "`-----\  `\.
            |   ;.-""--..
            | ,  .  :::: `.
            `;      .....  :
      .:""-.|`-._         ./
     /   _.-/    ";"------' 
     `--'\`|     /  /
         | /     |  |
         \|     /   |
          `-----`---'
"""

wolf = """
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'
"""

forest = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣦⠀⠀⣠⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣆⠀⠀⠀⠀⠀
⠀⠀⠒⣿⣿⣿⠓⠀⠀⠻⣿⣿⠀⢀⣴⣿⣦⡀⠀⢀⣾⣦⠘⢿⣿⣧⡀⠀⠀⠀
⠀⢀⣴⣿⡿⠃⡄⠈⠻⣿⣟⣉⣀⠉⣽⡿⠋⠡⠴⣿⣿⣿⠓⠀⠙⢇⠀⠀⠀⠀
⠀⠿⣿⠟⢁⣾⣿⣦⣀⠘⠿⠟⢁⣼⣿⣿⣷⠂⣴⣿⣿⣿⣆⠘⢶⣶⣿⠶⠤⠀
⠀⣀⣀⡀⢉⣿⣿⣿⡍⠀⢀⣀⠙⢻⠿⢋⣤⣾⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⡀⠀
⠀⠟⠋⣠⣾⣿⣿⣿⣿⣦⣌⠉⠠⣤⣤⣤⡌⢙⣿⣿⣿⣿⣿⣿⠛⠛⠂⢈⣙⠀
⠀⠀⣉⡉⣹⣿⣿⣿⣿⣏⠉⣉⣀⣈⠙⠋⣠⣿⣿⣿⣿⣿⣿⣿⣆⠙⠛⠛⠛⠀
⠀⠀⠋⣴⣿⣿⣿⣿⣿⣿⣷⣌⠉⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠴⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠦⠈⣙⠛⠛⠛⠛⠛⠛⠛⠛⣉⣉⠁⠀⠀⠀
⠀⠀⣦⣤⡄⢉⣉⣉⣉⠉⣡⣤⠀⠀⠀⣿⣿⣷⠀⢰⣿⣿⡇⢸⣿⣿⠀⠀⠀⠀
⠀⠀⣿⣿⡇⣸⣿⣿⣿⡄⢻⣿⠀⠀⠀⣿⣿⣿⠀⢸⣿⣿⡇⢸⣿⣿⠀⠀⠀⠀
⠀⠀⣿⣿⠁⣿⣿⣿⣿⡇⠸⠿⠀⠀⠀⣿⣿⣿⠀⢸⣿⣿⣇⠸⣿⣿⠀⠀⠀⠀
⠀⠀⠛⠛⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠉⠉⠉⠀⢸⣿⣿⣿⠀⠿⠿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀

"""
mush1 = False
mush2 = False
mush3 = False
room = 0

while True:
    print("""
              Welcome to
        Red Riding Hood Adventure!
        ==========================
        """) 
    print(forest)
    time.sleep(2)
    print("\n"
          "Your mother has asked you to pick up some mushrooms in the forest and bring it to your grandmother.\n"
          "You must be careful, a wolf has been seen in this area!\n")
    opt_1 = input("Type 's' to start. ").lower()
    if opt_1 == 's':
        room += 1
        print("\n"
            "The adventure begins!")    
        time.sleep(3)
    
        while room != 7: 
            if room == 1:
                print("\n"
                    "As soon as you leave the house, you feel like you are being watched.\n")
                time.sleep(2)
                print("Could it be the wolf following you?\n")
                time.sleep(2)
                print("You run into the forest but can\'t see mushrooms just yet. \n")
                time.sleep(2)
                print("You need to go deeper.\n")
                time.sleep(2)
            elif room == 2:
                print("\n"
                    "As you get deeper, you see a meadow full of mushrooms.\n")
                time.sleep(1)
                print(magic)
                time.sleep(1)
                print("You look at them closely but you haven\'t seen mushrooms like these yet. \n")
                time.sleep(1)
                print("They have pores so should be edible but that\'s not always the case.\n")
                time.sleep(1)
                print("Do you pick them? \n")
                time.sleep(1)
                opt_2 = input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                if opt_2 == "pick":
                    mush1 = True
                    print("\n"
                        "'Looks good to me' you think to yourself as you fill your basket.\n")
                elif opt_2 != "pick":
                    mush1 = False
                    print("\n"
                        "You decide not to risk taking the mushrooms you don\'t know.\n")
                    time.sleep(1)
                    print("It\'s your grandma\'s health on the line afterall! \n")
                    time.sleep(1)
                    print("Let\'s hope there is another mushroom spot on the way!\n")
                    time.sleep(1)

            elif room == 3 and mush1 == True:
                print("\n"
                    "As you move forward you spot another mushroom with the corner of your eye.\n")
                time.sleep(1)
                print("'OMG a chantarelle!!' you can\'t believe your luck.\n")
                time.sleep(1)
                print(chantarelle)
                print("But as you look around there\'s not much left in this patch. Four, maybe five little mushrooms.\n")
                time.sleep(1)
                print("Do you pick them and risk the wolf closing down on you, or move forward?")
                opt_2=input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                if opt_2== "pick":
                    mush2 = True
                    print("\n"
                    "You decide it makes sense to take the chantarelles. The more the merrier! \n")
                elif opt_2 != "pick":
                    mush2 = False
                    print("\n"
                        "'There\'s no point in taking those.' you think to yourself. 'I already have some anyway'.\n")
                    time.sleep(1)
                    print("And there could be more on the way.\n")
                    time.sleep(1)
            # You didn't take the magic mushrooms
            elif room == 3 and mush1 == False:
                print("\n"
                    "As you move forward you spot another mushroom with the corner of your eye.\n")
                time.sleep(1)
                print("'OMG a chantarelle!!' you can\'t believe your luck.\n")
                time.sleep(1)
                print(chantarelle)
                print("But as you look around there\'s not much left in this patch. Only few chantarelles left.\n")
                time.sleep(1)
                opt_2=input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                if opt_2== "pick":
                    mush2 = True
                    print("\n"
                        "You decide it makes sense to take the chantarelles. Better this than nothing!\n")
                    time.sleep(1)
                elif opt_2 != "pick":
                    mush2 = False
                    print("\n"
                        "You decide it doesn\'t make any sense to take them.") 
                    time.sleep(1)
                    print("'What will I do with 4 tiny chantarelles anyway?'\n")
                    time.sleep(1)
                    print("'Surely there will be more mushrooms on the way, right? RIGHT?'\n")
                        
            # You didn't pick any mushrooms yet
            elif room == 4 and mush1 == False and mush2 == False:
                print("\n"
                    "You are now on the straight way to your grandma, but you didn\'t pick any mushrooms.\n")
                time.sleep(1)
                print("You can take a detour to look for more mushrooms or go straight to your grandma")
                opt_3=input("Type 'look' to keep on looking for the mushrooms, or [n] for 'next' ")
                if opt_3 == "look":
                    print("\n"
                        "JACKPOT! As you turn to the right just before your grandma\'s house, you find a L A R G E patch of porcinis.\n")
                    time.sleep(1)
                    print(porcini)
                    time.sleep(1)
                    print("'Can I pick them before the wolf catches up with me?' - you are wondering. \n")
                    opt_2=input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                    if opt_2 == "pick":
                        print("You start to fill up your basket joyfully. \n")
                        time.sleep(1)
                        print("After a while you had quite some porcinis in your basket, but there are just so many of them! \n")
                        time.sleep(1)
                        print("Do you want to keep on picking porcinis or go to your grandma?")
                        opt_4 = input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                        if opt_4 == "pick":
                            print("\n"
                                "You decide you must have all of them. You try to fill up your basket in a hurry. \n")
                            time.sleep(1)
                            print("Out of nowhere, you begin to hear muffled growl. \n")
                            time.sleep(1)
                            print("The wolf is catching up with you, and there\'s nothing you can do about it. \n")
                            time.sleep(1)
                            print("You freeze and think about your options in panic.\n")
                            opt_5 = input("Type 'fight' to fight the wolf or 'n' to run ")
                            if opt_5 == "fight":
                                print("You want to fight the wolf, but you have nothing to fight with.\n")
                                time.sleep(1)
                                print("You lose the fight and barely make it alive. \n")
                                break
                            else:
                                print("\n"
                                "You run away as fast as possible, but the wolf is faster. \n")
                                time.sleep(1)
                                print("You try to fight him, but you lose and barely make it alive.")
                                break
                        else:
                            print("\n"
                                "You look at your basket and decide you have more than enough mushrooms already. \n")
                            time.sleep(1)
                            print("You look around quickly but the wolf doesn\'t seem to be catching up with you.")
                            mush3 = True
                    else:
                        print("\n"
                        "'Safety first' you decide. 'Better not to risk meeting the wolf'.\n")
                        time.sleep(1)
                        print("You don\'t really have any mushrooms to show your grandmother but at least you are alive.\n")
                        mush3 = False
                else:
                    print("\n"
                        "There seems to be not enough mushrooms in the forest today.\n"
                        "'I give up' you sigh. 'I just want to see my grandma already'\n")
                    mush3 = False

            # You didn't pick the magic mushrooms but you picked chantarelles
            elif room == 4 and mush1 == False and mush2 == True:
                print("\n"
                    "You are now on the straight way to your grandma, but you only have a few chantarelles.\n"
                    "Do you want to keep on looking or go to your grandma with what you have?\n")
                opt_3=input("Type 'look' to keep on looking for the mushrooms, or [n] for 'next' ")
                if opt_3 == "look":
                    print("\n"
                        "JACKPOT! As you turn to the right just before your grandma\'s house, you find a L A R G E patch of porcinis.\n")
                    print(porcini)
                    print("Can I pick them before the wolf catches up with me?\n")
                    opt_2=input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                    if opt_2 == "pick":
                        print("You turn around to cautiously but there is no sign of the wolf around you.\n"
                            "You joyfully begin filling your basket, not realizing the wolf was hiding behind a tree.\n"
                            "You barely picked 3 mushrooms and the wolf is right next to you. You freeze in fear.\n"
                            "'What do I do???' you think in panic.")
                        opt_4 = input("Type 'fight' to fight the wolf, or [n] to run away")
                        if opt_4 == "fight":
                            print("\n"
                                "You realize you don\'t really have anything to fight with. \n"
                                "Apart from those few chantarelles.\n"
                                "You throw them at the wolf in desperation but it\'s not enough to stop it.")
                                
                            ############wolf attacks you################################
                        else:
                            print("\n"
                                "You run away as fast as possible. You reach your grandma\'s house, and show her the chantarelles.\n"
                                "'Thank you, dear' she says. 'But it\'s just not enough to make the soup. \n")
                            #############quest not compelted###############################
                    else:
                        print("\n"
                        "'Safety first' you decide. 'Better not to risk meeting the wolf'.\n"
                        "You reach your grandma\'s house, and show her the chantarelles.\n"
                        "'Thank you, dear' she says. 'But it\'s just not enough to make the soup.' \n")
                        ##############quest not completed########################
                else:
                    print("\n"
                        "There seems to be not enough mushrooms in the forest today.\n"
                        "'I give up' you sigh. 'I just want to see my grandma already'\n")
                        ##############quest not completed########################

                    #"You got to your grandma but you didn\'t bring any mushrooms\n"
                    #"The quest is not completed. You have to start over...")
                #break

            # You have magic mushrooms but no chantarelles
            elif room == 4 and mush1 == True and mush2 == False:
                print("\n"
                    "You are now on the straight way to your grandma and you have some mushrooms.\n"
                    "They are questionable, though.\n"
                    "Do you want to keep on looking or go to your grandma with what you have?\n")
                opt_3=input("Type 'look' to keep on looking for the mushrooms, or [n] for 'next' ")
                if opt_3 == "look":
                    print("\n"
                        "JACKPOT! As you turn to the right just before your grandma\'s house, you find a L A R G E patch of porcinis.\n")
                    print(porcini)      
                    print("Can I pick them before the wolf catches up with me? \n")
                    opt_2=input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                    if opt_2 == "pick":
                        print("You turn around to cautiously but there is no sign of the wolf around you.\n"
                            "'Maybe I missed on those chantarelles, but I bought myself some time' - you deduct.\n"
                            "You joyfully begin filling your basket, but there are just so many mushrooms!.\n"
                            "Do you keep on picking or move forward?.\n")
                        opt_2 = input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                        if opt_2 == "pick":
                            print("\n"
                                "You look around cautiously but there is no sign of the wolf around you.\n"
                                "You continue filling your basket, not realizing the wolf was hiding behind a tree.\n"
                                "You barely picked 3 more mushrooms and the wolf is right next to you. You freeze in fear.\n"
                                "'What do I do???' you think in panic.")
                            opt_4 = input("Type 'fight' to fight the wolf, or [n] to run away")
                            if opt_4 == 'fight':
                                print("\n"
                                    "You realize you don\'t really have anything to fight with. \n"
                                    "Apart from those weird mushrooms.\n"
                                    "You throw them at the wolf in desperation and to your surprise, the wolf stops and devours them."
                                    "Then it just lies in the grass, his eyes large, and looks in the sky. \n")
                                mush3 = True
                            else:
                                print("\n"
                                "You run away as fast as possible. You reach your grandma\'s house, and show her the mushrooms.\n"
                                "'Thank you, dear' she says. 'There\'s not enough porcinis to make the soup' - she says. \n"
                                "Should you use the unknown mushrooms?")
                                opt_5 = input("Type 'use' to make the soup, or 'no' to leave them")
                                if opt_5 == 'use':
                                    print("You decide to risk it and make the soup.")
                                #############grandma trips and dies###############################
                                else:
                                    print("Better not to risk it. It\'s your grandma\'s health on the line after all!")
    ################# quest not completed
                        else:
                            print("\n"
                                "You start moving towards your grandma\'s house. Better safe than sorry!.\n"
                                "'Thank you, dear' she says. 'There\'s not enough porcinis to make the soup' - she says. \n"
                                "Should you use the unknown mushrooms?")
                            opt_5 = input("Type 'use' to make the soup, or 'no' to leave them")
                            if opt_5 == 'use':
                                print("You decide to risk it and make the soup.")
                                #############grandma trips and dies###############################
                            else:
                                    print("Better not to risk it. It\'s your grandma\'s health on the line after all!")
    ################# quest not completed
                    else:
                        print("\n"
                        "'Safety first' you decide. 'Better not to risk meeting the wolf'.\n"
                        "You reach your grandma\'s house, and show her the weird mushrooms.\n"
                        "'Thank you, dear' she says. 'I don\'t know those, but let\'s make this soup! \n")
                            #############grandma trips and dies###############################
                else:
                    print("\n"
                        "I guess I have enough mushrooms.\n"
                        "You reach your grandma\'s house, and show her the weird mushrooms.\n"
                        "'Thank you, dear' she says. 'I don\'t know those, but let\'s make this soup! \n")
                            #############grandma trips and dies###############################

            # You have magic shrooms and chantarelles
            elif room == 4 and mush1 == True and mush2 == True:
                print("\n"
                    "You are now on the straight way to your grandma and you have some mushrooms.\n"
                    "Do you want to keep on looking or go to your grandma with what you have?\n")
                opt_3=input("Type 'look' to keep on looking for the mushrooms, or [n] for 'next' ")
                if opt_3 == "look":
                    print("\n"
                        "JACKPOT! As you turn to the right just before your grandma\'s house, you find a L A R G E patch of porcinis.\n")
                    print(porcini)
                    print("Can I pick them before the wolf catches up with me?\n")
                    opt_2=input("Type 'pick' to pick up the mushrooms, or [n] for 'next' ")
                    if opt_2 == "pick":
                        print("You turn around cautiously but there is no sign of the wolf.\n"
                            "You joyfully begin filling your basket, not realizing the wolf is hiding behind a tree.\n"
                            "You barely picked 3 mushrooms when you hear the wolf's growling. You freeze in fear.\n"
                            "'What do I do???' you think in panic.")
                        opt_4 = input("Type 'fight' to fight the wolf, or [n] to run away")
                        if opt_4 == "fight":
                            print("\n"
                                "You realize you don\'t really have anything to fight with. \n"
                                "Maybe apart from those weird mushrooms you picked.\n"
                                "You throw them at the wolf in desperation and to your surprise, the wolf stops and devours them."
                                "Then it just lies in the grass, his eyes large, and looks in the sky. \n")
                            mush3 = True
                            ############you pick the mushrooms and go to your grandma, you win ################################
                        else:
                            print("\n"
                                "You run away as fast as possible. You reach your grandma\'s house, and show the mushrooms you picked.\n"
                                "'Thank you, dear' she says. 'I don\'t know those, but we have to use all the mushrooms to get enough soup.\n")
                            #############grandma trips and dies###############################
                    else:
                        print("\n"
                        "'Safety first' you decide. 'Better not to risk meeting the wolf'.\n"
                        "You reach your grandma\'s house, and show her the mushrooms you picked.\n"
                        "'Thank you, dear' she says. 'I don\'t know those, but we have to use all the mushrooms to get enough soup.\n")
                            #############grandma trips and dies###############################
                else:
                    print("\n"
                        "I guess I have enough mushrooms.\n"
                        "You reach your grandma\'s house, and show her the mushrooms you picked.\n"
                        "'Thank you, dear' she says. 'I don\'t know those, but we have to use all the mushrooms to get enough soup.\n")
                            #############grandma trips and dies###############################

            elif room == 5 and mush3 == True:
                print("\n"
                    "You slowly finish picking the porcinis as the wolf is running back to the forst, clearly tripping.\n"
                    "You get to your grandma\'s house and show her proudly a full basket of beautiful mushrooms\n"
                    "'Thank you, dear!' she exclaims happily. 'These are amazing! Let\'s make a soup!'"
                    "Congratulations, you won the game!\n")
                break
            elif room == 5 and mush1 == True and mush3 == False:
                print("\n"
                    "You feed the soup to your grandma and chat about your adventure.\n"
                    "After a while your grandma starts acting weird, staring at her palms. \n"
                    "'Whoaaaaa... have you seen my hand?' she says, pupils large like coins.\n"
                    "'My veins are wriggling like a bunch of little worms!' \n"
                    "You freeze in realization of what you have done. \n"
                    "You failed your quest and now you must make sure your grandmother has a good trip.\n"
                    "You have to start over..")
                break
            #action = input("Press 's' to start. ").lower()
            #if action == 's' and room == 0:
                #room = 1
            #else:
                #input("Press 's' to start. ").lower()
            action = input("Type [n] for 'next' or [b] for 'back': ").lower()
            if action == "n" and room < 7 and room > 0:
                room += 1
            #elif action == "b" and room == 0:
                #print("\n"
                    #"You cannot go back from here. Please try again.")
                time.sleep(3)
            elif action == "b" and room > 0:
                room = 0
                print("\n"
                    "You go back and the wolf catches up with you.")
                time.sleep(2)
                print(wolf)
                time.sleep(2)
                print("You have to try again...")
                time.sleep(2)
                break
            #elif action == "pick" and room == 2 and not mush1:
                mush1 = True
                print("Your basket is full of mushrooms.")
            #else:
                print("You see a wolf behind you. There is no going back!")
        print("The game will restart now. \n")
        time.sleep(5)

                
    else:
        print("\nInvalid input. ")