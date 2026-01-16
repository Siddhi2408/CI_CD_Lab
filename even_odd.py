def is_even(n):
    return n % 2 == 0

# Demo usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if is_even(num):
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
