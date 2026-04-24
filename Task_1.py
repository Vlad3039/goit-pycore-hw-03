from datetime import datetime


def get_days_from_today(date: str) -> int:

    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Некоректний формат дати: '{date}'. Очікується 'РРРР-ММ-ДД'.")

    today = datetime.today().date()
    delta = today - given_date
    return delta.days



if __name__ == "__main__":
    examples = ["2021-10-09", "2020-01-01", "2099-12-31", "2000-06-15", "не-дата"]

    for d in examples:
        try:
            print(f"get_days_from_today('{d}') = {get_days_from_today(d)}")
        except ValueError as e:
            print(f"Помилка: {e}")
