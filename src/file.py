# Deleting the data from a file
def delete_file_data(filename):
    try : 
        with open(f"{filename}", "a") as f : 
            f.truncate(0)
    except FileNotFoundError : 
        pass

# Writing a text in a file
def write_file_data(filename, text):
    try : 
        data = ""
        with open(filename, "r") as f : 
            data = f.read()

        with open(filename, "a") as f : 
            f.write(data + text)
    except FileNotFoundError : 
        pass

# Moving your image to this program
def move_image_to_path(image) : 
    import os
    from src.helpers import shell
    
    shell(f"cp {image} .")
    for file in os.listdir() : 
        if file in image : 
            shell(f"mv {file} output.jpg")
            break

def move_palettes_to_folder(foldername) : 
    import os 
    from src.helpers import shell
    
    for img in os.listdir() : 
        if ".png" in img : 
            if img != "hyprimage.png": 
                shell(f"mv {img} palettes") 
