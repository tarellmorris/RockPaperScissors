from random import randint

options = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}


def cpu_move():
    cpu_rand = randint(1, 3)
    return cpu_rand


def player_move():
    player = input("Choose a move: ('ROCK', 'PAPER', or 'SCISSORS'): ")
 #   if player.upper() != 'ROCK' or player.upper() != 'PAPER' or player.upper() != 'SCISSORS':
 #       print("Syntax error. Please re-enter your move; either 'ROCK', 'PAPER', or 'SCISSORS'...")
 #       player_move()
 #   else:
    return player.upper()


def results(cpu, player):
    while player == 'ROCK':
        if cpu == 2:
            return 'You lose!'
        elif cpu == 3:
            return 'You win!'
        else:
            return 'Draw!'
    while player == 'PAPER':
        if cpu == 3:
            return 'You lose!'
        elif cpu == 1:
            return 'You win!'
        else:
            return 'Draw!'
    while player == 'SCISSORS':
        if cpu == 1:
            return 'You lose!'
        elif cpu == 2:
            return 'You win!'
        else:
            return 'Draw!'


def main():
    print("This game will be played best two out of three.")
    match = 1
    cpu_tally = 0
    player_tally = 0
    while cpu_tally != 2 and player_tally != 2:
        print("Round {}...".format(match))
        player = player_move()
        cpu = cpu_move()
        print("CPU chose {}!".format(options[cpu]))
        score = results(cpu, player)
        if score == 'You win!':
            print('You win!')
            match += 1
            player_tally += 1
        elif score == 'You lose!':
            print('You lose!')
            match += 1
            cpu_tally += 1
        else:
            print('Draw!')
            match += 1
    if cpu_tally == 2:
        print("Oh no! You lose!")
    if player_tally == 2:
        print("Congratulations! You win!")


def play_again():
    confirm = input("Would you like to play again?: ('YES' or 'NO') ")
    if confirm.upper() == 'YES':
        main()
    else:
        SystemExit()


print("Are you ready to play Rock Paper Scissors?")
confirm = input("Enter 'YES' to continue or 'NO' to exit program: ")
if confirm.upper() == 'YES':
    main()
else:
    SystemExit()

play_again()

