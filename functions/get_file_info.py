import os
def get_files_info(working_directory, directory="."):
    relative_path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(relative_path)
    
    # if directory != '.':
    #     screen_output = [f"Result for '{directory}' directory:"]
    # else:
    #     screen_output = ["Result for current directory:"]
    screen_output = []
    
    if directory != '.' and directory not in os.listdir(working_directory):
        screen_output.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(screen_output)

    elif not os.path.isdir(full_path):
        screen_output.append(f'Error: "{directory}" is not a directory')
        return "\n".join(screen_output)
    try:
        for item in os.listdir(full_path):
            screen_output.append(f" - {item}: file_size={get_file_size(os.path.join(full_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_path, item))}")
        return "\n".join(screen_output)
    except Exception as e:
        return f"Error listing files {e}"


def get_file_size(full_path):
    return os.path.getsize(full_path)

