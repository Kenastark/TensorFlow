# useful link https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l02c01_celsius_to_fahrenheit.ipynb#scrollTo=pRllo2HLfXiu

import tensorflow as tf
import numpy as np
import logging
#logger = tf.get_logger()
#logger.setLevel(logging.ERROR)

celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

for i,c in enumerate(celsius_q):
  print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

# The Sequential model definition takes a list of layers as an argument, specifying the calculation order from the input to the output.
model = tf.keras.Sequential([l0])

# Compile the model, with loss and optimizer functions
model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))

# train the model
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

# display training statistics
import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])

# use the model to predict values
print(model.predict([100.0]))

# print the internal variables of the Dense layer.
print("These are the layer variables: {}".format(l0.get_weights()))

