import random
import tkinter as tk
from tkinter import messagebox

class RouletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roulette Simulator")

        self.result_label = tk.Label(root, text="Welcome to Roulette!", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.bet_type_var = tk.StringVar(value="color")
        self.bet_color_var = tk.StringVar(value="red")
        self.bet_number_var = tk.IntVar(value=0)

        # Bet type selection
        self.bet_type_frame = tk.Frame(root)
        self.bet_type_frame.pack(pady=10)
        
        tk.Radiobutton(self.bet_type_frame, text="Bet on Color", variable=self.bet_type_var, value="color", command=self.update_bet_options).grid(row=0, column=0, padx=10)
        tk.Radiobutton(self.bet_type_frame, text="Bet on Number", variable=self.bet_type_var, value="number", command=self.update_bet_options).grid(row=0, column=1, padx=10)

        # Bet on color options
        self.color_frame = tk.Frame(root)
        self.color_frame.pack(pady=10)
        
        tk.Radiobutton(self.color_frame, text="Red", variable=self.bet_color_var, value="red").grid(row=0, column=0, padx=10)
        tk.Radiobutton(self.color_frame, text="Black", variable=self.bet_color_var, value="black").grid(row=0, column=1, padx=10)

        # Bet on number options
        self.number_frame = tk.Frame(root)
        self.number_frame.pack(pady=10)

        tk.Label(self.number_frame, text="Number (0-36):").grid(row=0, column=0, padx=10)
        self.number_entry = tk.Entry(self.number_frame, textvariable=self.bet_number_var, width=5)
        self.number_entry.grid(row=0, column=1)

        self.update_bet_options()

        # Spin button
        self.spin_button = tk.Button(root, text="Spin the Wheel", command=self.spin_roulette)
        self.spin_button.pack(pady=20)

    def update_bet_options(self):
        """Update the bet options based on the selected bet type."""
        if self.bet_type_var.get() == "color":
            self.color_frame.pack(pady=10)
            self.number_frame.pack_forget()
        else:
            self.number_frame.pack(pady=10)
            self.color_frame.pack_forget()

    def spin_roulette(self):
        """Simulate spinning the roulette wheel and determine the outcome."""
        bet_type = self.bet_type_var.get()
        
        # Simulate spinning the roulette wheel
        result_number = random.randint(0, 36)
        result_color = self.determine_color(result_number)

        # Show result in the GUI
        self.result_label.config(text=f"The wheel landed on {result_number} ({result_color.capitalize()})")

        # Determine if the user won or lost
        if bet_type == "number":
            bet_number = self.bet_number_var.get()
            if bet_number == result_number:
                messagebox.showinfo("Result", "Congratulations! You win!")
            else:
                messagebox.showinfo("Result", "Sorry, you lose.")
        else:
            bet_color = self.bet_color_var.get()
            if bet_color == result_color:
                messagebox.showinfo("Result", "Congratulations! You win!")
            else:
                messagebox.showinfo("Result", "Sorry, you lose.")

    @staticmethod
    def determine_color(number):
        """Determine the color based on the number on the roulette wheel."""
        if number == 0:
            return 'green'
        elif number % 2 == 0:
            return 'black'
        else:
            return 'red'

def main():
    root = tk.Tk()
    app = RouletteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
