dates_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


def solve(month, date):
    total_dates = 0
    for i in range(month - 1):
        total_dates += dates_in_months[i]
    total_dates += date

    return weekdays[total_dates % 7 - 1]


def main():
    month, date = input().split(' ')
    month = int(month)
    date = int(date)

    print(solve(month, date))


if __name__ == '__main__':
    main()
