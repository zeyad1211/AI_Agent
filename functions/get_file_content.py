import os
from config import MAX_CHARS
from functions.utilis import within_working_directory, file_exists
def get_file_content(working_directory, file_path):

    # abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))

    # print(target_dir)
    # print(abs_working_dir)

    if not within_working_directory(working_directory, file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not file_exists(working_directory, file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_dir, "r") as f:
            truncated = f.read(MAX_CHARS +1)
            # print(len(truncated))
            # print(truncated)
            if len(truncated) > MAX_CHARS:
                return truncated + f"[...File \"{os.path.join(working_directory, file_path)}\" truncated at {MAX_CHARS} characters]"
            return truncated
    except Exception as e:
        return(f"Error: {e}")
            
