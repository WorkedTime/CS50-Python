def convert(time):

    time = time.strip().lower()
    if 'am' in time or 'pm' in time:
        time, period = time.split()
        hours, minutes = map(int, time.split(':'))

        if period == 'pm' and hours != 12:
            hours += 12
        elif period == 'am' and hours == 12:
            hours = 0
    else:
        hours, minutes = map(int, time.split(':'))

    return hours + minutes / 60

def main():

    try:
        time_str = input('What time is it? ').strip()
        time_float = convert(time_str)

        if 7 <= time_float <= 8:
            print('breakfast time')
        elif 12 <= time_float <= 13:
            print('lunch time')
        elif 18 <= time_float <= 19:
            print('dinner time')
    except ValueError:
        print('Formato inválido. Use HH:MM ou HH:MM AM/PM.')

if __name__ == '__main__':
    main()
