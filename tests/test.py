# import pytest
# import random
# from unittest.mock import MagicMock, patch
# from app import roll_dice, history_list
# # import sys
# # import os
# # sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# @pytest.fixture
# def mock_tk_labels():
#     """Mock Tkinter label before running tests."""
#     global lbl_results, lbl_history
#     lbl_results = MagicMock()
#     lbl_history = MagicMock()

# @pytest.fixture
# def reset_history():
#     """Reset history_list before each test."""
#     history_list.clear()
#     yield
#     history_list.clear()
    
# # Mock `random.randint` to control the random values returned
# @pytest.mark.parametrize(
#     "num_dice, dice_size, modifier, mock_rolls, expected_total, expected_rolls",
#     [
#         ("3", "6", "2", [3, 4, 5], 14, [3, 4, 5]),  # 3d6 + 2 -> (3+4+5) + 2 = 14
#         ("2", "6", "0", [2, 3], 5, [2, 3]),         # 2d6 + 0 -> (2+3) + 0 = 5
#         ("1", "10", "3", [5], 8, [5]),              # 1d10 + 3 -> 5+3 = 8
#         ("1", "20", "0", [20], 20, [20]),           # 1d20 -> 20 + 0 = 20
#     ]
# ) 
# def test_roll_dice(num_dice, dice_size, modifier, mock_rolls, expected_total, expected_rolls,mock_tk_labels):
#     with patch('random.randint', side_effect=mock_rolls):
#         roll_dice(num_dice, dice_size, modifier)


# def test_roll_dice_no_dice_no_modifier():
#     roll_dice("0", "6", "0")  # No dice, no modifier

# def test_roll_dice_negative_modifier():
#     with patch('random.randint', side_effect=[4, 5, 6]):
#         roll_dice("3", "6", "-2")  # Rolling 3d6 - 3
