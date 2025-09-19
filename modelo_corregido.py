import pandas as pd

# Cargar dataset
df = pd.read_csv("tennis_matches.csv")

# Filtrar por mujeres
df = df[df["league"] == "wta"]

# Agrupar por jugadora 
# x = promedio de puntos de ranking
# y = cantidad de torneos ganados distintos
df_grouped = df.groupby("winner_name").agg({
    "winner_rank_points": "mean",
    "tourney_id": pd.Series.nunique
}).reset_index()

x = df_grouped["winner_rank_points"].tolist()
y = df_grouped["tourney_id"].tolist()


# Medias
x_media = sum(x) / len(x)
y_media = sum(y) / len(y)

# Pendiente
num = sum((xi - x_media) * (yi - y_media) for xi, yi in zip(x, y))
den = sum((xi - x_media) ** 2 for xi in x)
m = num / den
b = y_media - m * x_media

print("Modelo entrenado:")
print(f"y = {m:.2f}x + {b:.2f}")

# Probamos el modelo
x_test = 3000  # ejemplo: jugadora con 3000 puntos de ranking
y_test = m * x_test + b
print(f"Si una jugadora tiene {x_test} puntos de ranking promedio, "
      f"la predicción es de {y_test:.2f} torneos ganados.")
