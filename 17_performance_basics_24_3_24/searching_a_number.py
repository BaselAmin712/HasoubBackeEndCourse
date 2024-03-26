import time
def linear_search(number, number_list):
    for num in number_list:
        if num == number:
            return True
    return False

# Example usage:
numbers = [2, 4, 6, 8, 10]
searched_number = 6
start = time.time()
result = linear_search(searched_number, numbers)
end = time.time()
print(f"The number {searched_number} {'is' if result else 'is not'} found in the list.")
print(1000*(start - end))

#########################


def binary_search(number, number_list):
    left, right = 0, len(number_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if number_list[mid] == number:
            return True
        elif number_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example usage:
numbers = [2, 4, 6, 8, 10]
searched_number = 6
result = binary_search(searched_number, numbers)
print(f"The number {searched_number} {'is' if result else 'is not'} found in the list.")