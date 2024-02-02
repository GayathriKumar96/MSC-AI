'''
    Author: Marek Grzes, University of Kent
    Date created: 23/12/2022
    Date last modified:
    Python Version: 3.10
'''

import sys
import getopt
import random

# config variables
pile_size = 10
whose_turn = "computer" # computer or human
opponent = "random"     # random or expert or learning


def expert_move(n):
    '''
    :param n: state
    :return: action (not action id)
    '''
    # TODO: implement your expert move here
    return random.randint(1,2)


def who_is_first():
    if random.choice([True, False]) is True:
        return "computer"
    else:
        return "human"


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hg:o:", ["help", "goes-first=", "opponent="])
    for opt, arg in opts:
        if opt == '-h':
            print(sys.argv[0] + ' --goes-first [human|computer] --opponent [random|expert]')
            sys.exit(0)
        elif opt in ("-g", "--goes-first"):
            whose_turn = arg
        elif opt in ("-o", "--opponent"):
            opponent = arg

    episode = 0
    while True:
        if episode > 0:
            # after one episode, we randomise who goes first
            whose_turn = who_is_first()
        print("New game no {} starts. {} plays first. The opponent is {}.".format(episode+1, whose_turn, opponent))
        curr_pile_size = pile_size
        while True:
            print("-" * 20)
            print("Current pile has " + str(curr_pile_size) + " stones: " + "*" * curr_pile_size)
            if whose_turn == "human":
                move = -1
                if curr_pile_size == 1:
                    print("Only action 1 is possible.")
                    move = 1
                    input("Please press ENTER:\n")
                else:
                    while not move == 1 and not move == 2:
                        move = int(input("Please enter 1 or 2 and press ENTER:\n"))
                print("The {} player moves next and removes {}.".format(whose_turn, move))
                curr_pile_size -= move
                if curr_pile_size == 0:
                    print("You won!")
                    break
            else:
                move = -1
                if opponent == "random":
                    move = random.randint(1, 2)
                    if curr_pile_size == 1:
                        move = 1
                elif opponent == "expert":
                    move = expert_move(curr_pile_size)
                    if curr_pile_size == 1:
                        move = 1
                else:
                    print("Wrong opponent. See the --opponent parameter.")
                    sys.exit(1)
                if (curr_pile_size == 1 and move != 1) or (move != 1 and move != 2):
                    print("Wrong action.")
                    sys.exit(1)
                print("The {} player moves next and removes {}.".format(whose_turn, move))
                curr_pile_size -= move
                if curr_pile_size == 0:
                    print("The {} player won!".format(opponent))
                    break
            if whose_turn == "human":
                whose_turn = "computer"
            else:
                whose_turn = "human"
        again = input("Play again y/n and press ENTER:\n")
        if again == "n":
            break
        episode += 1
