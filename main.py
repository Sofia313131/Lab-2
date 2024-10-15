import random
from csv import reader, writer, Dialect, register_dialect
from pprint import pprint
from xml.dom.minidom import parseString


class NormalCSV(Dialect):
    from _csv import QUOTE_MINIMAL
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = QUOTE_MINIMAL


register_dialect("csv", NormalCSV)


def task1(file="books.csv"):
    count = 0
    with open(file, "r", encoding="windows-1251") as csvfile:
        csv = reader(csvfile, dialect="csv")
        head = {s: i for i, s in enumerate(next(csv))}
        for row in csv:
            if len(row[head["Название"]]) > 30:
                count += 1
    print(count)


def task2(file="books.csv", output_file="result.csv"):
    search = input('Укажите автора для поиска: ').lower()
    with open(file, "r", encoding="windows-1251") as csvfile,\
            open(output_file, "w", encoding="windows-1251") as output:
        in_csv = reader(csvfile, dialect="csv")
        out_csv = writer(output, dialect="csv")
        head_row = next(in_csv)
        out_csv.writerow(head_row)
        head = {s: i for i, s in enumerate(head_row)}
        for row in in_csv:
            if int(row[head["Дата поступления"]].split()[0].split(".")[-1]) < 2018:
                continue
            if search in row[head["Автор (ФИО)"]].lower() \
                    or search in row[head["Автор"]].lower():
                out_csv.writerow(row)


def task3(file="books.csv", output_file="result.txt", num_of_books=20):
    with open(file, "r", encoding="windows-1251") as csvfile:
        csv = reader(csvfile, dialect="csv")
        head = {s: i for i, s in enumerate(next(csv))}
        rows = list(csv)
    nums = []
    while len(set(nums)) != num_of_books:
        nums = [random.randrange(0, len(rows)) for _ in range(num_of_books)]
    with open(output_file, "w", encoding="windows-1251") as output:
        for row in map(rows.__getitem__, nums):
            print(f"{row[head['Автор']]}."
                  f" {row[head['Название']]}"
                  f" - {int(row[head['Дата поступления']].split()[0].split('.')[-1])}", file=output)


def task4(file="currency.xml", key="Name", value="CharCode"):
    with open(file, "r", encoding="windows-1251") as xmlfile:
        tree = parseString(xmlfile.read())
    output_dict = {}
    for node in tree.firstChild.childNodes:
        output_dict[node.getElementsByTagName(key)[0].firstChild.data] = node.getElementsByTagName(value)[0].firstChild.data
    return output_dict


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # pprint(task4())
    print("EXIT")
