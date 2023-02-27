import os
folder_location = "E:/TorrentzDownloads/Data Engineering using python,spark and sql"

files = os.listdir(folder_location)

file_number = []

for file in files:
    file_no = int(file.split('.')[0])
    file_number.append(file_no)
print(len(file_number))
print(len(set(file_number)))

# to find the duplicate
# new_list = []
# dulicate_list = []
# for i in file_number:
#     if i not in new_list:
#         new_list.append(i)
#     else:
#         dulicate_list.append(i)
# print(len(new_list))
# print(dulicate_list)
# file_number.sort()


#  find the missing file
set_2 = set()

for i in range(1, 403):
    set_2.add(i)
# print(len(set_2))
print(set_2.symmetric_difference(set(file_number)))
# print(set(file_number).symmetric_difference(set_2))
