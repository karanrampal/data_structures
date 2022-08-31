# python3

class QueueWithMax:
    def __init__(self):
        self.__queue = []
        self.__max = []

    def Enque(self, a):
        self.__queue.append(a)
        while self.__max and (a > self.__max[-1]):
            self.__max.pop(-1)
        self.__max.append(a)

    def Deque(self):
        assert len(self.__queue)
        val = self.__queue.pop(0)
        if val == self.__max[0]:
            self.__max.pop(0)

    def Max(self):
        assert len(self.__queue)
        return max(self.__queue)
    
    def Max_fast(self):
        assert len(self.__queue) 
        return self.__max[0]

    def Size(self):
        return len(self.__queue)


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window_fast(sequence, m):
    maximums = []
    q = QueueWithMax()
    for i in sequence:
        if q.Size() == m:
            maximums.append(q.Max_fast())
            q.Deque()
        q.Enque(i)
    maximums.append(q.Max_fast())

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window_fast(input_sequence, window_size))

