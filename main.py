
import numpy as np


def print_array_info(name, array):
    print(f"\n--- {name} ---")
    print("Масив:", array)
    print("Тип масиву:", type(array))
    print("Тип елементів:", array.dtype)
    print("Форма:", array.shape)
    print("Кількість елементів (len):", len(array))
    print("Кількість елементів (size):", array.size)


prices = np.array([120, 250, 500, 750, 1000])
quantities = np.array([5, 3, 8, 2, 4])
discounts = np.array([10, 15, 0, 20, 5])


print("1. ІНФОРМАЦІЯ ПРО МАСИВИ")

print_array_info("prices", prices)
print_array_info("quantities", quantities)
print_array_info("discounts", discounts)


print("\n2. АРИФМЕТИЧНІ ОПЕРАЦІЇ")

total_sales = prices * quantities
print("Загальна вартість проданих товарів:", total_sales)

discounts = discounts + 3
print("Знижки після збільшення на 3%:", discounts)

prices_after_discount = prices * (1 - discounts / 100)
print("Ціни після знижок:", prices_after_discount)


print("\n3. ОПЕРАТОРИ ПОРІВНЯННЯ")

print("Ціни понад 500 грн:", prices[prices > 500])

print("Ціни від 200 до 800 грн:",
      prices[(prices >= 200) & (prices <= 800)])

print("Товари ціною рівно 500 грн:", prices[prices == 500])


print("\n4. ЛОГІЧНІ ОПЕРАТОРИ")

print("Ціни менші за 300 або більші за 800 грн:",
      prices[(prices < 300) | (prices > 800)])

print("Ціни, що не перевищують 500 грн:",
      prices[~(prices > 500)])

print("Товари дорожчі за 200 грн і з кількістю продажів понад 3:",
      prices[(prices > 200) & (quantities > 3)])


print("\n5. РОЗРАХУНОК ЗНИЖОК")

discount_20 = prices * 0.20
print("Знижка 20% для кожного товару:", discount_20)

individual_discount = prices * (discounts / 100)
print("Індивідуальна сума знижки:", individual_discount)

final_prices = prices - individual_discount
print("Кінцева вартість товарів:", final_prices)


print("\n6. ІНДЕКСАЦІЯ ТА ЗРІЗИ")

print("Ціна першого товару:", prices[0])
print("Ціна останнього товару:", prices[-1])

print("Перші три ціни:", prices[:3])

prices[1] = 300
print("Після зміни ціни другого товару:", prices)

print("Ціни у зворотному порядку:", prices[::-1])


print("\n7. ЗМІНА ТА ДОПОВНЕННЯ МАСИВУ")

prices = np.append(prices, 1500)
print("Після додавання ціни 1500:", prices)

prices = np.insert(prices, 2, 400)
print("Після вставлення ціни 400 на третю позицію:", prices)

prices = np.delete(prices, 0)
print("Після видалення першого товару:", prices)


print("\n8. ДОДАТКОВІ ОПЕРАТОРИ ТА МЕТОДИ NUMPY")

prices += 100
print("Ціни після збільшення на 100 грн:", prices)

quantities *= 2
print("Кількість товарів після подвоєння:", quantities)

print("Повні набори по 100 грн:", prices // 100)

print("Залишок від ділення цін на 100:", prices % 100)

prices_with_minimum = np.where(prices < 300, 300, prices)
print("Ціни після заміни значень менше 300 грн:",
      prices_with_minimum)

print("Унікальні ціни:", np.unique(prices))

print("Відсортовані ціни:", np.sort(prices))

print("Ціни в діапазоні від 200 до 800 грн:",
      np.clip(prices, 200, 800))
