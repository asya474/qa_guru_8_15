from pathlib import Path


def path(file_name):
    base_path = Path(__file__).resolve().parent.parent
    tests_folder_path = base_path / 'tests'
    absolute_file_path = tests_folder_path / file_name
    return str(absolute_file_path.resolve())

