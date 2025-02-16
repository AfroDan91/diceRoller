import pytest
from unittest.mock import MagicMock
import app  # Import the full app module

@pytest.fixture
def mock_lbl_history():
    """Mock the lbl_history label."""
    app.lbl_history = MagicMock()  # Replace the global lbl_history reference

def test_update_history_updates_label(mock_lbl_history):
    """Ensure update_history updates lbl_history with the correct text."""
    app.history_list.clear()  # Start with an empty history list
    app.history_list.append("3d6+2 = 15")  # Add a test roll

    app.update_history()  # Call the function

    app.lbl_history.config.assert_called_once_with(text="3d6+2 = 15")  # ✅ Ensure the label was updated

def test_update_history_with_multiple_entries(mock_lbl_history):
    """Ensure update_history correctly formats multiple history entries."""
    app.history_list.clear()
    app.history_list.extend(["3d6+2 = 15", "2d8+1 = 12"])  # Add multiple rolls

    app.update_history()

    app.lbl_history.config.assert_called_once_with(text="3d6+2 = 152d8+1 = 12")  # ✅ Ensure both rolls appear
