import csv

class CsvHandler:
    def __init__(self):
        pass

    def read_csv(self, path, delimiter=';'):
        output = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                output.append(row)
            return output

    def write_csv(self, path, data, delimiter=';'):
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=delimiter, lineterminator='\n')
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    import os
    directory_path = os.getcwd()

    writedata = [[1, 2, 3, 4],
                 ['a', 'b', 'c', 'd'],
                 ['one line of Text']]

    filename = '//test.csv'
    path = directory_path+filename

    CsvHandler(path, writedata).write_csv()
    readdata = CsvHandler(path).read_csv()
    for row in readdata:
        print(row)



