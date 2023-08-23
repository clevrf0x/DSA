def main():
    try:
        number = abs(int(input()))
        while True:
            print(number, end=" ")
            if number == 1:
                break
            elif number % 2 == 0:
                number = number // 2
            else:
                number = number * 3 + 1

    except ValueError:
        print("Invalid value")
        exit(0)


if __name__ == "__main__":
    main()
