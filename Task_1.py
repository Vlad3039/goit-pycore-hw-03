from datetime import datetime
def get_days_from_today(date: str) -> int:

    try:
        given_data = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Некоректний формат дати: '{date}'. Очікується 'РРРР-ММ-ДД'.")
    
    today = datetime.today().date()
    delta = today - given_data
    return delta.days



if __name__ == "__main__":
    examples = ["2021-10-09", "2020-01-01", "2099-12-31", "2000-06-15"]
    for d in examples:
        print(f"get_days_from_today('{d}') = {get_days_from_today(d)}")



try:
    get_days_from_today("не-дата")
except ValueError as e:
    print(f"Помилка: {e}")