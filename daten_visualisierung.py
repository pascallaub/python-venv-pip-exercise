import matplotlib.pyplot as plt

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen

x3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y3 = [i**3 for i in x3]

# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')
plt.plot(x3, y3, label='Kubikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadratzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Quadrat/Kubik')

# Legende anzeigen
plt.legend()

# Diagramm anzeigen
plt.savefig('Diagramm.png')