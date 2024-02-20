import matplotlib.pyplot as mpl
import numpy as np

chances = 0.2
lista = list()
epochs = 10000
print("programa para decidir se vou sair ou ficar em casa!")
nsim = 0
for i in np.arange(1, epochs, 1):
    if(np.random.uniform() > chances):
        #print("Sim")
        nsim = nsim + 1
        continue  

print(nsim/epochs)