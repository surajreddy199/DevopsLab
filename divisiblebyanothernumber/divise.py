def find_divisibles(n, divisor):
    return [i for i in range(1, n + 1) if i % divisor == 0]

n = 50
divisor = 5
print("Numbers divisible by", divisor, "up to", n, "are:", find_divisibles(n, divisor))
