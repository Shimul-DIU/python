def even_gt_10():
    for i in range(1, 21):
        if i > 10 and i % 2 == 0:
            yield i  # yield returns a value one by one

# Using the generator
numbers = list(even_gt_10())  # Convert generator to list
print(numbers)