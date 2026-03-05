def exchange_money(budget, exchange_rate):
    dinero_extranjero = budget / exchange_rate
    return dinero_extranjero

# Japón
resultado_japon = exchange_money(500, 0.0075)
print("Yenes:", resultado_japon)

# México
resultado_mexico = exchange_money(1000, 0.058)
print("Pesos Mexicanos:", resultado_mexico)

# Colombia
resultado_colombia = exchange_money(5000, 0.00025)
print("Pesos Colombianos:", resultado_colombia)
