This program is a simple implementation of the Hangman game where the player has to guess a word by suggesting letters. Here's a breakdown of how it works:

Word Selection:

A list of programming language names (python, java, kotlin, etc.) is provided.
A random word is chosen from this list using random.choice().
Word Display:

A list word_display is created to represent the word with underscores (_), where each underscore corresponds to an unguessed letter.
For example, for the word python, the display would initially show ["_", "_", "_", "_", "_", "_"].
Game Loop:

The game continues as long as the player has attempts remaining and the word is still partially hidden (there are underscores in the word_display).
In each iteration of the loop:
The current state of the word is displayed (e.g., _ y _ h _ n).
The player is prompted to guess a letter.
If the guessed letter is in the word, it reveals that letter in all its positions in the word_display.
If the guessed letter is not in the word, the player loses an attempt.
Ending the Game:

If the player guesses all the letters in the word (no underscores left), they win and the program displays the guessed word.
If the player runs out of attempts, the game ends, and the program reveals the correct word.
Attempts:

The player starts with 8 attempts, which are decreased with each incorrect guess.
The game provides feedback on whether the guessed letter is correct or not, and it also informs the player about the game outcome (whether they won or lost). This is a fun way to practice guessing and improve spelling and word recognition.
