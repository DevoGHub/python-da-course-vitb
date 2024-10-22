try:
    dividend = float(input())
    divisor = float(input())
    print(dividend / divisor)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter numeric values only")