def is_armstrong_number(num):
    # Convert the number to a string to iterate over its digits
    digits = str(num)
    power = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** power for digit in digits)
    
    return armstrong_sum == num

# Test the function
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
