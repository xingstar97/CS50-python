from datetime import date, timedelta
import inflect
import sys

p = inflect.engine()

def main():
    try:
        year, month, day = input("Birthday: ").split("-")
    except ValueError:
        sys.exit("Wrong date format!")
    today = date.today()
    birthday = date(year = int(year), month = int(month), day = int(day))
    passed = today - birthday
    passed_minutes = round(passed.total_seconds()/60)
    print(f"{p.number_to_words(passed_minutes)} minutes")
    




if __name__ == "__main__":
    main()