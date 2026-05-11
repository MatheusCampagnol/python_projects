sum = 0

def main():
    print("Welcome to the Gauss Challenge!")

    for n in range(1, 101):
        sum = n * (n + 1) // 2
    print(sum)

if __name__ == "__main__":
    main()