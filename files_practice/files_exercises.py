my_file = open("message.txt", 'w')
my_file.write("I love Python\n")
my_file.close()

my_file = open("message.txt", 'a')
my_file.write("Python is great for machine learning")
my_file.close()

my_file = open("message.txt")
print(my_file.read(3))
my_file.close()

my_file = open('message.txt')
print(my_file.readline())
print(my_file.readline())
my_file.close()

my_file = open('message.txt')
print(my_file.readlines())

my_file = open("hundred.txt", 'w')
for i in range(100):
    my_file.write("{}".format(i))
    my_file.write("\n")
my_file.close()

my_file = open("hundred.txt", 'r')
data = list(map(int, my_file.read().splitlines()))
my_file.close()
print(data)

import numpy as np

# X = np.arange(0, 1000, 0.01)
# Y = X ** 2
# my_file = open("parabole.txt", 'w')
# np.savetxt(my_file, np.c_[X, Y])
# my_file.close()

# import pandas as pd
#
# data = pd.read_table("parabole.txt", header=None, sep=' ')
# data.columns =["X","X^2"]
# print(data.head())
