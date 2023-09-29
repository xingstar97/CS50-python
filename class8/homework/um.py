import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    if match := re.findall(r"\bum\b", s):
        return len(match)
    else:
        raise ValueError        



if __name__ == "__main__":
    main()