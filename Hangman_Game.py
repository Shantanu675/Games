import random
import tkinter as tk
from tkinter import messagebox

# as per number on time you provide wrong input following stages executed
stages = ['''
    --+------
     |     |
     0     |
    /|\    |
     |     |
    / \    |
           |
   ---------
    ''', '''
    --+------
     |     |
     0     |
    /|\    |
     |     |
    /      |
           |
   ---------
    ''', '''
    --+------
     |     |
     0     |
    /|\    |
     |     |
           |
           |
   ---------
    ''', '''
    --+------
     |     |
     0     |
    /|\    |
           |
           |
           |
   ---------
    ''', '''
    --+------
     |     |
     0     |
    /|     |
           |
           |
           |
   ---------
    ''', '''
    --+------
     |     |
     0     |
     |     |
           |
           |
           |
   ---------
    ''', '''
    --+------
     |     |
     0     |
           |
           |
           |
           |
   ---------
    ''', '''
    --+------
     |     |
           |
           |
           |
           |
           |
   ---------
    ''']

# random word for the game
words = ["shantanu", "student", "college", "linkedin"]

# life is constant for game (global variables) 
life = 7
choice = random.choice(words)
display = ['_' for _ in choice]

# initialize the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x400")
root.config(bg="#FFD700")

def update_display():
    display_str = " ".join(display)
    word_label.config(text=display_str)
    
def guess_letter():
    global life
    guessed_letter = entry.get().lower()
    entry.delete(0, tk.END)
    
    if guessed_letter in choice:
        for position in range(len(choice)):
            letter = choice[position]
            if letter == guessed_letter:
                display[position] = guessed_letter
        update_display()
    else:
        life -= 1
        hangman_label.config(text=stages[life], fg="#FF0000") 
        
    if life == 0:
        messagebox.showinfo("Game Over", "You Lost!")
        reset_game()
        
    if "_" not in display:
        messagebox.showinfo("Congratulations", "You Win!")
        reset_game()

def reset_game():
    global life, choice, display
    life = 7
    choice = random.choice(words)
    display = ['_' for _ in choice]
    hangman_label.config(text=stages[life], fg="#008080")   
    update_display()

# elements for GUI
hangman_label = tk.Label(root, text=stages[life], font=("Courier", 14), fg="#008080", bg="#FFD700")  
hangman_label.pack(pady=20)

word_label = tk.Label(root, text=" ".join(display), font=("Helvetica", 18), bg="#FFD700", fg="#00008B")  
word_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 16), justify='center')
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter, bg="#00FF7F", fg="black", font=("Helvetica", 14))
guess_button.pack(pady=10)

# start the GUI loop
root.mainloop()