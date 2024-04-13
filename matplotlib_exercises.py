import matplotlib.pyplot as plt
import numpy as np


# k, b = 3, 2
# x = np.arange(-20, 20, 0.001)
# y = k * x + b
# plt.plot(x, y, label="y=$3*x+$2")
# plt.xlabel("x is between [-20, 20]")
# plt.ylabel("y")
# plt.title("y = 3x + 2")
# plt.legend()
# plt.xlim([-10, 10])
# plt.ylim([-15, 15])
# plt.show()

# x = np.arange(-20, 20, 0.001)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, '--r', label="sin(x)")
# plt.plot(x, y2, '--g', label="cos(x)")
# plt.legend(loc='best')
# plt.ylim([0, 1])
# plt.show()

# price = np.array([15, 16, 20, 30, 35, 40, 41])
# demand = np.array([8, 7, 4, 3, 2, 1.5, -0.5])
#
# plt.scatter(price, demand)
# plt.xlabel("price")
# plt.ylabel("demand")
# plt.savefig('./plots/price_demand_scatter_plot.png')
# plt.show()

# x = np.arange(-4, 4, 0.001)
# y1 = 3*x + 2
# y2 = x**2
# y3 = x**3
# y4 = x**4
#
# plt.figure("Function Subplots")
# plt.subplot(2, 2, 1)
# plt.plot(x, y1)
# plt.title("3x + 2")
# plt.subplot(2, 2, 2)
# plt.plot(x, y2)
# plt.title("x^2")
# plt.subplot(2, 2, 3)
# plt.plot(x, y3)
# plt.title("x^3")
# plt.subplot(2, 2, 4)
# plt.plot(x, y4)
# plt.title("x^4")
# plt.savefig('./plots/function_plots.png')
# plt.show()

# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)
# y1 = np.cos(x)

# fig, ax = plt.subplots(2)
# fig.suptitle("Trigonometric Functions")
# ax[0].plot(x, y)
# ax[1].plot(x, y1)
# plt.show()

# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('Vertically stacked subplots')
# ax1.plot(x, y)
# ax2.plot(x, -y)
# plt.show()

# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('Horizontally stacked subplots')
# ax1.plot(x, y)
# ax2.plot(x, -y)
# plt.show()

# x = np.linspace(0, 2*np.pi, 400)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)
# y4 = np.sqrt(x)
#
# fig, axs = plt.subplots(2, 2)
#
# axs[0, 0].plot(x, y1)
# axs[0, 0].set_title('Sin(x)')
# axs[0, 1].plot(x, y2, 'tab:orange')
# axs[0, 1].set_title('Cos(x)')
# axs[1, 0].plot(x, y3, 'tab:green')
# axs[1, 0].set_title('Tan(x)')
# axs[1, 1].plot(x, y4, 'tab:pink')
# axs[1, 1].set_title('Sqrt(x)')
#
# plt.show()


def demand(x):
    return -x + 10


data = np.arange(1, 10, 1)
plt.plot(data, demand(data), linewidth=1.0)
plt.axis((0, 10, 0, 10))
plt.xticks([])
plt.yticks([])
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.annotate("Demand", xy=(1.2, 9.5))
plt.show()
