# import os

# # main_directory = r"\Users\prink\Downloads"
# main_directory = "/Users/prink/Downloads"


# with os.scandir(main_directory) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)

# subfolder_name = "Download pdf"  # Replace with the actual subfolder name

# subfolder_path = os.path.join(main_directory, subfolder_name)

# if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
#     with os.scandir(subfolder_path) as subfolder_entries:
#         for entry in subfolder_entries:
#             if entry.is_file():
#                 print(entry.name)
# else:
#     print(f"The subfolder '{subfolder_name}' does not exist.")

# with os.scandir(main_directory) as entries:
#     for entry in entries:
#         if entry.is_dir():
#             print(entry.name)
from datetime import datetime
from os import scandir
import os

main_directory = "/Users/prink/Downloads"
subforlder_lst = []
file_inside_subfolder_lst = []


with os.scandir(main_directory) as entries:
    for entry in entries:
        if entry.is_dir():
            subforlder_lst.append(entry.name)
print(subforlder_lst)

print('__--__')

for i in range(0,len(subforlder_lst)):
    temp_lst = []
    subfolder_path = os.path.join(main_directory, subforlder_lst[i])
    if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
        with os.scandir(subfolder_path) as subfolder_entries:
            for entry in subfolder_entries:
                temp_lst.append(entry.name)
    file_inside_subfolder_lst.append(temp_lst)

print(file_inside_subfolder_lst[0][0])
# with os.scandir(main_directory) as dir_contents:
#      for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)



# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date

# def get_files(lst,num):
#     if lst[num].is_file():
#         info = lst[num].stat()
#         print(f'{lst[num].name}\t Last Modified: {convert_date(info.st_mtime)}')
# for i in range(0,len(file_inside_subfolder_lst)):
#     get_files(file_inside_subfolder_lst,i)


# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date

# def get_files():
#     for i in range(0,len(subforlder_lst)):
#     #     dir_entries = scandir(subforlder_lst[i])
#         dir_entries = scandir(os.path.join(main_directory,subforlder_lst[i]))
#         for entry in dir_entries:
#             if entry.is_file():
#                 info = entry.stat()
#                 print(f'{entry.name}\t\t\t\t\t\t\t Last Modified: {convert_date(info.st_mtime)}')
#         print('\n--\n--\n')
# get_files()