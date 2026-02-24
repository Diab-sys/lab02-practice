from calculator import add, divide
def test_divide():
    assert divide(10, 2) == 5, "Divide failed!"
    print("test_divide() ✓")
test_divide()
