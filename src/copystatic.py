import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # run 'ls' on the source_dir_path
    for filename in os.listdir(source_dir_path):

        # create "from" and "dest" paths for every item
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")

        # if "from_path" is a file, copy that file to the destination
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        # if it's a folder, rinse, repeat.
        else:
            copy_files_recursive(from_path, dest_path)
