import matplotlib.pyplot as plot
import pandas as pan

data = { 'Zahl': [0,1,2,3,4,5,6,7,8,9], 'Quadratzahl': [i**2 for i in range(10)], 'Kubikzahl': [i**3 for i in range (10)]}

xy = pan.DataFrame(data)
xy.plot(x='Zahl', y=['Quadratzahl','Kubikzahl'], kind='line')
plot.title('Quadrat und Kubikzahl von 0-9')
plot.xlabel('Zahl')
plot.ylabel('Wert')
plot.savefig('Kurvendings.png')