from game import Game

def main():
    game = Game()
    while game.playable:
        card_index = get_played_card_index(game)
        print()
        game.play(card_index)
    print("\n\n\n")
    print("Game over!")
    print(f"Total games played: {game.total_played}")
    print(f"Player wins: {game.player_wins}")

def get_played_card_index(game:Game)->int:
    print("Your cards:", game.player_hand)
    print()
    while( (val := int(input("Choose a card to play: ")) > len(game.player_hand)) or val < 0 ):
        print("Invalid card index. Please try again.")
        print()
        print("Your cards:", game.player_hand)
        
    return val

if __name__ == "__main__":
    main()