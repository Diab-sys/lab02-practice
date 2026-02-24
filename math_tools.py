def add(a, b): return a + b
def multiply(a, b): return a * b
def is_even(n): return n % 2 == 0
def subtract(a, b): return a - b
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]     
       
def find_min(numbers):
    if not numbers: return None
    min_val = numbers[0] 
    for n in numbers:
        if n < min_val:
            min_val = n
    return min_val

def remove_duplicates(items):
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
