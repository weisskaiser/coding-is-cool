class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def count_unival(tree):
    return count_unival_subtrees(tree)[0]

def count_unival_subtrees(tree):

    if not tree.left and not tree.right:
        return 1,True

    left, left_is_unival = count_unival(tree.left) if tree.left else 0,True
    right, right_is_unival = count_unival(tree.right) if tree.right else 0,True
    
    c_is_unival = left_is_unival and right_is_unival
    c_is_unival = c_is_unival and not tree.right or tree.value == tree.right.value 
    c_is_unival = c_is_unival and not tree.left or tree.value == tree.left.value

    found_unival = left + right + (1 if c_is_unival else 0)

    return found_unival, c_is_unival

def is_unival(tree):

    if tree.left:
        left = tree.left.value == tree.value and is_unival(tree.left)
    else:
        left = True

    if tree.right:
        right = tree.right.value == tree.value and is_unival(tree.right)
    else:
        right = True

    return right and left

assert is_unival(Node(0))
assert not is_unival(Node(0,Node(1)))
assert is_unival(Node(0,right=Node(0)))
assert is_unival(Node(0,Node(0)))
assert is_unival(Node(0,Node(0,Node(0))))

assert count_unival(Node(0,Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))) == 5