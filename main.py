def main():
    print("Hello world!")
    print(f"{3 + 4 = }")


def not_main(number: str):
    if number.isdigit():
        print("Is not a canonic number!") if int(number) != 42 else print("Well done!")
    else:
        print(f"I wanted a number, not {type(number).__name__}")



if __name__ == "__main__":
    main()
    not_main(input("Enter a number: "))
