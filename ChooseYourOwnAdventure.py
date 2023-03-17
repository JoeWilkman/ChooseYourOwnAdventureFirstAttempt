name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt path in the forrest when it suddenly stops and comes to a fork in the road. You can go left or you can go right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. Type walk to walk around it or swim to swim accross it: ")

    if answer == "swim":
        print("You attempted to swim accross the river and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked around the river for many miles. You eventually ran out of water and dehydrated and died. You lose the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge and it looks a bit wobbly. Do you want to cross it or do you want to head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and they give you some gold. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and they get highly offended and you lose the game.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name + "!")