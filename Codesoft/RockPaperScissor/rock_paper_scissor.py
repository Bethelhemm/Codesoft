import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"User choice: {user_choice}\nComputer choice: {computer_choice}\nResult: {result}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

choices = ["rock", "paper", "scissors"]

user_choice_var = tk.StringVar()
user_choice_var.set(choices[0])

label = tk.Label(root, text="Select your choice:")
label.pack()

option_menu = tk.OptionMenu(root, user_choice_var, *choices)
option_menu.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

root.mainloop()