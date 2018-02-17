import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
training_epochs = 100

x_train = np.linspace(1, 80, 80)
y_train = -2 * x_train + np.random.randn(*x_train.shape) * 10

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

def model(X, w):
    return tf.multiply(w, X)

w = tf.Variable(0.0, name="Weights")

y_model = model(X, w) 
cost = tf.square(Y-y_model)

training_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

session = tf.Session()
init = tf.global_variables_initializer()
session.run(init)

for epoch in range(training_epochs):
    for (x, y) in zip(x_train, y_train):
        session.run(training_op, feed_dict={X: x, Y: y})

w_val = session.run(w)


session.close()
plt.scatter(x_train, y_train)
y_learned = x_train*w_val
plt.plot(x_train, y_learned, 'r')
plt.show()