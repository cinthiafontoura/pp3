import random

print("""                  WELCOME TO THE ROCK PAPER SCISSORS GAME!
    _______                 
---'   ____)            This game is played by children and adults and is
      (_____)       popular all over the world. Apart from being a game played
      (_____)       to pass time, the game is usually played in situations
      (____)        where something has to be chosen. It is similar in that way
---.__(___)         to other games like flipping the coin, throwing dice or 
                    drawing straws. There is no room for cheating or for
    _______         knowing what the other person is going to do so the results
---'   ____)____    are usually very satisfying with no room for fighting or 
          ______)   error. 
          _______)                         
         _______)                           RULES
---.__________)     
                    * Rock wins against scissors. 
    _______         * Scissors win against paper.
---'   ____)____    * Paper wins against rock.    
          ______)        
       __________)      The rock will beat scissors every time but will be
      (____)        beaten by paper. Paper will beat rock but will be beaten by
---.__(___)         scissors in no time.      

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

game_images = [rock, paper, scissors]

def choose_move():
    """
    Ask to the player choose between rock, paper, and scissors by enter a number. 
    Create a random move to the computer.
    """
    user_move = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    computer_move = random.randint(0,2)

    return user_move, computer_move

moves = choose_move()
print(moves)
print(f"YOU choose: {moves[0]}")
print(f"The COMPUTER choose: {moves[1]}")