import pytest
import app  # Import the module where validate_inputs_new_preset is defined

@pytest.mark.parametrize("test_input, expected", [
    ("3d6+2", True),   # ✅ Valid: has "d" and a modifier
    ("2d8-1", True),   # ✅ Valid: has "d" and a minus modifier
    ("d20+0", True),   # ✅ Valid: has "d" and a "+0" modifier
    ("4d12-0", True),  # ✅ Valid: has "d" and a "-0" modifier
    ("5d10", False),   # ❌ Invalid: missing modifier
    ("d6", False),     # ❌ Invalid: missing modifier
    ("10", False),     # ❌ Invalid: missing "d"
    ("d20-", True),    # ✅ Valid: has "d" and a "-"
    ("d6+", True),     # ✅ Valid: has "d" and a "+"
    ("", False),       # ❌ Invalid: empty input
])
def test_validate_inputs_new_preset(test_input, expected):
    """Test various cases for validate_inputs_new_preset."""
    assert app.validate_inputs_new_preset(test_input) == expected
