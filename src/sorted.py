import os
import shutil
from src.logger import logger
from src.config_loader import load_config


def sort_files(directory):
    '''Sorting function'''
    
    config = load_config()

    if not config:
        logger.error("Sorting cannot be performed without configuration.")
        return

    directories = config['directories']

    for folder in directories.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        logger.info(f"Folder {folder_path} create or already exists")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()

            for folder, extensions in directories.items():
                if file_extension in extensions:
                    destination = os.path.join(directory, folder, filename)
                    try:
                        shutil.move(file_path, destination)
                        logger.info(f'File {filename} moved in {folder}')
                    except (shutil.Error, OSError) as e:
                        logger.error(f"{filename} transfer error: {e}")
                    break
