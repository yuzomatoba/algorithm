def find_duplicate(nums):
    stored_elements = set()

    for num in nums:
        if type(num) != int or num < 0:
            return False

        if num in stored_elements:
            return num

        stored_elements.add(num)

    return False
