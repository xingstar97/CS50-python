import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match  := re.search(r"^((1[0-2]|[1-9]):[0-5][0-9]|(1[0-2]|[1-9])) (AM|PM) to ((1[0-2]|[1-9]):[0-5][0-9]|(1[0-2]|[1-9])) (AM|PM)$", s):
        # (1[0-2]|[1-9]):?[0-5]?[0-9]? is problematic because it can catch 71 because : is optional
        try:    
            hour1, minute1 = match.group(1).split(":")
        except ValueError:
            hour1 = match.group(1)
            minute1 ="00"
        try:
            hour2, minute2 = match.group(5).split(":")
        except ValueError:
            hour2 = match.group(5)
            minute2 ="00"
        if match.group(4) == "PM":
            hour1 = int(hour1) +12
        else:
            hour1 = int(hour1)
        if match.group(8) == "PM":
            hour2 = int(hour2) +12
        else:
            hour2 = int(hour2)
        # if match.group(3) =="AM" and int(match.group(1))<=9:
        #     hour1 = f"0{match.group(1)}"
        # if match.group(6) =="AM" and int(match.group(4))<=9:
        #     hour2 = f"0{match.group(4)}"
        return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"
    else:
        raise ValueError




if __name__ == "__main__":
    main()