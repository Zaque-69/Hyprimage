print("""
Hyprimage - Z4que 2024 All rights reserved
Usage: python main.py [OPTION]
Dot generator

-p (palettes) + [FILE] : Generating palettes of colors for
your image.After this, some images will be loaded in "palettes".
ex : python main.py -p /path/to/your/image

-c (config) Generating configurations for the apps :
"kitty", "wlogout", "wofi", where :
    nr = number of palette image (from 0 to 1000)
ex : python main.py -c {nr}
                  
-t (theme) + NUMBER : Here are your configurations of
your backgrounds. ]. In "backgrounds" save your image
with ".png" extension and with the same name as your image
write a file in "theme" with a list of colors, one on each line
Check the folders for an example.
    nr = number of theme (from 0 to n)
ex : python main.py -t {nr}
""")