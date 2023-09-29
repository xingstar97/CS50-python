months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if day >31 or month>12:
            pass
        else:
            break
    except ValueError:
        md, year = date.split(",")
        month,day = md.split(" ")
        if month in months:
            month = months.index(month)+1
            day = int(day)
            year = int(year)
            if day>31:
                pass
            else:
                break

    
print(f"{year}-{month}-{day}")