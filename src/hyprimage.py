import sys

from src.color import *
from src.file import *
from src.helpers import *
from src.image import reduce_quality

def main() : 

    image_selected = sys.argv[1]
    match image_selected :
        case "-p" : 
            from src.config import change_config
            from src.helpers import eprint

            pal_name = sys.argv[2]
            
            apps = ["kitty", "wlogout", "wofi"]
            for app in apps : 
                try : 
                    change_config(pal_name, app)
                except KeyError as e: 
                    eprint(f"Error! The palette {e} doesn't exist!")

        case _ : 
            # Refreshing the files
            delete_file_data("json/palettes.json")
            write_file_data("json/palettes.json", "{}")

            shell("rm -rf palettes && mkdir palettes")
            quality_rates = [0, 5, 10, 15]
            
            for quality in quality_rates : 
                move_image_to_path(image_selected)
                reduce_quality("output.jpg", quality)
                generate_2_palettes("output.jpg")
                shell("rm output.jpg")
  
            move_palettes_to_folder("palettes")