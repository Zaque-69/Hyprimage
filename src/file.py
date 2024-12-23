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

# List with colors from a file
def file_colors(filename) :
    lines = [] 
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    return lines

# Returning a list from the "json/palettes.json" file to use in "change_config" function
def colors_from_json(pal_num) : 
    import json
    from src.helpers import eprint
    
    try : 
        return json.load(open("json/palettes.json", "r"))[pal_num]
    except KeyError : 
        return eprint("The palette doesn't exist!")

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
