import pytest
import tkinter as tk  # Required for StringVar
from app import modifier_change  # Import the function
import app

@pytest.fixture
def sv_modifier_fixture():
    """Creates a fresh StringVar and assigns it to the global variable in app.py."""
    root = tk.Tk()  # Create a Tkinter root window
    app.sv_modifier = tk.StringVar(value="0")  # Set the global sv_modifier in app
    return app.sv_modifier  # Return the same reference

def test_modifier_increases_value(sv_modifier_fixture):
    """Test increasing the modifier value."""
    modifier_change(1)  # Call the function (it will use the global sv_modifier)
    assert sv_modifier_fixture.get() == "1"  # Verify the update

def test_modifier_decreases_value(sv_modifier_fixture):
    """Test decreasing the modifier value."""
    modifier_change(-2)  # Subtract 2
    assert sv_modifier_fixture.get() == "-2"
    
def test_modifier_zero_value(sv_modifier_fixture):
    """Test decreasing the modifier value."""
    modifier_change(0)  # Subtract 2
    assert sv_modifier_fixture.get() == "0"

def test_modifier_with_non_integer(sv_modifier_fixture):
    """Test handling of non-integer input."""
    with pytest.raises(ValueError):  # Expect an error for non-int input
        modifier_change("invalid")

