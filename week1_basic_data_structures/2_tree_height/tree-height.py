# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
from typing import List, Optional, Tuple


class Node:
    def __init__(self, key: Optional[int] = None, children: Optional[List[int]] = None) -> None:
        self.key = key
        self.children = children

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight


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
    tree = TreeHeight()
    tree.read()
    #print(tree.compute_height())

    root, node_list = create_tree(tree.n, tree.parent)
    print(compute_height_fast(root, node_list))

threading.Thread(target=main).start()
