from PIL import Image
from collections import Counter
import cv2, subprocess, sys, os, json, random, string

from generate_image import create_palette_image 

def run_shell_command( command ) : 
    subprocess.run(command, shell = True)

def rgb_to_hex(rgb):
    #Converting a rgb code tuple into a hex code
    return "#" + format(rgb[0], '02x') + format(rgb[1], '02x') + format(rgb[2], '02x')

def hex_to_rgb(hex_code):
    #Converting a hex color code to an RGB tuple
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def reduce_quality(image, quality_rate) : 
    #Because there will be less colors on the image and save it as "output.jpg"

    #copying the image to this path
    run_shell_command(f"cp {image} .")
    jpgimg, filesave = "", ""
    for file in os.listdir() : 
        if file in image :
            jpgimg = file
            filesave = file

    if "png" in jpgimg : 
        #replacing the extension with "jpg" ( only with "jpg" works )
        jpgimg = jpgimg.replace("png", "jpg")

    run_shell_command(f"cp {filesave} output.jpg")
    #reading the image in cv2'
    img = cv2.imread("output.jpg")

    #compresing the image quality ( argument 2 ) 
    compression_params = [cv2.IMWRITE_JPEG_QUALITY, quality_rate]
    cv2.imwrite("output.jpg", img, compression_params)
    run_shell_command(f"rm {filesave}")

def mix_colors(color1, color2):
    #160042, #ffffff -> #8a7fa0
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    mixed_rgb = tuple((c1 + c2) // 2 for c1, c2 in zip(rgb1, rgb2))
    return rgb_to_hex(mixed_rgb)

def edit_json(element, content) : 
    #adding the lists of colors is a json to get them later
    data = ""
    with open("palettes.json", "r") as f : 
        data = json.load(f)

    data[element] = content

    with open("palettes.json", "w") as f:
        json.dump(data, f)

def main(image) :
    # Each "main()" function will generate 2 palettes

    red_max = []          # The max value of Red
    green_max = []        # The max value of Green
    blue_max = []         # The max value of Blue
    folder_name = ""      # Folder name

    # The names of the palettes to move in a folder
    name1 = str(random.randint(1, 1000))
    name2 = str(random.randint(1, 1000))

    boolean = False
    for file in os.listdir() : 
        if file == "output.jpg" : 
            boolean = True

    if not boolean : 
        run_shell_command(f"cp {image} .")

    name = ""
    for file in os.listdir() : 
        if file in image : name = file

    run_shell_command(f"mv {name} output.jpg")

    img = Image.open("output.jpg")
    #converting the image to RBB
    image_rgb = img.convert("RGB")

    # List of colors in the image
    colors = list(image_rgb.getdata())

    # Counting colors
    color_counts = Counter(colors)

    # Selecting the most 9 common colors from the imaglist
    top_colors = color_counts.most_common(9)
    
    # Adding each color to the lists they have the most shade ( red, green or blue )
    for color, count in top_colors: 

        # This will detete all the colors with the same number of red, green and blue.
        # The colors selected will be < 9 because we alse delete white, which we will add sooner
        if color[0] != color[1] != color[2] : 

            # Sorting the colors based on what is the most used RGB color in them
            if color.index(max(color)) == 0 : 
                red_max.append(color)

            elif color.index(max(color)) == 1 : 
                green_max.append(color)

            else : 
                green_max.append(color)

    # Making a list with the previsious lists of rgb
    rgb_max = [ red_max, green_max, blue_max ]
    final_list = [] 

    # Sorting the colors by their rgb sum and replacing them with their hex code
    for i in range(0, len(rgb_max)) : 
        rgb_max[i] = sorted(rgb_max[i], key=lambda x: x[0])
        
        for color in range(0, len(rgb_max[i])) : 
            rgb_max[i][color] = rgb_to_hex(rgb_max[i][color])
    
        for color in rgb_max[i] : 
            final_list.append(color)

    # If the list in full, that means there are many colors close in density. 
    # So we will delete them from the middle
    if len(final_list) == 9 : 
        final_list.remove(final_list[2])
        final_list.remove(final_list[4])

    # If the list isn'n complete and lower or equal to 7 we add the white 
    # color to get also a lighter shade.
    if len(final_list) <= 7 : 
        final_list.append("#ffffff")
        nr = len(final_list) - 1
        final_list.insert(nr, mix_colors(final_list[nr - 1], final_list[nr]))

    # Adding more colors between the colors
    nr = int(len(final_list) / 2)
    while len(final_list) < 9 : 
        mixed_color = mix_colors(final_list[nr - 1], final_list[nr])
        final_list.insert(nr, mixed_color)

        nr -= 1

    # Making 2 more palettes for more shades
    dark_palette = [mix_colors(col,"#000000") for col in final_list]
    light_palette = [mix_colors(col, mix_colors(col, "#ffffff")) for col in final_list]

    final_list.pop()
    dark_palette.pop()
    light_palette.pop()
    
    # Adding the lists in a JSON file
    edit_json(name1, final_list + dark_palette)
    edit_json(name2, light_palette + final_list)

    # Creating the palettes
    create_palette_image(final_list + dark_palette, name1)
    create_palette_image(light_palette + final_list, name2)

if __name__ == "__main__" :

    image_selected = sys.argv[1]

    match image_selected :
        case "-p" : 
            pal_name = sys.argv[2]
            from ch_palette import change_config
            change_config( pal_name, "kitty")

        case _ : 
            run_shell_command("rm -rf palettes && mkdir palettes")

            main(image_selected)
            run_shell_command("rm output.jpg")

            reduce_quality(image_selected, 10)
            main(image_selected)
            run_shell_command("rm output.jpg")

            reduce_quality(image_selected, 5)
            main(image_selected)
            run_shell_command("rm output.jpg")

            reduce_quality(image_selected, 0)
            main(image_selected)
            run_shell_command("rm output.jpg")

            for img in os.listdir() : 
                if ".png" in img : 
                    if img != "hyprimage.png" : 
                        run_shell_command(f"mv {img} palettes") 

    print("Succes!")
