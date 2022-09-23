#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def _is_bst(tree, node, min_val, max_val):
  if node == -1:
    return True
  key, left, right = tree[node]
  if (key < min_val) or (key > max_val):
    return False
  return _is_bst(tree, left, min_val, key - 1) and _is_bst(tree, right, key + 1, max_val)

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
    return True
  return _is_bst(tree, 0, -2**31, 2**31 - 1)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
