steps_possibility = (1,2,3,4)

def count_possible_steps(steps:int)->int:

    steps += 1

    possible = [0 for _ in range(steps)]

    for i in range(steps):
        
        c_pos = 0
        for p in steps_possibility:
            if i - p > 0:
                c_pos += possible[i - p]
            elif i - p == 0:
                c_pos += 1
            elif i - p < 0:
                break
   
        possible[i] = c_pos
    return possible.pop()

assert count_possible_steps(1) == 1
assert count_possible_steps(2) == 2
assert count_possible_steps(4) == 8