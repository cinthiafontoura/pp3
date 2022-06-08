import random

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


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




def choose_move():
    """
    Ask to the player choose between rock, paper, and scissors by enter a number. 
    Create a random move to the computer.
    """
    user_move = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    computer_move = random.randint(0,2)

    return user_move, computer_move


def check_round_winner():
    """
    Check if the player win, lose or draw and add points to the game
    """
    user_points = 0
    computer_points = 0
    result = ""

    if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        result = "You WIN! =D\n"  
        user_points += 100   
    elif user_choice == computer_choice:
        result = "It's a DRAW\n"
        user_points += 0
        computer_points += 0
    elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        result = "You LOSE. =(\n"
        computer_points += 100
    else:
        result = "Something went wrong.\n"   

    return user_points, computer_points, result

def print_moves(player,choice):
    """
    Print the moves choices to the game
    """
    game_images = [rock, paper, scissors]
    print(f"\n{player} choose:")
    print(game_images[choice])


    
game_round = 1
user_score = 0
computer_score = 0 

while game_round <= 4:
    if game_round <= 3:
        
        moves = choose_move()
        print(f"\nROUND: {game_round}")

        user_choice = int(moves[0])        
        print_moves("YOU",user_choice)
        computer_choice = moves[1]
        print_moves("COMPUTER",computer_choice)  

        print(check_round_winner()[2])
        user_score += check_round_winner()[0]
        computer_score += check_round_winner()[1] 

        print(f"YOU {user_score} x {computer_score} COMPUTER\n")                                                
        game_round += 1
    
    elif game_round > 3:
        game_round += 1
        print("the end")


            