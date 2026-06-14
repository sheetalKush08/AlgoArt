import random

# Function to choose a random word from the list
def choose_word():
    words = ["red", "pen", "book", "toy", "home", "bed","eye","nose","ear","mango","rat","head",]
    return random.choice(words)

# Function to jumble the selected word
def jumble_word(word):
    jumbled = list(word)
    random.shuffle(jumbled)
    return ''.join(jumbled)

# Function to play the game
def play_game():
    points = 0
    attempts = 3
    while True:
        selected_word = choose_word()
        jumbled = jumble_word(selected_word)
        print(f"Your jumbled word is: {jumbled}")
        guess = input("Guess the word: ").lower()
        
        if guess == selected_word:
            print("Congratulations! You guessed it right!")
            points += 1
        else:
            print(f"Sorry, the correct word was: {selected_word}")
            attempts -= 1
            if attempts == 0:
                print("Game Over!")
                break
        
        print(f"Your current points: {points}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Your total points: {points}")
            break

# Start the game
play_game()
