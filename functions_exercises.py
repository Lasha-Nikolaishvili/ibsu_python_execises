square = lambda x: x**2
print(square(5))

square_sum = lambda x, y: x**2 + y**2
print(f"Sum of squares of 3 and 4 is {square_sum(3,4)}")

is_even = lambda x: x % 2 == 0
print(is_even(9))
print(is_even(10))


my_list = list(range(1, 10))
even_nums = list(filter(is_even, my_list))
print(even_nums)


squared_nums = list(map(square, my_list))
print(squared_nums)


# Variable Arguments
def greetings(*names):
    for name in names:
        print(name)

greetings("Lasha", "Nika", "Guram", "Dato")


# Nested Functions
def num1(x):
    def num2(y):
        return x*y
    return num2

# res = num1(10)

print(num1(5)(10))