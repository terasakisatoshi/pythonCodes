"""
Check if a list contains all the elements of another list
"""

word_list = ["Hello", "World", "From", "Python"]
find_list_1 = ["Hello", "World"]
find_list_2 = ["Hello", "Python"]
find_list_3 = ["Python", "World"]
find_list_4 = ["Hate", "Python"]


def example_1():
    """
    Reference:
    https://stackoverflow.com/questions/3847386/testing-if-a-list-contains-another-list-with-python
    """
    for find_list in [find_list_1, find_list_2, find_list_3, find_list_4]:
        is_in = set(find_list).issubset(word_list)
        print(is_in)


def example_2():
    """
    using `all`
    """
    for find_list in [find_list_1, find_list_2, find_list_3, find_list_4]:
        is_in = all(element in word_list for element in find_list)
        print(is_in)


def example_3():
    """
    using `all`
    """
    for find_list in [find_list_1, find_list_2, find_list_3, find_list_4]:
        is_in = any(element in word_list for element in find_list)
        print(is_in)
    # output should be True\nTrue\nTrue\nTrue


def main():
    example_1()
    example_2()
    example_3()


if __name__ == '__main__':
    main()
