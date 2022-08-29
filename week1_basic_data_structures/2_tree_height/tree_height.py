# python3

import sys
import threading
from typing import List, Optional, Tuple


class Node:
    def __init__(self, key: Optional[int] = None, children: Optional[List[int]] = None) -> None:
        self.key = key
        self.children = children


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def create_tree(n: int, parents: List[int]) -> Tuple[int, List[Node]]:
    node_list = [Node(i, []) for i in range(n)]
    for i, parent_idx in enumerate(parents):
        if parent_idx == -1:
            root = i
        else:
            node_list[parent_idx].children.append(i)

    return root, node_list

def compute_height_fast(root, node_list):
    cur, next = [root], []
    height = 0
    while cur:
        idx = cur.pop(0)
        next += node_list[idx].children
        if not cur:
            height += 1
            cur, next = next, cur

    return height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    #print(compute_height(n, parents))

    root, node_list = create_tree(n, parents)
    print(compute_height_fast(root, node_list))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
