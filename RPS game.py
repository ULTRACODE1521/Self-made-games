import random

r_p_s = ["rock", "paper", "scissors"]

print("Rock Paper Scissors SHOOT!")
user_input = ""

while user_input.lower() != "stop":
    x = random.choice(r_p_s)
    user_input = input("> ")
    user_input = user_input.lower()

    if user_input == r_p_s[0] or user_input == r_p_s[1] or user_input == r_p_s[2]:
        # TIE
        if user_input == x:
            print(x.title())
            print("TIE!!!")

        # WIN
        elif user_input == "rock" and x == "scissors":
            print(x.title())
            print("YOU WIN!!!")
        elif user_input == "paper" and x == "rock":
            print(x.title())
            print("YOU WIN!!!")
        elif user_input == "scissors" and x == "paper":
            print(x.title())
            print("YOU WIN!!!")

        # LOSE
        else:
            print(x.title())
            print("YOU LOSE!!!")
    else:
        print("Please Try Again!")
