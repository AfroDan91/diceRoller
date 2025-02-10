import pytest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app import roll_dice

# Mock `random.randint` to control the random values returned
@pytest.mark.parametrize(
    "num_dice, dice_size, modifier, mock_rolls, expected_total, expected_rolls",
    [
        (3, 6, 2, [3, 4, 5], 14, [3, 4, 5]),  # 3d6 + 2 -> (3+4+5) + 2 = 14
        (2, 6, 0, [2, 3], 5, [2, 3]),         # 2d6 + 0 -> (2+3) + 0 = 5
        (1, 10, 3, [5], 8, [5]),              # 1d10 + 3 -> 5+3 = 8
        (0, 6, 5, [], 5, []),                 # 0d6 + 5 -> Only modifier = 5
        (1, 20, 0, [20], 20, [20]),           # 1d20 -> 20 + 0 = 20
    ]
)
def test_roll_dice(num_dice, dice_size, modifier, mock_rolls, expected_total, expected_rolls):
    with patch('random.randint', side_effect=mock_rolls):
        total, rolls = roll_dice(num_dice, dice_size, modifier)

        assert rolls == expected_rolls
        assert total == expected_total

def test_roll_dice_no_dice_no_modifier():
    total, rolls = roll_dice(0, 6, 0)  # No dice, no modifier
    assert rolls == []  # No rolls should be recorded
    assert total == 0   # Only the modifier (which is 0) should be returned

def test_roll_dice_negative_modifier():
    with patch('random.randint', side_effect=[4, 5, 6]):
        total, rolls = roll_dice(3, 6, -3)  # Rolling 3d6 - 3

        assert rolls == [4, 5, 6]  # Rolls should be correct
        assert total == 12  # (4+5+6) - 3 = 12
