import random
import csv
import re
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

wrapper_frame = tk.Frame(window)
wrapper_frame.pack()

left_frame = tk.Frame(wrapper_frame)
left_frame.grid(row=0, column=0,sticky="n")

right_frame = tk.Frame(wrapper_frame)
right_frame.grid(row=0, column=1,sticky="n")

##### number of dice
sv_dice_amount = tk.StringVar(value="1")

frm_dice_amount = tk.Frame(master=left_frame,relief=tk.GROOVE,borderwidth=5)
frm_dice_amount.grid(row=0,column=1,sticky="n")

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

frm_dice_size = tk.Frame(master=left_frame,relief=tk.GROOVE,borderwidth=5)
frm_dice_size.grid(row=0,column=2,sticky="n")

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

frm_modifier = tk.Frame(master=left_frame,relief=tk.GROOVE,borderwidth=5)
frm_modifier.grid(row=0,column=3,sticky="n")

lbl_dice_amount = tk.Label(master=frm_modifier, text="modifier", height=2)
lbl_dice_amount.grid(row=1,column=0)

btn_modifier_add_1 = ttk.Button(frm_modifier, text="+1", command=lambda: modifier_change("+1"))
btn_modifier_add_1.grid(row=2,column=0)

ent_modifier_text_box = ttk.Entry(frm_modifier, textvariable=sv_modifier, width=10, justify="center")
ent_modifier_text_box.grid(row=3,column=0)

btn_modifier_minus_1 = ttk.Button(frm_modifier, text="-1", command=lambda: modifier_change("-1"))
btn_modifier_minus_1.grid(row=4,column=0)

##### roll dice
frm_roll_dice = tk.Frame(master=left_frame,relief=tk.GROOVE,borderwidth=5,height=115,width=87)
frm_roll_dice.grid(row=0,column=4,sticky="ns")
frm_roll_dice.grid_propagate(False)

lbl_roll_dice = tk.Label(master=frm_roll_dice, text="roll dice", height=2)
lbl_roll_dice.grid(row=1,column=0)

btn_roll_dice = ttk.Button(frm_roll_dice, text="roll", command=lambda: roll_dice(sv_dice_amount.get(),sv_dice_size.get(),sv_modifier.get()))
btn_roll_dice.grid(row=2,column=0)

lbl_results = tk.Label(master=frm_roll_dice, text="", height=2)
lbl_results.grid(row=3,column=0)

##### history
history_list = []

frm_history = tk.Frame(master=left_frame,relief=tk.GROOVE,borderwidth=5)
frm_history.grid(row=1,column=0,columnspan=5,sticky="n")

lbl_history = tk.Label(master=frm_history, text="No history yet", height=len(history_list),width=50)
lbl_history.grid(row=3,column=0)

##### presets
row_count = 2
def generate_presets():
    global row_count
    lst_preset_labels = []
    lst_preset_roll_btn = []
    for label, roll in zip(lst_preset_labels,lst_preset_roll_btn):
        label.destroy()
        roll.destroy()
        
    row_count = 2
    
    with open("presets.csv", "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    for row in data:
        print(row)
        if int(row['Modifier']) < 0:
            lst_preset_labels.append(tk.Label(master=frm_presets, text=f"{row['Name']} {row['Number']}d{row['Size']}-{row['Modifier']}"))
        else:
            lst_preset_labels.append(tk.Label(master=frm_presets, text=f"{row['Name']} {row['Number']}d{row['Size']}+{row['Modifier']}"))

        lst_preset_roll_btn.append(ttk.Button(frm_presets, text="roll", command=lambda n=row['Number'], s=row['Size'], m=row['Modifier']: roll_dice(n, s, m)))

    for label, roll in zip(lst_preset_labels,lst_preset_roll_btn):
        label.grid(row=row_count,column=0)
        roll.grid(row=row_count,column=1)
        row_count += 1

frm_presets = tk.Frame(master=right_frame,relief=tk.GROOVE,borderwidth=5,height=115,width=87)
frm_presets.grid(row=0,column=5,rowspan=999, sticky="ns")

lbl_presets = tk.Label(master=frm_presets, text="Presets", height=2)
lbl_presets.grid(row=1,column=0,columnspan=2)

generate_presets()
generate_presets()
# new preset
def validate_inputs_new_preset(input):
    if "d" in input: 
        if re.search(r"[+-]", input):
            return True
    return False 

def new_preset_submit():
    new_row = []
    
    ent_new_preset_name.grid_forget()
    ent_new_preset_dice.grid_forget()
    btn_new_preset_submit.grid_forget()
    btn_new_preset.grid(row=row_count+1,column=0,columnspan=2)
    
    if validate_inputs_new_preset(sv_new_preset_dice.get()):
        new_row.append(sv_new_preset_name.get())
        new_dice = re.split(r"[d\+\-]", sv_new_preset_dice.get())
        print(new_dice)
        new_row.extend(new_dice)
        print(new_row)
        
        with open("presets.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_row) 
    
    generate_presets()
        
    
def new_preset_create():
    btn_new_preset.grid_forget()
    ent_new_preset_name.grid(row=row_count+1,column=0)
    ent_new_preset_dice.grid(row=row_count+1,column=1)
    btn_new_preset_submit.grid(row=row_count+2,column=0,columnspan=2)

sv_new_preset_dice = tk.StringVar(value="Enter Roll")
sv_new_preset_name = tk.StringVar(value="Input Name")

ent_new_preset_name = ttk.Entry(frm_presets, textvariable=sv_new_preset_name,width=15, justify="center")
ent_new_preset_dice = ttk.Entry(frm_presets, textvariable=sv_new_preset_dice, width=10, justify="center")
btn_new_preset_submit = ttk.Button(frm_presets, text="Submit", command=new_preset_submit)



btn_new_preset = ttk.Button(frm_presets, text="New", command=new_preset_create)
btn_new_preset.grid(row=row_count+1,column=0,columnspan=2)

window.mainloop()
