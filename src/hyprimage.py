import sys

from src.color import *
from src.file import *
from src.helpers import *
from src.image import reduce_quality

def main() : 

    arg = sys.argv[1]
    
    match arg :
        case "-p" : 
            # Generating palettes of colors with your image1
            delete_file_data("json/palettes.json")
            write_file_data("json/palettes.json", "{}")

            image = sys.argv[2]
            quality_rates = [0, 5, 10, 15]
            shell(f"rm -rf palettes && mkdir palettes && swww img {image}")
            
            for quality in quality_rates : 
                move_image_to_path(image)
                reduce_quality("output.jpg", quality)
                generate_2_palettes("output.jpg")
                shell("rm output.jpg")
  
            move_palettes_to_folder("palettes")


        case "-c" : 
            # Creating configurations for the following appos with your image 
            from src.config import change_config
            from src.file import colors_from_json
            from src.helpers import eprint

            pal_name = sys.argv[2]
            palette = colors_from_json(pal_name)

            apps = ["kitty", "wlogout", "wofi"]
            for app in apps : 
                try : 
                    change_config(palette, app)
                except KeyError as e: 
                    eprint(f"Error! The palette {e} doesn't exist!")

        case "-t" : 
            # Changing the theme as you saved the files
            import os
            from src.file import file_colors
            from src.config import change_config
            from src.helpers import eprint

            filenames = []
            for file in os.listdir("themes") : 
                filenames.append(file)

            theme_number = sys.argv[2]
            try : 
                file = filenames[int(theme_number)]
            except IndexError : 
                eprint("There are no more themes!")

            colors = file_colors(f"themes/{file}")
            shell(f"nohup swaybg -i backgrounds/{file}.png")

            apps = ["kitty", "wlogout", "wofi"]
            for app in apps : 
                change_config(colors, app)

        case "-h" :
            shell("python src/info.py")
