import random
from tkinter import *

option = ["Rock", "Paper", "Scissors"]

def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            return "You Win"
        else:
            return "You Lose :("
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            return "You Win"
        else:
            return "You Lose :("
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            return "You Win"
        else:
            return "You Lose :("

def player_choice_selected(choice):
    player_choice_label.config(text=f"You chose: {choice}")
    computer_choice = random.choice(option)
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=play_game(choice, computer_choice))

# Initialize Tkinter window
window = Tk()
window.title("Rock-Paper-Scissors")

# Create image buttons
gambar1 = PhotoImage(file="RockPaperScissors-main\latihanpy\pictures\kertas2.png")
gambar2 = PhotoImage(file="RockPaperScissors-main\latihanpy\pictures\kertas.png")
gambar3 = PhotoImage(file="RockPaperScissors-main\latihanpy\pictures\gunting.png")

# Place buttons using grid
rock_button = Button(window, image=gambar1, command=lambda: player_choice_selected("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = Button(window, image=gambar2, command=lambda: player_choice_selected("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = Button(window, image=gambar3, command=lambda: player_choice_selected("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Create labels and place them below the buttons
player_choice_label = Label(window, text="Your Choice:")
player_choice_label.grid(row=1, column=0, columnspan=3, pady=5)

computer_choice_label = Label(window, text="Computer's Choice:")
computer_choice_label.grid(row=2, column=0, columnspan=3, pady=5)

result_label = Label(window, text="")
result_label.grid(row=3, column=0, columnspan=3, pady=5)

# Run the Tkinter event loop
window.mainloop()
