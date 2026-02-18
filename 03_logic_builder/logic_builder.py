def logic_builder():

    rules = {
        3: "Fizz",
        5: "Buzz"
    }

    counts = {
        "Fizz": 0,
        "Buzz": 0,
        "FizzBuzz": 0
    }

    for number in range(1, 51):

        output = ""

        for divisor, word in rules.items():
            if number % divisor == 0:
                output += word

        if output == "":
            print(number)
        else:
            print(output)
            if output in counts:
                counts[output] += 1

    return counts


def main():
    result = logic_builder()

    print("\n--- Summary ---")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()