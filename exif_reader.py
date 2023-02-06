import shutil
import exifread
import os
import csv

type = ['JPG', 'jpg', 'NEF', 'ARW', 'CR2', 'CR3', 'PNG', 'png']
path = os.getcwd()
files = os.listdir(path)
os.mkdir('output')

csv_file = open(path + '\\output\\focal_length_static.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["焦段", "光圈"])

for file in files:
    if not os.path.isdir(file):
        appendix = os.path.splitext(file)[1]
        if appendix in type:
            f = open(path+'/'+file, 'rb')
            tags = exifread.process_file(f)
            csv_writer.writerow([eval(str(tags["EXIF FocalLength"])), eval(str(tags["EXIF FNumber"]))])
