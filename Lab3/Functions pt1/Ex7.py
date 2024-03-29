def spy_game(nums):
    zero_count = 0
    for num in nums:
        if num == 0 and zero_count < 2:
            zero_count += 1
        elif num == 7 and zero_count == 2:
            return True
    return False

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False
