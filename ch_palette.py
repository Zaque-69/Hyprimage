import json, subprocess

def change_config( palette_number, hyprland_app ) : 

    skeleton_app, color_lines, color_string, filename, path_name = "", "", "", "", ""
    json_list = []
    count, end_count = 0, 0

    #getting the structure of an app config without colors ;
    with open(f"skeletons/{hyprland_app}.txt", "r") as f : 
        skeleton_app = f.read()

    #getting the list of the colors from the .json file;
    with open("palettes.json", "r") as f : 
        json_list = json.load(f)[palette_number]

    #getting the name of the string name in app ( color -> Kitty, color_string -> Cava, etc. ); 
    with open("apps.json", "r") as f : 
        color_string = json.load(f)[hyprland_app]["name"]
    
    #getting the name of the extension for the config file
    with open("apps.json", "r") as f : 
        filename = json.load(f)[hyprland_app]["filename"]

    #getting the number when the colors get counted ( 0, 1 , etc. ); 
    with open("apps.json", "r") as f : 
        count =  int( json.load(f)[hyprland_app]["start"] )

    #getting the number when the colors get counted ( 0, 1 , etc. ); 
    with open("apps.json", "r") as f : 
        end_count =  int( json.load(f)[hyprland_app]["end"] )

    for i in range(count, end_count + 1) : 
        color_lines  = color_lines +  f'{color_string}{count} {json_list[i]}\n'
        count += 1

    skeleton_app = skeleton_app + '\n' + color_lines

    #creating a new file of the config
    subprocess.run(f"rm -rf $HOME/.config/{hyprland_app} && mkdir $HOME/.config/{hyprland_app} && echo $HOME > path", shell = True)

    with open("path", "r") as f : 
        path_name = f.read()

    with open(f"{path_name[:-1]}/.config/{hyprland_app}/{filename}", "w") as f : 
        f.write(skeleton_app)