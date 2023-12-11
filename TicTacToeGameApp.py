from TicTacToeClass import TicTacToe
import random

def player_selection(player_name):
    print(f"{player_name} Selection:")
    print("1. Random Player")
    print("2. MiniMax Player")
    print("3. Alpha Beta Player")
    print("4. Heuristic Alpha Beta Player")
    print("5. MCTS Player")
    print("6. Query Player")

    while True:
        try:
            choice = int(input(f"Please enter {player_name}'s strategy (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_player_move(player, strategy, game):
    if strategy == 1:  # Random Player
        return game.random_player()
    elif strategy == 2:  # MiniMax Player
        return game.minimax_decision(player)
    elif strategy == 3 or strategy == 4:  # Alpha Beta Players
        return game.minimax_decision(player)  # Use minimax_decision for Alpha Beta
    elif strategy == 5:  # MCTS Player
        return game.mcts_player(player)
    elif strategy == 6:  # Query Player
        print("Available Action by the Player X:", game.get_available_moves())
        print("\n")
        print("Enter your move (row, column):")
        while True:
            try:
                move = tuple(map(int, input().split(',')))
                if move in game.get_available_moves():
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid row and column numbers separated by a comma.")
    else:
        return None  # Invalid strategy
    
def display_board(game):
    game.display_board()

def display_available_actions(game, player):
    available_moves = game.get_available_moves()
    print(f"Available Action by the Player {player}: {available_moves}")

def main():
    while True:
        player_x = player_selection('Player X')
        player_o = player_selection('Player O')

        game = TicTacToe()

        for round_num in range(1, 4):
            print()
            display_available_actions(game, 'X')
            display_board(game)

            while not game.is_board_full() and not game.check_winner():
                if round_num % 2 == 1:  # Player X's turn
                    move = get_player_move('X', player_x, game)
                    player = 'X'
                else:  # Player O's turn
                    move = get_player_move('O', player_o, game)
                    player = 'O'

                if game.make_move(player, move):
                    print(f"The Action by {player} Is {move}")
                    display_board(game)
                else:
                    print("Invalid move. Try again.")

            winner = game.check_winner()
            if winner:
                print(f"{player} won the game in Round {round_num}")
            else:
                print(f"{player_x} and {player_o} drew the game in Round {round_num}")

        play_again = input("Would you like to play the game again? (Yes/No): ").lower()
        if play_again != 'yes':
            print("Thank You for Playing Our Game.")
            break

if __name__ == "__main__":
    main()
