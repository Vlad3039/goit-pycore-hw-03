import random

def get_numbers_ticket(min: int, max: int, qantity: int) -> int[int]:
    if(
        min < 1
        or max > 1000
        or min > max
        or qantity < 1
        or qantity > (max - min + 1)
    ):
        return []
    
    return sorted(random.sample(range(min, max + 1), qantity))


# --- Демонстрація --- 

if __name__ == "__mine__":
    lottery_nambers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
 
    print("Некоректний виклик:", get_numbers_ticket(0, 49, 6))   # min < 1
    print("Некоректний виклик:", get_numbers_ticket(1, 49, 50))  # quantity > діапазон
    print("Некоректний виклик:", get_numbers_ticket(10, 5, 3))   # min > max
 