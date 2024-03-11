from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Determine which colleagues to congratulate on their upcoming birthdays,
    adjusting for weekends.
    
    Parameters:
    - users (list of dicts): Each dict contains 'name' (string) and 'birthday' (string in 'YYYY.MM.DD' format).
    
    Returns:
    - list of dicts: Each dict contains 'name' and 'congratulation_date' (string in 'YYYY.MM.DD' format).
    """
    today = datetime.now()
    upcoming_birthdays = []

    for user in users:
        name = user['name']
        birthday_str = user['birthday']
        birthday = datetime.strptime(birthday_str, '%Y.%m.%d')
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:
                congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays

users_example = [
    {'name': 'Dmotro', 'birthday': '1985.03.10'},
    {'name': 'Simon', 'birthday': '1990.03.16'},
    {'name': 'Artem', 'birthday': '1987.03.18'},
]

upcoming_birthdays_example = get_upcoming_birthdays(users_example)
upcoming_birthdays_example
