# Datos x: horas entrenadas de padel al dia, y: torneos ganados al mes
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Calculo de medias
x_media = sum(x) / len(x)
y_media = sum(y) / len(y)

# Calculo de  pendiente
num = sum((xi - x_media) * (yi - y_media) for xi, yi in zip(x, y))
den = sum((xi - x_media) ** 2 for xi in x)
m = num / den
b = y_media - m * x_media

print("Modelo entrenado:")
print(f"y = {m:.2f}x + {b:.2f}")

# Probamos el modelo
x_test = 6
y_test = m * x_test + b
print(f"Si se entrena {x_test} horas, la predicción es de {y_test:.2f} torneos ganados al mes.")
