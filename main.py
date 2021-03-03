print(
    "(Please use the same capitilisation as the option when typing answers.) Welcome to The Critical Roll!"
)
player = (input("Choose one between (First name only).                                             Skout the Barbarin, Kahlil the Wizard or Quebellios the Rogue Theif"   
 ))

if player == "Skout":
  print(
 "You are Skout, the strongest fighter in the Scorched Fields and bravest barbarian of the Mognr clan. After leaving to find and slay a great beast, you find yourself wandering through the woods when, upon this fine morning, you see a wolf digging through your belongings!"
  )
Str = 5
Profbonus = 2
SkoutHP = 15
SkoutAC = 15

if player == "Kahlil":
    print(
        "You are Kahlil Siannodel, academic prodigy in all things Arcane and victim of memory loss, you seek your past through adventures into the great unknown. Though weak in physical strength, you are strong in ways of magic. This morning, however, you seem to have found yourself in a predicament... A wolf is digging through your bellongings! This wolf is not your familliar, it is wild. "
)
Int = 3
Profbonus = 2
KahlilHP = 10
KahlilAC = 12

if player == "Quebellios":
    print("You are Quebellios the Rogue Thief, raised on the streets and known nothing but criminality, you seek your fortune through mischevious means. Through any means. For the last few weeks you have been camping outside one of the kingdoms, plotting your next move when, a loud russeling behind you tells your trained ears that you are not alone... Someone... or Something... is going through your pack. A wolf! It seems to be hungry.")

Dex = 4
Snk = 5
QueHP = 13
QueAc = 14

WolfAC = 12
WolfHP = 11
Wolfbonus = 4
Bitedmg = 7 + Wolfbonus
import random
roll = random.randint(0, 21)
roll2 = random.randint(1, 21)
Wolfhit = roll2
Tohit = roll + Str + Profbonus

if player == "Skout":
  choice = input("How do you want to do this? Attack it?(Attack) or Leave it alone?(Leave) " )

if choice == "Attack":
  print("Roll an Attack!")
  (input("(Type Roll Attack) "))

if choice == "Leave":
  print("The wolf stole two days of food! Oh no!")
  input("Do you chase after it? Yes or No? " )

if choice == "No":
   print ("You may have lost two days of food but at least you still have your toothbrush. For now... END")

if choice == "Yes":
 print("You begin to run after the wolf.")     
 player = (input ("Roll an Athletics check to see if you can catch up to it!(Type Roll Athletics) " ))

if player == "Roll Athletics":
   import random
   roll = random.randint(0, 21)
total = roll + Str
print ("You rolled a", roll," and with your Strength mod of", Str," your total is", total,)

if total > 15:
  print("You caught up to the wolf!")
else: print ("You tripped over a stone and fell face-first into the mud! The wolf got away... END")

choice = input("Do you continue to Run with the wolf (Run) or do you Attack it? (Attack)")

if choice == "Run":
  print ("You continue to keep pace with the wolf, eventually following it back to the mouth of a cave. Inside, stalactites and stalagmites line the ceiling and floors. A musty smell fills the room and you watch as the wolf brings your food to the foot of a throne. This throne is made of bones, some human, some animal, some unrecognisable; but utop this throne sits a wicked beast of matted fur, lanky limbs and a crown of brittle and petrified sprigs. The beast steps down and greets you with a bony hand- 'You seem to be uninvited company' he says. 'All are welcome in the presence of The Wolf King... But now that you have witnessed this gathering, you may not leave alive...!' He jumps down from the throne and leaps toward you with a great howl.")

if player == "Attack":
  print("Roll an Attack!")
  (input("(Type Roll Attack) "))

#Player turn
if player == "Roll Attack":
    import random
    roll = random.randint(0, 21)
    Tohit = roll + Str + Profbonus

  #Hit confirmation
if Tohit > WolfAC:
  print("You rolled a", roll, " with your modifier of", Str,
   "and proficiency of", Profbonus, ", that's a", Tohit, " to hit.")
  print("You hit! Roll damage!")
player = (input("(Type Roll damage) "))

#Skout damage roll
if player == "Roll damage":
    import random
    roll = random.randint(0, 13)
    dmg = roll + Str + Profbonus
    print("You Rolled a", roll, " with your modifier of", Str,
          "and proficiency of", Profbonus, ", that's a total of", dmg,
          " points of damage! Now the Wolf's turn...")

#Wolf turn
if Tohit < WolfAC:
    print("You missed! Now it's the Wolf's turn...")
    import random
    roll2 = random.randint(1, 21)
    Wolfhit = roll2 + Wolfbonus
    print("The Wolf rolled a", roll2, " with its modifier of", Wolfbonus,
          "that's a", Wolfhit, " to hit.")

if Wolfhit > SkoutAC:
    print("The Wolf hit! you take", Bitedmg, "points of damage. Your turn!")
    (input("(Type Roll Attack) "))

#Wolf miss
if Wolfhit < SkoutAC:
    print("The Wolf missed! Your turn!")
    (input("(Type Roll Attack) "))

#Player turn
if player == "Roll Attack":
    import random
    roll = random.randint(0, 21)
    Tohit = roll + Str + Profbonus

  #Hit confirmation
if Tohit > WolfAC:
  print("You rolled a", roll, " with your modifier of", Str,
   "and proficiency of", Profbonus, ", that's a", Tohit, " to hit.")
  print("You hit! Roll damage!")
player = (input("(Type Roll damage) "))

#Skout damage roll
if player == "Roll damage":
    import random
    roll = random.randint(0, 13)
    dmg = roll + Str + Profbonus
    print("You Rolled a", roll, " with your modifier of", Str,
          "and proficiency of", Profbonus, ", that's a total of", dmg,
          " points of damage! Now the Wolf's turn...")

if dmg > WolfHP:
    print(
        "With a yelp, The Great Wolf falls slain at your feet! You are victorious! The other wolves scatter at the sight and your food is safe... For now. END"
    )

if Bitedmg > SkoutHP:
    print(
        "Though you fought bravely, the Wolf has claimed victory and now ownes your food... END"
    )
