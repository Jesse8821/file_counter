import os

def count_files(folder_path):
    try:
        files = os.listdir(folder_path)
        print(f"Number of files in '{folder_path}': {len(files)}")
    except FileNotFoundError:
        print("❌ Folder not found.")
    except Exception as e:
        print("❌ Error:", e)

path = input("Enter the folder path to count files in: ")
count_files(path)
