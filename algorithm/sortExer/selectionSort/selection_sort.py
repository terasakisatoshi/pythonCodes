"""
selection sort
"""


def get_arg_min(arr):
    m = min(arr)
    for i, a in enumerate(arr):
        if a == m:
            return i, m


def do_selection_sort(arr):
    for i, v in enumerate(arr):
        if i + 1 == len(arr):
            break
        seq = arr[i + 1:]
        arg_min, minimum = get_arg_min(seq)
        if v > minimum:
            arr[i], arr[i + 1 + arg_min] = arr[i + 1 + arg_min], arr[i]
        yield arr


def main():
    arr = [5, 4, 3, 2, 1]
    a = do_selection_sort(arr).__next__()
    print(arr)
if __name__ == '__main__':
    main()
