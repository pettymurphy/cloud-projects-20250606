import os

def get_file_metadata_grouped(path='.'):
    """
    Recursively scans a directory and groups file metadata by folder.

    Parameters:
    - path (str): Directory to scan. Defaults to current directory.

    Returns:
    - Dict[str, List[Dict]]: Keys are folder paths; values are lists of file info dictionaries.
    """
    grouped_files = {}

    for root, dirs, files in os.walk(path):  # Traverse all folders and subfolders
        folder_files = []

        for file in files:
            full_path = os.path.join(root, file)
            folder_files.append({
                'name': file,
                'size': os.path.getsize(full_path)
            })

        if folder_files:
            grouped_files[root] = folder_files  # Add files only if folder has any

    return grouped_files

# Example usage
if __name__ == "__main__":
    result = get_file_metadata_grouped()
    for folder, files in result.items():
        print(f"\nFolder: {folder}")
        for file in files:
            print(f"  - {file['name']} ({file['size']} bytes)")
