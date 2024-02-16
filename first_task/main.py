from datetime import datetime, timedelta


def unpack_schedule(schedule: list[tuple[datetime, datetime]]) -> str:
    '''
    Функция итерируется по списку с датами начала и конца сеанса и
    выводит все даты когда проходит показ фильма.

    :param schedule: list[tuple[datetime, datetime]]
    :return: str
    '''
    result = ''
    for start_date, end_date in schedule:
        current_date = start_date
        while current_date <= end_date:
            result += f"{current_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            current_date += timedelta(days=1)
    return result


result = (
    '2020-01-01 00:00:00\n'
    '2020-01-02 00:00:00\n'
    '2020-01-03 00:00:00\n'
    '2020-01-04 00:00:00\n'
    '2020-01-05 00:00:00\n'
    '2020-01-06 00:00:00\n'
    '2020-01-07 00:00:00\n'
    '2020-01-15 00:00:00\n'
    '2020-01-16 00:00:00\n'
    '2020-01-17 00:00:00\n'
    '2020-01-18 00:00:00\n'
    '2020-01-19 00:00:00\n'
    '2020-01-20 00:00:00\n'
    '2020-01-21 00:00:00\n'
    '2020-01-22 00:00:00\n'
    '2020-01-23 00:00:00\n'
    '2020-01-24 00:00:00\n'
    '2020-01-25 00:00:00\n'
    '2020-01-26 00:00:00\n'
    '2020-01-27 00:00:00\n'
    '2020-01-28 00:00:00\n'
    '2020-01-29 00:00:00\n'
    '2020-01-30 00:00:00\n'
    '2020-01-31 00:00:00\n'
    '2020-02-01 00:00:00\n'
    '2020-02-02 00:00:00\n'
    '2020-02-03 00:00:00\n'
    '2020-02-04 00:00:00\n'
    '2020-02-05 00:00:00\n'
    '2020-02-06 00:00:00\n'
    '2020-02-07 00:00:00\n'
)
assert unpack_schedule([
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))]) == result
