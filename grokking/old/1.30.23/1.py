class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if root is None:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)


def find_path_recursive(currentNode, sequence, sequenceIndex):

    if currentNode is None:
        return False

    seqLen = len(sequence)
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False

    # if the current node is a leaf, add it is the end of the sequence, we have found
    # a path!
    if (
        currentNode.left is None
        and currentNode.right is None
        and sequenceIndex == seqLen - 1
    ):
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return find_path_recursive(
        currentNode.left, sequence, sequenceIndex + 1
    ) or find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
