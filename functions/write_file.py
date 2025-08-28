from utilis import within_working_directory
def write_file(working_directory, file_path, content):
    if not within_working_directory(working_directory, file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'