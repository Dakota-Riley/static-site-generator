import os
import shutil

def copy_static_to_public(source_path, destination_path, is_root_call=True):
    # Print what we're currently processing
    print(f"Processing: {source_path}")

    # Only delete and recreate the destination at the top level
    if is_root_call:
        print(f"Starting copy from {source_path} to {destination_path}")
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        os.mkdir(destination_path)
    else:
        print(f"Processing subdirectory: {source_path}")

    # List all items in the source directory
    items = os.listdir(source_path)

    for item in items:
        # Build full paths
        source_item_path = os.path.join(source_path, item)
        dest_item_path = os.path.join(destination_path, item)
        # If it's a directory, recursively process it
        if os.path.isdir(source_item_path):
            # Make sure the destination directory exists
            if not os.path.exists(dest_item_path):
                os.mkdir(dest_item_path)
            # Recursive call for subdirectory
            copy_static_to_public(source_item_path, dest_item_path, False)
        # If it's a file, process it according to your needs
        elif os.path.isfile(source_item_path):
            print(f"Found file: {source_item_path}")
            # Here you would do something with the file
            # For example: shutil.copy(source_item_path, dest_item_path)
            shutil.copy(source_item_path, dest_item_path)

if __name__ == "__main__":
    copy_static_to_public("static", "public")
