import random

number_to_guess = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. У тебе є 3 спроби вгадати його.")

for i in range(attempts):
    try:
        guess = int(input(f"Спроба {i + 1}: "))
        
        if guess == number_to_guess:
            print("Вітаю! Ти вгадав число!")
            break
        elif guess > number_to_guess:
            print("Менше")
        else:
            print("Більше")
            
        if i == attempts - 1:
            print(f"На жаль, спроби закінчилися. Я загадав число {number_to_guess}.")
    except ValueError:
        print("Будь ласка, введіть число.")
