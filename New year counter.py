def add_days(year, month, day, k):
    """
    Returns the date (year, month, day) that is k days after the input date,
    under the simplifying assumption:
      - 1 year = 360 days
      - 1 month = 30 days
    """

    # 1. Convert the input date to a total-day count from a "zero" reference point.
    #    We subtract 1 from month and day so that:
    #      - if month=1 and day=1, that means 0 complete months and 0 complete days have passed this year.
    total_days = (year * 360) + ((month - 1) * 30) + (day - 1)

    # 2. Add k days to the total day count
    total_days += k

    # 3. Compute the new year from total_days (integer division by 360)
    new_year = total_days // 360

    # 4. Compute how many days remain after counting off full years
    remaining_days = total_days % 360

    # 5. Compute the new month (integer division by 30, plus 1)
    new_month = (remaining_days // 30) + 1

    # 6. Compute the new day (remainder after removing full months, plus 1)
    new_day = (remaining_days % 30) + 1

    # 7. Return the resulting date
    return new_year, new_month, new_day
y, m, d = 2025, 10, 1
k = 80
new_y, new_m, new_d = add_days(y, m, d, k)
print(add_days(y, m, d, k))
