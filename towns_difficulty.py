import csv
with open('towns.csv', newline='', encoding='utf-8') as File, open('city.txt', 'w', encoding='utf-8') as fout:  
    reader = csv.reader(File)
    next(reader)
    for row in reader:
        popul = float(row[1])
        if popul > 300:
            fout.write(row[0] + ' 100' + '\n')
        elif popul > 35:
            fout.write(row[0] + ' 10' + '\n')
        else:
            fout.write(row[0] + ' 1' + '\n')