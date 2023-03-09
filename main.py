import zipfile
import shutil


# The names of the files you want to zip
files_to_zip = ["Zone_3_Road_V7.xlsx", "main.py", "Zone_3_road_output.xlsx"]

# The name of the zipped file
zipped_file = "Zone_3_Road.zip"

# Create the zip archive
with zipfile.ZipFile(zipped_file, mode='w') as archive:
    for file in files_to_zip:
        archive.write(file)



# Open the original zip file in read mode
with zipfile.ZipFile('Zone_3_Road.zip', 'r') as original_zip:

    # Create a new zip file in write mode
    with zipfile.ZipFile('new.zip', 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:

        # Iterate over the files in the original zip file
        for file in original_zip.filelist:

            # Read the contents of the file
            data = original_zip.read(file.filename)

            # Write the contents of the file to the new zip file
            new_zip.writestr(file.filename, data)

# Replace the original zip file with the new zip file
import os
os.replace('new.zip', 'Zone_3_Road.zip')
