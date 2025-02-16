import pytest
import tkinter as tk  # Required for StringVar
from app import number_dice_change  # Import the function
import app

@pytest.fixture
def sv_dice_amount_fixture():
    """Creates a fresh StringVar and assigns it to the global variable in app.py."""
    root = tk.Tk()  # Create a Tkinter root window
    app.sv_dice_amount = tk.StringVar(value="2")  # Set the global sv_modifier in app
    return app.sv_dice_amount  # Return the same reference

def test_modifier_increases_value(sv_dice_amount_fixture):
    """Test increasing the modifier value."""
    number_dice_change(1)  # Call the function (it will use the global sv_modifier)
    assert sv_dice_amount_fixture.get() == "3"  # Verify the update

def test_dice_number_decrease_value(sv_dice_amount_fixture):
    """Test increasing the modifier value."""
    number_dice_change(-1)  # Call the function (it will use the global sv_modifier)
    assert sv_dice_amount_fixture.get() == "1"  # Verify the update
    
def test_dice_number_less_than_zero(sv_dice_amount_fixture):
    """Test increasing the modifier value."""
    number_dice_change(-14)  # Call the function (it will use the global sv_modifier)
    assert sv_dice_amount_fixture.get() == "1"  # Verify the update