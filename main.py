import os
from src.sorted import sort_files
from src.logger import logger


def main():
    directory_to_sort = input("Enter the path to the directory to sort: ")
    
    if not os.path.isdir(directory_to_sort):
        logger.error(f"Error: The {directory_to_sort} directory does not exist.")
        print(f"Error: The {directory_to_sort} directory does not exist")
        return
    
    sort_files(directory_to_sort)
    print(f"Sorting of files in the {directory_to_sort} directory is completed")


if __name__ == "__main__":
    main()
