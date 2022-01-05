def get_day(day, is_leap):
    months_days = {"January": 31, "February": 28, "March": 31, "April": 30,
                   "May": 31, "June": 30, "July": 31, "August": 31, "September": 30,
                   "October": 31, "November": 30, "December": 31}
    if is_leap:
        months_days["February"] = 29
    if not is_leap:
        months_days["February"] = 28

    for month in months_days:
        if day <= months_days[month]:
            return f"{month}, {day}"
        day -= months_days[month]
    return "wrong day"


print(get_day(78, False))
