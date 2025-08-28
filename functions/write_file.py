from functions.utilis import get_abs_target_directories, within_working_directory
import os
def write_file(working_directory, file_path, content):
    _, target_directory = get_abs_target_directories(working_directory, file_path)
    if not within_working_directory(working_directory, file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        parent_dir = os.path.dirname(target_directory)
        # print(parent_dir)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
        with open(target_directory, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
