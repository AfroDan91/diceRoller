import tkinter as tk
import random

def roll_dice():
    """Rolls a six-sided dice and updates the label with the result."""
    result = random.randint(1, 6)  # Get random number between 1 and 6
    label.config(text=f"🎲 You rolled: {result}")  # Update label text

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Create a label to display the result
label = tk.Label(root, text="Click to roll the dice!", font=("Arial", 14))
label.pack(pady=10)

# Create a button to roll the dice
button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 12))
button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
