from math_tools import add, multiply, is_even, subtract

def test_add():
    assert add(2, 3) == 5
    print("test_add : ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    print("test_multiply : ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    print("test_is_even : ALL PASSED")

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0
    print("test_subtract : ALL PASSED")

def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3   # Case 1: C is largest
    assert max_of_three(10, 5, 2) == 10 # Case 2: A is largest
    assert max_of_three(1, 9, 4) == 9   # Case 3: B is largest
    assert max_of_three(5, 5, 2) == 5   # Case 4: Two equal
    assert max_of_three(7, 7, 7) == 7   # Case 5: All equal
    print("test_max_of_three : ALL PASSED")

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True # Spaces/Case
    assert is_palindrome("") == True      # Edge case: Empty string
    assert is_palindrome("a") == True     # Edge case: Single character
    assert is_palindrome("racecar") == True
    print("test_is_palindrome : ALL PASSED")


test_add()
test_multiply()
test_is_even()
test_subtract()
print("--- All tests passed ! ---")
