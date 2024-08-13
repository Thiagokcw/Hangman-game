import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_list = ['python', 'tkinter', 'hangman', 'interface', 'programming']
        self.reset_game()

        self.label_word = tk.Label(root, text=" ".join(self.display_word), font=('Arial', 24))
        self.label_word.pack(pady=20)

        self.label_lives = tk.Label(root, text=f"Lives: {self.lives}", font=('Arial', 16))
        self.label_lives.pack(pady=10)

        self.entry_guess = tk.Entry(root, font=('Arial', 14))
        self.entry_guess.pack(pady=10)

        self.button_guess = tk.Button(root, text="Guess", command=self.make_guess, font=('Arial', 14))
        self.button_guess.pack(pady=10)

        self.button_reset = tk.Button(root, text="Reset Game", command=self.reset_game, font=('Arial', 14))
        self.button_reset.pack(pady=10)

    def reset_game(self):
        self.selected_word = random.choice(self.word_list)
        self.display_word = ["_" for _ in self.selected_word]
        self.lives = 6
        self.guessed_letters = set()

        if hasattr(self, 'label_word'):
            self.label_word.config(text=" ".join(self.display_word))
            self.label_lives.config(text=f"Lives: {self.lives}")
            self.entry_guess.delete(0, tk.END)

    def make_guess(self):
        guess = self.entry_guess.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)
        if guess in self.selected_word:
            for index, letter in enumerate(self.selected_word):
                if letter == guess:
                    self.display_word[index] = guess
            self.label_word.config(text=" ".join(self.display_word))
        else:
            self.lives -= 1
            self.label_lives.config(text=f"Lives: {self.lives}")

        self.entry_guess.delete(0, tk.END)
        self.check_game_over()

    def check_game_over(self):
        if "_" not in self.display_word:
            messagebox.showinfo("Congratulations!", "You won!")
            self.reset_game()
        elif self.lives == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was '{self.selected_word}'.")
            self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
