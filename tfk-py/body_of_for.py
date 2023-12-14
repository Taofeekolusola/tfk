iter_obj = iter(iterable)

while True:
    try:
        item = next(iter_obj)
        print(item)
    except StopIteration:
        break
