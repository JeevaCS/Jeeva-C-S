def generate_modified_odd_series(a: int):
    count = a if a % 2 != 0 else a - 1  # if a is even, subtract 1
    result = []
    for i in range(count):
        result.append(2 * i + 1)
    print(", ".join(map(str, result)))
a = int(input("Enter a number: "))
generate_modified_odd_series(a)
