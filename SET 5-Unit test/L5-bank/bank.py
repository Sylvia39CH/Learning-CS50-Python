def main():
    greeting = input("Input:")
    print(f"${value(greeting)}")


def value(greeting):
    if "hello" in greeting:
        return 0
    else:
        str(greeting).split()
        if greeting[0] == "h":
            return 20
        else:
            return 100


if __name__ == "__main__":
    main()