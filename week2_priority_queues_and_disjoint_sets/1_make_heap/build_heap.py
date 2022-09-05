# python3
from typing import List, Tuple

class BinaryMinHeap:
    def __init__(self):
        self.heap = []

    def size(self) -> int:
        return len(self.heap)

    def get_parent(self, i: int) -> int:
        return (i - 1 ) // 2 if i > 0 else 0

    def left_child(self, i: int) -> int:
        return i * 2 + 1

    def right_child(self, i: int) -> int:
        return (i + 1) * 2

    def sift_up(self, i: int) -> None:
        while (i > 0) and (self.heap[self.get_parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.get_parent(i)] = self.heap[self.get_parent(i)], self.heap[i]
            i = self.get_parent(i)

    def sift_down(self, i: int) -> None:
        cur = i
        left = self.left_child(i)
        if (left < self.size()) and (self.heap[left] < self.heap[cur]):
            cur = left
        right = self.right_child(i)
        if (right < self.size()) and (self.heap[right] < self.heap[cur]):
            cur = right
        if cur != i:
            self.heap[cur], self.heap[i] = self.heap[i], self.heap[cur]
            self.sift_down(cur)

    def sift_down_iterative(self, i: int) -> List[Tuple[int]]:
        swaps = []
        queue = [i]
        while queue:
            cur = i = queue.pop(0)
            left = self.left_child(i)
            if (left < self.size()) and (self.heap[left] < self.heap[cur]):
                cur = left
            right = self.right_child(i)
            if (right < self.size()) and (self.heap[right] < self.heap[cur]):
                cur = right
            if cur != i:
                self.heap[cur], self.heap[i] = self.heap[i], self.heap[cur]
                swaps.append((i, cur))
                queue.append(cur)

        return swaps

    def insert(self, x: int) -> None:
        self.heap.append(x)
        self.sift_up(self.size() - 1)

    def get_min(self) -> int:
        return self.heap[0]

    def extract_min(self) -> int:
        res = self.heap[0]
        self.heap[0] = self.heap[self.size() - 1]
        self.heap.pop()
        self.sift_down(0)
        return res

    def remove(self, i: int) -> None:
        self.heap[i] = self.get_min() - 1
        self.sift_up(i)
        self.extract_min()

    def change_priority(self, i: int, p: int) -> None:
        old_p = self.heap[i]
        self.heap[i] = p
        if p > old_p:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def build_heap(self, arr: List[int]) -> None:
        self.heap = arr
        for i in range(self.size() // 2, -1, -1):
            self.sift_down(i)
    
    def find_swaps(self, arr: List[int]) -> List[Tuple[int]]:
        self.heap = arr
        swaps = []
        for i in range(self.size() // 2, -1, -1):
            swaps += self.sift_down_iterative(i)

        return swaps

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    #swaps = build_heap(data)
    bmh = BinaryMinHeap()
    swaps = bmh.find_swaps(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
