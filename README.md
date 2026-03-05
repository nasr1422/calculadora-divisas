# calculadora-divisas

Este proyecto es una calculadora de divisas hecha en Python.  
El programa sirve para convertir una cantidad de dinero de una moneda a otra usando una tasa de cambio.

## Cómo funciona

El programa tiene una función llamada `exchange_money` que recibe:

- `budget`: el dinero que se quiere cambiar.
- `exchange_rate`: la tasa de cambio de la moneda.

La función calcula cuánto dinero se obtiene en la moneda extranjera.

## Fórmula

dinero_extranjero = budget / exchange_rate

## Ejemplo

```python
def exchange_money(budget, exchange_rate):
    dinero_extranjero = budget / exchange_rate
    return dinero_extranjero

print(exchange_money(300, 0.0075))
