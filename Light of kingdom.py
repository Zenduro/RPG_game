print("Welcome to Light of Kingdoms")

choice1 = input("you se a pathway that goes right and left, the left one has a light shining while the right path is dark, what do you chose to go?")
if choice1 == "right":
    choice2 = input("you choose the right path! Now you are at a bridge, Do you wish to go on the bridge or under?")
    if choice2 == "go on the bridge":
        choice3 = input("You see a strange man standing in the middle of the room, do you talk to him or ignore him?")
        if choice3 == "ignore him":
            choice4 = input("You come up to a Sword, Do you pick it up or leave it?")
            if choice4 == "pick it up":
             choice5 = input("Your sword talks to you, it ask if you wish to have the power of, Arcane or Fire or Shadow or Frost, the choice is your.")
             if choice5 == "Arcane":
              print("The Power Of Arcane is in your hands.")
             elif choice5 == "Fire":
              print("The Power Of Fire burns in your hands")
             elif choice5 == "Shadow":
              print("The Power of the Shadows comes trough your hands")
             elif choice5 == "Frost":
              print("The Power Of the Ice cold Frost is in your hands")
              choice6 = input("You come with your sword to a huge hallway, you se at the end a creture, you can´t really se what it is. Do you charge against it and fight or go other way?")
              if choice6 == "Charge against it":
               choice7 = input("You run like the wind and you start to se what the creture is, ITS A HUGE DRAGON! Do you wish to stand and fight or turn back?")
               if choice7 == "Stand and fight":
                 choice8 = input("You stand and fight the dragon with you holy sword, you use your swords power to defeat the beast! The dragon go down and you have a final choice Spare him or kill him? ")
                 if choice8 == "Spare him":
                    choice9 = input("The dragon goes up again while you stand there, the dragon is glad that you didnt kill him. The dragon gets away from the door and it whiches you to go in there as a good thing that you spared him, do you go in or not? ")
                    if choice9 == "Go in":
                       choice10 = input("Inside the room is alot of gold and jewelry, you pick up a lot of gold and jewelry and head out. The dragon goes back to sleep and you continue with you journey back to town.")
               
                    else: 
                     print("Why would you leave the treasure after all you have gone trough?")
                 else:
                  print("Blood thirsty huh? Go back and spare him trust me it´s better.")
              else:
               print("Game Over! The dragon killed you fucking pussy.")
             else:
              print("Game over, Why would you leave it?")
            else:
             print("Game Over! You are really boring, you got a sword to fight")
        else:
          print("Game over")
    else:
      print("Game Over")
else:
  print("Game Over")