# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
  
  def _inOrder(self, node: int) -> int:
    if node == -1:
      return
    self._inOrder(self.left[node])
    self.result.append(self.key[node])
    self._inOrder(self.right[node])

  def _preOrder(self, node: int) -> int:
    if node == -1:
      return
    self.result.append(self.key[node])
    self._preOrder(self.left[node])
    self._preOrder(self.right[node])

  def _postOrder(self, node: int) -> int:
    if node == -1:
      return
    self._postOrder(self.left[node])
    self._postOrder(self.right[node])
    self.result.append(self.key[node])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._inOrder(0)
                
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._preOrder(0)
                
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._postOrder(0)
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
