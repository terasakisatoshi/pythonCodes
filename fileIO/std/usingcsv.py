# reference:
# https://qiita.com/okadate/items/c36f4eb9506b358fb608
import csv


def open_csv():
    with open("test.txt", "r") as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        print("header", header)
        xs = [int(row[0]) for row in list(reader)]
        ys = [int(row[1]) for row in list(reader)]


def write_csv():
    with open("output.txt", "w") as f:
        xs = list(range(10))
        ys = list(map(lambda x: x**2, xs))
        writer = csv.writer(f, lineterminator="\n")
        for x, y in zip(xs, ys):
            writer.writerow([x, y])


def write_csv2():
    with open("output.txt", "w") as f:
        xs = list(range(10))
        arr2d = [[x, x**2] for x in xs]
        print(arr2d)
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(arr2d)


def main():
    write_csv()
if __name__ == '__main__':
    main()
