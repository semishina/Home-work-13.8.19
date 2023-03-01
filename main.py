number_of_tickets = int(input('Введите необходимое количество билетов: '))
ages = []
for i in range(0,number_of_tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}: '))
    ages.append(input_value)
print('_' * 30)
print(f'Количество участников: {number_of_tickets} \nВозраст участников: {ages}')

def price(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    else:
        return 1390

full_price = sum(map(price, ages))
discounted_price = int(full_price * 0.9)
if number_of_tickets > 3:
    print('При покупке более 3-х билетов Ваша скидка составит: 10%. \nСумма к оплате: ', discounted_price, "руб.")
else:
    print('Сумма к оплате: ', full_price, "руб.")
