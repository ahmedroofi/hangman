import random
from board import hangman_stage
from words import word_list


class Hangman:

    def __init__(self):
        self.word = random.choice(word_list).upper()
        self.guessed = False
        self.guessed_letters = set()
        self.guessed_words = set()
        self.tries = 6
        self.blanks = "_" * len(self.word)

    def display_hangman(self):
        return hangman_stage[self.tries]

    def validate_letter(self, guess):
        success = False
        if guess in self.guessed_letters:
            print("You already guessed the letter", guess)
        elif guess not in self.word:
            print(guess, "is not in the word.")
            self.tries -= 1
            self.guessed_letters.add(guess)
        else:
            print("Good job,", guess, "is in the word!")
            self.guessed_letters.add(guess)
            success = True
        return success

    def validate_word(self, guess):
        if guess in self.guessed_words:
            print("You already guessed the word", guess)
        elif guess != self.word:
            print(guess, "is not the word.")
            self.tries -= 1
            self.guessed_words.add(guess)
        else:
            self.guessed = True
            self.blanks = self.word

    def set_letters(self, guess):
        temp = list(self.blanks)
        indices = [i for i, letter in enumerate(self.word) if letter == guess]
        for index in indices:
            temp[index] = guess
        if "_" not in temp:
            self.guessed = True
        self.blanks = "".join(temp)

    def play(self):
        print("Welcome To Hangman")
        print("Let's Play!")
        print(self.display_hangman())
        print(self.blanks)
        print("\n")
        while not self.guessed and self.tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if self.validate_letter(guess):
                    self.set_letters(guess)

            elif len(guess) == len(self.word) and guess.isalpha():
                self.validate_word(guess)
            else:
                print("Invalid guess.")

            print(self.display_hangman())
            print(self.blanks)
            print("\n")

        if self.guessed:
            print("Congrats, you guessed the word, You win!")
        else:
            print("Sorry, you ran out of tries. The word was " +
                  self.word + ". Maybe next time!")


if __name__ == "__main__":
    Hm = Hangman()
    Hm.play()
    while input("Play Again? (Y/N) ").upper() == "Y":
        Hm = Hangman()
        Hm.play()
