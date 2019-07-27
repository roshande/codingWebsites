num_of_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:30,8:31,9:30,10:31,11:30,12:31}
even_days_months = [4,6,7,9,11]
odd_days_months = [1,3,5,8,10,12]

def faults(date):
    year, month, day = list(map(int,date.split(":")))
    if not is_leap_year(year):
        if day %2 == 0:
            total_days = (num_of_days[month] - day)//2
            if month not in [*even_days_months,2]:
                total_days += num_of_days[month+1]//2
        else:


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

for _ in range(int(input())):
    date = input()
    print(faults(date))
