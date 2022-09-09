# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def poly_hash(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans

def pre_compute_hashes(text, n, p, x):
    H = [0] * (len(text) - n + 1)
    S = text[len(text) - n:]
    H[-1] = poly_hash(S, p, x)
    y = 1
    for _ in range(1, n + 1):
        y = (y * x) % p
    for i in range(len(text) - n - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + n])) % p
    return H

def rabin_karp(pattern, text):
    x, p = 263, 1000000007
    pos = []
    p_hash = poly_hash(pattern, p, x)
    H = pre_compute_hashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            pos.append(i)
    return pos


if __name__ == '__main__':
    #print_occurrences(get_occurrences(*read_input()))
    print_occurrences(rabin_karp(*read_input()))

