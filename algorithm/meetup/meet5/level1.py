bool2str = {True: "true", False: "false"}


def list_to_string(input_list):
    output_list = []
    for element in input_list:
        if isinstance(element, bool):
            # print("Bool", element)
            output_list.append(bool2str[element])
        elif isinstance(element, int):
            # print("int", element)
            output_list.append(str(element))
        else:
            output_list.append(element)

    output = " ".join(output_list)

    return output


def test_one():
    input_list = [2, "hello", True, False, 10]
    output = list_to_string(input_list)
    print(output)


def test_two():
    input_list = ["hello", "world"]
    output = list_to_string(input_list)
    print(output)


def main():
    test_one()
    test_two()


if __name__ == '__main__':
    main()
