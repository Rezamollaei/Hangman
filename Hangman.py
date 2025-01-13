import random

words = ["python" , "java" , "kotlin" , "javascript" , "ruby" , "swift"]

# randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ["_" for _ in chosen_word]
# print(word_display)
attempt = 8

print("welcome to hangman!")

while attempt > 0 and "_" in word_display :
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index , letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess    #reveal letter
    else:
        print("That letter doesnt appear in the word.")
        attempt -= 1

#game conclution

if "_" not in word_display:
    print("you guessed the word!")
    print(" ".join(word_display))
    print("you survived!")
else:
    print("You run out of attempts. the word was: "+ chosen_word)
    print("You lost!")