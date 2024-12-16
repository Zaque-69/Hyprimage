# Converting RGB to a HEX code
def rgb_to_hex(rgb):
    return "#" + format(rgb[0], '02x') + format(rgb[1], '02x') + format(rgb[2], '02x')

# Converting HEX to a RGB code
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

# Function to mix 2 HEX codes
def mix_colors(color1, color2):
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    mixed_rgb = tuple((c1 + c2) // 2 for c1, c2 in zip(rgb1, rgb2))

    return rgb_to_hex(mixed_rgb)

# Function to return the most 8 colors found
def most_common_colors(filename) : 
    from collections import Counter
    from PIL import Image
    from src.helpers import eprint

    # List of colors in the image
    try : 
        img = Image.open(filename)
        image_rgb = img.convert("RGB")
        colors = list(image_rgb.getdata())
        
        return Counter(colors).most_common(8)

    except FileNotFoundError : 
        eprint("The image was not found!")
    
def sort_colors(filename) :
    red_max_value = []   
    green_max_value = [] 
    blue_max_value = []   

    for color, count in most_common_colors(filename): 
        if color.index(max(color)) == 0 : 
            red_max_value.append(color)

        elif color.index(max(color)) == 1 : 
            green_max_value.append(color)

        else : 
            green_max_value.append(color)

    return [ red_max_value, green_max_value, blue_max_value ]

# Sorting the colors by their rgb sum and replacing them with their hex code
def colors_from_image(filename) : 
    list = []
    rgb_max = sort_colors(filename)

    for i in range(0, len(rgb_max)) : 
        rgb_max[i] = sorted(rgb_max[i], key = lambda x: x[0])
        
        for color in range(0, len(rgb_max[i])) : 
            rgb_max[i][color] = rgb_to_hex(rgb_max[i][color])
    
        for color in rgb_max[i] : 
            list.append(color)

    return list

# Function to generate 2 palettes of colors but with different shades, one dark and one light
def generate_2_palettes(image) :
    import random 
    from src.addjson import add_list_json
    from src.palette import create_palette_image

    final_list = colors_from_image(image)
    name_1 = str(random.randint(1, 1000))
    name_2 = str(random.randint(1, 1000))

    # Making 2 more palettes for more shades
    dark_palette = [ mix_colors(col,"#000000") for col in final_list ]
    light_palette = [ mix_colors(col, mix_colors(col, "#ffffff")) for col in final_list ]

    # Adding the lists in a JSON file
    add_list_json(name_1, final_list + dark_palette)
    add_list_json(name_2, light_palette + final_list)

    # Creating the palettes
    create_palette_image(final_list + dark_palette, name_1)
    create_palette_image(light_palette + final_list, name_2)
