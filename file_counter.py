import os
import logging

# Configure logging to a file
logging.basicConfig(filename="file_counter.log", level=logging.INFO)

def log_result(message):
    logging.info(message)
    print(message)

# Function to count files
def count_files(folder_path, count_files_only=True):
    try:
        if not os.path.isdir(folder_path):
            log_result(f"❌ '{folder_path}' is not a valid directory.")
            return
        items = os.listdir(folder_path)
        if count_files_only:
            count = sum(1 for item in items if os.path.isfile(os.path.join(folder_path, item)))
            log_result(f"Number of files in '{folder_path}': {count}")
        else:
            count = sum(1 for item in items if os.path.isdir(os.path.join(folder_path, item)))
            log_result(f"Number of directories in '{folder_path}': {count}")
    except Exception as e:
        log_result(f"❌ Error: {e}")

# Recursively count files in subfolders
def count_files_recursive(folder_path):
    total_files = 0
    try:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            total_files += len(filenames)
        log_result(f"Total number of files in '{folder_path}' (including subfolders): {total_files}")
    except Exception as e:
        log_result(f"❌ Error: {e}")

# Count file types (extensions)
def count_file_types(folder_path):
    try:
        if not os.path.isdir(folder_path):
            log_result(f"❌ '{folder_path}' is not a valid directory.")
            return
        files = os.listdir(folder_path)
        file_types = [os.path.splitext(f)[1] for f in files if os.path.isfile(os.path.join(folder_path, f))]
        count = {file_type: file_types.count(file_type) for file_type in set(file_types)}
        log_result(f"File types in '{folder_path}':")
        for file_type, count in count.items():
            log_result(f"{file_type if file_type else 'No extension'}: {count}")
    except Exception as e:
        log_result(f"❌ Error: {e}")

# Ask for user input and call functions
if __name__ == "__main__":
    print("Welcome to File Counter!")

    choice = input("Do you want to count files, directories or both? (f/d/b): ").lower()
    path = input("Enter the folder path to count: ")

    if choice == 'f':
        count_files(path, count_files_only=True)
    elif choice == 'd':
        count_files(path, count_files_only=False)
    elif choice == 'b':
        count_files(path, count_files_only=True)
        count_files(path, count_files_only=False)
    else:
        log_result("❌ Invalid choice.")

    recursive = input("Do you want to count files recursively in subfolders? (y/n): ").lower()
    if recursive == 'y':
        count_files_recursive(path)

    types = input("Do you want to see a breakdown of file types? (y/n): ").lower()
    if types == 'y':
        count_file_types(path)
