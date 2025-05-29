from Randoms_generator import LCG_algo

user_option = {3: "GUN",2: "WATER",1: "SNAKE", 0:"EXIT"}
computer_option = {1: "GUN",2: "WATER",3: "SNAKE"}
i = 0
j=0
while True:
    random_list = LCG_algo(j+1)
    random_list[j]
    user_input = int(input("Enter your choice press \n 1.) Snake \n 2.) Water \n 3.) Gun \n and press 0 for exit"))
    if user_input in user_option:
        computer_choice= random_list[j] + 1
        j = j +1
        print("valid option")
        if user_input == 0:
            print("Thanks for Playing, we will meet next time")
            break
        elif user_input + computer_choice == 4:
            print(user_input,computer_choice)
            print(f"wow what a incident Both chooses the same option {user_input}")
        elif  user_input + computer_choice in [2,5]:
            print(f"computer Choice is {computer_option[computer_choice]} and your is {user_option[user_input]}, Computer have more luck !!!!!!!")
            print(user_input,computer_choice)
        elif user_input + computer_choice in [3,6]:
            print(f"computer Choice is {computer_option[computer_choice]} and your is {user_option[user_input]}  Computer are defeat here !!!!!!!")
            print(user_input,computer_choice)

    else:
        print("Please press A,B,C or a,b,c other will not acceptable")
        # continue
        if i == 3:
            print("You reached maximum limit, please run you program again")
            break
        i += 1