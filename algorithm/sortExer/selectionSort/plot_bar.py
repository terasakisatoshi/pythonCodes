from matplotlib import pyplot as plt


def main():
    fig, ax = plt.subplots()
    arr = [5, 4, 3, 2, 1]
    ax.bar(range(len(arr)), arr)
    plt.show()
if __name__ == '__main__':
    main()
