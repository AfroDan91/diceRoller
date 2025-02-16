import pytest
import tkinter as tk  # Required for StringVar
from app import dice_size_change  # Import the function
import app

@pytest.fixture
def sv_dice_size_fixture(request):
    """Creates a fresh StringVar with a configurable starting value and assigns it to app.sv_dice_size."""
    root = tk.Tk()  # Create a Tkinter root window
    starting_value = request.param  # Get parameter from test
    app.sv_dice_size = tk.StringVar(value=starting_value)  # Set the global variable
    return app.sv_dice_size  # Return reference for assertions

@pytest.mark.parametrize("sv_dice_size_fixture", ["d2", "d6", "d12"], indirect=True)
def test_dice_size_increases(sv_dice_size_fixture):
    """Test increasing the dice size from different starting values."""
    initial_size = int(sv_dice_size_fixture.get()[1:])  # Extract the number from "dX"    
    expected_size = f"d{initial_size + 1}"  # Expected result after increment
    dice_size_change(1)  # Call the function
    assert sv_dice_size_fixture.get() == expected_size  # Verify the update

@pytest.mark.parametrize("sv_dice_size_fixture", ["d3", "d6", "d12"], indirect=True)
def test_dice_size_decrease(sv_dice_size_fixture):
    """Test increasing the dice size from different starting values."""
    initial_size = int(sv_dice_size_fixture.get()[1:])  # Extract the number from "dX"    
    expected_size = f"d{initial_size - 1}"  # Expected result after increment
    dice_size_change(-1)  # Call the function
    assert sv_dice_size_fixture.get() == expected_size  # Verify the update
    
@pytest.mark.parametrize("sv_dice_size_fixture", ["d2"], indirect=True)
def test_dice_size_decrease_d2(sv_dice_size_fixture):
    """Test increasing the dice size from different starting values."""
    initial_size = int(sv_dice_size_fixture.get()[1:])  # Extract the number from "dX"    
    expected_size = "d2"  # Expected result after increment
    dice_size_change(-1)  # Call the function
    assert sv_dice_size_fixture.get() == expected_size  # Verify the update