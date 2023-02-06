import shutil
import exifread
import os
import csv

types = ['.JPG', '.jpg', '.NEF', '.ARW',
         '.CR2', '.CR3', '.PNG', '.png', '.tif', '.dng']
path = os.getcwd()
files = os.listdir(path)

csv_file = open(path + '\\output\\focal_length_static.csv',
                'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["焦段", "光圈"])

"""
for file in files:
    if not os.path.isdir(file):
        file_type = os.path.splitext(file)[1]
        if file_type in types:
            f = open(path+'\\'+file, 'rb')
            tags = exifread.process_file(f)
            csv_writer.writerow([eval(str(tags["EXIF FocalLength"])), eval(str(tags["EXIF FNumber"]))])
"""


def find_file(curr_path):
    files = os.listdir(curr_path)
    for file in files:
        if os.path.isdir(curr_path+'\\'+file):
            next_path = curr_path+'\\'+file
            find_file(next_path)
        else:
            curr_file_path = curr_path+'\\'+file
            file_type = os.path.splitext(curr_file_path)[1]
            if file_type in types:
                f = open(curr_file_path, 'rb')
                tags = exifread.process_file(f)
                focal_length = eval(str(tags["EXIF FocalLength"]))
                aperture_val = eval(str(tags["EXIF FNumber"]))
                print(file_type[1:]+"文件："+curr_file_path+" 解析结果：\n焦距：" +
                      str(focal_length)+"mm        光圈f/"+str(aperture_val))
                csv_writer.writerow([focal_length, aperture_val])


find_file(path)
print("统计完成！")
os.system("pause")