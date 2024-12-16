def change_config(palette_number, appname) : 
    import json
    from src.helpers import shell

    structure = ""
    color_lines = ""
    color_string = ""
    filename = ""
    path_name = "" 

    colors_list = []

    #getting the structure of an app config without colors ;
    with open(f"skeletons/{appname}.txt", "r") as f : 
        structure = f.read()

    #getting the list of the colors from the .json file;
    with open("json/palettes.json", "r") as f : 
        colors_list = json.load(f)[palette_number]

    #getting the name of the string name in app ( color -> Kitty, color_string -> Cava, etc. ); 
    with open("json/apps.json", "r") as f : 
        color_string = json.load(f)[appname]["name"]
    
    #getting the name of the extension for the config file
    with open("json/apps.json", "r") as f : 
        filename = json.load(f)[appname]["filename"]

    for i in range(0, 16) : 
        color_lines  = color_lines +  f'{color_string}{i} {colors_list[i]}\n'

    structure = structure + '\n' + color_lines

    #creating a new file of the config
    shell(f"rm -rf $HOME/.config/{appname} && mkdir $HOME/.config/{appname} && echo $HOME > path")

    with open("path", "r") as f : 
        path_name = f.read()

    with open(f"{path_name[:-1]}/.config/{appname}/{filename}", "w") as f : 
        f.write(structure)