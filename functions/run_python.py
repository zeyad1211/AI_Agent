from functions.utilis import within_working_directory, file_exists
import subprocess
import sys
def run_python_file(working_directory, file_path, args=[]):
    if not within_working_directory(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not file_exists(working_directory, file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        proc = subprocess.run([sys.executable, file_path, *args], cwd=working_directory, capture_output=True, timeout=30.0, text=True)
        out = proc.stdout.strip()
        err = proc.stderr.strip()
        parts = []
        if out:
            parts.append(f"STDOUT:\n{out}")
        if err:
            parts.append(f"STDERR:\n{err}")
        if proc.returncode != 0:
            parts.append(f"Process exited with code {proc.returncode}")
        result = "\n".join(parts) if parts else "No output produced."
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"