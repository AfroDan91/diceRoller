import tkinter as tk
import random

def roll_dice():
    """Starts the animation and sets a final dice roll result."""
    animate_roll(10)  # Number of animation frames before stopping

def animate_roll(count):
    """Displays random dice values in the label for an animation effect."""
    if count > 0:
        random_roll = random.randint(1, 6)  # Generate random dice roll
        label.config(text=f"🎲 Rolling... {random_roll}")  # Update label
        root.after(100, animate_roll, count - 1)  # Continue animation every 100ms
    else:
        final_result = random.randint(1, 6)  # Get final result
        label.config(text=f"🎲 You rolled: {final_result}")  # Show final result

# Create the main window
root = tk.Tk()
root.title("Animated Dice Roller")

# Create a label to display the result
label = tk.Label(root, text="Click to roll the dice!", font=("Arial", 16))
label.pack(pady=10)

# Create a button to roll the dice
button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 14))
button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
