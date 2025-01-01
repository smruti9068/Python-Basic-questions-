def find_numbers():
    result = []
    for number in range(100, 501):  # Range from 100 to 500 (inclusive)
        if number % 3 == 0 and number % 5 == 0:
            result.append(number)
    return result

# Sample usage
numbers = find_numbers()
print(numbers)