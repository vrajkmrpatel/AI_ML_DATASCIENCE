# people = ('Mario', 'Luigi', 'Tod')
# numbers = (10, 20, 30)

# zipped = zip(people, numbers)

# print(tuple(zipped))

# a = (1, 2, 3, 4, 5)
# b = (1, 2, 3, 4, 5)

# print(f"a: {id(a)}, b: {id(b)}")
# print(a is b)
# print(a == b)

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# # # Usage: Get the first 10 Fibonacci numbers
# fib_gen = fibonacci_generator() 
# for _ in range(10):
#     print(next(fib_gen))

# print(next(fib_gen))

# def decorator(func):
#     """Decorator exmaple"""
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#     return wrapper

# @decorator
# def greet():
#     print("Hello, World!")
# greet()

# Let's define the function `f(a, b)` as described in the image and calculate its output for f(15, 10).

def f(a, b):
    if a == 0:
        return b
    if a % 2 == 1:
        return 2 * f((a - 1) // 2, b)
    return b + f(a - 1, b)

# Calling the function with the given values (15, 10)
output = f(15, 10)
print(output)