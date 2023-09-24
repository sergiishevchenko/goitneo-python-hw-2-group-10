from datetime import datetime

from faker import Faker

fake = Faker()

users = []
for i in range(500):
    users.append(
        {
            'name': fake.name(),
            'birthday': fake.date_between_dates(
                date_start=datetime(1960,1,1),
                date_end=datetime(2010,12,31)
            )
        }
    )


def get_birthdays_per_week(users):
    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    today = datetime.today().date()

    for user in users:
        name = user['name']
        birthday = user['birthday']
        if (birthday.month == 2 and birthday.day == 29):
            day = birthday.day - 1
            birthday_this_year = birthday.replace(year=today.year, day=day)
        else:
            birthday_this_year = birthday.replace(year=today.year)
        delta_days = (birthday_this_year - today).days
        if birthday_this_year >= today and delta_days < 7:
            if birthday.strftime('%A') in result.keys():
                result[birthday.strftime('%A')].append(name)
            else:
                result['Monday'].append(name)

    for key, value in result.items():
        if value:
            print('{}: {}'.format(key, ', '.join(value)))


if __name__ == '__main__':
    get_birthdays_per_week(users)