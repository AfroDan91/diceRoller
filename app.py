import random
import csv
import tkinter as tk
from tkinter import ttk


# number_of_dice = 2
# dice_size = 8
# modifier = -1
# rolled_dice = []



window = tk.Tk()
window.title("Dice Roller")

def modifier_change(modifier):
    """change the value in the entry box by 1"""
    current_value = int(sv_modifier.get())  # Get current value
    sv_modifier.set(current_value + int(modifier))  # Increment and update
    
def dice_size_change(change):
    current = sv_dice_size.get()  # Convert current string to integer
    current = int(current[1:])
    new_value = current + int(change)  # Apply the change
    if new_value <= 2:
        new_value = 2
    sv_dice_size.set(f"d{new_value}")

def number_dice_change(change):
    current_value = int(sv_dice_amount.get())  # Get current value
    new_value = current_value + int(change)
    if new_value <= 1:
        new_value = 1
    sv_dice_amount.set(new_value)  # Increment and update
    
def roll_dice(number_of_dice,dice_size,modifier):
    # number_of_dice = sv_dice_amount.get()
    # dice_size = sv_dice_size.get()
    # modifier = sv_modifier.get()
    
    if 'd' in dice_size:
        dice_size = dice_size[1:]
    
    dice_total = 0
    dice_list = []
    current_dice = 0
    
    for i in range(int(number_of_dice)):
        current_dice = random.randint(1, int(dice_size))
        dice_list.append(current_dice)
        dice_total += current_dice
    
    dice_total += int(modifier)
    
    print(f"You rolled {number_of_dice}d{dice_size}+{modifier}\n dice = {dice_list} = {dice_total - int(modifier)} + {modifier} \n total = {dice_total}")
    
    formatted_result = f"{number_of_dice}d{dice_size}+{modifier} | {dice_list} + {modifier} = {dice_total}\n"
    
    history_list.append(formatted_result)
    
    lbl_results.config(text=dice_total) 
    
    update_history()
 
def update_history():
    lbl_history.config(text="".join(map(str, history_list)))

##### number of dice
sv_dice_amount = tk.StringVar(value="1")

frm_dice_amount = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5)
frm_dice_amount.grid(row=0,column=1)

lbl_dice_amount = tk.Label(master=frm_dice_amount, text="number of dice", height=2)
lbl_dice_amount.grid(row=1,column=0)

btn_dice_amount_add_1 = ttk.Button(frm_dice_amount, text="+1", command=lambda: number_dice_change("+1"))
btn_dice_amount_add_1.grid(row=2,column=0)

ent_dice_amount_text_box = ttk.Entry(frm_dice_amount, textvariable=sv_dice_amount, width=10, justify="center")
ent_dice_amount_text_box.grid(row=3,column=0)

btn_dice_amount_minus_1 = ttk.Button(frm_dice_amount, text="-1", command=lambda: number_dice_change("-1"))
btn_dice_amount_minus_1.grid(row=4,column=0)

##### size of dice
sv_dice_size = tk.StringVar(value="d2")

frm_dice_size = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5)
frm_dice_size.grid(row=0,column=2)

lbl_dice_amount = tk.Label(master=frm_dice_size, text="size of dice", height=2)
lbl_dice_amount.grid(row=1,column=0)

btn_dice_size_add_1 = ttk.Button(frm_dice_size, text="+1", command=lambda: dice_size_change("+1"))
btn_dice_size_add_1.grid(row=2,column=0)

ent_dice_size_text_box = ttk.Entry(frm_dice_size, textvariable=sv_dice_size, width=10, justify="center")
ent_dice_size_text_box.grid(row=3,column=0)

btn_dice_size_minus_1 = ttk.Button(frm_dice_size, text="-1", command=lambda: dice_size_change("-1"))
btn_dice_size_minus_1.grid(row=4,column=0)

##### modifier box 
sv_modifier = tk.StringVar(value="0")

frm_modifier = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5)
frm_modifier.grid(row=0,column=3)

lbl_dice_amount = tk.Label(master=frm_modifier, text="modifier", height=2)
lbl_dice_amount.grid(row=1,column=0)

btn_modifier_add_1 = ttk.Button(frm_modifier, text="+1", command=lambda: modifier_change("+1"))
btn_modifier_add_1.grid(row=2,column=0)

ent_modifier_text_box = ttk.Entry(frm_modifier, textvariable=sv_modifier, width=10, justify="center")
ent_modifier_text_box.grid(row=3,column=0)

btn_modifier_minus_1 = ttk.Button(frm_modifier, text="-1", command=lambda: modifier_change("-1"))
btn_modifier_minus_1.grid(row=4,column=0)

##### roll dice
frm_roll_dice = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5,height=115,width=87)
frm_roll_dice.grid(row=0,column=4)
frm_roll_dice.grid_propagate(False)

lbl_roll_dice = tk.Label(master=frm_roll_dice, text="roll dice", height=2)
lbl_roll_dice.grid(row=1,column=0)

btn_roll_dice = ttk.Button(frm_roll_dice, text="roll", command=lambda: roll_dice(sv_dice_amount.get(),sv_dice_size.get(),sv_modifier.get()))
btn_roll_dice.grid(row=2,column=0)

lbl_results = tk.Label(master=frm_roll_dice, text="", height=2)
lbl_results.grid(row=3,column=0)

##### history
history_list = []

frm_history = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5)
frm_history.grid(row=1,column=0,columnspan=5,rowspan=4)

lbl_history = tk.Label(master=frm_history, text="No history yet", height=len(history_list),width=50)
lbl_history.grid(row=3,column=0)

##### presets
row_count = 2
with open("presets.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

frm_presets = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5,height=115,width=87)
frm_presets.grid(row=0,column=5)

lbl_presets = tk.Label(master=frm_presets, text="Presets", height=2)
lbl_presets.grid(row=1,column=0)

lst_preset_labels = []
lst_preset_rolls = []

for row in data:
    print(row)
    if int(row['Modifier']) < 0:
        lst_preset_labels.append(tk.Label(master=frm_presets, text=f"{row['Number']}d{row['Size']}-{row['Modifier']}"))
    else:
        lst_preset_labels.append(tk.Label(master=frm_presets, text=f"{row['Number']}d{row['Size']}+{row['Modifier']}"))

    lst_preset_rolls.append(ttk.Button(frm_presets, text="roll", command=lambda: roll_dice(row['Number'],row['Size'],row['Modifier'])))

for label, roll in zip(lst_preset_labels,lst_preset_rolls):
    label.grid(row=row_count,column=0)
    roll.grid(row=row_count,column=1)
    row_count += 1

window.mainloop()
