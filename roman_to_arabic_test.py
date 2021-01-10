import pytest

from roman_to_arabic import Roman_to_Arabic

@pytest.fixture()
def roman_to_arabic():
    roman_to_arabic= Roman_to_Arabic()
    return roman_to_arabic

@pytest.mark.parametrize("roman_input, arabic_output", (
    ("I", 1),
    ("II", 2),
    ("XIV", 14),
    ("XVII", 17),
    ("XXIV", 24)
))
def test_change_roman_to_arabic(roman_to_arabic, roman_input, arabic_output):
    assert roman_to_arabic.change_roman_to_arabic(roman_input) == arabic_output




