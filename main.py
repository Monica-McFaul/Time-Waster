print(
    "(Please use the same capitilisation as the option when typing answers.) Welcome to The Critical Roll! You are Skout Mognr, the strongest fighter in the Scorched Fields and bravest barbarian of your clan, jaded by years of experience you find yourself wandering through the woods when, upon this fine morning, you see a wolf digging through your belongings!"
)
Str = 5
Profbonus = 2
SkoutHP = 25
SkoutAC = 15

WolfAC = 12
WolfHP = 11
Wolfbonus = 4
Bitedmg = 7 + Wolfbonus
import random
roll = random.randint(0, 21)
roll2 = random.randint(1, 21)
Wolfhit = roll2
Tohit = roll + Str + Profbonus

player = (input(
    "How do you want to do this: Attack it?(Attack) or Leave it alone?(Leave) "
))

if player == "Leave":
    print("The wolf stole two days of food! Oh no! END")

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

if dmg > WolfHP:
    print(
        "With a yelp, the wolf falls slain at your feet! You are victorious! Your food is safe... For now. END"
    )

if Bitedmg > SkoutHP:
    print(
        "Though you fought bravely, the Wolf has claimed victory and now ownes your food... END"
    )
