import tkinter as tk
from random import choice

class RockPaperScissors:
    def init(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0

        self.score_label = tk.Label(self.root, text="Player: 0 - Computer: 0", font=("Arial", 12))
        self.score_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack()

        self.rock_button = tk.Button(self.root, text="Rock", command=self.rock)
        self.paper_button = tk.Button(self.root, text="Paper", command=self.paper)
        self.scissors_button = tk.Button(self.root, text="Scissors", command=self.scissors)

        self.rock_button.pack()
        self.paper_button.pack()
        self.scissors_button.pack()

    def computer_choice(self):
        return choice(["rock", "paper", "scissors"])

    def rock(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.result_label['text'] = "It's a tie!"
        elif computer == "paper":
            self.computer_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Paper covers rock! Computer wins this round."
        else:
            self.player_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Rock smashes scissors! Player wins this round."

    def paper(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.player_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Paper covers rock! Player wins this round."
        elif computer == "paper":
            self.result_label['text'] = "It's a tie!"
        else:
            self.computer_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Scissors cuts paper! Computer wins this round."

    def scissors(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.computer_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Rock smashes scissors! Computer wins this round."
        elif computer == "paper":
            self.player_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Scissors cuts paper! Player wins this round."
        else:
            self.result_label['text'] = "It's a tie!"

    def run(self):
        self.root.mainloop()

if name== "main":
    game = RockPaperScissors()
game.run()
