def arithmetic_operations(a, b):
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else 'undefined'
    }

def string_manipulation(s):
    return {
        'uppercase': s.upper(),
        'lowercase': s.lower(),
        'reversed': s[::-1],
        'length': len(s)
    }

def list_operations(lst):
    return {
        'sum': sum(lst),
        'max': max(lst),
        'min': min(lst),
        'sorted': sorted(lst)
    }

if __name__ == "__main__":
    # Test arithmetic operations
    print("Arithmetic Operations:", arithmetic_operations(10, 5))

    # Test string manipulation
    print("String Manipulation:", string_manipulation("Hello World"))

    # Test list operations
    print("List Operations:", list_operations([3, 1, 4, 1, 5, 9]))