from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:

   today = datetime.today().date()
   upcoming = []
 
   for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
 
        # Підставляємо поточний рік
        birthday_this_year = birthday.replace(year=today.year)
 
        # Якщо цьогорічний день народження вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
 
        delta = (birthday_this_year - today).days
 
        # Вікно — 7 днів (0..6 включно)
        if 0 <= delta <= 6:
            congratulation_date = birthday_this_year
 
            # Субота (5) → +2 дні, Неділя (6) → +1 день
            weekday = congratulation_date.weekday()
            if weekday == 5:          # субота
                congratulation_date += timedelta(days=2)
            elif weekday == 6:        # неділя
                congratulation_date += timedelta(days=1)
 
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })
 
        return upcoming
 
 

if __name__ == "__main__":
    users = [
        {"name": "John Doe",   "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
 
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
 