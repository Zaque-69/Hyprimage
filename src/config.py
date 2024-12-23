BUTTON = """
button {
    color: #5f655e;
    background-color: color1;
    border: 1px solid #1f221f;
    margin: 20px;
    background-size: 33%;
    border-radius: 1rem;
    background-repeat: no-repeat;
    background-position: center;
    transition: .33s;
}
"""

ENTRY1 = """
#entry:nth-child(even){
    background-color: color1;
}
"""

ENTRY2 = """
#entry:selected {
    background-color: color2;
}
"""

# Function to add the colors to the apps configurations
def replace_color(bigtext, repl, color) : 
    lines = bigtext.splitlines()
    for i, line in enumerate(lines):
        if repl in line : 
            lines[i] = f"    {repl}:{color};"  
        
    return "\n".join(lines)

def change_config(palette, appname) : 
    import json
    from src.helpers import shell

    shell("echo $HOME > path")
    path_name = open("path", "r").read()[:-1]
    structure = open(f"skeletons/{appname}.txt", "r").read()
    color_string = json.load(open("json/apps.json", "r"))[appname]["name"]
    filename = json.load(open("json/apps.json", "r"))[appname]["filename"]
    
    color_lines = ""
 
    match appname : 
        case "kitty" : 
            for i in range(0, 16) : 
                color_lines  = color_lines +  f'{color_string}{i} {palette[i]}\n'

            structure = structure + '\n' + color_lines
            with open(f"{path_name}/.config/kitty/kitty.conf", "w") as f : 
                f.write(structure)

        case "wlogout" : 
            button = replace_color(BUTTON, "background-color", palette[4])
            structure += button

            with open(f"{path_name}/.config/wlogout/style.css", "w") as f : 
                f.write(structure)

        case "wofi" :
            entry1 = replace_color(ENTRY1, "background-color", palette[4])
            entry2 = replace_color(ENTRY2, "background-color", palette[12])

            structure = structure + '\n' + entry1
            structure += structure + '\n' + entry2

            with open(f"{path_name}/.config/wofi/style.css", "w") as f : 
                f.write(structure)
                
    print("Succes!")