def generate_odd_series(a: int):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    print(", ".join(map(str, result)))

a = int(input("Enter a number: "))
generate_odd_series(a)
