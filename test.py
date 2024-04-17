""" def func():
    temp = (lambda x :x * i for i in range(4))
    return temp
for i in func():
    print(i(3))


numbers = (i for i in range(5))

for number in numbers:
    print(number) """
""" 
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number) """
""" numbers = (i for i in range(5))

for number in numbers:
    print(number)
print(numbers) """

def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in r:
    print(i)

