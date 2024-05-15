import os
import shutil


def organize_files(directory):
    # Step 1: Get the list of files in the directory
    files = os.listdir(directory)

    # Step 3: Create a dictionary to store file extensions
    file_extensions = {}

    # Step 2: Loop through each file and extract its file extension
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            _, extension = os.path.splitext(file)
            file_extensions.setdefault(extension, []).append(file)

    # Step 4: Move files into their respective folders
    for extension, files in file_extensions.items():
        folder_name = extension[1:].upper() + " Files"
        folder_path = os.path.join(directory, folder_name)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        for file in files:
            source_path = os.path.join(directory, file)
            destination_path = os.path.join(folder_path, file)
            shutil.move(source_path, destination_path)


# Main function
def main():
    directory ="C:/Users/venka/Desktop/Test"

  # Replace this with your actual directory path
    organize_files(directory)
    print("Files organized successfully!")


if __name__ == "__main__":
    main()
