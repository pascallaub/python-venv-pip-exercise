import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Zahl': [0,1,2,3,4,5,6,7,8,9],
    'Quadratzahlen': [i**2 for i in range(10)],
    'Kubikzahlen': [i**3 for i in range(10)]
}

df = pd.DataFrame(data)

df.plot(x='Zahl', y=['Quadratzahlen', 'Kubikzahlen'], kind='line')

plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Werte')

plt.savefig('Diagramm.png')