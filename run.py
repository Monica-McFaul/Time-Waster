#Kahlil
player = (input(
    "(Type Kahlil's name again, this is just Python going to another file)."))
if player == "Kahlil":
    print(
        "You are Kahlil Siannodel, academic prodigy in all things Arcane and victim of memory loss, you seek your past through adventures into the great unknown. Though weak in physical Intength, you are Intong in ways of magic. This morning, however, you seem to have found yourself in a predicament... A wolf is digging through your bellongings! This wolf is not your familliar, it is wild. "
    )
Int = 5
SpellAtkBonus = 2
KahlilHP = 10
KahlilAC = 12

WolfAC = 12
WolfHP = 11
Wolfbonus = 4
Bitedmg = 7 + Wolfbonus
import random
roll = random.randint(0, 21)
roll2 = random.randint(1, 21)
Wolfhit = roll2
Total = roll + Int + SpellAtkBonus

choice = input(
  "How do you want to do this? Run away (Run) or try to cast a Spell? (Spell)")
  
if choice == "Spell":
  print("You attemted to cast the Spell 'Magic Missile' but it Missed the Wolf and blew up in your face! Literaly! END")


    
if choice == "Run":
    print(
        "You begin to sprint away from the wolf, it does not seem to notice you, though, it has taken something from your bag and is rushing away from your camp!"
    )
    choice = input("Do you follow it? Yes or No?")

if choice == "No":
    print(
        "You wait for the wolf to leave the area. Eventually you come back to camp and find that the wolf stole your spellbook! you have no way of tracking it down now... Aw man, now you need a new spellbook... END"
    )

if choice == "Yes":
    print(
        "You try to follow the wolf from a distance, eventually you find yourself in a large, cavernous cave. It is empty, aside from the one wolf, a small pile of things and a large throne-looking Intucture made of bones. Human, animal, and everything inbetween."
    )
    choice = input(
        "You seem to have a few options here, do you Attack the wolf with a spell?(Spell) Sift through the Pile of things to try and find your spellbook?(Search) or check out the throne?(Throne)"
    )

if choice == "Throne":
  print(
  "You see before you a tall hill of bones, utop that hill sits a Throne of bones. The seat is meant for something bigger than anything you've ever seen. But near the throne there is a small chest, inside are numerous bobouls and trinkets but there is a picture of yourself and someone else you have never seen before. Could this be a clue to your past...? END."
    )

if choice == "Search":
    print("Roll an Investigation check")
    player = input("Type Roll Investigation")

if player == "Roll Investigation":
  import random
  roll = random.randint(0, 21)
total = roll + Int
print("You rolled a", roll," and with your Investigation modifier of(And Proficiency)", Int," your total is", total,)

if total > 15:
  print(
   "As quiet as you can be, you rush over to the pile and begin to sift through it, after a moment, you find it! Your spellbook is now in your possession once again! END."
    )
else:
  print(
   "You search and search for your spellbook, but nothing turns up... Aw man, now you need a new spellbook... END."
    )

if choice == "Spell":
    print("Roll a Spell Attack")
    player = input("(Type Roll Spell Attack)")

if player == "Roll Spell Attack":
    import random
    roll = random.randint(0, 21)
    Total = roll + SpellAtkBonus
#Hit confirmation
if Total > WolfAC:
    print("You rolled a", roll, " with your modifier of", SpellAtkBonus,
          ", that's a", Total, " to hit.")
    print("You hit! Roll damage!")
player = (input("(Type Roll damage) "))

if Total < WolfAC:
    print("You try to cast 'Burning Hands' but it missed!")

#Skout damage roll
if player == "Roll damage":
    import random
    roll = random.randint(0, 13)
    dmg = roll + Int + SpellAtkBonus
    print("You Rolled a", roll, " with your modifier of", Int,
          "and proficiency of", SpellAtkBonus, ", that's a total of", dmg,
          " points of damage! Now the Wolf's turn...")
import random
roll2 = random.randint(1, 21)
Wolfhit = roll2 + Wolfbonus
print("The Wolf rolled a", roll2, " with its modifier of", Wolfbonus,
      "that's a", Wolfhit, " to hit.")

if Wolfhit > KahlilAC:
  print("The Wolf hit! you take", Bitedmg, "points of damage. Your turn!")
  (input("(Type Roll Spell Attack) "))

#Wolf miss
if Wolfhit < KahlilAC:
  print("The Wolf missed! Your turn!")
  (input("(Type Roll Spell Attack) "))

#Player turn
if player == "Roll Spell Attack":
  import random
  roll = random.randint(0, 21)
  Total = roll + Int + SpellAtkBonus

#Hit confirmation
if Total > WolfAC:
    print("You rolled a", roll, " with your modifier of", Int,
          "and proficiency of", SpellAtkBonus, ", that's a", Total, " to hit.")
    print("You hit! Roll damage!")
player = (input("(Type Roll damage) "))

#Skout damage roll
if player == "Roll damage":
    import random
    roll = random.randint(0, 13)
    dmg = roll + Int + SpellAtkBonus
    print("You Rolled a", roll, " with your modifier of", Int,
          " that's a total of", dmg,
          " points of damage! Now the Wolf's turn...")

if dmg > WolfHP:
  print(
  "The Wolf, injured by your Spell, yelps and drops your spellbook! You have your spellbook again! Hoorah! END"
  )

