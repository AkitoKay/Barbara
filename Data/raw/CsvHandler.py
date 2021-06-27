import csv

class CsvHandler:
    def __init__(self):
        pass

    def read_csv(self, path, delimiter=',', **kwargs):
        output = []
        with open(path, newline='',**kwargs) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                output.append(row)
            return output

    def write_csv(self, path, data, delimiter=',', **kwargs):
        with open(path, 'w', newline='', **kwargs) as csvfile:
            writer = csv.writer(csvfile, delimiter=delimiter, lineterminator='\n')
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    import os
    directory_path = os.getcwd()

    #Musik
    sourcename = '//albumlist.csv'
    path = directory_path+sourcename

    readdata = CsvHandler().read_csv(path)

    newdata = []
    for row in readdata:
        '''
        id, titel, artist, publisher, release, palcementId
        '''
        
        newdata.append([row[0],row[2],row[3], 'NonePublisher', row[1], 'NonePlacementId'])

    targetname = '//album_copy.csv'
    path = directory_path+targetname
    CsvHandler().write_csv(path, newdata)
    print('musik done')
    
    #Books
    sourcename = '//books.csv'
    path = directory_path+sourcename

    readdata = CsvHandler().read_csv(path, encoding='utf-8')

    newdata = []
    for row in readdata:
        '''
        id, titel, artist, publisher, release, palcementId
        '''
        
        newdata.append([row[0],row[1],row[2], 'NonePublisher', 'NoneYear', 'NonePlacementId'])

    targetname = '//books_copy.csv'
    path = directory_path+targetname
    CsvHandler().write_csv(path, newdata, encoding='utf-8')
    print('books done')
    
    #Movies
    sourcename = '//tmdb_5000_movies.csv'
    path = directory_path+sourcename

    readdata = CsvHandler().read_csv(path, encoding='utf-8')

    newdata = []
    for row in readdata:
        i = 0
        '''
        id, titel, artist, publisher, release, palcementId
        '''
        
        newdata.append([i if not i == 0 else 'id', row[17],'NoneArtist', row[9], row[11], 'NonePlacementId'])
        i+=1
    targetname = '//movies_copy.csv'
    path = directory_path+targetname
    CsvHandler().write_csv(path, newdata,  encoding='utf-8')
    print('movies done')
    



