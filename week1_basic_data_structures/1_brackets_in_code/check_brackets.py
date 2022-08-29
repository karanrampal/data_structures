# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            tmp = opening_brackets_stack.pop() if opening_brackets_stack else None
            if not tmp or not are_matching(tmp.char, next):
                return i + 1 

    idx = opening_brackets_stack.pop().position if opening_brackets_stack else 0
    return idx

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch:
        print(mismatch)
    else:
        print("Success")

if __name__ == "__main__":
    main()
