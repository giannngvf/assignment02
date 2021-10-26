price_apple = 20
print("The price of the apple is 20 pesos.")
pieces_apple = int(input('How many apples do you want to buy?: '))
price_orange = 25
print("The price of the orange is 25 pesos.")
pieces_orange = int(input('How many oranges do you want to buy?: '))
total_amount = int((price_apple*pieces_apple)+
(price_orange*pieces_orange))
print(f"The total amount is {total_amount}.")