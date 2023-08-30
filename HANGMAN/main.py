import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display += "_"

#print(display)

end_of_game = False
lives = 6

while not end_of_game :
    guess = input("Guess a letter:").lower()
    count = 0
    if guess in display:
        print(f"You've already guessed {guess}.")
    for letter in chosen_word:
        if guess == letter:
            display[count] = guess
        count += 1

    if guess not in chosen_word:
        lives -= 1
    if lives == 1:
        print("Your last chance.")
    if lives == 0:
        print("You Lose :( ")
        end_of_game = True
    if "_" not in display:
        print("You Win :)")
        end_of_game = True

    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

