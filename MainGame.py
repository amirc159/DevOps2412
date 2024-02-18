# MainGame.py

from Live import load_game, welcome

name = input("Enter your name: ")
print(welcome(name))

game_choice, difficulty = load_game()

print(f"Chosen game: {game_choice}")
print(f"Difficulty level: {difficulty}")
# Add further processing for the chosen game and difficulty if needed
