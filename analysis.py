import pandas as pd
import matplotlib.pyplot as plt

# Daten manuell eingeben (oder später CSV einlesen)
data = pd.DataFrame({
    "occupation": ["CEO", "CEO"],
    "gender": ["male", "female"],
    "count": [102, 9]
})

# Prozent berechnen
data["percentage"] = data["count"] / data["count"].sum() * 100

print(data)

# Diagramm erstellen
plt.bar(data["gender"], data["count"])
plt.title("Geschlechterverteilung CEO in Deutschland")
plt.xlabel("Geschlecht")
plt.ylabel("Anzahl")
plt.show()
``
