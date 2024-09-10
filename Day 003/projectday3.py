# Project: Treasure Island - Day 3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island.")
print("Will you be able to find the treasure?")
choice1 = input ("You find yourself on a deserted beach.\nThe sound of the waves crashing fills the air.\nBefore you, two paths lie ahead: one to the left and one to the right. ").lower()

if choice1 =="left":
    choice2 = input("You follow the right path, which leads you to a quiet lake.\nYou can see something glimmering on the other side, but the water is full of movement.\nWill you wait or try to swim? ").lower()
    if choice2 =="wait":
        print("You wait patiently, and after a while, the movement in the water subsides.\nThe fish seem to have moved on, and the water is calm.\nYou can now swim safely across.")
        choice3 = input("Once across, you find a mysterious door in the rocks.\nYou need to choose a door.\nWhich one will you choose? The red, blue or yellow door? ").lower()
        if choice3 == "yellow":
            print("You open the yellow door, and to your surprise, the treasure is right there!\nYou've found the hidden fortune of Treasure Island!")
        elif choice3 == "blue":
            print("You open the blue door and step inside, but the air is thick with the smell of smoke.\nBefore you can react, flames erupt all around you!")
        else:
            print("You open the red door, only to be met by a pack of wild beasts.\nThey snarl and leap at you before you can escape.\nGame Over!")
    else:
        print("You dive into the water and start swimming toward the glimmering object.\nSuddenly, you feel something tugging at your legs—it's a school of hungry trout!\nYou try to fight them off, but it's too late.\nGame Over!")

else:
   print("You walk down the left path, but after a few minutes, the ground gives way beneath you!\nYou fall into a deep hole, and there's no way out. You are trapped.\nGame Over!")