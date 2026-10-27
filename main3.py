import random

def get_player_move():
    """Prompt the player to input their move and validate it."""
    while True:
        move = input("Enter your move (Rock, Paper, or Scissors): ").strip().capitalize()
        if move in ["Rock", "Paper", "Scissors"]:
            return move
        print("Invalid move. Please choose Rock, Paper, or Scissors.")

def get_ai_move():
    """AI randomly selects between Rock, Paper, and Scissors."""
    moves = ["Rock", "Paper", "Scissors"]
    return random.choice(moves)

def determine_winner(player_move, ai_move):
    """Determine the winner based on traditional RPS rules."""
    if player_move == ai_move:
        return "tie"
    elif (
        (player_move == "Rock" and ai_move == "Scissors") or
        (player_move == "Scissors" and ai_move == "Paper") or
        (player_move == "Paper" and ai_move == "Rock")
    ):
        return "player"
    else:
        return "ai"

def play_game():
    """Main game loop managing multiple rounds and scores."""
    player_score = 0
    ai_score = 0
    
    print("=== Welcome to Rock, Paper, Scissors with AI! ===")
    
    while True:
        player_move = get_player_move()
        ai_move = get_ai_move()
        
        print(f"\nYou chose: {player_move}")
        print(f"AI chose: {ai_move}")
        
        winner = determine_winner(player_move, ai_move)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("AI wins this round!")
            ai_score += 1
            
        print(f"\nScore -> You: {player_score} | AI: {ai_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing!")
            print(f"Final Score -> You: {player_score} | AI: {ai_score}")
            break

if __name__ == "__main__":
    play_game()