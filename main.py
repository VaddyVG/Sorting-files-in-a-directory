import os
import shutil
import json


# Downloading the configuration from the config.json file

def load_congif(config_path='config.json'):
    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f'Error: configuration file "{config_path}" not found')
        return None
    except json.JSONDecodeError:
        print('Error: Invalid JSON format in the configuration file')
        return None
    
    
def sort_files(directory, config):
    if not config:
        print('Sorting cannot be performed without configuration')
        return
    
    directories = config['directories']
    
    # Creating folders for each category from the configuration
    for folder in directories.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        
    # Go through all the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # If it's file
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower() # Get extension
            
            # Check category
            for folder, extension in directories.items():
                if file_extension in extension:
                    destination = os.path.join(directory, folder, filename)
                    try:
                        shutil.move(file_path, destination)
                        print(f'The {filename} has been moved in {folder}')
                    except (shutil.Error, OSError) as e:
                        print(f'File transfer error {filename}: {e}')
                    break
                
                
# main function

def main():
    directory = input('Enter the path to the directory to sort: ')
    
    if not os.path.exists(directory):
        print(f'Error: Directory "{directory}" not found')
        return
    
    config = load_congif()
    sort_files(directory, config)
    

if __name__ == "__main__":
    main()
