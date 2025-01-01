def find_greatest_digits(number):
    # Convert the number to a string and then to a set of digits
    digits = set(int(digit) for digit in str(number))
    
    # Sort the digits in descending order
    sorted_digits = sorted(digits, reverse=True)
    
    # Get the first three greatest digits, or fewer if there aren't enough unique digits
    first_three_greatest = sorted_digits[:3]
    
    # Fill with None if there are less than three unique digits
    while len(first_three_greatest) < 3:
        first_three_greatest.append(None)
    
    return tuple(first_three_greatest)

# Sample usage
number = 6328
result = find_greatest_digits(number)
print(result)  # Output: (8, 6, 3)**