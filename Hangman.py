import random

words = ["mango", "phone", "table", "cloth", "plant"]
word = random.choice(words)
guessed_letters = []
attempts = 6
word_display = ["_"] * len(word)

print("🎮Welcome to HANGMAN GAME!🎮")
print("Guess the word letter by letter.")
print("You have 6 incorrect guesses. Let's begin!\n")

while attempts > 0 and "_" in word_display:
    print("Word: " + " ".join(word_display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet only.❌\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.⚠️\n")       
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!✅\n")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
    else:
        attempts -= 1
        print(f"Incorrect! You have {attempts} guesses left.❌❌\n")
if "_" not in word_display:
    print("🎉🎉Congratulations🎉🎉! You guessed the word:", word)
else:
    print("You ran out of guesses. The word was:", word)
