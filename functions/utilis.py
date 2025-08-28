import os

def get_abs_target_directories(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    return abs_working_dir, target_dir

def within_working_directory(working_directory, file_path):
    abs_working_dir, target_dir = get_abs_target_directories(working_directory, file_path)
    if target_dir.startswith(abs_working_dir):
        return True
    return False

def file_exists(working_directory, file_path):
    _, target_dir = get_abs_target_directories(working_directory, file_path)
    if os.path.isfile(target_dir):
        return True
    return False

    
