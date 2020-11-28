## /cygdrive/c/Users/JOSEA213/AppData/Local/Programs/Python/Python39/python
import csv
with open('eggs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['filename'], row['is_r1'], row['is_r2'], row['flag'])
exit()