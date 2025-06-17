n = [23, -9, 11, 24, 37, -16, 90, -3, -4, -51]
# a).sum of positive even numbers
positive_even = list(filter(lambda x: x > 0 and x % 2 == 0, n))
import functools

print(functools.reduce(lambda a, b: a + b, positive_even))
# b).sum of positive odd numbers
positive_odd = list(filter(lambda x: x > 0 and x % 2 != 0, n))
import functools

print(functools.reduce(lambda a, b: a + b, positive_odd))
# c)sum of negative even numbers
negative_even = list(filter(lambda x: x < 0 and x % 2 == 0, n))



import functools

print(functools.reduce(lambda a, b: a + b, negative_even))
# d).sum of negative odd numbers
negative_odd = list(filter(lambda x: x < 0 and x % 2 != 0, n))
import functools

print(functools.reduce(lambda a, b: a + b, negative_odd))

# e)count of positive numbers
print(len(list(filter(lambda x: x > 0, n))))
# f).count of negative numbers
print(len(list(filter(lambda x: x < 0, n))))

l = [10, 'hello', 9.8, 'abc', 11, 2, 'arun']
# 1,create a new list with string values from the given sequence.
print(list(filter(lambda x: type(x) == str, l)))
# 2.count of floating point values
print(len(list(filter(lambda x: type(x) == float, l))))
