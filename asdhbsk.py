'''pessoas = ['Joao', 'Melissa', 33, 25, 'Jorje', 12]

for p in pessoas:
    print(p)

Dessa forma, mostra na tela todos os itens da lista'''
'''from operator import attrgetter, itemgetter
Student = list()
Student.append(['john', 'A', 15])
Student.append(['jane', 'B', 12])
Student.append(['dave', 'B', 10])
print(Student)
sorted(Student, key=attrgetter(0), reverse=False)'''

'''tupla = 1, 5, 7
print(tupla)
if 7 in tupla == False:
    print('Tem na tupla')'''

'''n = int(input('Digite um número float: '))
print(f'{n!a}')'''

'''student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2], reverse= False))
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=attrgetter('age')))'''


'''from operator import  itemgetter
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(data)
print(sorted(data, key=itemgetter(0)))'''

'''import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
model = keras.Sequential(
model=keras.Sequential(
        [
            layers.Dense(2, activation="relu", name="layer1"),
            layers.Dense(3, activation="relu", name="layer2"),
            layers.Dense(4, name="layer3"),
        ]
    )
model.pop()
print(model)'''


import tensorflow as tf
import numpy as np
#import matplotlib.pyplot as plt
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

celsius_q = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

for i,c in enumerate(celsius_q):
  print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))
print(end='\n')

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

model = tf.keras.Sequential([l0])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)

model.predict([100.0])
print("\nEnd.")