import os

folder_numbers = 10

for i in range(folder_numbers):
    for j in os.listdir("./pre_process_group_photos/group_photos/" + str(i)):
        os.rename("./pre_process_group_photos/group_photos/" + str(i)+"/" +
                  str(j), "./pre_process_group_photos/group_photos/"+str(j))
    os.rmdir("./pre_process_group_photos/group_photos/" + str(i))
