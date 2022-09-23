import csv

print('module is there')

with open(r'D:\DataforArcObject\Shingtaluru_Data1.csv','r') as f1:
    r = csv.reader(f1)
    data = list(r)
    for row in data:
        for column in row:
            print(column,'\t',end='')
        print()
        
