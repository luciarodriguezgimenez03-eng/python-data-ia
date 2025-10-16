import tensorflow as tf


import numpy as np

import matplotlib.pyplot as plt

input_valores = np.array([2,4,6,10,20,60], dtype = float)
output_valores = np.array([31,32,33,35,40,50,60], dtype = float)

capa = tf.keras.layers.Dense(units=1, input_shape = [1])

modelo = tf.keras.Sequential([capa])

modelo.compile(optimizer = tf.keras.optimizers.Adam(0.1), loss = 'mean_squared_error')

print("Vamos al lio, Entrando...")

historial=modelo.fit(input_valores, output_valores, eponch=1000, verbose = False)

print("Por fin entro!!!!!!!!!")

plt.xlabel("A Epoca")
plt.ylabel( "Magnitud de perdida ")
plt.plot(historial.history["loss"])
plt.show()


print( " Probamos al engendro . .")
resultado = modelo.predict([900])
print(resultado)


print( 'Conclusiones del entrenamiento pesos y sesgos ')
print(capa.get_weights())