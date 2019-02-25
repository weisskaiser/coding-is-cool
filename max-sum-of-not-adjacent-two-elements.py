
def max_sum_not_adjacent(numbers):
    
    if not numbers:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    max_sum = max(max_sum_not_adjacent(numbers[2:])+numbers[0],max_sum_not_adjacent(numbers[1:]))

    return max_sum

def max_sum_not_adjacent_dyn(numbers):

    max_sum = [0 for _ in numbers]

    for i,n in enumerate(numbers):
        
        if i == 0:
            max_sum[i] = n
        elif i == 1:
            max_sum[i] = max(max_sum[i-1],n)
        else:
            max_sum[i] = max(max_sum[i-1],n + max_sum[i-2])

    return max_sum.pop()

assert max_sum_not_adjacent_dyn([1, 20, 3]) == 20
assert max_sum_not_adjacent_dyn([2, 4, 6, 2, 5]) == 13
assert max_sum_not_adjacent_dyn([5, 1, 1, 5]) == 10

assert max_sum_not_adjacent([1, 20, 3]) == 20
assert max_sum_not_adjacent([2, 4, 6, 2, 5]) == 13
assert max_sum_not_adjacent([5, 1, 1, 5]) == 10