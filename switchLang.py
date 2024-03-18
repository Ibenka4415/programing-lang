def add(m, n):
    if n == 1:
        return m + 1
    else:
        return add(m, n - 1) + 1

def plus(m, n):
    if n > 1:
        return plus(m, n - 1) + 1
    else:
        return m + 1
    
m = 5
n = 3

new = plus(m, n)
result = add(m, n)
print(f"{m} + {n} = {result}")
print(f"plus({m}, {n}) = {new}")
