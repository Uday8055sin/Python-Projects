import os
import shutil

# ==========================================
#       JPG FILE ORGANIZER
# ==========================================

print("=" * 45)
print("          JPG FILE ORGANIZER")
print("=" * 45)

# Ask the user for the folder path
source_folder = input("Enter the folder path: ")

# Check if the folder exists
if not os.path.exists(source_folder):

    print("Folder does not exist.")
    print("Please check the folder path.")

else:

    # Create destination folder
    destination_folder = os.path.join(source_folder, "JPG_Files")

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    # Count moved files
    count = 0

    # Find all files in the source folder
    for file in os.listdir(source_folder):

        # Check whether file is a JPG file
        if file.lower().endswith(".jpg"):

            source_path = os.path.join(source_folder, file)

            destination_path = os.path.join(
                destination_folder,
                file
            )

            # Move the file
            shutil.move(source_path, destination_path)

            print("Moved:", file)

            count += 1

    # Display result
    print("\n" + "=" * 45)
    print("TASK COMPLETED")
    print("=" * 45)

    print("Total JPG files moved:", count)
    print("Files moved to:", destination_folder)