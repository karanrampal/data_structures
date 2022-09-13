# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 10**9 + 7
        self.m2 = 10**9 + 9
        self.x = 263
        self._precompute()

    def _precompute(self):
        self.h1 = [0] * (len(self.s) + 1)
        self.h2 = [0] * (len(self.s) + 1)
        for i in range(1, len(self.s) + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
            self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

    def ask_fast(self, a, l):
        h1al = (self.h1[a + l] - pow(self.x, l, self.m1) * self.h1[a]) % self.m1
        h2al = (self.h2[a + l] - pow(self.x, l, self.m2) * self.h2[a]) % self.m2
        return h1al, h2al

def solve(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
                    ans = Answer(i, j, l)
    return ans

def solve_fast(s, t):
    ss = Solver(s)
    tt = Solver(t)
    ans = Answer(0, 0, 0)
    low, high = 1, min(len(s), len(t))
    while low <= high:
        mid = (low + high) // 2
        table1, table2 = {}, {}
        for i in range(len(s) - mid + 1):
            h1sl, h2sl = ss.ask_fast(i, mid)
            table1[h1sl] = i
            table2[h2sl] = i
        for j in range(len(t) - mid + 1):
            h1tl, h2tl = tt.ask_fast(j, mid)
            if (h1tl in table1) and (h2tl in table2):
                low = mid + 1
                ans = Answer(table1[h1tl], j, mid)
                break
        else:
            high = mid - 1

    return ans

for line in sys.stdin.readlines():
    s, t = line.split()
    #ans = solve(s, t)
    ans = solve_fast(s, t)
    print(ans.i, ans.j, ans.len)
