import shutil
import exifread
import os
import csv

types = ['.JPG', '.jpg', '.NEF', '.ARW', '.CR2', '.CR3', '.PNG', '.png', '.tif']
path = os.getcwd()
files = os.listdir(path)
os.mkdir('output')

csv_file = open(path + '\\output\\focal_length_static.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["焦段", "光圈"])

for file in files:
    if not os.path.isdir(file):
        file_type = os.path.splitext(file)[1]
        if file_type in types:
            f = open(path+'\\'+file, 'rb')
            tags = exifread.process_file(f)
            csv_writer.writerow([eval(str(tags["EXIF FocalLength"])), eval(str(tags["EXIF FNumber"]))])
