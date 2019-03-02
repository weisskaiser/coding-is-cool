
def k_substring_length(string, k):

    state_length = [[0 for _ in string] for _ in string]
    state = [set() for _ in string]
    
    for i,_ in enumerate(string):

        can_add = True
        for j in range(i,len(string)):
            
            c = string[j]
            
            if not can_add:
                state_length[i][j] = state_length[i][j-1]
                continue

            elif len(state[i]) == k and c in state[i]:
                state_length[i][j] = state_length[i][j-1] + 1
                
            elif len(state[i]) == k and c not in state[i]:
                can_add = False
                state_length[i][j] = state_length[i][j-1]

            elif len(state[i]) < k:

                state[i].add(c)
                if (i == j):
                    state_length[i][j] = 1
                else:
                    state_length[i][j] = state_length[i][j-1] + 1

    return max([lengths[-1] for lengths in state_length])

assert k_substring_length("abcba", 2) == 3