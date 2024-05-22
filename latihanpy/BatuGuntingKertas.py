import random
from tkinter import *

option = ["Rock","Paper","Scissors"]
    
def play_game(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "Draw"
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            return "You Win"
        else:
            return "You Lose:("
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            return "You Win"
        else:
            return "You Lose:("
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            return "You Win"
        else:
            return "You Lose:("
            
def player_choice_selected(choice):
    
  player_choice_label.config(text=f"You chose: {choice}")
  computer_choice = random.choice(option)
  computer_choice_label.config(text=f"Computer chose: {computer_choice}")
  result_label.config(text=play_game(choice, computer_choice))

# Initialize Tkinter window
window = Tk()
window.title("Rock-Paper-Scissors")

# Create labels and buttons
player_choice_label = Label(window, text="Your Choice:")
player_choice_label.pack(side="bottom")

gambar1 = PhotoImage(file=".\pictures\kertas2.png")
rock_button = Button(window, image=gambar1, command=lambda: player_choice_selected("Rock")).pack(side="right")

gambar2 = PhotoImage(file=".\pictures\kertas.png")
paper_button = Button(window, image=gambar2, command=lambda: player_choice_selected("Paper")).pack(side="right")

gambar3 = PhotoImage(file=".\pictures\gunting.png")
scissors_button = Button(window, image=gambar3, command=lambda: player_choice_selected("Scissors")).pack(side="right")

computer_choice_label = Label(window, text="Computer's Choice:")
computer_choice_label.pack(side="bottom")

result_label = Label(window, text="")
result_label.pack(side="bottom")

# Run the Tkinter event loop
window.mainloop()