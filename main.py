import os
import shutil


# Dictionary for file categories

FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}


# Function for sorting files by category

def sort_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directroies
        if os.path.isdir(file_path):
            continue
    
        # Defining the file extension
        _, file_extension = os.path.splitext(filename)
    
    # Going through the file categories
        moved = False
        for category, extension in FILE_CATEGORIES.items():
            if file_extension.lower() in extension:
                category_path = os.path.join(directory, category)
            
                # If the folder for the category does not exist, create it
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                
                # Move the file to the appropriate folder
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved {filename} to {category_path}")
                moved = True
                break
    
        # If the file was not moved to any category, move it to the 'Others' folder
        if not moved:
            other_path = os.path.join(directory, "Other")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(file_path, os.path.join(other_path, filename))
            print(f"Moved {filename} to {category_path}")
        
# Specify the path to the directory you want to sort
directory_path = r"F:\vad_path"

sort_files(directory_path)
    
        
