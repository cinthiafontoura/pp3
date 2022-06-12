import random
import time

print("""                    WELCOME TO THE ROCK PAPER SCISSORS GAME!
    _______                 
---'   ____)            This game is played by children and adults and is
      (_____)       popular all over the world. Apart from being a game played
      (_____)       to pass time, the game is usually played in situations
      (____)        where something has to be chosen. It is similar in that way
---.__(___)         to other games like flipping the coin, throwing dice or
                    drawing straws. There is no room for cheating or for
    _______         knowing what the other person is going to do so the results
---'   ____)____    are usually very satisfying with no room for fighting or
          ______)   error. WIN the best of the 3 rounds!
          _______)                         
         _______)                           RULES
---.__________)     * Rock wins against scissors.
                    * Scissors win against paper.
    _______         * Paper wins against rock.
---'   ____)____        
          ______)       The rock will beat scissors every time but will be
       __________)  beaten by paper. Paper will beat rock but will be beaten by
      (____)        scissors in no time.
---.__(___)         
""")  


def choose_move():
    """
    Ask to the player choose between rock, paper, and scissors.
    """
    return input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")


def validate_user_move():
    """
    Check if the user enter the correct input and print a feedback.
    """
    valid_enter = False
    while valid_enter != True:
        user_enter = choose_move()
        if user_enter.isdigit():
            if int(user_enter) >= 0 and int(user_enter) <= 2:
                valid_enter = True              
            else:
                print(f"Ops! Wrong choice. You typed: {user_enter}.\n")                
                continue
        else:
            print(f"You should enter a number.  You typed: {user_enter}.\n")
            continue              
    return int(user_enter)    


def check_round_winner():
    """
    Check if the player win, lose or draw and add points to the game
    """
    user_points = 0
    computer_points = 0
    if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        user_points += 100            
    elif user_choice == computer_choice:
        user_points += 0
        computer_points += 0
    elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        computer_points += 100
    else:
        print("Something went wrong.\n")
    return user_points, computer_points


def print_moves(player, choice):
    """
    Print the moves choices to the game
    """
    game_images = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
    print(f"{player} choose:")
    print(game_images[choice])


def check_game_winner():
    """
    Check who win the game after the third round.
    """
    if user_score > computer_score:
        return """                             _______________
                            |####|     |####|
                            |####|     |####|
                            |####|     |####|
                            \####|     |####/
                             \###|     |###/
                              `##|_____|##'
                                   (O)
                                .-'''''-.
                              .'  * * *  `.
                             :  *       *  :
                            :  *  Y O U  *  :
                            :  *  W I N   * :
                             :  *       *  :
                              `.  * * *  .'
                                `-.....-'
        """
    elif user_score < computer_score:
        return """




    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
   ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
   ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
   ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
   ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝




                                                                        
        """    

    else:
        return """




                 _                    _                           
                | |__  _ __ ___  __ _| | __   _____   _____ _ __  
                | '_ \| '__/ _ \/ _` | |/ /  / _ \ \ / / _ \ '_ \ 
                | |_) | | |  __/ (_| |   <  |  __/\ V /  __/ | | |
                |_.__/|_|  \___|\__,_|_|\_\  \___| \_/ \___|_| |_|






        """ 
    print('To play again hit the "RUN PROGRAM" button')


game_round = 1
user_score = 0
computer_score = 0
while game_round <= 4:
    if game_round <= 3:
        user_move = validate_user_move()        
        computer_move = random.randint(0, 2)
        print(f"ROUND: {game_round}\n")
        user_choice = user_move
        computer_choice = computer_move
        print_moves("YOU", user_choice)        
        print_moves("COMPUTER", computer_choice)
        check_round_winner()
        user_score += check_round_winner()[0]
        computer_score += check_round_winner()[1]
        print(f"YOU {user_score} x {computer_score} COMPUTER\n")
        game_round += 1
    elif game_round > 3:
        game_round += 1
        time.sleep(1.3)
        print(check_game_winner())
        print('\nTo play again click on the "RUN PROGRAM" button.\n')

        