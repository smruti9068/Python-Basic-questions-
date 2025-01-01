def sum_of_squares_of_evens():
    total = 0
    for number in range(1, 51):  # Range from 1 to 50 (inclusive)
        if number % 2 == 0:  # Check if the number is even
            total += number ** 2  # Add the square of the even number to total
    return total

# Sample usage
result = sum_of_squares_of_evens()
print(result)  # Output the result