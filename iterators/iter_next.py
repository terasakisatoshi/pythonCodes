def count():
    c = 0
    while True:
        yield c
        c += 1

gen = count()

print(next(gen)) # 0と表示
print(next(gen)) # 1と表示
print(next(gen)) # 2と表示
print(next(gen)) # 3と表示