import pytest
from typing import List

from solutions.LC_0408_Valid_Word_Abbreviation import Solution

solver = Solution()

def test_example_1():
    """Test case from Example 1 of the problem description."""
    word = "internationalization"
    abbr = "i12iz4n"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_example_2():
    """Test case from Example 2 of the problem description."""
    word = "apple"
    abbr = "a2e"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_full_word_match():
    """Test case where the abbreviation is the full word itself."""
    word = "word"
    abbr = "word"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_full_number_abbreviation():
    """Test case where the entire word is abbreviated to its length."""
    word = "developer"
    abbr = "9"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_number_at_start():
    """Test case with a number at the beginning of the abbreviation."""
    word = "testing"
    abbr = "3ting"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_number_in_middle():
    """Test case with a number in the middle of the abbreviation."""
    word = "example"
    abbr = "ex3le"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_number_at_end():
    """Test case with a number at the end of the abbreviation."""
    word = "python"
    abbr = "pyth2"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_multiple_numbers():
    """Test case with multiple numbers in the abbreviation.
    'b2u2l' for 'beautiful' accounts for 7 characters (b + ea + u + ti + l),
    but 'beautiful' has 9 characters. Should be False.
    """
    word = "beautiful"
    abbr = "b2u2l"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_leading_zero_single_digit():
    """Test case with a single digit leading zero, which is invalid."""
    word = "abc"
    abbr = "a0b"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_leading_zero_multi_digit():
    """Test case with a multi-digit number having a leading zero, which is invalid."""
    word = "internationalization"
    abbr = "i012iz4n"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_leading_zero_full_word():
    """Test case where the full word abbreviation has a leading zero, which is invalid."""
    word = "word"
    abbr = "04"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_mismatch_character():
    """Test case where a character in abbr does not match word."""
    word = "hello"
    abbr = "hxllo"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_mismatch_length_abbr_too_short():
    """Test case where the abbreviation is too short to cover the word."""
    word = "abcdef"
    abbr = "abc"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_mismatch_length_abbr_too_long():
    """Test case where the abbreviation implies a longer word than available."""
    word = "abc"
    abbr = "abcd"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_number_exceeds_remaining_length():
    """Test case where a number in abbr implies skipping more characters than available."""
    word = "apple"
    abbr = "a5" # 'a' matches, then '5' tries to skip 5 chars, but only 4 remain
    assert solver.validWordAbbreviation(word, abbr) == False

def test_single_character_word_match():
    """Test case for a single character word matching itself."""
    word = "a"
    abbr = "a"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_single_character_word_number():
    """Test case for a single character word abbreviated by '1'."""
    word = "z"
    abbr = "1"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_single_character_word_mismatch():
    """Test case for a single character word with a mismatching abbreviation."""
    word = "a"
    abbr = "b"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_mixed_chars_and_numbers_valid_example():
    """
    A valid complex mix of characters and numbers.
    'abbreviation' (length 12) with 'a4i4on'
    a (1) + bbre (4) + v (1) + atio (4) + n (1) = 11. Word is 12.
    This should be False.
    """
    word = "abbreviation"
    abbr = "a4i4on"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_mixed_chars_and_numbers_invalid():
    """Complex mix of characters and numbers leading to invalid."""
    word = "abbreviation"
    abbr = "a4i5n" # a-bbrev-i-atio-n, 5 is too many for 'atio'
    assert solver.validWordAbbreviation(word, abbr) == False

def test_large_input_max_word_length():
    """
    Test case with word at max length (20) and abbr near max length (10),
    representing a valid abbreviation.
    """
    word = "abcdefghijklmnopqrst" # Length 20
    abbr = "a18t" # a + 18 chars + t = 1 + 18 + 1 = 20
    assert solver.validWordAbbreviation(word, abbr) == True

def test_large_input_max_word_length_full_number():
    """
    Test case with word at max length (20) abbreviated by its full length.
    """
    word = "abcdefghijklmnopqrst" # Length 20
    abbr = "20"
    assert solver.validWordAbbreviation(word, abbr) == True

def test_large_input_max_word_length_complex_invalid():
    """
    Test case with word at max length (20) and a complex abbreviation that is 
    invalid due to mismatch.
    'a8c8u' for 'abcdefghijklmnopqrsu'
    'a' matches 'a' (idx 0). 
    Skip 8 chars -> 'bcdefghi'.
    Next word char is 'j' (idx 9).
    Next abbr char is 'c'. 'c' != 'j'.
    Should be False.
    """
    word = "abcdefghijklmnopqrsu" # Length 20
    abbr = "a8c8u"
    assert solver.validWordAbbreviation(word, abbr) == False

def test_large_input_max_word_length_invalid_number():
    """
    Test case with word at max length (20) and an abbreviation that's invalid
    due to a number skipping too many characters.
    """
    word = "abcdefghijklmnopqrst" # Length 20
    abbr = "a19t" # Tries to consume 21 chars, but only 20 available.
    assert solver.validWordAbbreviation(word, abbr) == False

def test_large_input_max_word_length_invalid_leading_zero():
    """
    Test case with word at max length (20) and an abbreviation with a leading zero.
    """
    word = "abcdefghijklmnopqrsu" # Length 20
    abbr = "a08c8u" # Leading zero
    assert solver.validWordAbbreviation(word, abbr) == False

def test_multiple_adjacent_numbers_parsed_as_one():
    """
    Test case to confirm that adjacent digits in abbr are parsed as a single number,
    as per the problem's implicit handling by the provided solution.
    """
    word = "abcdefghij" # Length 10
    abbr = "a123fg" # a + 123 chars (too many) + fg
    assert solver.validWordAbbreviation(word, abbr) == False

    word = "abcdefghij" # Length 10
    abbr = "a8fg" # a + 8 chars + fg = 1 + 8 + 2 = 11. Too long.
    assert solver.validWordAbbreviation(word, abbr) == False

    word = "abcdefghij" # Length 10
    abbr = "a7ij" # a + 7 chars + ij = 1 + 7 + 2 = 10. Valid.
    assert solver.validWordAbbreviation(word, abbr) == True