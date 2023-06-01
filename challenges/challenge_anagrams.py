def quick_sort(word):
    if len(word) <= 1:
        return word

    pivot = word[0]
    lesser = ''.join([char for char in word[1:] if char < pivot])
    greater = ''.join([char for char in word[1:] if char >= pivot])

    return quick_sort(lesser) + pivot + quick_sort(greater)


def is_anagram(first_string, second_string):
    first_sorted = quick_sort(first_string.lower())
    second_sorted = quick_sort(second_string.lower())    
    if first_string == '' or second_sorted == '':
        return (first_sorted, second_sorted, False)
    return (first_sorted, second_sorted, first_sorted == second_sorted)