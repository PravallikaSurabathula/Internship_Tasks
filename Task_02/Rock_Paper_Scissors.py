from random import choice

done = False
all_choices = ["rock", "paper", "scissors"]
CPU_score = 0
user_score = 0

#game looprrrrr
while not done:
    choice_made = None

    #generate random choice for bot
    CPU_choice = choice(all_choices)

    #ask user for user's choice
    user_input = input("\nEnter 1 for Rock, 2 for Paper, or 3 for Scissor. Enter x to quit: ")

    #validate user's input
    if user_input == "1":
        user_choice = "rock"
        choice_made = "valid"
    elif user_input == "2":
        user_choice = "paper"
        choice_made = "valid"
    elif user_input == "3":
        user_choice = "scissors"
        choice_made = "valid"
    elif user_input == "x":
        choice_made = "quit"
    else:
        print("Invalid input. Try again!!!")

    #11rrrrif user input is valid, compare
    if choice_made == "valid":
        print(f"Machine selects \'{CPU_choice}\', user selects \'{user_choice}\'")

        if user_choice == CPU_choice:
            print("Its a tie !!!")
        else:
            if user_choice == "rock":
                if CPU_choice == "paper":
                    print("Machine wins!!!")
                    CPU_score += 1
                else:
                    print("You win!!!")
                    user_score += 1
            if user_choice == "paper":
                if CPU_choice == "scissors":
                    print("Machine wins!!!")
                    CPU_score += 1
                else:
                    print("You win!!!")
                    user_score += 1
            if user_choice == "scissors":
                if CPU_choice == "rock":
                    print("Machine wins!!!")
                    CPU_score += 1
                else:
                    print("You win!!!")
                    user_score += 1
        print(f"Current Score: \tMachine = {CPU_score}, User = {user_score}")

    #if user input is to quit, end program
    elif choice_made == "quit":
        print("Thanks for playing")
        print(f"Final Score: Machine = {CPU_score}, User = {user_score}")
        done = True
