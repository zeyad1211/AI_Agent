from functions.get_files_info import get_files_info
import os
# print(os.path.getsize("calculator"))
print(get_files_info("calculator", "."))
print("-------------------------------")
print(get_files_info("calculator", "pkg"))
print("-------------------------------")
print(get_files_info("calculator", "/bin"))
print("-------------------------------")
print(get_files_info("calculator", "../"))
print("-------------------------------")
