import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"(https?://(?:www.)?youtu)(be).com/embed(/(\w)+)", s):
        return f"{match.group(1)}.{match.group(2)}{match.group(3)}"
    else:
        return None    





if __name__ == "__main__":
    main()