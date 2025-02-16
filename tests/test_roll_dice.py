# import pytest
# import random
# from unittest.mock import MagicMock, patch
# from app import roll_dice, history_list, lbl_history
# import app

# @pytest.fixture
# def mock_tk_labels():
#     """Mock Tkinter labels before each test."""
#     app.lbl_history = MagicMock()
#     app.lbl_results = MagicMock()

# @pytest.fixture
# def reset_history():
#     """Reset history_list before each test."""
#     history_list.clear()
#     yield
#     history_list.clear()

# @patch("app.update_history")
# def test_roll_dice_normal(mock_update, mock_tk_labels, reset_history):
#     """Test rolling dice with standard input."""
#     roll_dice(2, "6", 3)

#     assert len(history_list) == 1  # A new entry should be added
#     mock_update.assert_called_once()  # update_history should be called
#     lbl_results.config.assert_called()  # UI should be updated

# @patch("app.update_history")
# def test_roll_dice_with_d_prefix(mock_update, mock_tk_labels, reset_history):
#     """Test rolling dice when dice_size includes 'd' (e.g., 'd8')."""
#     roll_dice(1, "d8", 2)

#     assert len(history_list) == 1
#     assert "1d8+2" in history_list[0]  # Ensure correct format
#     mock_update.assert_called_once()
#     lbl_results.config.assert_called()

# @patch("app.update_history")
# def test_roll_dice_correct_math(mock_update, mock_tk_labels, reset_history):
#     """Ensure dice rolls and modifiers are summed correctly."""
#     random.seed(1)  # Fix randomness for a predictable test
#     roll_dice(2, "6", 2)  # Two dice, each between 1-6, plus 2

#     expected_total = sum([random.randint(1, 6) for _ in range(2)]) + 2
#     assert str(expected_total) in history_list[0]  # Result should match

# @patch("app.update_history")
# def test_roll_dice_valid_dice_range(mock_update, mock_tk_labels, reset_history):
#     """Ensure dice results are within the correct range."""
#     roll_dice(3, "10", 0)

#     # Extract dice values from history_list
#     dice_values = [int(x) for x in history_list[0].split("[")[1].split("]")[0].split(", ")]
    
#     assert all(1 <= roll <= 10 for roll in dice_values)  # Each roll should be in range

# @patch("app.update_history")
# def test_roll_dice_calls_update_history(mock_update, mock_tk_labels, reset_history):
#     """Ensure update_history is called after rolling dice."""
#     roll_dice(2, "6", 1)
#     lbl_results.config.assert_called()  # ✅ Ensure lbl_results was updated
#     lbl_history.config.assert_called()  # ✅ Ensure lbl_history was updated
#     mock_update.assert_called_once()  # ✅ Ensure update_history was called
