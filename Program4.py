input_str = input("Enter numbers separated by commas: ")
numbers = list(map(int, input_str.split(',')))
multiples_count = {}
for i in range(1, 10):
    count = sum(1 for num in numbers if num % i == 0)
    multiples_count[i] = count
print(multiples_count)
